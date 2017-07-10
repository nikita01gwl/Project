from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.core.urlresolvers import reverse


# Create your models here.
class employee(models.Model):

    Name=models.CharField(max_length=100)
    Adhaar = models.IntegerField()
    Licence_Number=models.IntegerField()
    RC_Card_No=models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?([0,7,8,9]{1})}?\d{9,11}$',
                                 message="Phone number must be entered in the format: '9848281223'. Only 10 digits allowed.")
    Mobile_No = models.CharField(validators=[phone_regex], max_length=10)
    Current_Address=models.TextField(max_length=500)
    Permanent_Address=models.TextField(max_length=500)
    Father_spouse_Name=models.CharField(max_length=100)
    Address=models.TextField(max_length=500)

    Employee_Id=models.CharField(max_length=100,default='Id',primary_key=True)
    Hub=models.CharField(max_length=100,default='Hub')
    Date_of_Joining=models.DateField(default=date.today)
    Choices=(('Rider', 'RIDER'), ('Admin', 'ADMIN'))
    Role=models.CharField(max_length=5,choices=Choices,null=True)

    


    def __str__(self):
        return self.Employee_Id

    def get_absolute_url(self):
        return reverse ("emp:download", kwargs={"Id":self.Employee_Id})


