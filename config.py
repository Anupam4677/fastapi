from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str ='localhost'
    database_port: str = '5432'
    database_password: str ='Muzaffarpur@10'
    database_name: str ='fastapi'
    database_username: str = 'postgres'
    secret_key: str = 'OHBDTFBSNY6Y3780KSG23453BBDJD7667NDEJY6TWJW99X65544R2Y48'
    algorithm: str = 'HS256'
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

# DATABASE_HOSTNAME=localhost
# DATABASE_PORT=5432
# DATABASE_PASSWPRD=Muzaffarpur@10
# DATABASE_NAME= fastapi
# DATABASE_USERNAME=postgres
# SECRET_KEY=OHBDTFBSNY6Y3780KSG23453BBDJD7667NDEJY6TWJW99X65544R2Y48
# ALGORITHM=HS256
settings = Settings()
print(settings)