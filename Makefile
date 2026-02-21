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
