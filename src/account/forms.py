from django import forms
from django.contrib.auth import authenticate
import re
from django.contrib.auth.models import User
from django.db.models import Q

from .models import MultiLoginBackend
from . import models

from staff import models as staff_model


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'email'}))
    password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))


    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if len(username) < 1:
            raise forms.ValidationError("Enter username!")
        else:
            user_exist = User.objects.filter(username__iexact=username).exists()
            if user_exist:
                raise forms.ValidationError("Username already taken!")
            else:
                if len(email) < 1:
                    raise forms.ValidationError("Enter email address!")
                else:
                    email_correction = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
                    if email_correction == None:
                        raise forms.ValidationError("Email not correct!")
                    else:
                        email_exist = User.objects.filter(email__iexact=email).exists()
                        if email_exist:
                            raise forms.ValidationError("Email already exist!")
                        else:
                            if len(password1) < 8:
                                raise forms.ValidationError("Password is too short!")
                            else:
                                if password1 != password2:
                                    raise forms.ValidationError("Password not matched!")


    def registration(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password1)

        user.save()



# login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if len(username) < 1:
            raise forms.ValidationError("Enter Username!")
        else:
            if len(password) < 8:
                raise forms.ValidationError("Password is too short!")
            else:
                user = MultiLoginBackend.authenticate(self, username=username, password=password)
                if not user or not user.is_active:
                    raise forms.ValidationError("Username or Password not matched!")
        return self.cleaned_data


    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = MultiLoginBackend.authenticate(self, username=username, password=password)
        return user



#personal form for resume
gender_list = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),)

class PersonalForm(forms.Form):
    photo = forms.ImageField(required=False)
    name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    phone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    email = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    gender = forms.ChoiceField(choices=gender_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    date_of_birth = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))

    division = forms.ModelChoiceField(queryset=staff_model.Division.objects.all(), required=False,widget=forms.Select(attrs={'class':'input-field'}))

    def clean(self):
        photo = self.cleaned_data.get('photo')
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        gender = self.cleaned_data.get('gender')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        division = self.cleaned_data.get('division')


        if photo == None:
            raise forms.ValidationError('Choose your photo!')
        else:
            if len(name) == 0:
                raise forms.ValidationError('Enter name!')
            else:
                if len(phone) == 0:
                    raise forms.ValidationError('Enter your phone number!')
                if gender == None:
                    raise forms.ValidationError('Choose your gender!')
                else:
                    if date_of_birth == None:
                        raise forms.ValidationError('Choose your birth date!')
                    if division == None:
                        raise forms.ValidationError('Select your division!')



    def deploy(self, request, district, thana):
        photo = self.cleaned_data.get('photo')
        name = self.cleaned_data.get('name')
        phone = self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        gender = self.cleaned_data.get('gender')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        division = self.cleaned_data.get('division')

        district_obj = staff_model.District.objects.get(Q(division=division) & Q(id=district))
        thana_obj = staff_model.Thana.objects.get(Q(district__division=division) & Q(district=district_obj) & Q(id=thana))


        deploy = models.Personal(user=request.user, photo=photo, name=name, phone=phone, email=email, gender=gender, date_of_birth=date_of_birth, division=division, district=district_obj, thana=thana_obj)

        deploy.save()



#add education form
education_level = (
        ('highest_education_level', 'Highest education level'),
        ('primary_school', 'Primary School'),
        ('high_school', 'High School'),
        ('ssc_o_level', 'SSC / O Level'),
        ('hsc_a_level', 'HSC / A Level'),
        ('diploma', 'Diploma'),
        ('bachelor_honors', 'Bachelor / Honors'),
        ('masters', 'Masters'),
        ('phd_doctorate', 'PhD / Doctorate'),
        ('other', 'Other'),)

educational_specialization = (
    ('educational_specialization', 'Educational Specialization'),
    ('arts_humanities', 'Art & Humanities'),
    ('business_management', 'Business & Management'),
    ('accounting', 'Accounting'),
    ('design_fashion', 'Design & Fashion'),
    ('engineering', 'Engineering'),
    ('events_hospitality', 'Events & Hospitality'),
    ('finance_commerce', 'Finance & Commerce'),
    ('human_resources', 'Human Resources'),
    ('information_technology', 'Information Technology'),
    ('law', 'Law'),
    ('marketing_sales', 'Marketing & Sales'),
    ('mass_communication', 'Mass Communication'),
    ('medicine', 'Medicine'),
    ('Sciences', 'Sciences'),
    ('vocational_technical', 'Vocational & Technical'),
    ('other', 'Other'),
)

class EducationForm(forms.Form):
    education_level = forms.ChoiceField(choices=education_level, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    education_specialization = forms.ChoiceField(choices=educational_specialization, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    institute_university = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def clean(self):
        education_level = self.cleaned_data.get('education_level')
        education_specialization = self.cleaned_data.get('education_specialization')
        institute_university = self.cleaned_data.get('institute_university')

        if education_level == 'highest_education_level':
            raise forms.ValidationError('Select education level!')
        else:
            if institute_university == 'educational_specialization':
                raise forms.ValidationError('Enter your institute / university name!')


    def deploy(self, request):
        education_level = self.cleaned_data.get('education_level')
        education_specialization = self.cleaned_data.get('education_specialization')
        institute_university = self.cleaned_data.get('institute_university')

        deploy = models.Education(user=request.user, education_level=education_level, education_specialization=education_specialization, institute_university=institute_university)
        deploy.save()

