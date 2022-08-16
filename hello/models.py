from pydoc import describe
from turtle import title
from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


from django.db import models
from django.contrib.auth.models import User

def increment_car_number():
    last_car = CAR.objects.all().order_by('id').last()
    if not last_car:
        return '01'  + str(20)
    else:
        car_number = last_car.car_number
        car_int =str(car_number)
        new_car_int = int(car_int [-1])+ 18
        new_car_n = car_int + str(new_car_int)
    return new_car_n




class CAR(models.Model):
    # car_number = models.CharField(auto_created=True ,  max_length = 20, default = increment_car_number, editable=False)
    # typo = models.ForeignKey(VICL, on_delete=models.CASCADE)
    person = models.CharField(help_text = 'اسم صاحب السيارة '  , max_length=60, blank = True)
    C_number = models.IntegerField(unique = True)

    car_type_choices = (
    ('Private','Private'),
    ('Goverment', 'Goverment'),
    ('Taxi', 'Taxi'),
    )

    privGovTaxi = models.CharField(default='Private', help_text='اجرة - خصوصي - عمومي' , max_length=10 ,choices=car_type_choices)


    def __str__(self):
        self.C_number =str(self.C_number)
        return self.C_number



class VIOLATION(models.Model):
    desc=models.CharField(default="ركون خاطئ" , max_length=50)
    car = models.ForeignKey(CAR, related_name='violations', on_delete=models.CASCADE)
    V_number = models.BigAutoField(primary_key=True, editable=False)

    cost = models.PositiveIntegerField()
    created_dt = models.DateTimeField(auto_now_add=True)
    IsPaid = models.BooleanField(default=False)

    def __str__(self):
        o = self.V_number
        o =  str(self.cost)
        return str(self.cost) + " car number>" + str(self.car.C_number)

class CUSTOMER(models.Model):
    account = models.ForeignKey(User, auto_created=True,related_name='User', on_delete=models.CASCADE)
    # mobile = models.IntegerField(max_length=9)
    # email = models.EmailField( max_length=254)
    test_number = models.IntegerField(unique = True, blank = True, null = True, default = None)
    car = models.ForeignKey(CAR, related_name='Car', on_delete=models.CASCADE)
    def __str__(self):
        # self.account =str(self.car) + str(self.account.username)
        return self.account.username


class Desc(models.Model):
    title=models.CharField( max_length=20)
    describe=models.CharField( max_length=50)
    def __str__(self) -> str:
        return self.title