from django.shortcuts import render, redirect
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

        categories = None
        if type:
            categories = models.Catagory.objects.filter(type_of=type)

        variables = {
            'type': type,

            'categories': categories,
        }

        return render(request, self.template_name, variables)


#post location
class PostLocation(View):
    template_name = 'home/post-location.html'

    def get(self, request):

        type = request.GET.get('type')
        subcategory = request.GET.get('subcategory')

        divisions = None
        if type:
            divisions = staff_model.Division.objects.all()

        variables = {
            'type': type,

            'divisions': divisions,
        }

        return render(request, self.template_name, variables)


#post details
class PostDetails(View):
    template_name = 'home/post-details.html'

    def get(self, request):

        type = request.GET.get('type')

        if type:
            categories = models.Catagory.objects.filter(type_of=type)

        variables = {
            'type': type,

            'categories': categories,
        }

        return render(request, self.template_name, variables)




