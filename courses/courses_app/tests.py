from django.test import TestCase
from django.urls import reverse

from .models import Course


class CourseTest(TestCase):

    def setUp(self):
        Course.objects.create(
            name='test_course', start_date='2021-04-21',
            end_date='2021-04-21', lectures_amount='5'
            )

    def test_course_content(self):
        course = Course.objects.get(id=1)

        self.assertEqual(f'{course.name}', 'test_course')
        self.assertEqual(f'{course.start_date}', '2021-04-21')
        self.assertEqual(f'{course.end_date}', '2021-04-21')
        self.assertEqual(f'{course.lectures_amount}', '5')

    def test_course_detail_view(self):
        response = self.client.get('/course/1/')
        no_response = self.client.get('/post/10000')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Курс test_course')
        self.assertTemplateUsed(response, 'courses_app/detail.html')

    def test_course_create_view(self):
        response = self.client.post(
            reverse('course_create'),
            {
                'name': 'test_course_2',
                'start_date': '2021-04-28',
                'end_date': '2021-04-28',
                'lectures_amount': '5'
                }
            )
        self.assertEqual(response.status_code, 302)
        created_course = self.client.get('/course/2/')
        self.assertContains(created_course, 'test_course_2')

    def test_bad_course_create_view(self):
        response = self.client.post(
            reverse('course_create'),
            {
                'name': 'test_course_11',
                'start_date': '2021-04-28',
                'end_date': '2021-04-18',
                'lectures_amount': '5'
                }
            )
        self.assertEqual(response.status_code, 200)
        created_course = self.client.get('/course/3/')
        self.assertEqual(created_course.status_code, 404)

    def test_course_update_view(self):
        response = self.client.post(
            reverse('course_update', args='1'),
            {
                'name': 'test_course_3',
                'start_date': '2021-04-19',
                }
            )
        self.assertEqual(response.status_code, 200)

    def test_course_delete_view(self):
        self.client.get(reverse('course_delete', args='2'))
        deleted_course = self.client.get('/course/2/')
        self.assertEqual(deleted_course.status_code, 404)


class HomePageViewTest(TestCase):

    def setUp(self):
        Course.objects.create(
            name='test_2222', start_date='2021-04-22',
            end_date='2021-04-22', lectures_amount='1'
            )

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/course/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'courses_app/home.html')
