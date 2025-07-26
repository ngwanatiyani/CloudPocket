# CloudPocket

This project is a minimal, academic distributed storage system built with Python and FastAPI. It provides a REST API that allows users to upload, list, and download files using AWS S3 as the storage backend, while maintaining an in-memory index for metadata.

## Features

- **Upload Files**: Store files in AWS S3 via a REST API.
- **Download Files**: Retrieve files from S3 by S3 key.
- **List Files**: View all filenames uploaded in the current server session.
- **Concurrent Access**: FastAPI enables handling multiple requests at once.
- **In-Memory Metadata Index**: Metadata is stored in memory for simplicity.

## Requirements

- Python 3.7 or newer
- AWS account with access keys
- An S3 bucket for storage

## Setup

1. **Clone the Repository**
    ```bash
    git clone <your-repo-url>
    cd <repo-directory>
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Environment Variables**
    Make sure to set your AWS credentials and bucket name:
    ```bash
    export AWS_ACCESS_KEY_ID=your_access_key
    export AWS_SECRET_ACCESS_KEY=your_secret_key
    export AWS_REGION=your_aws_region
    export S3_BUCKET=your_bucket_name
    ```

4. **Run the Server**
    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints

### `POST /upload/`
Upload a file.

- **Request:**  
  - Form-data, with a `file` field.

- **Response:**  
  - JSON with upload status and the assigned `s3_key`.

### `GET /download/{s3_key}`
Download a file by its S3 key.

- **Request:**  
  - URL parameter: `s3_key`

- **Response:**  
  - File stream (binary content)

### `GET /files/`
List all filenames uploaded during the current server session.

- **Response:**  
  - JSON list of filenames

## Notes

- **Metadata is not persistent:**  
  The in-memory index is cleared if the server restarts, but files remain in S3.

- **No authentication:**  
  Anyone with API access can upload, list, or download files.

- **For demonstration and academic purposes only.**  
  Not suitable for production without enhancements (persistent metadata, authentication, error handling, etc.).

## Example Usage

```bash
# Upload a file
curl -F "file=@path/to/yourfile.txt" http://localhost:8000/upload/

# List files
curl http://localhost:8000/files/

# Download a file
curl -O http://localhost:8000/download/<s3_key>
```

## License

This project is for academic demonstration purposes only.
