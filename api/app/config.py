from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Qiymat yo'q bo'lsa ilova ishga tushmaydi: sozlama kodda emas, env'da turadi.
    database_url: str


settings = Settings()
