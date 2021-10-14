from django.test import TestCase
from django.urls import reverse
from django.urls.base import resolve
from ..models import Category, Course
from ..serializers import CourseListSerializer
from ..views import CourseListView, CourseDetailView


class TestViews(TestCase):
	def setUp(self):
		category = Category.objects.create(id=1, name='Bleach', imgpath='media/bleach.jpg')
		Course.objects.create(id=1, name='Bleach', description='SHINIGAMI ICHIGO KUROSAKI', category=category, logo='BLEACH ANIME')

	def test_course_list(self):
		response = self.client.get(reverse('courses_list'))
		self.assertEquals(response.status_code, 200)

	def test_course_list_data(self):
		courses = Course.objects.all()
		serializer = CourseListSerializer(courses, many=True)
		response = self.client.get(reverse('courses_list'))
		self.assertEquals(response.data, serializer.data)

	def test_course_list_2(self):
		url = reverse('courses_list')
		self.assertEquals(resolve(url).func.view_class, CourseListView)

	def test_course_detail(self):
		url = reverse('courses_detail', args=[1])
		self.assertEquals(resolve(url).func.view_class, CourseDetailView)