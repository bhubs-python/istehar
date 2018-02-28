from django.shortcuts import render
from django.views import View


#staff home page
class Home(View):
    template_name = 'staff/index.html'

    def get(self, request):

        return render(request, self.template_name)
