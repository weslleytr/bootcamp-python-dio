run:
	@poetry run uvicorn store.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest

test-matching:
	@poetry run pytest -s -rx -k $(K) --pdb store ./tests/
#make test-matching K=test_usecases_update_should_return_success
#source C:/Users/wesli/AppData/Local/pypoetry/Cache/virtualenvs/tdd-project-xc7tcPV0-py3.13/Scripts/activate
