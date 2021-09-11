from peewee import PostgresqlDatabase

from bot import settings

db = PostgresqlDatabase(
    settings.DB_NAME,
    host=settings.POSTGRES_HOST,
    port=settings.POSTGRES_PORT,
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD
)
