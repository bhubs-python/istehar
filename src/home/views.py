from django.shortcuts import render, redirect
from django.views import View



#site home page
class Home(View):
    template_name = 'home/index.html'

    def get(self, request):

        return render(request, self.template_name)
