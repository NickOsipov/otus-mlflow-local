from invoke import task

@task
def down(ctx):
    """Остановить и удалить все контейнеры"""
    ctx.run("docker-compose down")

@task
def build(ctx):
    """Собрать образы"""
    ctx.run("docker-compose build")

@task
def up(ctx):
    """Запустить сервисы с пересборкой"""
    ctx.run("docker-compose up -d --build")

@task
def reqs(ctx):
    """Обновить зависимости"""
    ctx.run("uv add --requirements requirements.txt")