FROM python:3.13-slim-bookworm@sha256:9d7f287598e1a5a978c015ee176d8216435aaf335ed69ac3c38dd1bbb10e8d64

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Create a dedicated runtime identity so the application is not PID 1 as root.
RUN groupadd --system app \
    && useradd --system --gid app --home-dir /app --no-create-home app

COPY pyproject.toml ./
COPY src ./src

RUN python -m pip install --no-cache-dir .

USER app
EXPOSE 8000

CMD ["uvicorn", "containerised_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
