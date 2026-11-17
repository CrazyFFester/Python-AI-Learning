# Python gaps after CS50P

What CS50P skips and an AI backend engineer uses every day. Roadmap v3, Level 0, module 1.

| # | Topic | Covers | Status |
|---|-------|--------|--------|
| 01 | Errors and exceptions | tutorial ch. 8: chaining (`raise ... from`), `finally` semantics, `add_note`, `ExceptionGroup` | ⬜ |
| 02 | Classes and scopes | tutorial ch. 9: namespaces, `nonlocal`/`global`, closures, dunder methods, iterator protocol | ⬜ |
| 03 | Iterators and generators | `yield`, `yield from`, generator expressions, `itertools`, lazy pipelines | ⬜ |
| 04 | Decorators | functions as objects, `functools.wraps`, decorators with arguments, class decorators, `lru_cache` | 🟨 |
| 05 | Context managers | `__enter__`/`__exit__`, `contextlib.contextmanager`, `ExitStack`, `suppress` | ⬜ |
| 06 | Type hints | generics, `Protocol`, `TypedDict`, `Callable`, mypy in strict mode | ⬜ |
| 07 | Dataclasses | `field`, `frozen`, `slots`, `__post_init__`, vs `NamedTuple` and Pydantic | ⬜ |
| 08 | pytest in depth | `parametrize`, fixtures and scopes, `conftest.py`, `tmp_path`, `monkeypatch`, `capsys` | ⬜ |
| 09 | Packaging and tooling | `pyproject.toml`, uv, `src/` layout, Ruff, entry points | ⬜ |

## Conventions

- One folder per topic: `NN-topic/` with the practice code and its `test_*.py` next to it.
- Code and tests live here; theory goes to Obsidian, definitions and formulas to Anki.
- A topic is done when its tests pass and I can explain it without notes.
- Never name a module after the stdlib (`dataclasses.py`, `typing.py`, `contextlib.py`): pytest puts the test folder first on `sys.path`, so the stdlib module gets shadowed. Use names like `dataclass_drills.py` instead.
