import unittest

from practice.task_23_sliding_window_limiter.starter import RateLimiter


class Tests(unittest.TestCase):
    def test_limit_and_expiry_boundary(self):
        limiter = RateLimiter(2, 10)
        self.assertTrue(limiter.allow("u", 0))
        self.assertTrue(limiter.allow("u", 2))
        self.assertFalse(limiter.allow("u", 9))
        self.assertTrue(limiter.allow("u", 10))

    def test_keys_are_independent_and_rejections_do_not_count(self):
        limiter = RateLimiter(1, 5)
        self.assertTrue(limiter.allow("a", 1))
        self.assertFalse(limiter.allow("a", 2))
        self.assertTrue(limiter.allow("b", 2))
        self.assertTrue(limiter.allow("a", 6))

    def test_global_timestamp_order(self):
        limiter = RateLimiter(2, 5)
        limiter.allow("a", 4)
        with self.assertRaises(ValueError): limiter.allow("b", 3)

    def test_validation(self):
        for args in [(0, 1), (1, 0), (True, 1), (1, True)]:
            with self.subTest(args=args), self.assertRaises(ValueError): RateLimiter(*args)
        limiter = RateLimiter(1, 1)
        for key, timestamp in [("", 1), (1, 1), ("a", True)]:
            with self.subTest(key=key, timestamp=timestamp), self.assertRaises(ValueError):
                limiter.allow(key, timestamp)


if __name__ == "__main__":
    unittest.main()
