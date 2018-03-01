from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import login, logout

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

        variables = {
            'personals': personals,
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

        variables = {
            'add_education_form': add_education_form,
        }
        return render(request, self.template_name, variables)



#=============================================================================
#=============================================================================
#                             end resume module
#=============================================================================
#=============================================================================
