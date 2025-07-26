import boto3
import os
from typing import Optional
from botocore.exceptions import ClientError, NoCredentialsError

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
S3_BUCKET = os.environ.get("S3_BUCKET")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)


def upload_to_s3(file_bytes: bytes, s3_key: str) -> None:
    """Upload file bytes to S3 bucket."""
    try:
        s3.put_object(Bucket=S3_BUCKET, Key=s3_key, Body=file_bytes)
    except (ClientError, NoCredentialsError) as e:
        raise Exception(f"Failed to upload to S3: {e}")


def download_from_s3(s3_key: str) -> Optional[bytes]:
    """Download file from S3 bucket by key."""
    try:
        obj = s3.get_object(Bucket=S3_BUCKET, Key=s3_key)
        return obj['Body'].read()
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return None
        raise Exception(f"Failed to download from S3: {e}")
    except NoCredentialsError as e:
        raise Exception(f"AWS credentials not found: {e}")


def delete_from_s3(s3_key: str) -> bool:
    """Delete file from S3 bucket by key."""
    try:
        s3.delete_object(Bucket=S3_BUCKET, Key=s3_key)
        return True
    except ClientError as e:
        raise Exception(f"Failed to delete from S3: {e}")
    except NoCredentialsError as e:
        raise Exception(f"AWS credentials not found: {e}")


def list_s3_objects(prefix: str = "") -> list:
    """List objects in S3 bucket with optional prefix."""
    try:
        response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=prefix)
        return response.get('Contents', [])
    except ClientError as e:
        raise Exception(f"Failed to list S3 objects: {e}")
    except NoCredentialsError as e:
        raise Exception(f"AWS credentials not found: {e}")
