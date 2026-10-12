import unittest

from practice.task_24_circular_queue.starter import CircularQueue


class Tests(unittest.TestCase):
    def test_basic_state(self):
        queue = CircularQueue(2)
        self.assertTrue(queue.is_empty())
        self.assertTrue(queue.enqueue("a")); self.assertTrue(queue.enqueue("b"))
        self.assertFalse(queue.enqueue("c")); self.assertTrue(queue.is_full())
        self.assertEqual((queue.front(), queue.rear(), len(queue)), ("a", "b", 2))

    def test_wraparound(self):
        queue = CircularQueue(3)
        for value in [1, 2, 3]: self.assertTrue(queue.enqueue(value))
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertTrue(queue.enqueue(4)); self.assertTrue(queue.enqueue(5))
        self.assertEqual([queue.dequeue(), queue.dequeue(), queue.dequeue()], [3, 4, 5])
        self.assertTrue(queue.is_empty())

    def test_empty_errors(self):
        queue = CircularQueue(1)
        for method in [queue.dequeue, queue.front, queue.rear]:
            with self.subTest(method=method.__name__), self.assertRaises(IndexError): method()

    def test_validation(self):
        for capacity in [0, -1, 1.5, True]:
            with self.subTest(capacity=capacity), self.assertRaises(ValueError): CircularQueue(capacity)


if __name__ == "__main__":
    unittest.main()
