from django.shortcuts import render, redirect
from django.views import View

from . import models



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

        if type:
            categories = models.Catagory.objects.filter(type_of=type)

        variables = {
            'type': type,

            'categories': categories,
        }

        return render(request, self.template_name, variables)
