import config
import logic
import os
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


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


@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join(config.DOWNLOAD_FILE_PATH, filename)
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type='application/octet-stream'
    )