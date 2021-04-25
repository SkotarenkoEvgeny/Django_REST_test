import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses_app.models import Course


class CourseApiTest(APITestCase):

    def setUp(self):
        Course.objects.create(
            name='test_course_api', start_date='2021-04-21',
            end_date='2021-04-21', lectures_amount='5'
            )

    def test_course_api_content(self):
        course = Course.objects.get(id=1)
        self.assertEqual(f'{course.name}', 'test_course_api')
        self.assertEqual(f'{course.start_date}', '2021-04-21')
        self.assertEqual(f'{course.end_date}', '2021-04-21')
        self.assertEqual(f'{course.lectures_amount}', '5')

    def test_course_api_detail_view(self):
        response = self.client.get('/api/1/')
        no_response = self.client.get('/api/10000/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'test_course_api')
        self.assertEqual(no_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_course_api_update_view(self):
        response = self.client.put(
            reverse('course_api_detail', kwargs={'pk': 1}),
            data=json.dumps(
                {
                    "name": 'test_course_api_3',
                    "lectures_amount": '10',
                    "start_date": '2021-04-21',
                    "end_date": '2021-04-21'
                    }
                ),
            content_type='application/json'
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'test_course_api_3')

    def test_course_api_bad_update_view(self):
        response = self.client.put(
            reverse('course_api_detail', kwargs={'pk': 1}),
            data=json.dumps(
                {
                    "name": 'test_course_api_3',
                    "lectures_amount": '10',
                    "start_date": '2021-04-22',
                    "end_date": '2021-04-21'
                    }
                ),
            content_type='application/json'
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_course_api_delete_view(self):
        response = self.client.delete(
            reverse('course_api_detail', kwargs={'pk': '1'})
            )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
