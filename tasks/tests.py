from django.test import TestCase

from .models import Task


class TaskModelTests(TestCase):
    def test_task_str_returns_title(self):
        task = Task.objects.create(title="Buy milk")
        self.assertEqual(str(task), "Buy milk")

    def test_toggle_marks_task_complete(self):
        task = Task.objects.create(title="Write report", completed=False)

        task.toggle()

        self.assertTrue(task.completed)
