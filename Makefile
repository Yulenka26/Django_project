run:
	uv run src/project/manage.py runserver

lint:
	uv run pre-commit run --all

create_migrations:
	uv run src/project/manage.py makemigrations

migrate:
	uv run src/project/manage.py migrate

admin:
	uv run src/project/manage.py createsuperuser

print:
	uv run src/project/manage.py print_post

publish:
	uv run src/project/manage.py print_published_posts

create:
	uv run src/project/manage.py create_post

delete:
	uv run src/project/manage.py delete_post

update:
	uv run src/project/manage.py update_post

test_blog_app:
	uv run src/project/manage.py test blog_app

test_feedback_app:
	uv run src/project/manage.py test feedback_app

test:
	uv run src/project/manage.py test

test_verbose:
	uv run src/project/manage.py test -v 2

check:
	uv run src/project/manage.py check

dump_all:
	uv run src/project/manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 --output fixtures/datadump.json

restore:
	uv run src/project/manage.py loaddata fixtures/datadump.json

create_db:
	docker run \
	--name blog_db \
	-e POSTGRES_USER=myuser \
	-e POSTGRES_PASSWORD=mypassword \
	-e POSTGRES_DB=mydb \
	-p 5432:5432 \
	-v blog_db_data:/var/lib/postgresql/data \
	-d postgres:17

stop_db:
	docker stop blog_db

remove_db:
	docker rm blog_db

remove_db_force:
	docker rm -f blog_db

remove_storage:
	docker volume rm blog_db_data

start_db:
	docker start blog_db

create_container:
	docker run \
	--name blog \
	--network blog_net \
	-p 8000:8000 \
	--env-file .env \
	-d blog_image

create_image:
	docker build -t blog_image .

delete_container:
	docker rm -f blog

in_container:
	docker exec -it blog bash

connecting_storage:
	 docker run --name blog \
	 --network blog_net \
	 -p 8000:8000 \
	 --env-file .env \
	 -v ./src/project/media/:/app/src/project/media/ \
	 -d blog_image

run_all: migrate restore
	uv run src/project/manage.py runserver 0.0.0.0:8000

compose_start:
	docker compose up -d

compose_rebuild:
	docker compose up -d --build

compose_logs:
	docker compose logs -f

compose_down: #останавливаем  docker compose, удаляем контейнеры
	docker compose down

check_celery:
	uv run celery -A blog_project --workdir=src/project inspect registered

run_celery:
	uv run celery -A blog_project --workdir=src/project worker -l INFO --pool=solo

celery_run_docker:
	uv run celery -A blog_project --workdir=src/project worker -l INFO
