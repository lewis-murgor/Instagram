from django.test import TestCase
from .models import Profile,Image


# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.lewis=Profile(Bio='Lewis Murgor',followers=0,following=0)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lewis,Profile))

    # Testing Save Method
    def test_save_profile(self):
        self.lewis.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    # Testing Delete Method
    def test_delete_profile(self):
        self.lewis.save_profile()
        self.lewis.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

class ImageTestClass(TestCase):

     # Set up method
    def setUp(self):
        # Creating a new profile and saving it
        self.lewis=Profile(Bio='Lewis Murgor',followers=0,following=0)
        self.lewis.save_profile()

        self.new_image=Image(name='murgor',caption='My photo',likes=10,comments='Beautiful')
        self.new_image.save_image()

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()

    # Testing  instance
    def test_check_instance_variables(self):
        self.assertEqual(self.new_image.name, 'murgor')
        self.assertEqual(self.new_image.caption, 'My photo')
        self.assertEqual(self.new_image.likes, 10)
        self.assertEqual(self.new_image.comments, 'Beautiful')

    # Testing Save Method
    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing Delete Method
    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_search_by_name(self):
        image = Image.search_by_name('murgor')
        self.assertTrue(len(image))
