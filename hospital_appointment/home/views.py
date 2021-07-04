from django.http import response, HttpResponse
from django.shortcuts import render,HttpResponse
from .models import*
from django.contrib.auth.models import User,Group
import logging

# Create your views here.

def homepage(request):
    return render(request,'index.html')

# -------------------------------------------------------------------------------------------------------------------------------------
# about
 
def about(request):
    return render(request,'about.html')

#--------------------------------------------------------------------------------------------------------------------------------------
#log in

def login(request):
    return render(request,'login.html')
#--------------------------------------------------------------------------------------------------------------------------------------
# sign up

def createacc(request):
    user = 'none'
    error = ''
    if request.POST == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirm password']
        gender = request.POST['gender']
        phonenumber = request.POST['phone number']
        address = request.POST['address']
        birthday = request.POST['birthday']
        bloodgroup = request.POST['bloodgroup']
        
        try:
            if password == confirmpassword:
                Patient.object(name = 'name', email = 'email', gender ='gender', phonenumber = 'phonenumber', address = 'address', birthday = 'birthday', bloodgroup = 'bloodgroup')
                user = User.object.create_user(first_name = 'name', email = 'email',password = 'password ',username = 'email')
                pat_group = Group.objects.get(name ='patient')
                pat_group.user_set.add(user)
                user.save()
                error = 'no'
            else:
                error = 'yes'
        except Exception as e:
            # raise e
            error = 'yes'
    dicte ={'error' : error}
    return render(request,'createaccount.html',dicte)

# def subData():
#     logging.basicConfig(level=logging.WARNING)
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.DEBUG)
#     logger.debug("some debugging...")
