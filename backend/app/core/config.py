import secrets
from typing import List
from typing import Optional
from typing import Union

from pydantic import AnyHttpUrl
from pydantic import BaseSettings
from pydantic import PostgresDsn
from pydantic import validator
from pydantic import RedisDsn


class Settings(BaseSettings):
    DEBUG: Optional[bool] = True
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    CURRENT_API_BASE_URL: Optional[AnyHttpUrl]
    FILE_ALLOWED_SIZE: int = 100_000_000
    REQUIRE_VERIFICATION: Optional[bool] = True
    """
    Delay in seconds for fetch data
    """

    POSTGRES_DB: Optional[str] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None
    POSTGRES_SERVER: Optional[str] = None
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    REDIS_DATABASE_URI: Optional[RedisDsn] = None
    DATABASE_URL: Optional[str] = None

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True


settings = Settings()
