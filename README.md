# OTUS. MLflow Local

Готовое решение для развертывания MLflow сервера с использованием Docker. Включает в себя MinIO в качестве S3-совместимого хранилища для артефактов и MySQL для хранения метаданных.

## Описание

Этот проект предоставляет настроенную инфраструктуру для MLflow с:
- MLflow сервер
- MinIO (S3-совместимое хранилище)
- MySQL база данных
- Поддержка Docker и docker-compose

## Установка

### Предварительные требования
- Docker
- docker-compose

### Быстрый старт

1. Клонируйте репозиторий:

```bash
git clone https://github.com/NickOsipov/otus-mlflow-local.git
cd otus-mlflow-local
```

2. Создайте файл .env со следующими переменными:

```bash
AWS_ACCESS_KEY_ID=minio
AWS_SECRET_ACCESS_KEY=minio123
MYSQL_DATABASE=mlflow_database
MYSQL_USER=mlflow_user
MYSQL_PASSWORD=mlflow
MYSQL_ROOT_PASSWORD=mysql
```

3. Запустите сервер:

Через make:
```bash
make up
```

Через invoke:
```bash
# Создать виртуальное окружение
python3 -m venv .venv
# Активировать виртуальное окружение
source .venv/bin/activate
# Установить зависимости
pip install -r requirements.txt
# Запустить сервисы
invoke up
```

MLflow UI будет доступен по адресу: http://localhost:5000

## Contributing

1. Fork репозитория
2. Создайте ветку для новой функциональности
3. Отправьте pull request

## Лицензия

MIT License

## Автор

[Nick Osipov](https://t.me/NickOsipov)

https://blog.min.io/back-up-restic-minio/