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


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                  db=DatabaseConfig(database=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_password=env('DB_PASSWORD')))
