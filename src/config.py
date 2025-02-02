from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    DATABSE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHUM: str
    REDIS_URL: str
    model_conf = SettingsConfigDict(env_file=".env",extra="ignore")


config = Settings()

broker_url = config.REDIS_URL
result_be = config.REDIS_URL
broker_connenction_retry_on_startup = True