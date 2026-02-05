#!/usr/bin/env sh
set -e

# Defaults
: "${UVICORN_HOST:=0.0.0.0}"
: "${UVICORN_PORT:=8000}"

# Wait for Postgres if configured
if [ -n "$POSTGRES_HOST" ]; then
	echo "Waiting for Postgres at $POSTGRES_HOST:${POSTGRES_PORT:-5432}..."
	for i in $(seq 1 30); do
		nc -z "$POSTGRES_HOST" "${POSTGRES_PORT:-5432}" && break
		sleep 1
	done
fi

exec uvicorn app.main:app --host "$UVICORN_HOST" --port "$UVICORN_PORT" --reload

