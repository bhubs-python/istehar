from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View

from . import models
from staff import models as staff_model



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
        if subcategory:
            subcategories = models.SubCatagory.objects.filter(id=subcategory)

        locations = None
        if location:
            locations = staff_model.Thana.objects.filter(id=location)

        variables = {
            'type': type,
            'subcategory': subcategory,
            'location': location,

            'subcategories': subcategories,
            'locations': locations,
        }

        return render(request, self.template_name, variables)




