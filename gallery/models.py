from django.db import models

# Create your models here.

# category model
class Category(models.Model):

    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()



# location model
class Location(models.Model):
    location_name = models.CharField(max_length=100)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self) -> str:
        return self.location_name


    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to="photos/")
    image_name = models.CharField(max_length=200)
    image_description = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)


    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


    @classmethod
    def filter_by_location(cls,location):

        image_location = cls.objects.filter(location = Location.objects.filter(location_name__contains = location).first()).all()
        print(location)
        return image_location

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def searching_image(cls, searched_image):
        images = cls.objects.filter(image_name__icontains = searched_image)
        return images
        

    def __str__(self) -> str:
        return self.image_name


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['date']