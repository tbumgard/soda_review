run:
	poetry run python ./soda_review/soda_review.py
run_server:
	uvicorn soda_review.main:app --reload
test:
	poetry run pytest
fmt:
	poetry run black .