# TestPyPI Package Demo

This repository contains a single safe package, `emantto-gurobi-poc`, for publishing to `TestPyPI` and demonstrating a visible install result.

The package installs a console command that prints:

```text
INJECTED DEMO: TestPyPI package selected
```

## Files

- `pyproject.toml`: package metadata
- `src/emantto_gurobi_poc/__init__.py`: package code and console entrypoint
- `.github/workflows/publish-testpypi.yml`: GitHub Actions publish workflow

## Publish with GitHub Actions

Use the workflow in [.github/workflows/publish-testpypi.yml](/home/nicobuzeta/Documents/latamairlines/emantto-gurobi-test/.github/workflows/publish-testpypi.yml#L1).

It:

- builds the root package
- publishes it to `https://test.pypi.org/legacy/`

Configure the project on `TestPyPI` to trust this GitHub repository before running the workflow.

## Verify after publish

```bash
python -m venv .venv-testpypi
. .venv-testpypi/bin/activate
env -u PIP_INDEX_URL -u PIP_EXTRA_INDEX_URL -u PIP_TRUSTED_HOST \
  python -m pip install --isolated --disable-pip-version-check --no-cache-dir \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  emantto-gurobi-poc
emantto-gurobi-poc
```
