from django.shortcuts import render
# from django.http import HttpResponse
from .models import Greeting
from django.contrib.auth import login as auth_login
from .forms import  SignUpForm 
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
# from .forms import SignUpForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import CUSTOMER, VIOLATION, CAR
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def click (request):
    cars = CAR.objects.all()
    for i in cars:
        print(i)
    c={
        'cars':cars
    }
    
    return render(request,'click.html',c)


def clic (request):
    cars = CAR.objects.all()
    for i in cars:
        print(i)
    c={
        'cars':cars
    }
    
    return render(request,'clic.html',c)



def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index')
    return render(request,'signup.html',{'form':form})



@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name','last_name','email',)
    template_name = 'accounts/my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})



# def index(request):
#     return render(request, 'carsapp/index.html')
def index1(request):
    return render(request, 'carsapp/test.html')


def index(request):
    return render(request, 'index.html')

def profile(request):
    class MyCar:
        row_num =0
        car_no=0
        car_id=0
        car_vals=[]
    
    try:
        usrCarsObj =CUSTOMER.objects.filter(account=request.user.id)
    except:
        messages.info(request, 'you dont have any car yet')


    myCars=[]
    v_lst=[]
    row_id=1
    myCars.clear()
    for itm in usrCarsObj:
        tmpCar=MyCar()
        tmpCar.car_id=itm.car.id
        tmpCar.car_no=itm.car.C_number
        tmpCar.row_num=row_id
        myCars.append(tmpCar)
        row_id=row_id+1



    ndx =0
    while ndx < len(myCars):
        the_car =myCars[ndx]
        print("index => ",ndx,"size is ", the_car.car_id)
        vs = VIOLATION.objects.filter(car=the_car.car_id,IsPaid=False)
        print(len(vs), "was ln of vs",the_car.car_id)
        for in_val in vs :
            v_lst.append(in_val)
            print(" val added ",in_val.V_number,in_val.cost)
        myCars[ndx].car_vals=v_lst
        v_lst=[]
        ndx+=1


    cbv={

        'myCars':myCars
    }

    # print(myCars[0].car_id,myCars[1].car_id)    
    if len(myCars)>0:
        return render(request, 'carsapp/profile_page.html',cbv)
    else:
        messages.info(request, 'you dont have any car yet')
        return render(request, 'index.html', cbv)


@login_required
def new_carTest(request):
    user1=request.user
    u_nn=user1.id
    if request.method=='POST':
        car_n3 = request.POST['car_number']
        cars=CAR.objects.all()
        ca =CAR.objects.filter(C_number=car_n3)
        if len(ca)>1:
            pass
        elif len(ca)==1 :
            car=ca.first()
        elif len(ca) ==0 :
            messages.info(request, 'this car dose not exist')
            return render(request,'carsapp/test_form.html')
        else:
            messages.info(request, 'you dont have any car yet')
            return render(request,'carsapp/test_form.html')
        user1=request.user
        
        list_c=[]
        for i in CUSTOMER.objects.filter(account=request.user):
            print(i.car)
            list_c.append(i.car)
            # make sure that car not regiser twice for the same user 
        # print(car,"l")
        if car in list_c:
            messages.info(request, 'you already regisered this car')
            
        else:
            
            new_customer=CUSTOMER.objects.create(
                account=user1,
                car=car
            )
            u_nn=user1.id
            return redirect('profile')
    return render(request,'carsapp/test_form.html')










def new_payment(request,v_n):
    my_val= VIOLATION.objects.filter(V_number=v_n,IsPaid=False).first()
    print("***************",my_val.IsPaid)
    my_car=my_val.car
    # print("***************",my_car)

    data={
        'my_val':my_val,
        'my_car':my_car,
    }

    return render(request, 'carsapp/payment.html',data)



def pay_done(request,v_n1):
    my_val= VIOLATION.objects.filter(V_number=v_n1).update(IsPaid=True)
    my_val2= VIOLATION.objects.filter(V_number=v_n1).first()

    my_car=my_val2.car
    data={
        'my_val':my_val2,
        'my_car':my_car,

    }

    return redirect('profile')
