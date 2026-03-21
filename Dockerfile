FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim

WORKDIR /app

RUN apt update && apt install make

ENV PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml uv.lock README.md ./

COPY src/project/__init__.py ./src/project/

RUN uv sync --frozen

COPY . .

CMD ["uv", "run", "src/project/manage.py", "runserver", "0.0.0.0:8000"]
