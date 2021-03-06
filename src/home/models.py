from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from staff import models as staff_model



#type
class Type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)


#catagory
class Catagory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=None, null=True, blank=True)

    sell_item_or_service = models.BooleanField(default=False)
    offer_property_for_rent = models.BooleanField(default=False)
    post_job_vacancy = models.BooleanField(default=False)
    look_for_property_to_rent = models.BooleanField(default=False)
    look_for_something_to_buy = models.BooleanField(default=False)

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
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True, blank=True)
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

    class Meta:
        ordering = ('?', '-date')



#======================================================================================
#======================================================================================
#                              electronics category
#======================================================================================
#======================================================================================


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


#======================================================================================
#======================================================================================
#                              end electronics category
#======================================================================================
#======================================================================================




#======================================================================================
#======================================================================================
#                              start cars and vehicles
#======================================================================================
#======================================================================================



#cars
class Car(models.Model):
    model_year = models.DateTimeField(null=True, blank=True)
    registration_year = models.DateTimeField(null=True, blank=True)

    transmission = models.CharField(max_length=100, null=True, blank=True)
    body_type = models.CharField(max_length=255, null=True, blank=True)
    fuel_type = models.CharField(max_length=255, null=True, blank=True)

    engine_capacity = models.FloatField(null=True, blank=True)
    kilometer_run = models.FloatField(null=True, blank=True)


    def __str__(self):
        return str(self.id)


#motorbike and scooter
class MotorbikeScooter(models.Model):
    model_year = models.DateTimeField(null=True, blank=True)

    engine_capacity = models.FloatField(null=True, blank=True)
    kilometer_run = models.FloatField(null=True, blank=True)


    def __str__(self):
        return str(self.id)



#bicycle and three wheelers
class BicycleThreeWheeler(models.Model):
    vehicle_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.id)


#truck van bus
class TruckVanBus(models.Model):
    model_year = models.DateTimeField(null=True, blank=True)
    kilometer_run = models.FloatField(null=True, blank=True)


    def __str__(self):
        return str(self.id)


#category :::::::::::::::::: auto parts and accessories
class AutoPartAccessory(models.Model):
    item_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.item_type)


#category :::::::::::::::::: auto service
class AutoService(models.Model):
    item_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.item_type)


#======================================================================================
#======================================================================================
#                              end cars and vehicles
#======================================================================================
#======================================================================================




#======================================================================================
#======================================================================================
#                              start property category
#======================================================================================
#======================================================================================



#apertments and flats
class ApartmentFlat(models.Model):
    bed = models.IntegerField(null=True, blank=True)
    bath = models.IntegerField(null=True, blank=True)
    size = models.FloatField(null=True, blank=True)
    address = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#houses
class House(models.Model):
    bed = models.IntegerField(null=True, blank=True)
    bath = models.IntegerField(null=True, blank=True)

    land_size = models.FloatField(null=True, blank=True)
    land_size_scale = models.CharField(max_length=20, null=True, blank=True)

    house_size = models.FloatField(null=True, blank=True)
    house_size_scale = models.CharField(max_length=20, null=True, blank=True)

    address = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#plot and lands
class PlotLand(models.Model):
    land_type = models.CharField(max_length=50, null=True, blank=True)

    land_size = models.FloatField(null=True, blank=True)
    land_size_scale = models.CharField(max_length=20, null=True, blank=True)

    address = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#garage
class Garage(models.Model):
    address = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.id)


#commercial property
class CommercialProperty(models.Model):
    property_type = models.CharField(max_length=50, null=True, blank=True)

    size = models.FloatField(null=True, blank=True)
    size_scale = models.CharField(max_length=20, null=True, blank=True)

    address = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#======================================================================================
#======================================================================================
#                              end property category
#======================================================================================
#======================================================================================



#======================================================================================
#======================================================================================
#                              start services
#======================================================================================
#======================================================================================


#business and technical services
class BusinessTechnical(models.Model):
    service_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#travel and visa
class TravelVisa(models.Model):
    service_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.id)




#business and technical services
class Ticket(models.Model):
    service_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#events and hospitality
class EventHospitality(models.Model):
    service_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#domestic and personal
class DomesticPersonal(models.Model):
    service_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#health and lifestyle
class HealthLifestyle(models.Model):
    service_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#======================================================================================
#======================================================================================
#                              end services
#======================================================================================
#======================================================================================




#======================================================================================
#======================================================================================
#                              start home and garden
#======================================================================================
#======================================================================================



#furniture
class Furniture(models.Model):
    furniture_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#home appliance
class HomeAppliance(models.Model):
    item_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#Electricity, AC, Bathroom & Garden
class ElectricityACBathroomGarden(models.Model):
    item_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#======================================================================================
#======================================================================================
#                              end home and garden
#======================================================================================
#======================================================================================




#======================================================================================
#======================================================================================
#                              start cloth health and beauty
#======================================================================================
#======================================================================================



#cloth
class Cloth(models.Model):
    gender = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#cloth
class ShoeFootware(models.Model):
    gender = models.CharField(max_length=20, null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return str(self.id)


#Health & Beauty Products
class HealthBeauty(models.Model):
    item_type = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#======================================================================================
#======================================================================================
#                              end cloth health and beauty
#======================================================================================
#======================================================================================





#======================================================================================
#======================================================================================
#                              start Hobby, Sport & Kids
#======================================================================================
#======================================================================================




#musical instrument
class MusicalInstrument(models.Model):
    instrument_type = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#sports equipment
class SportEquipment(models.Model):
    instrument_type = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#Handicrafts & Decoration
class HandicraftDecoration(models.Model):
    item_type = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#Music, Books & Movies
class MusicBookMovie(models.Model):
    item_type = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#children item
class ChildrenItem(models.Model):
    item_type = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.id)


#======================================================================================
#======================================================================================
#                              end Hobby, Sport & Kids
#======================================================================================
#======================================================================================





#======================================================================================
#======================================================================================
#                              start Education
#======================================================================================
#======================================================================================



#textbooks
class Textbook(models.Model):
    textbook_type = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#tution
class Tution(models.Model):
    tution_type = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#======================================================================================
#======================================================================================
#                              end Education
#======================================================================================
#======================================================================================





#======================================================================================
#======================================================================================
#                              start Pets & Animals
#======================================================================================
#======================================================================================


#pets
class Pet(models.Model):
    animal_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.animal_type)


#farm animal
class FarmAnimal(models.Model):
    animal_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.animal_type)




#======================================================================================
#======================================================================================
#                              end Pets & Animals
#======================================================================================
#======================================================================================






#======================================================================================
#======================================================================================
#                              start food and agriculture
#======================================================================================
#======================================================================================




#food
class Food(models.Model):
    food_type = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return str(self.food_type)




#======================================================================================
#======================================================================================
#                              end food and agriculture
#======================================================================================
#======================================================================================





#======================================================================================
#======================================================================================
#                              start Offer a property for rent
#======================================================================================
#======================================================================================




#rent Apartments & Flats
class RentApartmentFlat(ApartmentFlat):
    feature = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return str(self.id)



#rent Apartments & Flats
class RentHouse(House):

    def __str__(self):
        return str(self.id)



#rent plot and lands
class RentPlotLand(PlotLand):

    def __str__(self):
        return str(self.id)


#rent room
class RentRoom(models.Model):
    property_type = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.id)


#rent garage
class RentGarage(Garage):
    pass


#rent commercial property
class RentCommercialProperty(CommercialProperty):
    pass



#======================================================================================
#======================================================================================
#                              end Offer a property for rent
#======================================================================================
#======================================================================================




#======================================================================================
#======================================================================================
#                              start jobs
#======================================================================================
#======================================================================================




#jobs in bangladesh
class JobBangladesh(models.Model):
    job_type = models.CharField(max_length=50, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    business_function = models.CharField(max_length=100, null=True, blank=True)
    role_designation = models.CharField(max_length=100, null=True, blank=True)
    receive_applications_via = models.CharField(max_length=100, null=True, blank=True)
    total_vacancy = models.IntegerField(null=True, blank=True)
    application_deadline = models.DateField(auto_now_add=True)

    company_employer = models.CharField(max_length=100, null=True, blank=True)

    minimum_qualification = models.CharField(max_length=100, null=True, blank=True)
    required_experience = models.FloatField(null=True, blank=True)
    educational_specialization = models.CharField(max_length=100, null=True, blank=True)
    skill = models.CharField(max_length=255, null=True, blank=True)
    maximum_age = models.IntegerField(null=True, blank=True)
    gender_preference = models.CharField(max_length=20, null=True, blank=True)



    def __str__(self):
        return str(self.id)




#Overseas Jobs
class OverseasJob(models.Model):
    job_type = models.CharField(max_length=50, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    apply_via = models.CharField(max_length=100, null=True, blank=True)
    company_website = models.URLField(max_length=100, null=True, blank=True)
    application_deadline = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)




#======================================================================================
#======================================================================================
#                              end jobs
#======================================================================================
#======================================================================================
