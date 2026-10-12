from collections.abc import Callable
from typing import Any


def collect_experiments(
    fetch_page: Callable[[str | None], dict[str, Any]],
    start_cursor: str | None = None,
    max_retries: int = 2,
) -> list[dict[str, Any]]:
    """Collect unique experiments from a cursor-paginated API."""
    if type(max_retries) is not int or max_retries < 0:
        raise ValueError("max_retries must be non-negative")

    res = []
    seen_ids = set()
    seen_cursors = set()
    cursor = start_cursor

    while True:
        if cursor in seen_cursors:
            raise ValueError("Repeated cursor")
        
        seen_cursors.add(cursor)

        for attempt in range(max_retries + 1):
            try:
                page = fetch_page(cursor)
                break
            except TimeoutError:
                if attempt == max_retries:
                    raise
        
        # Validate Page
        if not isinstance(page, dict):
            raise ValueError("Invalid page")
        
        if "items" not in page or "next_cursor" not in page:
            raise ValueError("Missing fields")
        
        items = page["items"]
        next_cursor = page["next_cursor"]

        if not isinstance(items, list):
            raise ValueError("Invalid items")
        
        if next_cursor is not None and not isinstance(next_cursor, str):
            raise ValueError("Invalid cursor")

        # Duplicate experiments
        for item in items:
            if not isinstance(item, dict):
                raise ValueError("Invalid item")
            
            item_id = item.get("id")
            if not isinstance(item_id, str):
                raise ValueError("Invalid ID")
            
            if item_id not in seen_ids:
                seen_ids.add(item_id)
                res.append(item.copy())
        
        if next_cursor is None:
            break
        
        cursor = next_cursor

    return res