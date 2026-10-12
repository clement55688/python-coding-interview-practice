# 30 — Vending machine

Implement `VendingMachine(catalog)`.

`catalog` maps a product code to `{"price": cents, "stock": count}`. Prices must be positive multiples of 5. Accepted coins are `5`, `10`, `25`, and `100` cents.

- `insert_coin(coin)` adds credit and returns the new balance.
- `select(code)` rejects unknown/out-of-stock products or insufficient funds with `ValueError`; failed selections retain the balance.
- A successful selection decrements stock, resets balance to zero, and returns `{"code": code, "change": [...]}`.
- Return change with the fewest accepted coins, largest denominations first.
- `refund()` resets the balance and returns the inserted value as a minimal coin list.
- `snapshot()` returns a defensive copy of balance and catalog.
- Validate catalog entries, codes, and coins.

Explain object state, invariants, and why greedy change is valid for these denominations.

Follow-up: track a finite internal coin inventory and reject purchases when exact change is unavailable.
