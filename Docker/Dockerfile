FROM python:3.12-slim-bookworm

WORKDIR /app

# Install curl and certificates
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml ./
COPY . . 

RUN rm -rf .venv

EXPOSE ${PORT}

CMD ["uv", "run", "start.py"]