from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Eco Buy"
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/ecobuy"
    
    S3_BUCKET: str = "ecobuy-assets"
    S3_REGION: str = "ap-southeast-1"
    S3_ACCESS_KEY: str = ""
    S3_SECRET_KEY: str = ""
    S3_ENDPOINT_URL: str = "" # For MinIO or other S3-compat

    model_config = ConfigDict(env_file=".env", extra="ignore")

settings = Settings()

