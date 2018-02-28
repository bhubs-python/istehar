from django.db import models


#division
class Division(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


#district
class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.division.name) + ":" + str(self.name)


#thana
class Thana(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.division.name) + "-" + str(self.district.name) + ":" + str(self.name)
