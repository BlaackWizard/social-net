.PHONY: migrations
migrations:
	alembic -c src/subscription/adapters/db/alembic/alembic.ini revision --autogenerate

.PHONY: upgrade-migrations
upgrade-migrations:
	alembic -c src/subscription/adapters/db/alembic/alembic.ini upgrade head

