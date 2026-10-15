import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

import main


class TaskTrackerTests(unittest.TestCase):
    def test_add_task_strips_title_and_sets_not_done(self):
        tasks = []
        with patch("builtins.input", return_value="  Study Python  "):
            main.add_task(tasks)

        self.assertEqual(tasks, [{"title": "Study Python", "done": False}])

    def test_add_task_rejects_empty_title(self):
        tasks = []
        with patch("builtins.input", return_value="   "):
            main.add_task(tasks)

        self.assertEqual(tasks, [])

    def test_complete_task_marks_selected_task_done(self):
        tasks = [{"title": "Read chapter 7", "done": False}]
        with patch("builtins.input", return_value="1"):
            main.complete_task(tasks)

        self.assertTrue(tasks[0]["done"])

    def test_remove_task_removes_selected_task(self):
        tasks = [
            {"title": "First task", "done": False},
            {"title": "Second task", "done": False},
        ]
        with patch("builtins.input", return_value="2"):
            main.remove_task(tasks)

        self.assertEqual(tasks, [{"title": "First task", "done": False}])

    def test_show_tasks_reports_empty_list(self):
        output = StringIO()
        with redirect_stdout(output):
            main.show_tasks([])

        self.assertIn("No tasks yet", output.getvalue())


if __name__ == "__main__":
    unittest.main()
