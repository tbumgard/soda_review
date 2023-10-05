run:
	poetry run python ./soda_review/soda_review.py
test:
	poetry run pytest
fmt:
	poetry run black .