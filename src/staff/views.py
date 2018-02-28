from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from . import models
from . import forms


#staff home page
class Home(View):
    template_name = 'staff/index.html'

    def get(self, request):

        return render(request, self.template_name)



#=============================================================================
#=============================================================================
#                             start add division module
#=============================================================================
#=============================================================================


#add division
class AddDivision(View):
    template_name = 'staff/add-division.html'

    def get(self, request):

        division_form = forms.DivisionForm()

        variables = {
            'division_form': division_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):

        division_form = forms.DivisionForm(request.POST or None)

        if division_form.is_valid():
            division_form.deploy()

        variables = {
            'division_form': division_form,
        }

        return render(request, self.template_name, variables)



#division view
class DivisionView(View):
    template_name = 'staff/division-view.html'

    def get(self, request):

        divisions = models.Division.objects.all()
        count = models.Division.objects.all().count()

        variables = {
            'divisions': divisions,
            'count': count,
        }

        return render(request, self.template_name, variables)



#=============================================================================
#=============================================================================
#                             end add division module
#=============================================================================
#=============================================================================



#=============================================================================
#=============================================================================
#                             start add district module
#=============================================================================
#=============================================================================

#add district division list
class AddDistrictDivisionList(View):
    template_name = 'staff/add-district-division-list.html'

    def get(self, request):

        divisions = models.Division.objects.all()
        count = models.Division.objects.all().count()

        variables = {
            'divisions': divisions,
            'count': count,
        }

        return render(request, self.template_name, variables)



#add district
class AddDistrict(View):
    template_name = 'staff/add-district.html'

    def get(self, request, division):
        get_object_or_404(models.Division, name=division)

        district_form = forms.DistrictForm()

        variables = {
            'district_form': district_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request, division):
        get_object_or_404(models.Division, name=division)

        district_form = forms.DistrictForm(request.POST or None)

        if district_form.is_valid():
            district_form.deploy(division)

        variables = {
            'district_form': district_form,
        }

        return render(request, self.template_name, variables)



#district view
class DistrictView(View):
    template_name = 'staff/district-view.html'

    def get(self, request):

        divisions = models.Division.objects.all()
        districts = models.District.objects.all()
        count = models.District.objects.all().count()

        variables = {
            'divisions': divisions,
            'districts': districts,
            'count': count,
        }

        return render(request, self.template_name, variables)



#=============================================================================
#=============================================================================
#                             end add district module
#=============================================================================
#=============================================================================


#=============================================================================
#=============================================================================
#                             start add thana module
#=============================================================================
#=============================================================================



#add thana division list
class AddThanaDivisionList(View):
    template_name = 'staff/add-thana-division-list.html'

    def get(self, request):

        divisions = models.Division.objects.all()
        count = models.Division.objects.all().count()

        variables = {
            'divisions': divisions,
            'count': count,
        }

        return render(request, self.template_name, variables)



#add thana district list
class AddThanaDistrictList(View):
    template_name = 'staff/add-thana-district-list.html'

    def get(self, request, division):
        get_object_or_404(models.Division, name=division)

        districts = models.District.objects.filter(division__name=division)
        count = models.District.objects.filter(division__name=division).count()

        variables = {
            'districts': districts,
            'count': count,
        }

        return render(request, self.template_name, variables)



#add thana
class AddThana(View):
    template_name = 'staff/add-thana.html'

    def get(self, request, division, district):
        get_object_or_404(models.Division, name=division)
        get_object_or_404(models.District, id=district)

        thana_form = forms.ThanaForm()

        variables = {
            'thana_form': thana_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request, division, district):
        get_object_or_404(models.Division, name=division)
        get_object_or_404(models.District, id=district)

        thana_form = forms.ThanaForm(request.POST or None)

        if thana_form.is_valid():
            thana_form.deploy(division, district)

        variables = {
            'thana_form': thana_form,
        }

        return render(request, self.template_name, variables)



#thana view
class ThanaView(View):
    template_name = 'staff/thana-view.html'

    def get(self, request):

        divisions = models.Division.objects.all()
        districts = models.District.objects.all()
        thanas = models.Thana.objects.all()
        count = models.Thana.objects.all().count()

        variables = {
            'divisions': divisions,
            'districts': districts,
            'thanas': thanas,
            'count': count,
        }

        return render(request, self.template_name, variables)



#=============================================================================
#=============================================================================
#                             start add thana module
#=============================================================================
#=============================================================================

