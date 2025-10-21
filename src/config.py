from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_DEPLOYMENT: str = "gpt-4o-mini"
    OPENAI_API_KEY: str
    
    LANGSMITH_API_KEY: str
    LANGSMITH_TRACING: str
    LANGSMITH_ENDPOINT: str
    LANGSMITH_PROJECT: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        env_prefix = ""
    
settings = Settings()