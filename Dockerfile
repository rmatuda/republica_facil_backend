FROM python:3.13-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY republica_facil/ ./republica_facil
COPY README.md ./

RUN pip install --no-cache-dir poetry

RUN poetry install --no-interaction --no-root

EXPOSE 8000

CMD ["poetry", "run", "fastapi", "dev", "republica_facil/app.py", "--host", "0.0.0.0"]