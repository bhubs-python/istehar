from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from staff import models as staff_model




#catagory
class Catagory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    type_of = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)



#sub catagory
class SubCatagory(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.name)



#universal product post
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(SubCatagory, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(staff_model.Thana, on_delete=None, blank=True, null=True)

    """
    
    Application:
        #get product obj
        phn = model_name.objects.get(id=1)
        
        #assign to product obj
        Product(product_object=phn)
    
    """

    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    product_object = GenericForeignKey('content_type', 'object_id')

    photos = models.ImageField(upload_to='product/', default='no-img.jpg', blank=True, null=True)

    condition = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)

    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)

    model = models.CharField(max_length=100, null=True, blank=True)

    authenticity = models.CharField(max_length=20, null=True, blank=True)

    price = models.FloatField(null=True, blank=True)

    phone_number = models.CharField(max_length=30, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)



#catagory :::::: mobile phones
class MobilePhone(models.Model):
    bluetooth = models.BooleanField(default=False)
    camera = models.BooleanField(default=False)
    dual_lens_camera = models.BooleanField(default=False)
    dual_sim = models.BooleanField(default=False)
    expandable_memory = models.BooleanField(default=False)
    fingerprint_sensor = models.BooleanField(default=False)
    gps = models.BooleanField(default=False)
    physical_keyboard = models.BooleanField(default=False)
    motion_sensors = models.BooleanField(default=False)

    three_g = models.BooleanField(default=False)
    four_g = models.BooleanField(default=False)

    gsm = models.BooleanField(default=False)
    touch_screen = models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)



#category ::::::::::::: computer tablet
class ComputerTablet(models.Model):
    device_type = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.device_type)



#category :::::::::::::::::: computer accessories
class ComputerAccessories(models.Model):
    item_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.item_type)



#category :::::::::::::::::: tv accessories
class TvAccessories(models.Model):
    item_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.item_type)



#category :::::::::::::::::: camera and camcoders
class CameraCamcoder(models.Model):
    item_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.item_type)


#category :::::::::::::::::: audio and mp3
class AudioMP3(models.Model):
    item_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.item_type)


