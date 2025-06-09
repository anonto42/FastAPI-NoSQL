from pydantic import BaseSettings

class env_vars( BaseSettings ):
    JWT_SECRET: str

    class Config:
        env_file = ".env"

env = env_vars()