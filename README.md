# CloudPocket

A cloud storage service built with FastAPI and AWS S3 that allows users to upload, download, list, and delete files.

## Features

- 📁 Upload files to AWS S3
- 📥 Download files from S3
- 📋 List all uploaded files
- 🗑️ Delete files from storage
- 🔒 Thread-safe metadata storage
- ⚡ Fast API with async support

## Requirements

- Python 3.8+
- AWS Account with S3 access
- AWS credentials configured

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ngwanatiyani/CloudPocket.git
cd CloudPocket
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=us-east-1
export S3_BUCKET=your-bucket-name
```

## Usage

1. Start the server:
```bash
uvicorn main:app --reload
```

2. Open your browser and go to `http://localhost:8000/docs` to see the API documentation.

## API Endpoints

- `POST /upload/` - Upload a file
- `GET /download/{s3_key}` - Download a file by S3 key
- `GET /files/` - List all uploaded files
- `DELETE /delete/{s3_key}` - Delete a file
- `GET /` - API information

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | AWS Access Key ID | Required |
| `AWS_SECRET_ACCESS_KEY` | AWS Secret Access Key | Required |
| `AWS_REGION` | AWS Region | `us-east-1` |
| `S3_BUCKET` | S3 Bucket Name | Required |

## Project Structure

```
CloudPocket/
├── main.py              # FastAPI application
├── s3_client.py         # AWS S3 client functions
├── metadata_store.py    # Thread-safe metadata storage
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
