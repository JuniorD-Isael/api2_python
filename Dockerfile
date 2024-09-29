# Dockerfile for API2 (FastAPI with Poetry)
FROM python:3.11-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the pyproject.toml and poetry.lock first to leverage caching
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the application
COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
