from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv(
        "APP_NAME",
        "Multi-Agent AI Research Assistant"
    )

    APP_VERSION: str = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    DEBUG: bool = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"

    HOST: str = os.getenv(
        "HOST",
        "127.0.0.1"
    )

    PORT: int = int(
        os.getenv(
            "PORT",
            "8000"
        )
    )


settings = Settings()