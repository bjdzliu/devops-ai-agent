import os
from fastapi import FastAPI
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import yaml

# Load environment variables
load_dotenv()

from pydantic import Field

class Settings(BaseSettings):
    # Database configuration
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_NAME: str = Field(..., env="DB_NAME")
    
    # # API configuration
    # api_base_url: str
    # api_timeout: int
    # api_retries: int
    
    # # Jenkins configuration
    # jenkins_url: str
    # jenkins_user: str
    # jenkins_token: str
    
    # # GitHub configuration
    # github_base_url: str
    # github_token: str
    
    # # JFrog configuration
    # jfrog_url: str
    # jfrog_user: str
    # jfrog_password: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        extra = 'forbid'

# Load YAML config
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

# Initialize FastAPI
app = FastAPI()

try:
    settings = Settings()
except Exception as e:
    print(f"Configuration error: {str(e)}")
    raise

@app.get("/")
async def root():
    return {"message": "AI Agent is running"}

if __name__ == "__main__":
    import uvicorn
    print(settings.DB_HOST)
    uvicorn.run(app, host="0.0.0.0", port=8000)
