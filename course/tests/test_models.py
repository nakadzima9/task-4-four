from django.test import TestCase
from ..models import Category, Course, Contact, Branch

class CategoryModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Category.objects.create(name='Bleach', imgpath='media/bleach.jpg')
	def test_name_label(self):
		category = Category.objects.get(id=1)
		field = category._meta.get_field('name').verbose_name
		self.assertEquals(field, 'name')
	def test_name_max_length(self):
		category = Category.objects.get(id=1)
		max_length = category._meta.get_field('name').max_length
		self.assertEquals(max_length, 150)


class CourseModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		category = Category.objects.create(name='Bleach', imgpath='media/bleach.jpg')
		Course.objects.create(name='BLEACH', description='About shinigami Ichigo Kurosaki', category=category, logo='BLEACH ANIME')
	def test_name_label(self):
		course = Course.objects.get(id=1)
		field = course._meta.get_field('name').verbose_name
		self.assertEquals(field, 'name')
	def test_name_max_length(self):
		course = Course.objects.get(id=1)
		max_length = course._meta.get_field('name').max_length
		self.assertEquals(max_length, 200)
	def test_description_label(self):
		course = Course.objects.get(id=1)
		field = course._meta.get_field('description').verbose_name
		self.assertEquals(field, 'description')
	def test_foreignkey_label(self):
		course = Course.objects.get(id=1)
		field = course._meta.get_field('category').verbose_name
		self.assertEquals(field, 'category')
	def test_imagefield(self):
		course = Course.objects.get(id=1)
		field = course._meta.get_field('logo').verbose_name
		self.assertEquals(field, 'logo')


class BranchModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		course = Course.objects.create(name='Shounen', logo='BLEACH ANIME')
		Branch.objects.create(laitude='Zangetsu', longitude='Bankai', adress='Japan - Tokyo')
	def test_laitude_label(self):
		branch = Branch.objects.get(id=1)
		field = branch._meta.get_field('laitude').verbose_name
		self.assertEquals(field, 'laitude')
	def test_laitude_max_length(self):
		branch = Branch.objects.get(id=1)
		max_length = branch._meta.get_field('laitude').max_length
		self.assertEquals(max_length, 200)
	def test_longitude_label(self):
		branch = Branch.objects.get(id=1)
		field = branch._meta.get_field('longitude').verbose_name
		self.assertEquals(field, 'longitude')
	def test_longitude_max_length(self):
		branch = Branch.objects.get(id=1)
		max_length = branch._meta.get_field('longitude').max_length
		self.assertEquals(max_length, 200)
	def test_foreignkey_label(self):
		branch = Branch.objects.get(id=1)
		field = branch._meta.get_field('course').verbose_name
		self.assertEquals(field, 'course')
	def test_adress_label(self):
		branch = Branch.objects.get(id=1)
		field = branch._meta.get_field('adress').verbose_name
		self.assertEquals(field, 'adress')
	def test_adress_max_length(self):
		branch = Branch.objects.get(id=1)
		max_length = branch._meta.get_field('adress').max_length
		self.assertEquals(max_length, 200)