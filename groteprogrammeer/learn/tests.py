from django.test import TestCase
from .models import Lesson


# Create your tests here.
class LearnTests(TestCase):

    def test_lesson_str(self):
        # Test unauthenticated user sees the index template
        lesson = Lesson()
        lesson.title = 'How To Be Cool'
        lesson.path = 'chapter-1.1'

        self.assertEqual("chapter-1.1: How To Be Cool", lesson.__str__())
