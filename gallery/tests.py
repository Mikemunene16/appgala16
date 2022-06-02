from django.test import TestCase

from .models import Category, Location, Image

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='Best Sceneries')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(location_name='Turkey')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)


    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class TestImage(TestCase):
    def setUp(self):
        self.location = Location(location_name='Turkey')
        self.location.save_location()

        self.category = Category(category_name='Best Sceneries')
        self.category.save_category()

        self.image_test = Image(id=1, image_name='Pamukkale', image_description='Put every infinity pool you’ve ever seen to shame with these natural, snow-white hot springs overlooking the nearby city of Denizli. On top of the picturesque soak, Pamukkale is also home to the impressively preserved ruins of the ancient Roman spa-city Hierapolis where you can bathe like an emperor among the submerged centuries-old columns.', location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/hbz-pamukkaleTurkey.jpg')
        changed_img = Image.objects.filter(image='photos/hbz-pamukkaleTurkey.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_get_image_by_id(self):
        self.image_test.save_image()
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    

    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='Turkey')
        self.assertTrue(len(found_images) > 0)

    def test_search_image_by_category(self):
        self.image_test.save_image()
        found_img = Image.search_by_category(self.image_test.category)
        self.assertTrue(len(found_img) > 0)
        

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()