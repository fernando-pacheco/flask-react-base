lint:
	blue . && isort . --profile black --line-length 79
test: lint
	pytest -s -x --cov=src -vv
build:
	docker compose up --build -d
db:
	docker compose up --force-recreate db
backend:
	docker compose up --force-recreate db management