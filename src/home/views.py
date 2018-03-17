from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View

from . import models
from staff import models as staff_model

from . import forms



#site home page
class Home(View):
    template_name = 'home/index.html'

    def get(self, request):

        return render(request, self.template_name)


#post add
class PostAd(View):
    template_name = 'home/post-ad.html'

    def get(self, request):

        return render(request, self.template_name)


#post category
class PostCategory(View):
    template_name = 'home/post-category.html'

    def get(self, request):

        type = request.GET.get('type')
        location = request.GET.get('location')

        categories = None
        if type:
            categories = models.Catagory.objects.filter(type_of=type)

        variables = {
            'type': type,
            'location': location,

            'categories': categories,
        }

        return render(request, self.template_name, variables)


#post location
class PostLocation(View):
    template_name = 'home/post-location.html'

    def get(self, request):

        type = request.GET.get('type')
        subcategory = request.GET.get('subcategory')

        location = request.GET.get('location')

        if location:
            url = '/post-ad/details/?type=' + type + '&subcategory='+ subcategory + '&location=' + location
            return HttpResponseRedirect(url)

        subcategories = None
        if subcategory:
            subcategories = models.SubCatagory.objects.filter(id=subcategory)


        divisions = None
        if type:
            divisions = staff_model.Division.objects.all()

        variables = {
            'type': type,
            'subcategory': subcategory,

            'divisions': divisions,

            'subcategories': subcategories,

        }

        return render(request, self.template_name, variables)


#post details
class PostDetails(View):
    template_name = 'home/post-details.html'

    def get(self, request):

        type = request.GET.get('type')
        subcategory = request.GET.get('subcategory')
        location = request.GET.get('location')

        subcategories = None
        s_category = None
        if subcategory:
            subcategories = models.SubCatagory.objects.filter(id=subcategory)

            for sub_category in subcategories:
                s_category = sub_category.name


        locations = None
        if location:
            locations = staff_model.Thana.objects.filter(id=location)

        #mobile phone form
        form = None
        if s_category == 'mobile phones':
            form = forms.MobilePhoneForm()


        #mobile phone accessories form
        elif s_category == 'mobile phone accessories':
            form = forms.MobilePhoneAccessoriesForm()


        #computer and tablet form
        elif s_category == 'computers & tablets':
            form = forms.ComputerTabletForm()


        #computer accessories form
        elif s_category == 'computer accessories':
            form = forms.ComputerAccessoriesForm()


        #tv form
        elif s_category == 'tvs':
            form = forms.TvForm()


        #tv accessories
        elif s_category == 'tv & video accessories':
            form = forms.TvAccessoriesForm()


        #camera and camcoders
        elif s_category == 'cameras & camcorders':
            form = forms.CameraCamcoderForm()


        #audio and mp3
        elif s_category == 'audio & MP3':
            form = forms.AudioMP3Form()


        #lighting form
        elif s_category == 'lighting':
            form = forms.LightingForm()


        #video games and console form
        elif s_category == 'video games & consoles':
            form = forms.VideoGameForm()


        #other electronics form
        elif s_category == 'other electronics':
            form = forms.OtherElectronicForm()


        #===============================================
        #        end electronic category
        #===============================================

        #===============================================
        #        start cars and vehicles category
        #===============================================


        #car
        elif s_category == 'cars':
            form = forms.CarForm()


        #motorbike and scooter
        elif s_category == 'motorbikes & scooters':
            form = forms.MotorbikeScooterForm()


        #bicycle and three wheeler
        elif s_category == 'bicycles and three wheelers':
            form = forms.BicycleThreeWheelerForm()


        #truck van bus
        elif s_category == 'trucks, vans & buses':
            form = forms.TruckVanBusForm()


        #tructor and heavy duty
        elif s_category == 'tractors & heavy-duty':
            form = forms.TructorHeavyDutyForm()


        #auto parts and accessories
        elif s_category == 'auto parts & accessories':
            form = forms.AutoPartAccessoryForm()


        #boats and water transport
        elif s_category == 'boats & water transport':
            form = forms.BoatWaterTransportForm()


        #auto services
        elif s_category == 'auto services':
            form = forms.AutoServiceForm()


        #===============================================
        #       end cars and vehicles category
        #===============================================


        #===============================================
        #       start property category
        #===============================================


        #apartment and flat
        elif s_category == 'apartments & flats':
            form = forms.ApartmentFlatForm()


        #houses
        elif s_category == 'houses':
            form = forms.HouseForm()



        #plot and land
        elif s_category == 'plots & land':
            form = forms.LandPlotForm()


        #garages
        elif s_category == 'garages':
            form = forms.GarageForm()


        #commercial property
        elif s_category == 'commercial property':
            form = forms.CommercialPropertyForm()


        #===============================================
        #       end property category
        #===============================================


        #===============================================
        #       start service
        #===============================================


        #business and technical
        elif s_category == 'business & technical services':
            form = forms.BusinessTechnicalForm()


        #travel and visa form
        elif s_category == 'travel & visa':
            form = forms.TravelVisaForm()


        #tickets
        elif s_category == 'tickets':
            form = forms.TicketForm()


        #events and hospitality
        elif s_category == 'events & hospitality':
            form = forms.EventHospitalityForm()


        #domestic and personal
        elif s_category == 'domestic & personal':
            form = forms.DomesticPersonalForm()


        #health and lifestyle
        elif s_category == 'health & lifestyle':
            form = forms.HealthLifestyleForm()



        #===============================================
        #       end service
        #===============================================



        #===============================================
        #       start home and gardern
        #===============================================


        #furniture
        elif s_category == 'furniture':
            form = forms.FurnitureForm()


        #home appliance
        elif s_category == 'home appliances':
            form = forms.HomeApplianceForm()


        #Electricity, AC, Bathroom & Garden
        elif s_category == 'electricity, ac, bathroom & garden':
            form = forms.ElectricityACBathroomGardenForm()


        #other home item
        elif s_category == 'other home items':
            form = forms.OtherHomeItemForm()

        #===============================================
        #       end home and gardern
        #===============================================


        #===============================================
        #       start cloth health and beauty
        #===============================================

        #cloth
        elif s_category == 'clothing':
            form = forms.ClothForm()


        #shoe footware
        elif s_category == 'shoes & footwear':
            form = forms.ShoeFootwareForm()


        #jewelery
        elif s_category == 'jewellery':
            form = forms.JeweleryForm()



        #optical items
        elif s_category == 'optical items':
            form = forms.OpticalItemForm()


        #watches
        elif s_category == 'watches':
            form = forms.WatchForm()



        #bag
        elif s_category == 'bags':
            form = forms.BagForm()


        #wholesale bulk
        elif s_category == 'wholesale - bulk':
            form = forms.WholesaleBulkForm()



        #other fashion accessory
        elif s_category == 'other fashion accessories':
            form = forms.OtherFashionAccessoryForm()


        #other personal item
        elif s_category == 'other personal items':
            form = forms.OtherPersonalItemForm()


        #health and beauty product
        elif s_category == 'health & beauty products':
            form = forms.HealthBeautyForm()


        #===============================================
        #       end cloth health and beauty
        #===============================================


        #===============================================
        #       start Hobby, Sport & Kids
        #===============================================


        #musical instrument
        elif s_category == 'musical instruments':
            form = forms.MusicalInstrumentForm()


        #sports equipment
        elif s_category == 'sports equipment':
            form = forms.SportEquipmentForm()


        #handicraft and decoration
        elif s_category == 'handicrafts & decoration':
            form = forms.HandicraftDecorationForm()



        #antique art and collectible
        elif s_category == 'antique, art & collectibles':
            form = forms.AntiqueArtCollectibleForm()



        #music book movie
        elif s_category == 'music, books & movies':
            form = forms.MusicBookMovieForm()



        #children item
        elif s_category == 'childrens items':
            form = forms.ChildrenItemForm()


        #other hobby sports kids
        elif s_category == 'other hobby, sport & kids items':
            form = forms.OtherHobbySportKidForm()


        #===============================================
        #       end Hobby, Sport & Kids
        #===============================================


        #===============================================
        #       start Business & Industry
        #===============================================


        ##Office Supplies & Stationary
        elif s_category == 'office supplies & stationary':
            form = forms.OfficeSuppliesStationaryForm()


        #Industry Machinery & Tools
        elif s_category == 'industry machinery & tools':
            form = forms.IndustryMachineryToolForm()


        #raw materials & industrial supplies
        elif s_category == 'raw materials & industrial supplies':
            form = forms.RawMaterialIndustrialSupplyForm()



        #licences, titles & tenders
        elif s_category == 'licences, titles & tenders':
            form = forms.LicencesTitleTenderForm()



        #medical equipment & supplies
        elif s_category == 'medical equipment & supplies':
            form = forms.MedicalEquipmentSupplyForm()


        #===============================================
        #       end Business & Industry
        #===============================================


        #===============================================
        #       start Education
        #===============================================


        #textbooks
        elif s_category == 'textbooks':
            form = forms.TextbookForm()



        #===============================================
        #       end Education
        #===============================================




        variables = {
            'type': type,
            'subcategory': subcategory,
            'location': location,

            'subcategories': subcategories,
            'locations': locations,

            'form': form,
            's_category': s_category,
        }

        return render(request, self.template_name, variables)

    def post(self, request):

        type = request.GET.get('type')
        subcategory = request.GET.get('subcategory')
        location = request.GET.get('location')

        subcategories = None
        s_category = None
        if subcategory:
            subcategories = models.SubCatagory.objects.filter(id=subcategory)

            for sub_category in subcategories:
                s_category = sub_category.name


        locations = None
        if location:
            locations = staff_model.Thana.objects.filter(id=location)



        #mobile phone form
        form = None
        if s_category == 'mobile phones':
            form = forms.MobilePhoneForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #mobile phone accessories form
        elif s_category == 'mobile phone accessories':
            form = forms.MobilePhoneAccessoriesForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #computer tablet form
        elif s_category == 'computers & tablets':
            form = forms.ComputerTabletForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #computer accessories form
        elif s_category == 'computer accessories':
            form = forms.ComputerAccessoriesForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #tv form
        elif s_category == 'tvs':
            form = forms.TvForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #tv accessories
        elif s_category == 'tv & video accessories':
            form = forms.TvAccessoriesForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #camera and camcoders
        elif s_category == 'cameras & camcorders':
            form = forms.CameraCamcoderForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #audio and mp3
        elif s_category == 'audio & MP3':
            form = forms.AudioMP3Form(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #lighting form
        elif s_category == 'lighting':
            form = forms.LightingForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #video games and console form
        elif s_category == 'video games & consoles':
            form = forms.VideoGameForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #other electronics form
        elif s_category == 'other electronics':
            form = forms.OtherElectronicForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #===============================================
        #        end electronic category
        #===============================================


        #===============================================
        #        start cars and vehicles category
        #===============================================


        #car
        elif s_category == 'cars':
            form = forms.CarForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #motorbike and scooter
        elif s_category == 'motorbikes & scooters':
            form = forms.MotorbikeScooterForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #bicycle and three wheeler
        elif s_category == 'bicycles and three wheelers':
            form = forms.BicycleThreeWheelerForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)



        #truck van bus
        elif s_category == 'trucks, vans & buses':
            form = forms.TruckVanBusForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #tructor and heavy duty
        elif s_category == 'tractors & heavy-duty':
            form = forms.TructorHeavyDutyForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #auto parts and accessories
        elif s_category == 'auto parts & accessories':
            form = forms.AutoPartAccessoryForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #boats and water transport
        elif s_category == 'boats & water transport':
            form = forms.BoatWaterTransportForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #auto services
        elif s_category == 'auto services':
            form = forms.AutoServiceForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #===============================================
        #       end cars and vehicles category
        #===============================================


        #===============================================
        #       start property category
        #===============================================


        #apartment and flat
        elif s_category == 'apartments & flats':
            form = forms.ApartmentFlatForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #houses
        elif s_category == 'houses':
            form = forms.HouseForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #plot and land
        elif s_category == 'plots & land':
            form = forms.LandPlotForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #garages
        elif s_category == 'garages':
            form = forms.GarageForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)



        #commercial property
        elif s_category == 'commercial property':
            form = forms.CommercialPropertyForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)



        #===============================================
        #       end property category
        #===============================================


        #===============================================
        #       start service
        #===============================================


        #business and technical
        elif s_category == 'business & technical services':
            form = forms.BusinessTechnicalForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #travel and visa form
        elif s_category == 'travel & visa':
            form = forms.TravelVisaForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #tickets
        elif s_category == 'tickets':
            form = forms.TicketForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #events and hospitality
        elif s_category == 'events & hospitality':
            form = forms.EventHospitalityForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #domestic and personal
        elif s_category == 'domestic & personal':
            form = forms.DomesticPersonalForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #health and lifestyle
        elif s_category == 'health & lifestyle':
            form = forms.HealthLifestyleForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #===============================================
        #       end service
        #===============================================


        #===============================================
        #       start home and garden
        #===============================================


        #furniture
        elif s_category == 'furniture':
            form = forms.FurnitureForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)

        #home appliance
        elif s_category == 'home appliances':
            form = forms.HomeApplianceForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #Electricity, AC, Bathroom & Garden
        elif s_category == 'electricity, ac, bathroom & garden':
            form = forms.ElectricityACBathroomGardenForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #other home item
        elif s_category == 'other home items':
            form = forms.OtherHomeItemForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #===============================================
        #       end home and garden
        #===============================================


        #===============================================
        #       start cloth health and beauty
        #===============================================


        #cloth
        elif s_category == 'clothing':
            form = forms.ClothForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #shoe footware
        elif s_category == 'shoes & footwear':
            form = forms.ShoeFootwareForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #jewelery
        elif s_category == 'jewellery':
            form = forms.JeweleryForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #optical items
        elif s_category == 'optical items':
            form = forms.OpticalItemForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #watches
        elif s_category == 'watches':
            form = forms.WatchForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #bag
        elif s_category == 'bags':
            form = forms.BagForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #wholesale bulk
        elif s_category == 'wholesale - bulk':
            form = forms.WholesaleBulkForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)



        #other fashion accessory
        elif s_category == 'other fashion accessories':
            form = forms.OtherFashionAccessoryForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #other personal item
        elif s_category == 'other personal items':
            form = forms.OtherPersonalItemForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #health and beauty product
        elif s_category == 'health & beauty products':
            form = forms.HealthBeautyForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)


        #children item
        elif s_category == 'childrens items':
            form = forms.ChildrenItemForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #===============================================
        #       end cloth health and beauty
        #===============================================


        #===============================================
        #       start Hobby, Sport & Kids
        #===============================================


        #musical instrument
        elif s_category == 'musical instruments':
            form = forms.MusicalInstrumentForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #sports equipment
        elif s_category == 'sports equipment':
            form = forms.SportEquipmentForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #handicraft and decoration
        elif s_category == 'handicrafts & decoration':
            form = forms.HandicraftDecorationForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #antique art and collectible
        elif s_category == 'antique, art & collectibles':
            form = forms.AntiqueArtCollectibleForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #music book movie
        elif s_category == 'music, books & movies':
            form = forms.MusicBookMovieForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)



        #other hobby sports kids
        elif s_category == 'other hobby, sport & kids items':
            form = forms.OtherHobbySportKidForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)


        #===============================================
        #       end Hobby, Sport & Kids
        #===============================================


        #===============================================
        #       start Business & Industry
        #===============================================



        ##Office Supplies & Stationary
        elif s_category == 'office supplies & stationary':
            form = forms.OfficeSuppliesStationaryForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)




        #Industry Machinery & Tools
        elif s_category == 'industry machinery & tools':
            form = forms.IndustryMachineryToolForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)



        #raw materials & industrial supplies
        elif s_category == 'raw materials & industrial supplies':
            form = forms.RawMaterialIndustrialSupplyForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)



        #licences, titles & tenders
        elif s_category == 'licences, titles & tenders':
            form = forms.LicencesTitleTenderForm(request.POST or None, request.FILES)

            if form.is_valid():
                form.deploy(request, subcategory, location)



        #medical equipment & supplies
        elif s_category == 'medical equipment & supplies':
            form = forms.MedicalEquipmentSupplyForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #===============================================
        #       end Business & Industry
        #===============================================



        #===============================================
        #       start Education
        #===============================================


        #textbooks
        elif s_category == 'textbooks':
            form = forms.TextbookForm(request.POST or None, request.FILES)


            if form.is_valid():
                form.deploy(request, subcategory, location)



        #===============================================
        #       end Education
        #===============================================




        variables = {
            'type': type,
            'subcategory': subcategory,
            'location': location,

            'subcategories': subcategories,
            'locations': locations,

            'form': form,
            's_category': s_category,
        }

        return render(request, self.template_name, variables)




