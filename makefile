.PHONY: clean dist install dev release test lint format

clean: ## Remove build artifacts
	rm -rf build/ dist/ *.egg-info

dist: clean ## Build source and wheel package
	uv build

install: ## Install package to current environment
	uv pip install -e .

dev: ## Install with dev dependencies
	uv pip install -e ".[dev]"

test: ## Run tests
	uv run pytest

release: dist ## Upload package to PyPI
	uv publish

lint: ## Check code style
	ruff check .

format: ## Format code
	ruff format .