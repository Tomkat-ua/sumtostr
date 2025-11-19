#!/bin/sh

# Встановлює PORT = 8000, якщо він не встановлений у середовищі
PORT=${PORT:-8000}

echo "Starting server on port $PORT"

# Запуск Gunicorn з динамічним портом
exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b "0.0.0.0:${PORT}" "main:app"