from django.db import models



#catagory
class Catagory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    type_of = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)



#sub catagory
class SubCatagory(models.Model):
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.name)
