# проект "docker_delicious_way" 
Этот репозиторий содержит Dockerfile и скрипты для сборки и запуска приложения (сайта) в Docker-контейнере с использованием базы данных PostgreSQL.
Веб-приложение (подробное описание в репозитории ![django_delicious_way](https://github.com/alenaVSk/django_delicious_way)).
## Технологии
* Python 3.10.12
* Django  4.2
* PostgreSQL 
* Docker 27.1.2
* Docker Compose (опционально, для упрощения запуска) v2.29.1
## Установка и запуск:
### 1. Клонируйте репозиторий:
```python
git clone https://github.com/alenaVSk/docker_delicious_way.git
```
### 2. Сборка Docker-образа:
```python
docker-compose build
```
### 3. Запуск:
```python
docker-compose up -d
```
### 4. Миграции:
```python
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
### 5. Перенести данные:
```
docker-compose exec db psql -U <имя пользователя PostgreSQL> -d delisious_way -f /dumps/dump_dw
```
### 6. Открыть в браузере:
0.0.0.0:8000


