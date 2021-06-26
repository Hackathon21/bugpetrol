from django.shortcuts import render
# from models import*

# Create your views here.

def homepage(request):
    return render(request,'index.html')

# -------------------------------------------------------------------------------------------------------------------------------------
# about
 
def about(request):
    return render(request,'about.html')

#--------------------------------------------------------------------------------------------------------------------------------------
# sign up
#log in

def login(request):
    # if re
    return render(request,'login.html')
#--------------------------------------------------------------------------------------------------------------------------------------
#
# def about(request):
#     return render(request,'about.html')