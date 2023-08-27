import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:    
    # We use the singleton creational design pattern to ensure we always have only one instance of this class
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Settings, self).__new__(self)
        return self.instance
    
    DB_USER = os.getenv("POSTGRES_USER")
    DB_NAME = os.getenv("POSTGRES_DB")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_HOST= os.getenv("POSTGRES_SERVER")
    DB_PORT = os.getenv("POSTGRES_PORT")
    DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
settings:Settings = Settings()