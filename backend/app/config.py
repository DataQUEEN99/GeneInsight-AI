"""Application Configuration Management"""

from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application Settings"""

    # Application
    app_name: str = "GeneInsight AI"
    debug: bool = False
    environment: str = "development"
    version: str = "0.1.0"

    # Database
    database_url: str = Field(..., alias="DATABASE_URL")
    sqlalchemy_echo: bool = False

    # JWT
    secret_key: str = Field(..., alias="SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # LLM
    llm_provider: str = "openai"
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4"
    openai_temperature: float = 0.7
    openai_max_tokens: int = 2000
    anthropic_api_key: Optional[str] = None
    anthropic_model: str = "claude-3-opus-20240229"

    # RAG
    chroma_db_path: str = "./chroma_data"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    chunk_size: int = 512
    chunk_overlap: int = 100
    min_similarity_score: float = 0.6
    top_k_results: int = 5

    # CORS
    cors_origins: str = "http://localhost:5173,http://localhost:3000"
    cors_allow_credentials: bool = True
    cors_allow_methods: str = "*"
    cors_allow_headers: str = "*"

    # Logging
    log_level: str = "INFO"

    # File Upload
    max_upload_size_mb: int = 500
    allowed_file_extensions: str = "vcf,csv,tsv"

    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def cors_origins_list(self) -> list[str]:
        """Parse CORS origins"""
        return [origin.strip() for origin in self.cors_origins.split(",")]

    @property
    def allowed_extensions_list(self) -> list[str]:
        """Parse allowed file extensions"""
        return [ext.strip() for ext in self.allowed_file_extensions.split(",")]


settings = Settings()
