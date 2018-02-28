from django import forms

from . import models

#division form
class DivisionForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))


    def clean(self):
        name = self.cleaned_data.get('name')

        if len(name) == 0:
            raise forms.ValidationError('Enter division name!')
        else:
            division_exists = models.Division.objects.filter(name=name).exists()

            if division_exists:
                raise forms.ValidationError('This division is already exists!')


    def deploy(self):
        name = self.cleaned_data.get('name')

        deploy = models.Division(name=name)
        deploy.save()


#division form
class DistrictForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))

    def clean(self):
        name = self.cleaned_data.get('name')

        if len(name) == 0:
            raise forms.ValidationError('Enter district name!')
        else:
            district_exists = models.District.objects.filter(name=name).exists()

            if district_exists:
                raise forms.ValidationError('This district is already exists!')


    def deploy(self, division):
        name = self.cleaned_data.get('name')

        division_obj = models.Division.objects.get(name=division)

        deploy = models.District(division=division_obj, name=name)
        deploy.save()


#thana form
class ThanaForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))

    def clean(self):
        name = self.cleaned_data.get('name')

        if len(name) == 0:
            raise forms.ValidationError('Enter district name!')


    def deploy(self, division, district):
        name = self.cleaned_data.get('name')

        division_obj = models.Division.objects.get(name=division)
        district_obj = models.District.objects.get(id=district)

        deploy = models.Thana(division=division_obj, district=district_obj, name=name)
        deploy.save()


