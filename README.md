# OpenCareNet

[![CI](https://github.com/opencarenet/opencarenet/actions/workflows/ci.yml/badge.svg)](https://github.com/opencarenet/opencarenet/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> MVP – modular open‑source health‑assistants network.

OpenCareNet is a modular, open-source framework for building health assistant agents. It is designed for extensibility, strict code quality, and modern Python best practices.

---

## Quickstart

1. **Install Poetry** (if not already installed):

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. **Install dependencies:**

    ```bash
    poetry install
    ```

3. **Run tests:**

    ```bash
    poetry run pytest
    ```

4. **Serve docs locally:**

    ```bash
    poetry run mkdocs serve
    ```

---

## Code Quality & Typing

- **Strict typing is enforced** via [mypy](https://mypy-lang.org/) and [ruff](https://docs.astral.sh/ruff/).
- All code must pass type checks and linting before merging.
- Pre-commit hooks are configured for formatting, linting, and typing.

---

🚧 Work in progress.

📖 Official documentation: https://chrisweinrich.github.io/opencarenet/
