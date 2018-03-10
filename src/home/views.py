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




