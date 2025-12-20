# Development Guide

## Prerequisites

- [uv](https://github.com/astral-sh/uv)
- [ruff](https://github.com/astral-sh/ruff)

## Install Dev Dependencies

```bash
make dev
```

## Generate Data

Data source: [漢語拆字字典](https://github.com/kfcd/chaizi) (CC BY 3.0)

```bash
uv run python raw_data/parse.py
```

This parses the raw data and generates `hanzi_chaizi/data/data.pkl`.

## Run Tests

```bash
make test
```

## Lint

```bash
make lint
```

## Format

```bash
make format
```

## Build Package

```bash
make dist
```

Output will be in `dist/`.

## Publish to PyPI

```bash
make release
```
