from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str           # Database name
    db_host: str            # Database URL
    db_user: str            # Username of the database user
    db_password: str        # Database password


@dataclass
class TgBot:
    token: str              # Telegram bot access token
    admin_ids: list[int]    # List of id administrators of the bot


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('bot_token'),
                               admin_ids=list(map(int, env.list('admin_ids')))),
                  db=DatabaseConfig(database=env('database'),
                                    db_host=env('db_host'),
                                    db_user=env('db_user'),
                                    db_password=env('db_password')))
