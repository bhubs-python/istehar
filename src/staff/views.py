from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from django.db.models import Q

from . import models
from . import forms

from home import models as home_model


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



#division edit
class DivisionEdit(View):
    template_name = 'staff/division-edit.html'

    def get(self, request, division):
        get_object_or_404(models.Division, id=division)

        division_edit_form = forms.DivisionEditForm(instance=models.Division.objects.get(id=division))

        variables = {
            'division_edit_form': division_edit_form,
            'division': division,
        }

        return render(request, self.template_name, variables)

    def post(self, request, division):
        get_object_or_404(models.Division, id=division)

        division_edit_form = forms.DivisionEditForm(request.POST or None, instance=models.Division.objects.get(id=division))

        if division_edit_form.is_valid():
            division_edit_form.save()

        variables = {
            'division_edit_form': division_edit_form,
            'division': division,
        }

        return render(request, self.template_name, variables)



#division delete
class DivisionDelete(View):
    template_name = 'staff/division-delete.html'

    def get(self, request, division):
        get_object_or_404(models.Division, id=division)

        variables = {
            'division': division,
        }

        return render(request, self.template_name, variables)

    def post(self, request, division):
        get_object_or_404(models.Division, id=division)

        if request.POST.get('yes') == 'yes':
            division_obj = models.Division.objects.get(id=division)
            division_obj.delete()

            return redirect('staff:division-view')
        elif request.POST.get('no') == 'no':
            return redirect('staff:division-view')

        variables = {
            'division': division,
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



#district edit
class DistrictEdit(View):
    template_name = 'staff/district-edit.html'

    def get(self, request, district):
        get_object_or_404(models.District, id=district)

        district_edit_form = forms.DistrictEditForm(instance=models.District.objects.get(id=district))

        variables = {
            'district_edit_form': district_edit_form,
            'district': district,
        }

        return render(request, self.template_name, variables)

    def post(self, request, district):
        get_object_or_404(models.District, id=district)

        district_edit_form = forms.DivisionEditForm(request.POST or None, instance=models.District.objects.get(id=district))

        if district_edit_form.is_valid():
            district_edit_form.save()

        variables = {
            'district_edit_form': district_edit_form,
            'district': district,
        }

        return render(request, self.template_name, variables)



#district delete
class DistrictDelete(View):
    template_name = 'staff/district-delete.html'

    def get(self, request, district):
        get_object_or_404(models.District, id=district)

        variables = {
            'district': district,
        }

        return render(request, self.template_name, variables)

    def post(self, request, district):
        get_object_or_404(models.District, id=district)

        if request.POST.get('yes') == 'yes':
            district_obj = models.District.objects.get(id=district)
            district_obj.delete()

            return redirect('staff:district-view')
        elif request.POST.get('no') == 'no':
            return redirect('staff:district-view')

        variables = {
            'district': district,
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
            thana_form.deploy(district)

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



#district edit
class ThanaEdit(View):
    template_name = 'staff/thana-edit.html'

    def get(self, request, thana):
        get_object_or_404(models.Thana, id=thana)

        thana_edit_form = forms.ThanaEditForm(instance=models.Thana.objects.get(id=thana))

        variables = {
            'thana_edit_form': thana_edit_form,
            'thana': thana,
        }

        return render(request, self.template_name, variables)

    def post(self, request, thana):
        get_object_or_404(models.Thana, id=thana)

        thana_edit_form = forms.ThanaEditForm(request.POST or None, instance=models.Thana.objects.get(id=thana))

        if thana_edit_form.is_valid():
            thana_edit_form.save()

        variables = {
            'thana_edit_form': thana_edit_form,
            'thana': thana,
        }

        return render(request, self.template_name, variables)



#thana delete
class ThanaDelete(View):
    template_name = 'staff/thana-delete.html'

    def get(self, request, thana):
        get_object_or_404(models.Thana, id=thana)

        variables = {
            'thana': thana,
        }

        return render(request, self.template_name, variables)

    def post(self, request, thana):
        get_object_or_404(models.Thana, id=thana)

        if request.POST.get('yes') == 'yes':
            thana_obj = models.Thana.objects.get(id=thana)
            thana_obj.delete()

            return redirect('staff:thana-view')
        elif request.POST.get('no') == 'no':
            return redirect('staff:thana-view')

        variables = {
            'thana': thana,
        }

        return render(request, self.template_name, variables)




#=============================================================================
#=============================================================================
#                             start add thana module
#=============================================================================
#=============================================================================





#=============================================================================
#=============================================================================
#                             start api module
#=============================================================================
#=============================================================================




#district list api view
class DistrictAPI(APIView):
    def get(self, request):
        if request.GET.get("division"):
            division = request.GET.get("division")

            division_obj = models.District.objects.filter(division__id=division)

            serializer = serializers.DistrictSerializer(division_obj, many=True)

            return Response(serializer.data)
        else:
            return redirect('account:login')


#thana list api view
class ThanaAPI(APIView):
    def get(self, request):
        if request.GET.get("division") and request.GET.get('district'):
            division = request.GET.get("division")
            district = request.GET.get("district")

            thana_obj = models.Thana.objects.filter(Q(district__division__id=division) & Q(district__id=district))

            serializer = serializers.DistrictSerializer(thana_obj, many=True)

            return Response(serializer.data)
        else:
            return redirect('account:login')


#subcategory list api view
class SubCategoryAPI(APIView):
    def get(self, request):
        if request.GET.get("type"):
            type = request.GET.get("type")

            subcategory_obj = home_model.SubCatagory.objects.filter(Q(catagory__id=type))

            serializer = serializers.SubCategorySerializer(subcategory_obj, many=True)

            return Response(serializer.data)
        else:
            return redirect('account:login')


#=============================================================================
#=============================================================================
#                             end api module
#=============================================================================
#=============================================================================






