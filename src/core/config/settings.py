from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        case_sensitive: bool = True
        env_file: str = '.env'


settings: Settings = Settings() # noqa

TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": [
                "src.app.db.models.tasks",
                "src.app.db.models.users",
                "src.app.db.models.refresh_token",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}

TORTOISE_ORM_TEST = {
    "connections": {"default": "sqlite://:memory:"},
    "apps": {
        "models": {
            "models": [
                "src.app.db.models.tasks",
                "src.app.db.models.users",
                "src.app.db.models.refresh_token",
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}


