import sys
from typing import Any, Dict, List, Optional
from pydantic import BaseSettings, HttpUrl, PostgresDsn, validator






class Settings(BaseSettings):
    PROJECT_NAME: str = "Tutu Fashion"
    VERSION: str = "0.1.0"
    SENTRY_DSN: Optional[HttpUrl] = None
    API_PATH: str = "/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS: List[str] = []
    TEST_DATABASE_URL: Optional[PostgresDsn]
    DATABASE_URL: PostgresDsn
    ASYNC_DATABASE_URL: Optional[PostgresDsn]
    TEST_BUCKET_NAME: Optional[str]
    BUCKET_NAME: str
    SECRET_KEY: str
    CLOUD_STORAGE: str
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str
    EMAIL_FROM: str
    EMAIL_PORT: str
    EMAIL_SERVER: str
    EMAIL_START_TLS: bool
    EMAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool
    VALIDATE_CERTS: bool
    TWITTER_API: str
    VITE_APP_BACKEND_URL: str
    GCP_TYPE: str
    GCP_PROJECT_ID: str
    GCP_PRIVATE_KEY_ID: str
    GCP_PRIVATE_KEY: str
    GCP_CLIENT_EMAIL: str
    GCP_CLIENT_ID: str
    GCP_AUTH_URI: str
    GCP_TOKEN_URI: str
    GCP_AUTH_PROVIDER_X509_CERT_URL: str
    GCP_CLIENT_X509_CERT_URL: str


    class Config:
        env_file = ".env"


    @validator("DATABASE_URL", pre=True)
    def build_test_database_url(cls, v: Optional[str], values: Dict[str, Any]):
        if "pytest" in sys.modules:
            if not values.get("TEST_DATABASE_URL"):
                raise Exception("pytest detected, but TEST_DATABASE_URL is not set in environment")
            return values["TEST_DATABASE_URL"]
        return v


    @validator("SYNC_DATABASE_URL")
    def build_test_bucket_name(selfcls, v: Optional[str], values: Dict[str, Any]):
        v= values["DATABASE_URL"]
        return v.replace("postgresql", "postgresql+asyncpg") if v else v


    @validator("BUCKET_NAME", pre=True)
    def build_test_bucket_name(cls, v: Optional[str], values: Dict[str, Any]):
        if "pytest" in sys.modules:
            if not values.get("TEST_BUCKET_NAME"):
                raise Exception("pytest detected, but TEST_BUCKET_NAME is not set in environment")
            return values["TEST_BUCKET_NAME"]
        return v







settings = Settings()




















