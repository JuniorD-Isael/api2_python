FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y tesseract-ocr libgl1

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

COPY . .


EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
