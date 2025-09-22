import os


os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

SEPARATOR = "&"

# Server Ports
UI_PORT = 8080
API_PORT = 8081

# Model
MODEL_NAME = 'intfloat--e5-base-v2' # BAAI/bge-m3 / MiniLM-L6-v2 / intfloat/e5-base-v2
FINETUNED_MODEL_NAME = f'fine_tuned_{MODEL_NAME}'
MODEL_PATH = os.path.join(BASE_PATH, "model", MODEL_NAME)
FINETUNED_MODEL_PATH = os.path.join(BASE_PATH, "model", FINETUNED_MODEL_NAME)

# Dataset
DATASET = 'NZCClassification'
DATA_PATH = os.path.join(BASE_PATH, 'data', f'{DATASET}.csv')
HS_CODE_PATH = os.path.join(BASE_PATH, 'vectors', f'code_{DATASET}_{MODEL_NAME.replace("/", "_")}.pkl')
HS_CODE_DESCRIPTION_PATH = os.path.join(BASE_PATH, 'vectors', f'description_{DATASET}_{MODEL_NAME.replace("/", "_")}.pkl')
HS_INDEX_PATH = os.path.join(BASE_PATH, 'vectors', f'descriptionIndex_{DATASET}_{MODEL_NAME.replace("/", "_")}.faiss')


# Response Format
RESULT_FORMAT_UI = "1"
RESULT_FORMAT_API = "2"