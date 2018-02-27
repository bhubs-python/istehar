from django.shortcuts import render, redirect
from django.views import View



#site registration
class Registration(View):
    template_name = 'account/registration.html'

    def get(self, request):
        return render(request, self.template_name)
