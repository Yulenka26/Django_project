run:
	uv run src/project/manage.py runserver

lint:
    uv run pre-commit run --all
