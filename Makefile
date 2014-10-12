
## pycd10api Makefile

.PHONY: default serve


default: serve

help:
	@echo "help		--	print help"
	@echo "serve	--  serve the application locally"

develop:
	python setup.py develop

get_data:
	(cd ./data; ./get_icd10.sh)

test_setup:
	pip install -r requirements-test.txt
	touch test_setup

test: test_setup
	python setup.py nosetests

setup:
	$(MAKE) develop
	$(MAKE) get_data
	$(MAKE) test


serve:
	pserve ./pycd10api.ini
