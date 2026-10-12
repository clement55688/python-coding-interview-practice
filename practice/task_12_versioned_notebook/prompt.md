# Module 12: Versioned lab notebook

Original practice exercise; not an actual Benchling interview question.

Implement an in-memory `NotebookStore`.

- `create(entry_id, fields)` creates version 1; duplicate IDs raise `ValueError`. Copy the input fields so later caller mutations do not change stored history.
- `update(entry_id, changes)` creates a new version by shallow-merging fields. The prior version must remain unchanged, and later caller mutations to `changes` must not change stored history.
- `get(entry_id, version=None)` returns a deep defensive copy of the latest or requested version.
- `history(entry_id)` returns version numbers in ascending order.
- `revert(entry_id, version)` creates a new latest version whose content equals the requested old version.
- Missing IDs or versions raise `KeyError`. Entry IDs must be non-empty strings and fields/changes must be dictionaries.

Never expose internal mutable data.
