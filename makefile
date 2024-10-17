pkg_build:
	python setup.py bdist_wheel
pkg_upload:
	twine upload dist/*
pkg_clean:
	rm -rf build dist *.egg-info
test:
	pytest