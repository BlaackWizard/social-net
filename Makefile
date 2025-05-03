PYTHONPATH := /Users/asylbek/Documents/pet-projects/social-net

.PHONY: create-auth-migrations
create-auth-migrations:
	cd src/auth/adapters/db/alembic && PYTHONPATH=$(PYTHONPATH) alembic revision --autogenerate

.PHONY: create-subscription-migrations
create-subscription-migrations:
	cd src/subscription/adapters/db/alembic && PYTHONPATH=$(PYTHONPATH) alembic revision --autogenerate

.PHONY: upgrade-auth-migrations
upgrade-auth-migrations:
	cd src/auth/adapters/db/alembic && PYTHONPATH=$(PYTHONPATH) alembic upgrade head

.PHONY: upgrade-subscription-migrations
upgrade-subscription-migrations:
	cd src/subscription/adapters/db/alembic && PYTHONPATH=$(PYTHONPATH) alembic upgrade head

.PHONY: create-all-migrations
create-all-migrations:
	make create-auth-migrations
	make create-subscription-migrations

.PHONY: upgrade-all-migrations
upgrade-all-migrations:
	make upgrade-auth-migrations
	make upgrade-subscription-migrations
