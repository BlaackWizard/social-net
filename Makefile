.PHONY: migrations
migrations:
	alembic -c src/subscription/adapters/db/alembic/alembic.ini revision --autogenerate
	alembic -c src/auth/adapters/db/alembic/alembic.ini revision --autogenerate

.PHONY: upgrade-migrations
upgrade-migrations:
	alembic -c src/subscription/adapters/db/alembic/alembic.ini upgrade head
	alembic -c src/auth/adapters/db/alembic/alembic.ini upgrade head

