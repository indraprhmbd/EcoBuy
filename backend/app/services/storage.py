import logging

import boto3
from botocore.exceptions import ClientError

from app.core.config import settings

logger = logging.getLogger(__name__)

class StorageService:
    def __init__(self):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=settings.S3_ACCESS_KEY,
            aws_secret_access_key=settings.S3_SECRET_KEY,
            region_name=settings.S3_REGION,
            endpoint_url=settings.S3_ENDPOINT_URL if settings.S3_ENDPOINT_URL else None
        )
        self.bucket = settings.S3_BUCKET

    def upload_file(self, file_data, object_name: str) -> str:
        """Upload a file to an S3 bucket and return the public URL"""
        try:
            self.s3.put_object(
                Bucket=self.bucket,
                Key=object_name,
                Body=file_data,
                ContentType='image/jpeg' # Default, should be dynamic
            )
            
            if settings.S3_ENDPOINT_URL:
                return f"{settings.S3_ENDPOINT_URL}/{self.bucket}/{object_name}"
            return f"https://{self.bucket}.s3.{settings.S3_REGION}.amazonaws.com/{object_name}"
        except ClientError as e:
            logger.error(f"S3 upload failed: {e}")
            raise e
