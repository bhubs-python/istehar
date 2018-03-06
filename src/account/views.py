from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import login, logout
from django.contrib.auth import update_session_auth_hash

from . import forms
from staff import models as staff_model
from . import models


# logout
def logout_request(request):
    logout(request)
    return redirect('account:login')


#site registration options
class RegistrationOptions(View):
    template_name = 'account/registration-options.html'

    def get(self, request):

        return render(request, self.template_name)


#site registration
class Registration(View):
    template_name = 'account/registration.html'

    def get(self, request):

        registration_form = forms.RegistrationForm()

        variables = {
            'registration_form': registration_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):

        registration_form = forms.RegistrationForm(request.POST or None)

        if registration_form.is_valid():
            registration_form.registration()

            return redirect('account:login')

        variables = {
            'registration_form': registration_form,
        }

        return render(request, self.template_name, variables)



#site registration
class Login(View):
    template_name = 'account/login.html'

    def get(self, request):

        login_form = forms.LoginForm()

        variables = {
            'login_form': login_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):

        login_form = forms.LoginForm(request.POST or None)

        if login_form.is_valid():
            user = login_form.login()

            if user:
                login(request, user)
                return redirect('account:dashboard')

        variables = {
            'login_form': login_form,
        }

        return render(request, self.template_name, variables)


#=============================================================================
#=============================================================================
#                             start dashboard module
#=============================================================================
#=============================================================================



#dashboard - ads list
class Dashboard(View):
    template_name = 'account/dashboard.html'

    def get(self, request):

        return render(request, self.template_name)



#=============================================================================
#=============================================================================
#                             end dashboard module
#=============================================================================
#=============================================================================


#=============================================================================
#=============================================================================
#                             start membership module
#=============================================================================
#=============================================================================


#membership
class Membership(View):
    template_name = 'account/membership.html'

    def get(self, request):

        return render(request, self.template_name)




#=============================================================================
#=============================================================================
#                             end membership module
#=============================================================================
#=============================================================================




#=============================================================================
#=============================================================================
#                             start resume module
#=============================================================================
#=============================================================================



#resume
class Resume(View):
    template_name = 'account/resume.html'

    def get(self, request):
        personals = models.Personal.objects.filter(user=request.user)
        educations = models.Education.objects.filter(user=request.user)
        professionals = models.Professional.objects.filter(user=request.user)
        past_employments = models.PastEmployment.objects.filter(user=request.user)

        variables = {
            'personals': personals,
            'educations': educations,
            'professionals': professionals,
            'past_employments': past_employments,
        }

        return render(request, self.template_name, variables)



#add personal
class AddPersonal(View):
    template_name = 'account/add-personal.html'

    def get(self, request):
        add_personal_form = forms.PersonalForm()

        variables = {
            'add_personal_form': add_personal_form,
        }
        return render(request, self.template_name, variables)


    def post(self, request):
        add_personal_form = forms.PersonalForm(request.POST or None, request.FILES)

        if add_personal_form.is_valid():
            district = request.POST.get('district')
            thana = request.POST.get('thana')

            add_personal_form.deploy(request, district, thana)

            return redirect('account:add-education')

        variables = {
            'add_personal_form': add_personal_form,
        }
        return render(request, self.template_name, variables)



#add personal
class EditPersonal(View):
    template_name = 'account/edit-personal.html'

    def get(self, request):
        personals = models.Personal.objects.filter(user=request.user)

        my_division = None
        my_district = None
        for personal in personals:
            my_division = personal.division
            my_district = personal.district

        divisions = staff_model.Division.objects.all()
        districts = staff_model.District.objects.filter(division=my_division)
        thanas = staff_model.Thana.objects.filter(district=my_district)

        edit_personal_form = forms.EditPersonalForm(instance=models.Personal.objects.get(user=request.user))

        variables = {
            'edit_personal_form': edit_personal_form,

            'personals': personals,

            'divisions': divisions,
            'districts': districts,
            'thanas': thanas,
        }
        return render(request, self.template_name, variables)


    def post(self, request):
        personals = models.Personal.objects.filter(user=request.user)

        my_division = None
        my_district = None
        for personal in personals:
            my_division = personal.division
            my_district = personal.district

        divisions = staff_model.Division.objects.all()
        districts = staff_model.District.objects.filter(division=my_division)
        thanas = staff_model.Thana.objects.filter(district=my_district)

        edit_personal_form = forms.EditPersonalForm(request.POST or None, request.FILES, instance=models.Personal.objects.get(user=request.user))

        if edit_personal_form.is_valid():
            user_division = request.POST.get('division')
            user_district = request.POST.get('district')
            user_thana = request.POST.get('thana')

            if user_division == 'none' or user_division == None:
                division_obj = staff_model.Division.objects.get(name='none')
            else:
                division_obj = staff_model.Division.objects.get(id=user_division)

            if user_district == 'none' or user_district == None:
                district_obj = staff_model.District.objects.get(name='none')
            else:
                district_obj = staff_model.District.objects.get(id=user_district)

            if user_thana == 'none' or user_thana == None:
                thana_obj = staff_model.Thana.objects.get(name='none')
            else:
                thana_obj = staff_model.Thana.objects.get(id=user_thana)

            edit_obj = edit_personal_form.save()
            edit_obj_id = edit_obj.id

            update_location = models.Personal.objects.filter(id=edit_obj_id).update(division=division_obj, district=district_obj, thana=thana_obj)

            return redirect('account:resume')

        variables = {
            'edit_personal_form': edit_personal_form,
            'personals': personals,

            'divisions': divisions,
            'districts': districts,
            'thanas': thanas,
        }
        return render(request, self.template_name, variables)



#add education
class AddEducation(View):
    template_name = 'account/add-education.html'

    def get(self, request):
        add_education_form = forms.EducationForm()

        variables = {
            'add_education_form': add_education_form,
        }
        return render(request, self.template_name, variables)


    def post(self, request):
        add_education_form = forms.EducationForm(request.POST or None)

        if add_education_form.is_valid():
            add_education_form.deploy(request)

            return redirect('account:add-professional')

        variables = {
            'add_education_form': add_education_form,
        }
        return render(request, self.template_name, variables)



#edit education
class EditEducation(View):
    template_name = 'account/edit-education.html'

    def get(self, request):
        edit_education_form = forms.EditEducationForm(instance=models.Education.objects.get(user=request.user))

        variables = {
            'edit_education_form': edit_education_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        edit_education_form = forms.EditEducationForm(request.POST or None, instance=models.Education.objects.get(user=request.user))

        if edit_education_form.is_valid():
            edit_education_form.save()

        variables = {
            'edit_education_form': edit_education_form,
        }

        return render(request, self.template_name, variables)


#add Professionale
class AddProfessional(View):
    template_name = 'account/add-professional.html'

    def get(self, request):
        add_professional_form = forms.ProfessionalForm()

        variables = {
            'add_professional_form': add_professional_form,
        }
        return render(request, self.template_name, variables)


    def post(self, request):
        add_professional_form = forms.ProfessionalForm(request.POST or None)

        if add_professional_form.is_valid():
            add_professional_form.deploy(request)

            return redirect('account:add-employment-history')

        variables = {
            'add_professional_form': add_professional_form,
        }
        return render(request, self.template_name, variables)


#edit professional
class EditProfessional(View):
    template_name = 'account/edit-professional.html'

    def get(self, request):
        edit_professional_form = forms.EditProfessionalForm(instance=models.Professional.objects.get(user=request.user))

        variables = {
            'edit_professional_form': edit_professional_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        edit_professional_form = forms.EditProfessionalForm(request.POST or None, instance=models.Professional.objects.get(user=request.user))

        if edit_professional_form.is_valid():
            edit_professional_form.save()

        variables = {
            'edit_professional_form': edit_professional_form,
        }

        return render(request, self.template_name, variables)



#add past employment
class AddPastEmployment(View):
    template_name = 'account/add-past-employment.html'

    def get(self, request):
        add_past_employment_form = forms.PastEmploymentForm()

        variables = {
            'add_past_employment_form': add_past_employment_form,
        }
        return render(request, self.template_name, variables)


    def post(self, request):
        add_past_employment_form = forms.PastEmploymentForm(request.POST or None)

        if add_past_employment_form.is_valid():
            add_past_employment_form.deploy(request)

            return redirect('account:resume')

        variables = {
            'add_past_employment_form': add_past_employment_form,
        }
        return render(request, self.template_name, variables)



#edit past employment
class EditPastEmployment(View):
    template_name = 'account/edit-past-employment.html'

    def get(self, request):
        edit_past_employment_form = forms.EditPastEmploymentForm(instance=models.PastEmployment.objects.get(user=request.user))

        variables = {
            'edit_past_employment_form': edit_past_employment_form,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        edit_past_employment_form = forms.EditPastEmploymentForm(request.POST or None, instance=models.PastEmployment.objects.get(user=request.user))

        if edit_past_employment_form.is_valid():
            edit_past_employment_form.save()

        variables = {
            'edit_past_employment_form': edit_past_employment_form,
        }

        return render(request, self.template_name, variables)



#settings
class Settings(View):
    template_name = 'account/settings.html'

    def get(self, request):

        locations = models.PermanentLocation.objects.filter(user=request.user)

        change_password_form = forms.ChangePasswordForm(request.user)

        my_division = None
        my_district = None
        for location in locations:
            my_division = location.division
            my_district = location.district

        divisions = staff_model.Division.objects.all()
        districts = staff_model.District.objects.filter(division=my_division)
        thanas = staff_model.Thana.objects.filter(district=my_district)

        variables = {
            'change_password_form': change_password_form,
            'locations': locations,
            'divisions': divisions,
            'districts': districts,
            'thanas': thanas,
        }

        return render(request, self.template_name, variables)

    def post(self, request):
        locations = models.PermanentLocation.objects.filter(user=request.user)
        change_password_form = forms.ChangePasswordForm(data=request.POST or None, user=request.user)

        my_division = None
        my_district = None
        for location in locations:
            my_division = location.division
            my_district = location.district

        divisions = staff_model.Division.objects.all()
        districts = staff_model.District.objects.filter(division=my_division)
        thanas = staff_model.Thana.objects.filter(district=my_district)

        if request.POST.get('change_location') == 'change_location':
            user_division = request.POST.get('division')
            user_district = request.POST.get('district')
            user_thana = request.POST.get('thana')

            if user_division == 'none' or user_division == None:
                division_obj = staff_model.Division.objects.get(name='none')
            else:
                division_obj = staff_model.Division.objects.get(id=user_division)

            if user_district == 'none' or user_district == None:
                district_obj = staff_model.District.objects.get(name='none')
            else:
                district_obj = staff_model.District.objects.get(id=user_district)

            if user_thana == 'none' or user_thana == None:
                thana_obj = staff_model.Thana.objects.get(name='none')
            else:
                thana_obj = staff_model.Thana.objects.get(id=user_thana)


            #update_location = models.PermanentLocation.objects.filter(user=request.user).update(division=division_obj, district=district_obj, thana=thana_obj)

            update_or_create_location = models.PermanentLocation.objects.update_or_create(user=request.user, defaults={'division': division_obj, 'district': district_obj, 'thana': thana_obj})


            return redirect('account:settings')


        if request.POST.get('change_password') == 'change_password':
            if change_password_form.is_valid():
                change_password_form.save()
                update_session_auth_hash(request, change_password_form.user)

                return redirect('account:settings')

        variables = {
            'change_password_form': change_password_form,
            'locations': locations,
            'divisions': divisions,
            'districts': districts,
            'thanas': thanas,
        }

        return render(request, self.template_name, variables)



#=============================================================================
#=============================================================================
#                             end resume module
#=============================================================================
#=============================================================================
