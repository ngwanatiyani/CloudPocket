from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from s3_client import upload_to_s3, download_from_s3
from metadata_store import MetadataStore
from typing import List
import io
import time

app = FastAPI()
metadata_store = MetadataStore()


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    s3_key = f"{int(time.time())}_{file.filename}"
    upload_to_s3(contents, s3_key)
    metadata_store.add_entry(file.filename, s3_key)
    return {"message": "File uploaded successfully", "s3_key": s3_key}


@app.get("/download/{s3_key}")
def download_file(s3_key: str):
    file_content = download_from_s3(s3_key)
    if not file_content:
        raise HTTPException(status_code=404, detail="File not found")
    return StreamingResponse(
        io.BytesIO(file_content),
        media_type="application/octet-stream"
    )


@app.get("/files/", response_model=List[str])
def list_files():
    """List all uploaded files."""
    return metadata_store.list_filenames()


@app.delete("/delete/{s3_key}")
def delete_file(s3_key: str):
    """Delete a file from S3 and remove from metadata store."""
    from s3_client import delete_from_s3
    
    # Check if file exists in metadata store
    entry = metadata_store.get_entry(s3_key)
    if not entry:
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        # Delete from S3
        delete_from_s3(s3_key)
        # Remove from metadata store
        metadata_store.remove_entry(s3_key)
        return {"message": "File deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to delete file: {e}"
        )


@app.get("/")
def read_root():
    """Root endpoint with API information."""
    return {
        "message": "CloudPocket API",
        "version": "1.0.0",
        "endpoints": {
            "upload": "POST /upload/",
            "download": "GET /download/{s3_key}",
            "list": "GET /files/",
            "delete": "DELETE /delete/{s3_key}"
        }
    }
