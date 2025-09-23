import config
import pandas as pd
import faiss
import numpy as np
import pickle
import os
import time
from sentence_transformers import SentenceTransformer


model = SentenceTransformer(config.MODEL_PATH)


def preprocess():
    df = pd.read_csv(config.DATA_PATH)
    hscodes = df['code'].astype(str).tolist()
    h0descriptions = df['h0description'].astype(str).tolist()
    h1descriptions = df['h1description'].astype(str).tolist()
    descriptions = [f"h0Description:{h0.strip()}\nh1Description:{h1.strip()}".strip() for h0, h1 in zip(h0descriptions, h1descriptions) if pd.notna(h0) or pd.notna(h1)]
    # print(descriptions[:5], hscodes[:5])

    embeddings = model.encode(descriptions, convert_to_numpy=True, show_progress_bar=True)

    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)

    faiss.write_index(index, config.HS_INDEX_PATH)

    with open(config.HS_CODE_DESCRIPTION_PATH, "wb") as f:
        pickle.dump(descriptions, f)

    with open(config.HS_CODE_PATH, "wb") as f:
        pickle.dump(hscodes, f)


def Load():
    if not os.path.exists(config.HS_INDEX_PATH) or not os.path.exists(config.HS_CODE_DESCRIPTION_PATH) or not os.path.exists(config.HS_CODE_PATH):
        print("Preprocessing data and building index...")
        preprocess()

    index, descriptions, hscodes = load_index_and_data()
    return index, descriptions, hscodes


def load_index_and_data():
    try:
        if not os.path.exists(config.HS_INDEX_PATH):
            raise FileNotFoundError(f"No such file: {config.HS_INDEX_PATH}")
        idx = faiss.read_index(config.HS_INDEX_PATH)
    except Exception as e:
        print(f"No such file: {e}")
        return None, None, None

    try:
        if not os.path.exists(config.HS_CODE_DESCRIPTION_PATH):
            raise FileNotFoundError(f"No such file: {config.HS_CODE_DESCRIPTION_PATH}")
        with open(config.HS_CODE_DESCRIPTION_PATH, "rb") as f:
            desc = pickle.load(f)
    except Exception as e:
        print(f"No such file: {e}")
        return None, None, None

    try:
        if not os.path.exists(config.HS_CODE_PATH):
            raise FileNotFoundError(f"No such file: {config.HS_CODE_PATH}")
        with open(config.HS_CODE_PATH, "rb") as f:
            codes = pickle.load(f)
    except Exception as e:
        print(f"No such file: {e}")
        return None, None, None

    return idx, desc, codes


def batch_query(texts, index, descriptions, hscodes, top_k=1):
    query_embs = model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
    faiss.normalize_L2(query_embs)

    distances, indices = index.search(query_embs, top_k)

    batch_results = []
    for i, (dists, idxs) in enumerate(zip(distances, indices)):
        results = []
        for dist, idx in zip(dists, idxs):
            if idx == -1:
                continue
            results.append({
                'hscode': hscodes[idx],
                'description': descriptions[idx],
                'score': float(dist)
            })
        batch_results.append((texts[i], results))

    return batch_results


def formatted_result_for_UI(batch_results):
    queryResultTextList = []
    for text, results in batch_results:
        queryResultText = f"### Query: {text}\n"
        for res in results:
            queryResultText += f"\nHSCode: {res['hscode']}"
            queryResultText += f"\n{res['description'].replace('`', '')}"
            queryResultText += F"\nConfidence Score (Cos sim): {res['score']:.4f}\n"
        queryResultTextList.append(queryResultText)
    return "\n".join(queryResultTextList)


def formatted_result_for_API(batch_results):
    formatted_results = []
    for text, results in batch_results:
        entry = {
            "query": text,
            "predictions": []
        }
        for res in results:
            entry["predictions"].append({
                "hscode": res['hscode'],
                "description": res['description'].replace('`', ''),
                "confidence_score": round(res['score'], 4)
            })
        formatted_results.append(entry)
    return formatted_results


def HSCodeSearch(index, descriptions, hscodes, query_text, resultFormat=config.RESULT_FORMAT_UI, top_k=3):
    queries = [q.strip() for q in query_text.strip().split(config.SEPARATOR) if q.strip()]
    if not queries:
        return "No valid query provided."
    start = time.time()
    batch_results = batch_query(queries, index, descriptions, hscodes, top_k)
    end = time.time()
    timeCostText = f"### Time Cost on {len(queries)} Querie(s): {end - start:.4f} s\n\n"

    if resultFormat == config.RESULT_FORMAT_UI:
        return timeCostText + formatted_result_for_UI(batch_results)
    elif resultFormat == config.RESULT_FORMAT_API:
        return formatted_result_for_API(batch_results)
