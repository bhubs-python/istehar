from django.db import models
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.models import User

from staff import models as staff_model


#multiple login system : username or email login
class MultiLoginBackend(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        users = UserModel._default_manager.filter(
            Q(**{UserModel.USERNAME_FIELD: username}) | Q(email__iexact=username))

        for user in users:
            if user.check_password(password):
                return user

        if not users:
            UserModel().set_password(password)



#personal model for resume
class Personal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='profile/picture/', default='/media/no-img.jpg', null=True, blank=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    division = models.ForeignKey(staff_model.Division, on_delete=None, null=True, blank=True)
    district = models.ForeignKey(staff_model.District, on_delete=None, null=True, blank=True)
    thana = models.ForeignKey(staff_model.Thana, on_delete=None, null=True, blank=True)


    def __str__(self):
        return str(self.user.username)


#education model for resume
class Education(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    education_level = models.CharField(max_length=50, null=True, blank=True)
    education_specialization = models.CharField(max_length=100, null=True, blank=True)
    institute_university = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return str(self.user.username)


#current professional model for resume
class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    experience = models.FloatField(null=True, blank=True)
    skill = models.CharField(max_length=255, null=True, blank=True)
    about_yourself = models.TextField(max_length=1000, null=True, blank=True)
    current_industry = models.CharField(max_length=100, null=True, blank=True)
    current_business_function = models.CharField(max_length=100, null=True, blank=True)
    role_designation = models.CharField(max_length=255, null=True, blank=True)
    started_in = models.DateField(null=True, blank=True)
    about_current_role = models.TextField(max_length=1000, null=True, blank=True)
    current_salary = models.FloatField(null=True, blank=True)


    def __str__(self):
        return str(self.user.username)



#past employments model for resume
class PastEmployment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    company_name = models.CharField(max_length=100, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    business_function = models.CharField(max_length=100, null=True, blank=True)
    role_designation = models.CharField(max_length=255, null=True, blank=True)
    started_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    about_role = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.user.username)


#permanent location for settings
class PermanentLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    division = models.ForeignKey(staff_model.Division, models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(staff_model.District, models.CASCADE, null=True, blank=True)
    thana = models.ForeignKey(staff_model.Thana, models.CASCADE, null=True, blank=True)


    def __str__(self):
        return str(self.user.username)
