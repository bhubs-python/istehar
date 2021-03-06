from django import forms

from . import models
from staff import models as staff_model




#======================================================================================
#======================================================================================
#                              start electronics category
#======================================================================================
#======================================================================================


#mobile phone forms
condition_list = (
    ('used', 'Used'),
    ('new', 'New'),
)

authenticity_list = (
    ('original', 'Original'),
    ('replica_clone', 'Replica / Clone'),
)
class MobilePhoneForm(forms.Form):
    photos = forms.ImageField(required=False)
    condition = forms.ChoiceField(choices=condition_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    brand = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )

    model = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    authenticity = forms.ChoiceField(choices=authenticity_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def clean(self):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        model = self.cleaned_data.get('model')
        authenticity = self.cleaned_data.get('authenticity')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')


        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if condition == None:
                raise forms.ValidationError('Select product condition!')
            else:
                if len(brand) == 0:
                    raise forms.ValidationError('Enter product brand!')
                else:
                    if len(model) == 0:
                        raise forms.ValidationError('Enter product model!')
                    else:
                        if authenticity == None:
                            raise forms.ValidationError('Select authenticity!')
                        else:
                            if price == None:
                                raise forms.ValidationError('Enter product price!')
                            else:
                                if len(phone_number) == 0:
                                    raise forms.ValidationError('Enter phone number!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        model = self.cleaned_data.get('model')
        authenticity = self.cleaned_data.get('authenticity')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        bluetooth = request.POST.get('bluetooth')
        camera = request.POST.get('camera')
        dual_lens_camera = request.POST.get('dual_lens_camera')
        dual_sim = request.POST.get('dual_sim')
        expandable_memory = request.POST.get('expandable_memory')
        fingerprint_sensor = request.POST.get('finger_print')
        gps = request.POST.get('gps')
        physical_keyboard = request.POST.get('physical_keyboard')
        motion_sensors = request.POST.get('motion_sensor')
        three_g = request.POST.get('three_g')
        four_g = request.POST.get('four_g')
        gsm = request.POST.get('gsm')
        touch_screen = request.POST.get('touch_screen')

        if bluetooth == 'on':
            bluetooth = True
        else:
            bluetooth = False

        if camera == 'on':
            camera = True
        else:
            camera = False

        if dual_lens_camera == 'on':
            dual_lens_camera = True
        else:
            dual_lens_camera = False

        if dual_sim == 'on':
            dual_sim = True
        else:
            dual_sim = False

        if expandable_memory == 'on':
            expandable_memory = True
        else:
            expandable_memory = False

        if fingerprint_sensor == 'on':
            fingerprint_sensor = True
        else:
            fingerprint_sensor = False

        if gps == 'on':
            gps = True
        else:
            gps = False

        if physical_keyboard == 'on':
            physical_keyboard = True
        else:
            physical_keyboard = False

        if motion_sensors == 'on':
            motion_sensors = True
        else:
            motion_sensors = False

        if three_g == 'on':
            three_g = True
        else:
            three_g = False

        if four_g == 'on':
            four_g = True
        else:
            four_g = False

        if gsm == 'on':
            gsm = True
        else:
            gsm = False

        if touch_screen == 'on':
            touch_screen = True
        else:
            touch_screen = False

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, brand=brand, title=title, description=description, model=model, authenticity=authenticity, price=price, phone_number=phone_number)

        phone = models.MobilePhone(bluetooth=bluetooth, camera=camera, dual_lens_camera=dual_lens_camera, dual_sim=dual_sim, expandable_memory=expandable_memory, fingerprint_sensor=fingerprint_sensor, gps=gps, physical_keyboard=physical_keyboard, motion_sensors=motion_sensors, three_g=three_g, four_g=four_g, gsm=gsm, touch_screen=touch_screen)
        phone.save()

        deploy.product_object = phone
        deploy.save()



#mobile phone accessories form
class MobilePhoneAccessoriesForm(forms.Form):
    photos = forms.ImageField(required=False)
    condition = forms.ChoiceField(choices=condition_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    def clean(self):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if condition == None:
                raise forms.ValidationError('Select product condition!')
            else:
                if price == None:
                    raise forms.ValidationError('Enter product price!')
                else:
                    if len(phone_number) == 0:
                        raise forms.ValidationError('Enter phone number!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()


#computer and tablet forms
device_type_list = (
    ('desktop_computer', 'Desktop Computer'),
    ('laptop_notebook', 'Laptop / Notebook'),
    ('tablet', 'Tablet'),
)
class ComputerTabletForm(MobilePhoneForm):
    device_type = forms.ChoiceField(choices=device_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        model = self.cleaned_data.get('model')
        authenticity = self.cleaned_data.get('authenticity')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        device_type = self.cleaned_data.get('device_type')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, brand=brand, title=title, description=description, model=model, authenticity=authenticity, price=price, phone_number=phone_number)

        computer_tablet = models.ComputerTablet(device_type=device_type)
        computer_tablet.save()

        deploy.product_object = computer_tablet
        deploy.save()



#computer accessories form
item_type_list = (
    ('blog_domain_website', 'Blog / Domain / Website'),
    ('graphics_card', 'Graphics Card'),
    ('hard_drive', 'Hard Drive'),
    ('keyboard', 'Keyboard'),
    ('modem_router', 'Modem / Router'),
    ('monitor', 'Monitor'),
    ('motherboard', 'Motherboard'),
    ('mouse', 'Mouse'),
    ('printer_scanner', 'Printer / Scanner'),
    ('processor', 'Processor'),
    ('ram', 'RAM'),
    ('software', 'Software'),
    ('other', 'Other'),
)
class ComputerAccessoriesForm(MobilePhoneAccessoriesForm):
    item_type = forms.ChoiceField(choices=item_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        computer_acc = models.ComputerAccessories(item_type=item_type)
        computer_acc.save()

        deploy.product_object = computer_acc
        deploy.save()



#mobile phone accessories form
class TvForm(forms.Form):
    photos = forms.ImageField(required=False)
    condition = forms.ChoiceField(choices=condition_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    brand = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    model = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    def clean(self):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        model = self.cleaned_data.get('model')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if condition == None:
                raise forms.ValidationError('Select product condition!')
            else:
                if price == None:
                    raise forms.ValidationError('Enter product price!')
                else:
                    if len(phone_number) == 0:
                        raise forms.ValidationError('Enter phone number!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        model = self.cleaned_data.get('model')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, brand=brand, title=title, description=description, model=model, price=price, phone_number=phone_number)
        deploy.save()



#tv accessories form
tv_item_type_list = (
    ('projector', 'Projector'),
    ('video_player', 'Video Player'),
    ('other', 'Other'),
)
class TvAccessoriesForm(MobilePhoneAccessoriesForm):
    item_type = forms.ChoiceField(choices=tv_item_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        tv_acc = models.TvAccessories(item_type=item_type)
        tv_acc.save()

        deploy.product_object = tv_acc
        deploy.save()



#camera and camcoder form
camera_camcoder_item_type_list = (
    ('digital_camera', 'Digital camera'),
    ('digital_camcoder', 'Digital camcoder'),
    ('camera_accessory', 'Camera accessory'),
    ('security_surveillance_camera', 'Security and surveillance camera'),
    ('other', 'Other'),
)
class CameraCamcoderForm(MobilePhoneAccessoriesForm):
    item_type = forms.ChoiceField(choices=camera_camcoder_item_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    brand = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, brand=brand, title=title, description=description, price=price, phone_number=phone_number)

        camera_camcoder = models.CameraCamcoder(item_type=item_type)
        camera_camcoder.save()

        deploy.product_object = camera_camcoder
        deploy.save()


#audio and mp3 form
audio_mp3_item_type_list = (
    ('headphone', 'Headphones'),
    ('ipod_mp3', 'iPod / MP3 player'),
    ('speaker_sound_system', 'Speakers / sound system'),
    ('other', 'Other'),
)
class AudioMP3Form(MobilePhoneAccessoriesForm):
    item_type = forms.ChoiceField(choices=audio_mp3_item_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        camera_camcoder = models.AudioMP3(item_type=item_type)
        camera_camcoder.save()

        deploy.product_object = camera_camcoder
        deploy.save()



#lighting form
class LightingForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()


#video games and console form
class VideoGameForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()


#other electronic form
class OtherElectronicForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()


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


#car form
car_body_type_list = (
    ('saloon', 'Saloon'),
    ('hatchback', 'Hatchback'),
    ('estate', 'Estate'),
    ('convertible', 'Convertible'),
    ('coupe_sports', 'Coupe / Sports'),
    ('suv_4x4', 'SUV / 4 X 4'),
    ('MPV', 'MPV'),
)

car_fuel_type_list = (
    ('diesel', 'Diesel'),
    ('petrol', 'Petrol'),
    ('cng', 'CNG'),
    ('octane', 'Octane'),
    ('other_fuel_type', 'Other fuel type'),
)

car_transmission_type_list = (
    ('manual', 'Manual'),
    ('automatic', 'Automatic'),
    ('other', 'Other transmission'),
)

class CarForm(MobilePhoneAccessoriesForm):
    model_year = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))
    registration_year = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))

    transmission = forms.ChoiceField(choices=car_transmission_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    body_type = forms.ChoiceField(choices=car_body_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    fuel_type = forms.ChoiceField(choices=car_fuel_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    brand = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    model = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    engine_capacity = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    kilometer_run = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        model = self.cleaned_data.get('model')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        model_year = self.cleaned_data.get('model_year')
        registration_year = self.cleaned_data.get('registration_year')
        transmission = self.cleaned_data.get('transmission')
        body_type = self.cleaned_data.get('body_type')
        fuel_type = self.cleaned_data.get('fuel_type')
        engine_capacity = self.cleaned_data.get('engine_capacity')
        kilometer_run = self.cleaned_data.get('kilometer_run')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, brand=brand, title=title, description=description, model=model, price=price, phone_number=phone_number)

        cars = models.Car(model_year=model_year, registration_year=registration_year, transmission=transmission, body_type=body_type, fuel_type=fuel_type, engine_capacity=engine_capacity, kilometer_run=kilometer_run)
        cars.save()

        deploy.product_object = cars
        deploy.save()



#motorbike and scooter
class MotorbikeScooterForm(MobilePhoneAccessoriesForm):
    model_year = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))

    brand = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    model = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    engine_capacity = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    kilometer_run = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        model = self.cleaned_data.get('model')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        model_year = self.cleaned_data.get('model_year')
        engine_capacity = self.cleaned_data.get('engine_capacity')
        kilometer_run = self.cleaned_data.get('kilometer_run')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, brand=brand, title=title, description=description, model=model, price=price, phone_number=phone_number)

        motorbike = models.MotorbikeScooter(model_year=model_year, engine_capacity=engine_capacity, kilometer_run=kilometer_run)
        motorbike.save()

        deploy.product_object = motorbike
        deploy.save()


#bicycle and three wheelers
vehicle_type_list = (
    ('bicycle', 'Bicycle'),
    ('threewheeler_cng', 'Three Wheeler / CNG'),
)
class BicycleThreeWheelerForm(MobilePhoneAccessoriesForm):
    brand = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    vehicle_type = forms.ChoiceField(choices=vehicle_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        vehicle_type = self.cleaned_data.get('vehicle_type')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, brand=brand, title=title, description=description, price=price, phone_number=phone_number)

        bicycle = models.BicycleThreeWheeler(vehicle_type=vehicle_type)
        bicycle.save()

        deploy.product_object = bicycle
        deploy.save()



#truck van bus
class TruckVanBusForm(MobilePhoneAccessoriesForm):
    model_year = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))

    brand = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    model = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    kilometer_run = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        brand = self.cleaned_data.get('brand')
        model = self.cleaned_data.get('model')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        model_year = self.cleaned_data.get('model_year')
        kilometer_run = self.cleaned_data.get('kilometer_run')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, brand=brand, title=title, description=description, model=model, price=price, phone_number=phone_number)

        truck_van_bus = models.TruckVanBus(model_year=model_year, kilometer_run=kilometer_run)
        truck_van_bus.save()

        deploy.product_object = truck_van_bus
        deploy.save()



#tructor and heavy duty form
class TructorHeavyDutyForm(forms.Form):
    photos = forms.ImageField(required=False)
    condition = forms.ChoiceField(choices=condition_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    def clean(self):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if condition == None:
                raise forms.ValidationError('Select product condition!')
            else:
                if price == None:
                    raise forms.ValidationError('Enter product price!')
                else:
                    if len(phone_number) == 0:
                        raise forms.ValidationError('Enter phone number!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()



#auto parts and accessory form
auto_part_type_list = (
    ('auto_part', 'Auto Part'),
    ('car_audio_video', 'Car audio / video'),
    ('maintenance_repair', 'Maintenance / repair'),
    ('security_safety', 'Security / safety'),
    ('tyres_rims', 'Tyres / rims'),
    ('other', 'Other accessory'),
)
class AutoPartAccessoryForm(MobilePhoneAccessoriesForm):
    item_type = forms.ChoiceField(choices=auto_part_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        auto_part_acc = models.AutoPartAccessory(item_type=item_type)
        auto_part_acc.save()

        deploy.product_object = auto_part_acc
        deploy.save()



#boats and water transport
class BoatWaterTransportForm(TructorHeavyDutyForm):
   pass




#auto service form
auto_service_type_list = (
    ('car_rental', 'Car Rentals'),
    ('commercial_vehicle_rental', 'Commercial vehicle rentals'),
    ('car_maintenance', 'Car maintenance'),
    ('two_wheeler_maintenance', 'Two wheelar maintenance'),
    ('other', 'Other services'),
)
class AutoServiceForm(MobilePhoneAccessoriesForm):
    item_type = forms.ChoiceField(choices=auto_service_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        #category_obj = models.Catagory.objects.get(id=category)
        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        auto_service = models.AutoService(item_type=item_type)
        auto_service.save()

        deploy.product_object = auto_service
        deploy.save()



#======================================================================================
#======================================================================================
#                              end cars and vehicles
#======================================================================================
#======================================================================================


#======================================================================================
#======================================================================================
#                              start property
#======================================================================================
#======================================================================================


#apartment flat form
bed_amount = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
)

bath_amount = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
)
class ApartmentFlatForm(forms.Form):
    photos = forms.ImageField(required=False)
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    bed = forms.ChoiceField(choices=bed_amount, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    bath = forms.ChoiceField(choices=bath_amount, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    size = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    address = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )



    def clean(self):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        bed = self.cleaned_data.get('bed')
        bath = self.cleaned_data.get('bath')
        size = self.cleaned_data.get('size')
        address = self.cleaned_data.get('address')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')
                else:
                    if size == None:
                        raise forms.ValidationError('Write apartment size in square ft!')
                    else:
                        if len(address) == 0:
                            raise forms.ValidationError('Enter street address, building no and floor!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        bed = self.cleaned_data.get('bed')
        bath = self.cleaned_data.get('bath')
        size = self.cleaned_data.get('size')
        address = self.cleaned_data.get('address')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        apartment_flat = models.ApartmentFlat(bed=bed, bath=bath, size=size, address=address)
        apartment_flat.save()

        deploy.product_object = apartment_flat
        deploy.save()



#house
land_size_scale = (
    ('katha', 'Katha'),
    ('bigha', 'Bigha'),
    ('acres', 'Acres'),
    ('shotok', 'Shotok'),
    ('decimal', 'Decimal'),
)

house_size_scale = (
    ('sqft', 'sqft'),
    ('katha', 'Katha'),
    ('shotok', 'Shotok'),
    ('decimal', 'Decimal'),
)
class HouseForm(forms.Form):
    photos = forms.ImageField(required=False)
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    bed = forms.ChoiceField(choices=bed_amount, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    bath = forms.ChoiceField(choices=bath_amount, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    land_size = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    land_size_scale = forms.ChoiceField(choices=land_size_scale, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    house_size = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    house_size_scale = forms.ChoiceField(choices=house_size_scale, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    address = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )




    def clean(self):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        bed = self.cleaned_data.get('bed')
        bath = self.cleaned_data.get('bath')
        land_size = self.cleaned_data.get('land_size')
        land_size_scale = self.cleaned_data.get('land_size_scale')
        house_size = self.cleaned_data.get('house_size')
        house_size_scale = self.cleaned_data.get('house_size_scale')
        address = self.cleaned_data.get('address')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')
                else:
                    if len(address) == 0:
                        raise forms.ValidationError('Enter street address, building no and floor!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        bed = self.cleaned_data.get('bed')
        bath = self.cleaned_data.get('bath')
        land_size = self.cleaned_data.get('land_size')
        land_size_scale = self.cleaned_data.get('land_size_scale')
        house_size = self.cleaned_data.get('house_size')
        house_size_scale = self.cleaned_data.get('house_size_scale')
        address = self.cleaned_data.get('address')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        houses = models.House(bed=bed, bath=bath, land_size=land_size, land_size_scale=land_size_scale, house_size=house_size, house_size_scale=house_size_scale, address=address)
        houses.save()

        deploy.product_object = houses
        deploy.save()



#land and plot
land_type_list = (
    ('agriculture', 'Agriculture'),
    ('commercial', 'Commercial'),
    ('residential', 'Residential'),
    ('other', 'Other'),
)
class LandPlotForm(forms.Form):
    photos = forms.ImageField(required=False)
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    land_type = forms.ChoiceField(choices=land_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    land_size = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    land_size_scale = forms.ChoiceField(choices=land_size_scale, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    address = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )




    def clean(self):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        land_type = self.cleaned_data.get('land_type')
        land_size = self.cleaned_data.get('land_size')
        land_size_scale = self.cleaned_data.get('land_size_scale')

        address = self.cleaned_data.get('address')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')
                else:
                    if len(address) == 0:
                        raise forms.ValidationError('Enter street address, building no and floor!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        land_type = self.cleaned_data.get('land_type')
        land_size = self.cleaned_data.get('land_size')
        land_size_scale = self.cleaned_data.get('land_size_scale')

        address = self.cleaned_data.get('address')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        plot_land = models.PlotLand(land_type=land_type, land_size=land_size, land_size_scale=land_size_scale, address=address)
        plot_land.save()

        deploy.product_object = plot_land
        deploy.save()



#garage form
class GarageForm(forms.Form):
    photos = forms.ImageField(required=False)
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    address = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )

    def clean(self):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        address = self.cleaned_data.get('address')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')
                else:
                    if len(address) == 0:
                        raise forms.ValidationError('Enter street address, building no and floor!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        address = self.cleaned_data.get('address')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        garage = models.Garage(address=address)
        garage.save()

        deploy.product_object = garage
        deploy.save()




#commercial property
property_type_list = (
    ('building', 'building'),
    ('factory_mill', 'Factory / mill'),
    ('hotel', 'Hotel'),
    ('office', 'Office'),
    ('restaurent', 'Restaurent'),
    ('shop', 'Shop'),
    ('warehouse', 'Warehouse'),
    ('other', 'Other'),
)
class CommercialPropertyForm(forms.Form):
    photos = forms.ImageField(required=False)
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    property_type = forms.ChoiceField(choices=property_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    size = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    size_scale = forms.ChoiceField(choices=land_size_scale, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    address = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )




    def clean(self):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        property_type = self.cleaned_data.get('property_type')
        size = self.cleaned_data.get('size')
        size_scale = self.cleaned_data.get('size_scale')

        address = self.cleaned_data.get('address')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')
                else:
                    if len(address) == 0:
                        raise forms.ValidationError('Enter street address, building no and floor!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        property_type = self.cleaned_data.get('property_type')
        size = self.cleaned_data.get('size')
        size_scale = self.cleaned_data.get('size_scale')

        address = self.cleaned_data.get('address')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        commercial_property = models.CommercialProperty(property_type=property_type, size=size, size_scale=size_scale, address=address)
        commercial_property.save()

        deploy.product_object = commercial_property
        deploy.save()




#======================================================================================
#======================================================================================
#                              end property
#======================================================================================
#======================================================================================



#======================================================================================
#======================================================================================
#                              start services
#======================================================================================
#======================================================================================


#business and technical form
business_service_type_list = (
    ('computer_laptop', 'Computers & Laptops'),
    ('electrical_carpentry', 'Electricals & Carpentry'),
    ('electronics_engineering', 'Electronics & Engineering'),
    ('facility_management', 'Facility Management'),
    ('financial_legal', 'Financial & Legal'),
    ('interior_design', 'Interior Design'),
    ('marketing_social_media', 'Marketing & Social Media'),
    ('masonry_civil_works', 'Masonry & Civil Works'),
    ('mobile_phone', 'Mobile Phone'),
    ('packers_movers', 'Packers & Movers'),
    ('photography', 'Photography'),
    ('plumbing_maintenance', 'Plumbing & Maintenance'),
    ('printing', 'Printing'),
    ('rental_services', 'Rental Services'),
    ('repair_services', 'Repair Servcies'),
    ('security', 'Security'),
    ('software_web_development', 'Software & Web Development'),
)
class BusinessTechnicalForm(forms.Form):
    photos = forms.ImageField(required=False)
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    service_type = forms.ChoiceField(choices=business_service_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def clean(self):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        service_type = self.cleaned_data.get('service_type')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')
                else:
                    if service_type == None:
                        raise forms.ValidationError('Select service type!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        service_type = self.cleaned_data.get('service_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        business = models.BusinessTechnical(service_type=service_type)
        business.save()

        deploy.product_object = business
        deploy.save()



#travel and visa
travel_visa_type_list = (
    ('hotel_booking', 'Hotel Bookings'),
    ('travel_tourism', 'Travel & Tourism'),
    ('visa', 'Visa'),
)
class TravelVisaForm(BusinessTechnicalForm):
    service_type = forms.ChoiceField(choices=travel_visa_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        service_type = self.cleaned_data.get('service_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        travel = models.TravelVisa(service_type=service_type)
        travel.save()

        deploy.product_object = travel
        deploy.save()




#ticket
ticket_type_list = (
    ('air_ticket', 'Air tickets'),
    ('bus_train_ticket', 'Bus & train tickets'),
    ('event_ticket', 'Event tickets'),
    ('movie_tickets', 'Movie tickets'),
    ('sport_ticket', 'Sport tickets'),
)
class TicketForm(BusinessTechnicalForm):
    service_type = forms.ChoiceField(choices=ticket_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        service_type = self.cleaned_data.get('service_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        ticket = models.Ticket(service_type=service_type)
        ticket.save()

        deploy.product_object = ticket
        deploy.save()



#events and hospitality
event_type_list = (
    ('corporate_gifting', 'Corporate Gifting'),
    ('entertainment', 'Entertainment'),
    ('event_party_management', 'Event and party management'),
    ('food_catering', 'Food and catering'),
    ('weeding_planner', 'Weeding Planners'),
)
class EventHospitalityForm(BusinessTechnicalForm):
    service_type = forms.ChoiceField(choices=event_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        service_type = self.cleaned_data.get('service_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        event = models.EventHospitality(service_type=service_type)
        event.save()

        deploy.product_object = event
        deploy.save()




#domestic and personal
domestic_personal_type_list = (
    ('drying_cleaning', 'Drying & Cleaning'),
    ('home_service', 'Home Services'),
    ('pest_control', 'Pest Control'),
)

class DomesticPersonalForm(BusinessTechnicalForm):
    service_type = forms.ChoiceField(choices=domestic_personal_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        service_type = self.cleaned_data.get('service_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        domestic = models.DomesticPersonal(service_type=service_type)
        domestic.save()

        deploy.product_object = domestic
        deploy.save()



#health and lifestyle
health_lifestyle_type_list = (
    ('fashion_grooming', 'Fashion & Grooming'),
    ('fitness_training', 'Fitness & Training'),
    ('wellness_beauty', 'Wellness & Beauty'),
)

class HealthLifestyleForm(BusinessTechnicalForm):
    service_type = forms.ChoiceField(choices=health_lifestyle_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        service_type = self.cleaned_data.get('service_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        health = models.HealthLifestyle(service_type=service_type)
        health.save()

        deploy.product_object = health
        deploy.save()


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
furniture_type_list = (
    ('antique_art', 'Antique / art'),
    ('bed_bedroom_item', 'Bed / bedroom item'),
    ('lighting', 'Lighting'),
    ('sofa_livingroom_item', 'Sofa / living room item'),
    ('storage', 'Storage'),
    ('table_chair', 'Table / chair'),
    ('textile', 'Textile'),
    ('tv_stereo', 'Tv / stereo'),
    ('other', 'Other'),
)

class FurnitureForm(forms.Form):
    photos = forms.ImageField(required=False)
    condition = forms.ChoiceField(choices=condition_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    furniture_type = forms.ChoiceField(choices=furniture_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def clean(self):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        furniture_type = self.cleaned_data.get('furniture_type')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        furniture_type = self.cleaned_data.get('furniture_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        furniture = models.Furniture(furniture_type=furniture_type)
        furniture.save()

        deploy.product_object = furniture
        deploy.save()



#home appliance
home_appliance_type_list = (
    ('dryer_cleaner', 'Dryer / cleaner'),
    ('kitchen_dining', 'Kitchen / dining'),
    ('maker_toaster', 'Maker / toaster'),
    ('refrigerator_freezer', 'Refrigerator / freezer'),
    ('stove_oven_microwave', 'Stove / oven / microwave'),
    ('utensil_cooker', 'Utensil / cooker'),
    ('washing_machine_dishwasher', 'Washing machine / dishwasher'),
    ('water_purifier', 'Water purifier'),
    ('other_appliance', 'Other appliance'),
)

class HomeApplianceForm(FurnitureForm):
    item_type = forms.ChoiceField(choices=home_appliance_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        home_appliance = models.HomeAppliance(item_type=item_type)
        home_appliance.save()

        deploy.product_object = home_appliance
        deploy.save()



#Electricity, AC, Bathroom & Garden
electricity_ac_bathroom_type_list = (
    ('bathroom_wc', 'Bathroom / WC'),
    ('garden_tool_machinery', 'Garden tool / machinery'),
    ('generator', 'Generator'),
    ('heating_cooling_ac', 'Heating / cooling / AC'),
    ('ups_inverter', 'UPS / inverter'),
    ('other', 'Other'),
)

class ElectricityACBathroomGardenForm(FurnitureForm):
    item_type = forms.ChoiceField(choices=electricity_ac_bathroom_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        home_appliance = models.ElectricityACBathroomGarden(item_type=item_type)
        home_appliance.save()

        deploy.product_object = home_appliance
        deploy.save()


#other home item
class OtherHomeItemForm(forms.Form):
    photos = forms.ImageField(required=False)
    condition = forms.ChoiceField(choices=condition_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    def clean(self):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')


        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()


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


#clothing
gender_list = (
    ('men', 'Men'),
    ('women', 'Women'),
    ('unisex', 'Unisex'),
)

class ClothForm(FurnitureForm):
    gender = forms.ChoiceField(choices=gender_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        gender = self.cleaned_data.get('gender')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        cloth = models.Cloth(gender=gender)
        cloth.save()

        deploy.product_object = cloth
        deploy.save()



#shoe footware
class ShoeFootwareForm(FurnitureForm):
    gender = forms.ChoiceField(choices=gender_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    size = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        gender = self.cleaned_data.get('gender')
        size = self.cleaned_data.get('size')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        shoe = models.ShoeFootware(gender=gender, size=size)
        shoe.save()

        deploy.product_object = shoe
        deploy.save()



#jewelery
class JeweleryForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()




#optical item
class OpticalItemForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()



#watch
class WatchForm(MobilePhoneAccessoriesForm):
    authenticity = forms.ChoiceField(choices=authenticity_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        authenticity = self.cleaned_data.get('authenticity')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, authenticity=authenticity, price=price, phone_number=phone_number)
        deploy.save()



#bag
class BagForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()



#wholesale bulk
class WholesaleBulkForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()


#other fashion accessories
class OtherFashionAccessoryForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()



#other fashion accessories
class OtherPersonalItemForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()



#Health & Beauty Products
health_beauty_item_type = (
    ('cosmetics', 'Cosmetics'),
    ('grooming_bodycare', 'Grooming / bodycare'),
    ('perfume', 'Perfume'),
    ('weight_loss', 'Weight loss'),
    ('other', 'Other'),
)
class HealthBeautyForm(FurnitureForm):
    item_type = forms.ChoiceField(choices=health_beauty_item_type, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        health_beauty = models.HealthBeauty(item_type=item_type)
        health_beauty.save()

        deploy.product_object = health_beauty
        deploy.save()



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
musical_instrument_type_list = (
    ('keyboard_piano', 'Keyboard / Piano'),
    ('percussion_drums', 'Percussion / drums'),
    ('sheet_music', 'Sheet Music'),
    ('string_instrument_amplifier', 'String Instrument / Amplifier'),
    ('studio_live_music_equipment', 'Studio / Live Music Equipment'),
    ('vinyl', 'Vinyl'),
    ('woodwind_brass', 'Woodwind / brass'),
    ('other', 'Other Instrument'),
)

class MusicalInstrumentForm(FurnitureForm):
    instrument_type = forms.ChoiceField(choices=musical_instrument_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        instrument_type = self.cleaned_data.get('instrument_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        musical_instrument = models.MusicalInstrument(instrument_type=instrument_type)
        musical_instrument.save()

        deploy.product_object = musical_instrument
        deploy.save()



#sport equipment
sport_equipment_type_list = (
    ('boxing_martial_arts', 'Boxing / martial arts'),
    ('cricket', 'Cricket'),
    ('fishing_camping', 'Fishing / camping'),
    ('fitness_gym', 'Fitness / gym'),
    ('football', 'Football'),
    ('game_board', 'Game / Board Game'),
    ('hockey', 'Hockey'),
    ('indoor_sport', 'Indoor Sports'),
    ('other', 'Other'),
)

class SportEquipmentForm(FurnitureForm):
    instrument_type = forms.ChoiceField(choices=sport_equipment_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        instrument_type = self.cleaned_data.get('instrument_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        sport_equipment = models.SportEquipment(instrument_type=instrument_type)
        sport_equipment.save()

        deploy.product_object = sport_equipment
        deploy.save()




#sport equipment
handycraft_decoration_type_list = (
    ('clothing_bag_accessory', 'Clothing / bag / accessory'),
    ('nokshi_katha', 'Nokshi Kantha'),
    ('other', 'Other Handicraft'),
)

class HandicraftDecorationForm(FurnitureForm):
    item_type = forms.ChoiceField(choices=handycraft_decoration_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        handicraft = models.HandicraftDecoration(item_type=item_type)
        handicraft.save()

        deploy.product_object = handicraft
        deploy.save()





#Antique, Art & Collectibles
class AntiqueArtCollectibleForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()



#Music, Books & Movies
music_book_movie_type_list = (
    ('book_novel', 'Book / Novel'),
    ('cd', 'CD'),
    ('dvd', 'DVD'),
    ('game_board_game', 'Game / Board Game'),
    ('magazine_comic', 'Magazine / Comic'),
    ('other', 'Other'),
)

class MusicBookMovieForm(FurnitureForm):
    item_type = forms.ChoiceField(choices=music_book_movie_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        music_book_movie = models.MusicBookMovie(item_type=item_type)
        music_book_movie.save()

        deploy.product_object = music_book_movie
        deploy.save()




#children item
children_item_type_list = (
    ('baby_item', 'Baby item'),
    ('car_seat_carrier', 'Car seat / carrier'),
    ('cloth_shoe', 'Clothes / shoes'),
    ('furniture', 'Furniture'),
    ('pram_stroller', 'Pram / stroller'),
    ('toy', 'Toy'),
    ('other', 'Other'),
)

children_item_gender_list = (
    ('boys', 'Boys'),
    ('girls', 'Girls'),
    ('baby', 'Baby'),
    ('unisex', 'Unisex'),
)

class ChildrenItemForm(FurnitureForm):
    item_type = forms.ChoiceField(choices=children_item_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    gender = forms.ChoiceField(choices=children_item_gender_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        item_type = self.cleaned_data.get('item_type')
        gender = self.cleaned_data.get('gender')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        children_item = models.ChildrenItem(item_type=item_type, gender=gender)
        children_item.save()

        deploy.product_object = children_item
        deploy.save()



#Other Hobby, Sport & Kids items
class OtherHobbySportKidForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()



#======================================================================================
#======================================================================================
#                              end Hobby, Sport & Kids
#======================================================================================
#======================================================================================



#======================================================================================
#======================================================================================
#                              start Business & Industry
#======================================================================================
#======================================================================================



#Office Supplies & Stationary
class OfficeSuppliesStationaryForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()


#Industry Machinery & Tools
class IndustryMachineryToolForm(OfficeSuppliesStationaryForm):
    pass



#raw materials & industrial supplies
class RawMaterialIndustrialSupplyForm(OfficeSuppliesStationaryForm):
    pass


#Licences, Titles & Tenders
class LicencesTitleTenderForm(forms.Form):
    photos = forms.ImageField(required=False)
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    def clean(self):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()


#Medical Equipment & Supplies
class MedicalEquipmentSupplyForm(OfficeSuppliesStationaryForm):
    pass


#======================================================================================
#======================================================================================
#                              end Business & Industry
#======================================================================================
#======================================================================================





#======================================================================================
#======================================================================================
#                              start Education
#======================================================================================
#======================================================================================



#textbook
textbook_type_list = (
    ('college_university', 'College / University'),
    ('school', 'School'),
    ('other', 'Other'),
)

class TextbookForm(FurnitureForm):
    textbook_type = forms.ChoiceField(choices=textbook_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        textbook_type = self.cleaned_data.get('textbook_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        textbook = models.Textbook(textbook_type=textbook_type)
        textbook.save()

        deploy.product_object = textbook
        deploy.save()



#tution
tution_type_list = (
    ('bangla_medium', 'Bangla medium'),
    ('english_medium', 'English medium'),
    ('private_lesson', 'Private lesson'),
    ('other', 'Other'),
)

class TutionForm(FurnitureForm):
    tution_type = forms.ChoiceField(choices=tution_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        tution_type = self.cleaned_data.get('tution_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        tution = models.Tution(tution_type=tution_type)
        tution.save()

        deploy.product_object = tution
        deploy.save()



#study abroad
class StudyAbroadForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()



#other education
class OtherEducationForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()




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




#pet
animal_type_list = (
    ('bird', 'Bird'),
    ('cat', 'Cat'),
    ('dog', 'Dog'),
    ('fish', 'Fish'),
    ('gunea_pig_mouse', 'Guinea pig / mouse'),
    ('rabbit', 'Rabbit'),
    ('reptile', 'Reptile'),
    ('other', 'Other'),
)

class PetForm(FurnitureForm):
    animal_type = forms.ChoiceField(choices=animal_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        animal_type = self.cleaned_data.get('animal_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        pet = models.Pet(animal_type=animal_type)
        pet.save()

        deploy.product_object = pet
        deploy.save()



#pet
farm_animal_type_list = (
    ('livestock', 'Livestock'),
    ('poultry', 'Poultry'),
    ('other', 'Other'),
)

class FarmAnimalForm(FurnitureForm):
    animal_type = forms.ChoiceField(choices=farm_animal_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        condition = self.cleaned_data.get('condition')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        animal_type = self.cleaned_data.get('animal_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, condition=condition, title=title, description=description, price=price, phone_number=phone_number)

        farm_animal = models.FarmAnimal(animal_type=animal_type)
        farm_animal.save()

        deploy.product_object = farm_animal
        deploy.save()




#Pet & Animal Accessories
class PetAnimalAccessoryForm(OfficeSuppliesStationaryForm):
    pass


#Other Pets & Animals
class OtherPetAnimalForm(OtherEducationForm):
    pass



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




#pet
food_type_list = (
    ('fish', 'Fish'),
    ('fruit', 'Fruit'),
    ('meat', 'Meat'),
    ('vegetable', 'Vegetable'),
    ('other', 'Other'),
)

class FoodForm(FurnitureForm):
    food_type = forms.ChoiceField(choices=food_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))


    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        food_type = self.cleaned_data.get('food_type')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        food = models.Food(food_type=food_type)
        food.save()

        deploy.product_object = food
        deploy.save()




#Crops, Seeds & Plants
class CropSeedPlantForm(MobilePhoneAccessoriesForm):

    def deploy(self, request, subcategory, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        subcategory_obj = models.SubCatagory.objects.get(id=subcategory)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, subcategory=subcategory_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)
        deploy.save()




#Farming Tools & Machinery
class FarmingToolMachineryForm(OfficeSuppliesStationaryForm):
    pass



#Other Food & Agriculture
class OtherFoodAgricultureForm(OtherEducationForm):
    pass


#======================================================================================
#======================================================================================
#                              end food and agriculture
#======================================================================================
#======================================================================================



#======================================================================================
#======================================================================================
#                              start other category
#======================================================================================
#======================================================================================

#Other
class OtherForm(OfficeSuppliesStationaryForm):
    pass


#======================================================================================
#======================================================================================
#                              end other
#======================================================================================
#======================================================================================





#======================================================================================
#======================================================================================
#                              start Offer a property for rent
#======================================================================================
#======================================================================================



#Apartments & Flats
rent_apartment_flat_feature = (
    ('full_furnished', 'Full-Furnished'),
    ('semi_furnished', 'Semi-Furnished'),
    ('not_furnished', 'Not Furnished'),
)
class RentApartmentFlatForm(ApartmentFlatForm):
    feature = forms.ChoiceField(choices=rent_apartment_flat_feature, required=False, widget=forms.Select(attrs={'class': 'validate'}))

    def deploy(self, request, category, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        bed = self.cleaned_data.get('bed')
        feature = self.cleaned_data.get('feature')
        bath = self.cleaned_data.get('bath')
        size = self.cleaned_data.get('size')
        address = self.cleaned_data.get('address')

        category_obj = models.Catagory.objects.get(id=category)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, category=category_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        rent_apartment_flat = models.RentApartmentFlat(bed=bed, bath=bath, size=size, address=address, feature=feature)
        rent_apartment_flat.save()

        deploy.product_object = rent_apartment_flat
        deploy.save()



#rent house
class RentHouseForm(HouseForm):

    def deploy(self, request, category, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        bed = self.cleaned_data.get('bed')
        bath = self.cleaned_data.get('bath')
        land_size = self.cleaned_data.get('land_size')
        land_size_scale = self.cleaned_data.get('land_size_scale')
        house_size = self.cleaned_data.get('house_size')
        house_size_scale = self.cleaned_data.get('house_size_scale')
        address = self.cleaned_data.get('address')

        category_obj = models.Catagory.objects.get(id=category)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, category=category_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        houses = models.RentHouse(bed=bed, bath=bath, land_size=land_size, land_size_scale=land_size_scale, house_size=house_size, house_size_scale=house_size_scale, address=address)
        houses.save()

        deploy.product_object = houses
        deploy.save()



#rent plot and land
class RentPlotLandForm(LandPlotForm):

    def deploy(self, request, category, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        land_type = self.cleaned_data.get('land_type')
        land_size = self.cleaned_data.get('land_size')
        land_size_scale = self.cleaned_data.get('land_size_scale')

        address = self.cleaned_data.get('address')

        category_obj = models.Catagory.objects.get(id=category)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, category=category_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        plot_land = models.RentPlotLand(land_type=land_type, land_size=land_size, land_size_scale=land_size_scale, address=address)
        plot_land.save()

        deploy.product_object = plot_land
        deploy.save()



#rent room
rent_room_type = (
    ('apartment', 'Apartment'),
    ('house', 'House'),
    ('other', 'Other'),
)
class RentRoomForm(MobilePhoneAccessoriesForm):
    property_type = forms.ChoiceField(choices=rent_room_type, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    address = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )

    def deploy(self, request, category, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        property_type = self.cleaned_data.get('property_type')
        address = self.cleaned_data.get('address')


        category_obj = models.Catagory.objects.get(id=category)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, category=category_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        rent_room = models.RentRoom(property_type=property_type, address=address)
        rent_room.save()

        deploy.product_object = rent_room
        deploy.save()



#rent garage
class RentGarageForm(GarageForm):
    def deploy(self, request, category, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        address = self.cleaned_data.get('address')

        category_obj = models.Catagory.objects.get(id=category)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, category=category_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        garage = models.RentGarage(address=address)
        garage.save()

        deploy.product_object = garage
        deploy.save()



#rent commercial property
class RentCommercialProperty(CommercialPropertyForm):
    def deploy(self, request, category, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        property_type = self.cleaned_data.get('property_type')
        size = self.cleaned_data.get('size')
        size_scale = self.cleaned_data.get('size_scale')

        address = self.cleaned_data.get('address')

        category_obj = models.Catagory.objects.get(id=category)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, category=category_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        commercial_property = models.RentCommercialProperty(property_type=property_type, size=size, size_scale=size_scale, address=address)
        commercial_property.save()

        deploy.product_object = commercial_property
        deploy.save()




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
job_bd_type_list = (
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
    ('contractual', 'Contractual'),
    ('internship', 'Internship'),
)

receive_application_via_list = (
    ('employer_dashboard', 'Employer dashboard'),
    ('phone', 'Phone'),
    ('email', 'Email'),
)

from account.forms import current_industry_list, current_business_function_list, education_level, educational_specialization, gender_list

class JobBangladeshForm(forms.Form):
    photos = forms.ImageField(required=False)
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    job_type = forms.ChoiceField(choices=job_bd_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    industry = forms.ChoiceField(choices=current_industry_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    business_function = forms.ChoiceField(choices=current_business_function_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    role_designation = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    receive_applications_via = forms.ChoiceField(choices=receive_application_via_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    total_vacancy = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    application_deadline = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))

    company_employer = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    minimum_qualification = forms.ChoiceField(choices=education_level, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    required_experience = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    educational_specialization = forms.ChoiceField(choices=educational_specialization, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    skill = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    maximum_age = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    gender_preference = forms.ChoiceField(choices=gender_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))



    def clean(self):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        job_type = self.cleaned_data.get('job_type')
        industry = self.cleaned_data.get('industry')
        business_function = self.cleaned_data.get('business_function')
        role_designation = self.cleaned_data.get('role_designation')
        receive_applications_via = self.cleaned_data.get('receive_applications_via')
        total_vacancy = self.cleaned_data.get('total_vacancy')
        application_deadline = self.cleaned_data.get('application_deadline')

        company_employer = self.cleaned_data.get('company_employer')

        minimum_qualification = self.cleaned_data.get('minimum_qualification')
        required_experience = self.cleaned_data.get('required_experience')
        educational_specialization = self.cleaned_data.get('educational_specialization')
        skill = self.cleaned_data.get('skill')
        maximum_age = self.cleaned_data.get('maximum_age')
        gender_preference = self.cleaned_data.get('gender_preference')

        if photos == None:
            raise forms.ValidationError('Select product photo!')
        else:
            if price == None:
                raise forms.ValidationError('Enter product price!')
            else:
                if len(phone_number) == 0:
                    raise forms.ValidationError('Enter phone number!')


    def deploy(self, request, category, location):
        photos = self.cleaned_data.get('photos')
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        job_type = self.cleaned_data.get('job_type')
        industry = self.cleaned_data.get('industry')
        business_function = self.cleaned_data.get('business_function')
        role_designation = self.cleaned_data.get('role_designation')
        receive_applications_via = self.cleaned_data.get('receive_applications_via')
        total_vacancy = self.cleaned_data.get('total_vacancy')
        application_deadline = self.cleaned_data.get('application_deadline')

        company_employer = self.cleaned_data.get('company_employer')

        minimum_qualification = self.cleaned_data.get('minimum_qualification')
        required_experience = self.cleaned_data.get('required_experience')
        educational_specialization = self.cleaned_data.get('educational_specialization')
        skill = self.cleaned_data.get('skill')
        maximum_age = self.cleaned_data.get('maximum_age')
        gender_preference = self.cleaned_data.get('gender_preference')

        category_obj = models.Catagory.objects.get(id=category)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, category=category_obj, location=location_obj, photos=photos, title=title, description=description, price=price, phone_number=phone_number)

        job_bd = models.JobBangladesh(job_type=job_type, industry=industry, business_function=business_function, role_designation=role_designation, receive_applications_via=receive_applications_via, total_vacancy=total_vacancy, application_deadline=application_deadline, company_employer=company_employer, minimum_qualification=minimum_qualification, required_experience=required_experience, educational_specialization=educational_specialization, skill=skill, maximum_age=maximum_age, gender_preference=gender_preference)
        job_bd.save()

        deploy.product_object = job_bd
        deploy.save()




#overseas job
class OverseasJobForm(forms.Form):
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    description = forms.CharField( required=False, max_length= 1000 ,widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}) )
    price = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))

    job_type = forms.ChoiceField(choices=job_bd_type_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    industry = forms.ChoiceField(choices=current_industry_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    apply_via = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    company_website = forms.URLField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    application_deadline = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))


    def clean(self):
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        job_type = self.cleaned_data.get('job_type')
        industry = self.cleaned_data.get('industry')
        apply_via = self.cleaned_data.get('apply_via')
        company_website = self.cleaned_data.get('company_website')
        application_deadline = self.cleaned_data.get('application_deadline')

        if price == None:
            raise forms.ValidationError('Enter product price!')
        else:
            if len(phone_number) == 0:
                raise forms.ValidationError('Enter phone number!')


    def deploy(self, request, category, location):
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        price = self.cleaned_data.get('price')
        phone_number = self.cleaned_data.get('phone_number')

        job_type = self.cleaned_data.get('job_type')
        industry = self.cleaned_data.get('industry')
        apply_via = self.cleaned_data.get('apply_via')
        company_website = self.cleaned_data.get('company_website')
        application_deadline = self.cleaned_data.get('application_deadline')

        category_obj = models.Catagory.objects.get(id=category)
        location_obj = staff_model.Thana.objects.get(id=location)

        deploy = models.Product(user=request.user, category=category_obj, location=location_obj, title=title, description=description, price=price, phone_number=phone_number)

        overseas_job = models.OverseasJob(job_type=job_type, industry=industry, apply_via=apply_via, company_website=company_website, application_deadline=application_deadline)
        overseas_job.save()

        deploy.product_object = overseas_job
        deploy.save()




#======================================================================================
#======================================================================================
#                              end jobs
#======================================================================================
#======================================================================================

