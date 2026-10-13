from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name : str = "FastAPI_Shop"
    debug : True 
    database_url : str = 'sqlite:///./shop.db'
    cors_orogins : list = [
        "https: //localhost:5173",
        "https: //localhost:3000",
        "https: //127.0.1:5173",
        "https: //127.0.1:3000"
    ]
    static_dir : str = "static"
    image_dir : str = "static/images"
    
    class Config:
        env_file = '.env'
        

settings = Settings()