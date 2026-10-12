# Module 10: Dependency-free JSON schema validator

Original practice exercise; not an actual Benchling interview question.

Implement `validate(value, schema) -> list[str]`. Return deterministic error strings; do not raise for invalid data.

Supported schema keys:

- `type`: `object`, `array`, `string`, `integer`, `number`, or `boolean`.
- Objects: `properties`, `required`, and `additionalProperties` (default `True`).
- Arrays: `items`, `minItems`, and `maxItems`.
- Strings: `minLength` and `maxLength`.

Paths use `$`, `$.name`, and `$[0]`. Report type errors as `PATH: expected TYPE`; required fields as `PATH: required`; unexpected fields as `PATH: unexpected`; and length errors as `PATH: too short` / `too long` / `too few items` / `too many items`.

Do not treat booleans as integers or numbers. Sort object keys when traversing so output is deterministic. An unsupported schema type raises `ValueError`.
