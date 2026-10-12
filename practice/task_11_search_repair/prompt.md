# Module 11: Debug and extend a search engine

Original practice exercise; not an actual Benchling interview question.

The starter contains bugs. Repair it and add field filters.

`SearchIndex.search(query)` accepts space-separated tokens. Plain tokens are case-insensitive substring matches against `title` or `body`. Tokens shaped like `field:value` filter exact, case-insensitive equality for `type` and `owner`. All tokens use AND semantics. Return matching IDs in input order. Repeated spaces are ignored; a blank query returns every ID.

Unknown filter fields raise `ValueError`. Documents must have unique `id`, plus string `title`, `body`, `type`, and `owner` fields; validate them in the constructor. Keep an independent copy of the documents so later changes to the caller's list or dictionaries do not affect searches.
