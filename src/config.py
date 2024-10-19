import os

from pydantic import BaseModel
from yaml import safe_load

CONFIG_DIR = os.getcwd() + '/configs'


class BotConfig(BaseModel):
    token: str
    admin_id: int


class DBConfig(BaseModel):
    database: str
    host: str
    user: str
    password: str

    @property
    def url(self) -> str:
        return f'postgresql+asyncpg://{self.user}:{self.password}' \
               f'@{self.host}/{self.database}'


class RedisConfig(BaseModel):
    host: str
    port: int

    @property
    def url(self) -> str:
        return f'redis://{self.host}:{self.port}'


class LoggingConfig(BaseModel):
    level: str


class Config(BaseModel):
    bot: BotConfig
    db: DBConfig
    redis: RedisConfig
    logging: LoggingConfig

    @classmethod
    def create(cls, config_file: str) -> 'Config':
        with open(f'{CONFIG_DIR}/{config_file}', mode='r', encoding='utf-8') as file:
            data = safe_load(file)
        return Config(
            bot=BotConfig(**data['bot']),
            db=DBConfig(**data['db']),
            redis=RedisConfig(**data['redis']),
            logging=LoggingConfig(**data['logging'])
        )
