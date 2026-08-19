FROM mcr.microsoft.com/playwright/python:latest

ARG TEST_PROFILE=api
ARG BACKEND_URL=http://host.docker.internal:4111/api

ENV TEST_PROFILE=${TEST_PROFILE}
ENV BACKEND_URL=${BACKEND_URL}

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD pytest -m api --alluredir=/app/reports/allure


#
# FROM mcr.microsoft.com/playwright/python:latest
#
# ARG TEST_PROFILE=api
# ARG BACKEND_URL=http://backend:4111/api  # ← поменяли на backend (имя сервиса)
#
# ENV TEST_PROFILE=${TEST_PROFILE}
# ENV BACKEND_URL=${BACKEND_URL}
#
# WORKDIR /app
#
# # Установка системных зависимостей для PostgreSQL
# RUN apt-get update && apt-get install -y \
#     postgresql-client \
#     wait-for-it \
#     && rm -rf /var/lib/apt/lists/*
#
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
#
# # Установка браузеров Playwright
# RUN playwright install chromium --with-deps
#
# COPY . .
#
# # Ждём БД и бэкенд перед запуском
# CMD wait-for-it postgres:5432 -- wait-for-it backend:4111 -- pytest -m api --alluredir=/app/reports/allure