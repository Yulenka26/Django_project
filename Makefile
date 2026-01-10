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

print:
	python manage.py print_post

publish:
	python manage.py print_published_posts

create:
	python manage.py create_post

delete:
	python manage.py delete_post

update:
	python manage.py update_post
