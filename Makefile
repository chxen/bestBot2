migrate:
	pem migrate

makemigrations:
	pem watch --traceback

run_postgres:
	docker run -e POSTGRES_PASSWORD=bot -e POSTGRES_USER=bot -p 5432:5432 postgres:12.5
