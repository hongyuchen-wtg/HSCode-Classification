from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import config
import logic


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

index, descriptions, hscodes = logic.Load()


@app.get("/query")
def query_hscode(
    query: str = Query(..., description=f"Split queries by '{config.SEPARATOR}'"),
    resultFormat: str = Query(config.RESULT_FORMAT_API, description="Format parameter for search results")
):
    result = logic.HSCodeSearch(index, descriptions, hscodes, query, resultFormat)
    return {
        "query": query,
        "result": result
    }
