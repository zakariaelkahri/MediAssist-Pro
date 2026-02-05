from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config =  SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False        
    )
    
    
    
    PROJECT_NAME: str = "MediAssist"
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    # for rag
    EMBEDDING_MODEL: str
    
    # db
    DATABASE_URL: str
    
    # rout
    API_V1_STR: str = "/api/v1"
    

        

settings = Settings()
        