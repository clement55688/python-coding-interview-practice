import unittest

from practice.task_04_workflow_prerequisites.starter import can_run_all


class WorkflowPrerequisitesTests(unittest.TestCase):
    def test_valid_chain_and_independent_steps(self):
        steps = {
            "analyze": ["prepare"],
            "prepare": ["collect"],
            "collect": [],
            "independent": [],
        }
        self.assertTrue(can_run_all(steps))
        self.assertTrue(can_run_all({}))

    def test_cycle_missing_prerequisite_and_duplicate_edge(self):
        self.assertFalse(can_run_all({"a": ["b"], "b": ["a"]}))
        self.assertFalse(can_run_all({"a": ["missing"]}))
        self.assertTrue(can_run_all({"a": ["b", "b"], "b": []}))
