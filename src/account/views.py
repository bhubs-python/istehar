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

            return redirect('account:add-professional')

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

            return redirect('account:add-professional')

        variables = {
            'add_education_form': add_education_form,
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



#=============================================================================
#=============================================================================
#                             end resume module
#=============================================================================
#=============================================================================
