import copy
import importlib
import unittest

collect_experiments = importlib.import_module("practice.task_16_api_pagination.starter").collect_experiments


class Tests(unittest.TestCase):
    def test_pagination_deduplication_and_copy(self):
        pages = {
            None: {"items": [{"id": "e1", "name": "A"}], "next_cursor": "p2"},
            "p2": {"items": [{"id": "e1", "name": "new"}, {"id": "e2"}], "next_cursor": None},
        }
        original = copy.deepcopy(pages)
        result = collect_experiments(lambda cursor: pages[cursor])
        self.assertEqual(result, [{"id": "e1", "name": "A"}, {"id": "e2"}])
        result[0]["name"] = "changed"
        self.assertEqual(pages, original)

    def test_timeout_retry_is_per_cursor(self):
        calls = {None: 0}
        def fetch(cursor):
            calls[cursor] = calls.get(cursor, 0) + 1
            if calls[cursor] < 3:
                raise TimeoutError("slow")
            return {"items": [], "next_cursor": None}
        self.assertEqual(collect_experiments(fetch, max_retries=2), [])
        self.assertEqual(calls[None], 3)

    def test_timeout_budget_and_other_errors(self):
        with self.assertRaises(TimeoutError):
            collect_experiments(lambda _: (_ for _ in ()).throw(TimeoutError()), max_retries=1)
        with self.assertRaises(RuntimeError):
            collect_experiments(lambda _: (_ for _ in ()).throw(RuntimeError("bad")))

    def test_malformed_pages_and_cursor_cycle(self):
        bad_pages = [None, {}, {"items": "bad", "next_cursor": None}, {"items": [{}], "next_cursor": None}]
        for page in bad_pages:
            with self.subTest(page=page), self.assertRaises(ValueError):
                collect_experiments(lambda _: page)
        with self.assertRaises(ValueError):
            collect_experiments(lambda _: {"items": [], "next_cursor": "loop"}, start_cursor="loop")
        with self.assertRaises(ValueError):
            collect_experiments(lambda _: {"items": [], "next_cursor": None}, max_retries=-1)


if __name__ == "__main__":
    unittest.main()

