FROM python:3.10.14-alpine
ENV PYTHONUNBUFFERED=1
ENV PYCURL_SSL_LIBRARY=openssl
ENV UV_SYSTEM_PYTHON=true
ENV UV_LINK_MODE=copy
ENV UV_CACHE_DIR=/root/.cache/pip
RUN apk add --no-cache --virtual .build-dependencies build-base curl-dev bash libcurl
RUN mkdir -p /app
WORKDIR /app
COPY pyproject.toml /app/
COPY uv.lock /app/
RUN --mount=type=cache,target=/root/.cache/pip pip install uv && uv sync
COPY . /app/
#RUN python /opt/manage.py check
