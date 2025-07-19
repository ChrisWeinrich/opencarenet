# Aider Coding Instructions (read‑only)

When Aider generates or modifies **any** code in this repository, it **must**:

1. **Pass Ruff** according to the repository's configuration.
2. **Pass MyPy** with the project's strict settings.
3. If Ruff or MyPy report issues, **adjust the code automatically** until the checks succeed.
4. Prefer type‑annotations and dataclasses; avoid `Any` unless unavoidable.
5. Do not relax linter/type rules globally; fix the underlying code instead.
