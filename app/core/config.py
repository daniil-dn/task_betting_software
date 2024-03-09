from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings

load_dotenv('.env_uvicorn')
BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """SERVER CONFIG"""
    DEBUG: Optional[bool] = True

    @validator("DEBUG", pre=True)
    def assemble_debug(cls, v: Union[str, List[str]], values: Dict[str, Any]) -> Any:

        if v:
            return v
        else:
            return False

    API_V1_STR: str = "/api/v1"

    # 60 minutes * 24 hours * 8 days = 8 days
    SERVER_NAME: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: str
    RABBITMQ_LOGIN: str
    RABBITMQ_PASSWORD: str
    ARMQ_URL: str = None

    @validator("ARMQ_URL", pre=True)
    def assemble_armq_url(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            print(v)
            return v

        host = values.get("RABBITMQ_HOST")
        port = values.get("RABBITMQ_PORT")
        login = values.get("RABBITMQ_LOGIN")
        password = values.get("RABBITMQ_PASSWORD")

        if all([host, port, login, password]):
            return f"amqp://{login}:{password}@{host}:{port}"
        else:
            return None

    SERVER_HOST: AnyHttpUrl

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str

    # PYTHONPATH
    PYTHONPATH: str

    """USERBOT CONFIG"""
    USER_BOT_API_ID: int
    USER_BOT_API_HASH: str

    # logger config
    LOGGER_PATH: Path = None
    LOGGER_ROTATION: str = "10 MB"
    LOGGER_COMPRESSION: str = "zip"
    LOGGER_DEBUG: bool = False
    LOGGER_LEVELS: list = []

    @validator("LOGGER_LEVELS", pre=True)
    def assemble_logger_level(cls, v: Optional[list], values: Dict[str, Any]) -> Any:

        debug_lvl = values.get("LOGGER_DEBUG")

        if debug_lvl is True:
            return ["INFO", "DEBUG", "ERROR"]
        else:
            return ["INFO", "ERROR"]

    @validator("LOGGER_PATH", pre=True)
    def assemble_logger_path(cls, v: Optional[list], values: Dict[str, Any]) -> Any:

        python_path = values.get("PYTHONPATH")

        if python_path:
            return Path(python_path).resolve() / 'app' / 'logs'

        else:
            return BASE_DIR / 'logs'

    class Config:
        case_sensitive = True


settings = Settings()
