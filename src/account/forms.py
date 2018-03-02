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



#add professional form
current_industry_list = (
    ('current_industry', 'Current Industry'),
    ('agri_food', 'Agriculture & Food Processing'),
    ('automobiles', 'Automobiles'),
    ('bank_finance_services', 'Banking & Finance Services'),
    ('civil_construction', 'Civil & Construction'),
    ('consumer_durables', 'Consumer Goods & Durables'),
    ('consulting', 'Consulting'),
    ('education', 'Education'),
    ('engineering', 'Engineering'),
    ('ecommerce_internet', 'Ecommerce & Internet'),
    ('events_entertainment', 'Events & Entertainment'),
    ('export_import', 'Export & Import'),
    ('garments_textile', 'Garments & Textile'),
    ('govt_public_sector', 'Government & Public Sector'),
    ('healthcare', 'Healthcare'),
    ('hotel_travel_leisure', 'Hotel, Travel & Leisure'),
    ('insurance', 'Insurance'),
    ('it_telecom', 'IT & Telecom'),
    ('logistics_transport', 'Logistics & Transportation'),
    ('manufacturing', 'Manufacturing'),
    ('news_media', 'News & Media'),
    ('nonprofit_ngo', 'NGO & Non Profit'),
    ('outsourcing', 'Outsourcing'),
    ('pharma', 'Pharmaceutical'),
    ('real_estate', 'Real Estate'),
    ('security_services', 'Security Services'),
    ('wholesale_retail', 'Wholesale & Retail'),
    ('others', 'Others'),
)


current_business_function_list = (
    ('current_business_function', 'Current Business Function'),
    ('administration', 'Administration'),
    ('accounting_finance', 'Accounting & Finance'),
    ('customer_support', 'Customer Support'),
    ('data_entry_analysis', 'Data Entry & Analysis'),
    ('creative_design_architecture', 'Creative, Design & Architecture'),
    ('education_training', 'Education & Training'),
    ('hospitality', 'Hospitality'),
    ('human_resources', 'Human Resources'),
    ('it_telecom', 'IT & Telecom'),
    ('legal', 'Legal'),
    ('logistics', 'Logistics'),
    ('management', 'Management'),
    ('manufacturing', 'Manufacturing'),
    ('marketing', 'Marketing'),
    ('operations', 'Operations'),
    ('quality_assurance', 'Quality Assurance'),
    ('research_technical', 'Research & Technical'),
    ('sales_distribution', 'Sales & Distribution'),
    ('security', 'Security'),
    ('others', 'Others'),
)

class ProfessionalForm(forms.Form):
    experience = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    skill = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    about_yourself = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}))
    current_industry = forms.ChoiceField(choices=current_industry_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    current_business_function = forms.ChoiceField(choices=current_business_function_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    role_designation = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    started_in = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))
    about_current_role = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}))
    current_salary = forms.FloatField(required=False, widget=forms.TextInput(attrs={'class': 'validate'}))


    def clean(self):
        experience = self.cleaned_data.get('experience')
        skill = self.cleaned_data.get('skill')
        about_yourself = self.cleaned_data.get('about_yourself')
        current_industry = self.cleaned_data.get('current_industry')
        current_business_function = self.cleaned_data.get('current_business_function')
        role_designation = self.cleaned_data.get('role_designation')
        started_in = self.cleaned_data.get('started_in')
        about_current_role = self.cleaned_data.get('about_current_role')
        current_salary = self.cleaned_data.get('current_salary')

        if experience == None:
            raise forms.ValidationError('Enter year of experience!')
        else:
            if current_industry == 'current_industry':
                raise forms.ValidationError('Choose Current Industry!')
            else:
                if current_business_function == 'current_business_function':
                    raise forms.ValidationError('Select Current Business Function!')
                else:
                    if len(started_in) == 0:
                        raise forms.ValidationError('Select start date!')


    def deploy(self, request):
        experience = self.cleaned_data.get('experience')
        skill = self.cleaned_data.get('skill')
        about_yourself = self.cleaned_data.get('about_yourself')
        current_industry = self.cleaned_data.get('current_industry')
        current_business_function = self.cleaned_data.get('current_business_function')
        role_designation = self.cleaned_data.get('role_designation')
        started_in = self.cleaned_data.get('started_in')
        about_current_role = self.cleaned_data.get('about_current_role')
        current_salary = self.cleaned_data.get('current_salary')


        deploy = models.Professional(user=request.user, experience=experience, skill=skill, about_yourself=about_yourself, current_industry=current_industry, current_business_function=current_business_function, role_designation=role_designation, started_in=started_in, about_current_role=about_current_role, current_salary=current_salary)
        deploy.save()




class PastEmploymentForm(forms.Form):
    company_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    industry = forms.ChoiceField(choices=current_industry_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    business_function = forms.ChoiceField(choices=current_business_function_list, required=False, widget=forms.Select(attrs={'class': 'validate'}))
    role_designation = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    started_date = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))
    end_date = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate datepicker'}))
    about_role = forms.CharField(required=False, max_length=1000, widget=forms.Textarea(attrs={'class': 'validate materialize-textarea'}))


    def clean(self):
        company_name = self.cleaned_data.get('company_name')
        industry = self.cleaned_data.get('industry')
        business_function = self.cleaned_data.get('business_function')
        role_designation = self.cleaned_data.get('role_designation')
        started_date = self.cleaned_data.get('started_date')
        end_date = self.cleaned_data.get('end_date')
        about_role = self.cleaned_data.get('about_role')

        if len(company_name) == 0:
            raise forms.ValidationError('Enter company name!')
        else:
            if len(role_designation) == 0:
                raise forms.ValidationError('Enter your role / designation')
            else:
                if len(started_date) == 0:
                    raise forms.ValidationError('Select start date!')
                else:
                    if len(end_date) == 0:
                        raise forms.ValidationError('Select end date!')



    def deploy(self, request):
        company_name = self.cleaned_data.get('company_name')
        industry = self.cleaned_data.get('industry')
        business_function = self.cleaned_data.get('business_function')
        role_designation = self.cleaned_data.get('role_designation')
        started_date = self.cleaned_data.get('started_date')
        end_date = self.cleaned_data.get('end_date')
        about_role = self.cleaned_data.get('about_role')

        deploy = models.PastEmployment(user=request.user, company_name=company_name, industry=industry, business_function=business_function, role_designation=role_designation, started_date=started_date, end_date=end_date, about_role=about_role)
        deploy.save()







