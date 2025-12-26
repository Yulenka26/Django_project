run:
	uv run src/project/manage.py runserver

lint:
	uv run pre-commit run --all

create:
	uv run src/project/manage.py makemigrations

migrate:
	uv run src/project/manage.py migrate

admin:
	uv run src/project/manage.py createsuperuser

