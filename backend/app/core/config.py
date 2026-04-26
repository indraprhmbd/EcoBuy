from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Eco Buy"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/ecobuy"
    
    S3_BUCKET_NAME: str = "ecobuy-assets"
    S3_REGION: str = "ap-southeast-1"
    S3_ACCESS_KEY_ID: str = ""
    S3_SECRET_ACCESS_KEY: str = ""
    S3_ENDPOINT: str = "" # For MinIO or other S3-compat
    GEMINI_API_KEY: str = ""
    HUGGINGFACE_API_KEY: str = ""
    HF_MODEL_ID: str = "google/vit-base-patch16-224"


    model_config = ConfigDict(env_file=".env", extra="ignore")


settings = Settings()

