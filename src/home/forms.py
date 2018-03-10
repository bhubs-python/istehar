from django import forms

from . import models
from staff import models as staff_model


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
