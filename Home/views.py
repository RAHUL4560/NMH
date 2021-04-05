from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.
def Home(request):
    return render(request,'home.html')
def Interior(request):
    return render(request,'interior.html')
def Collection(request):
    return render(request,'COLLECTIONS.html')
def Cleaning(request):
    return render(request,'cleaning.html')
def kitchen(request):
    return render(request,'kitchen-quote.html')
def wardrobes(request):
    return render(request,'wardrobes-quote.html')
def rooms(request):
    return render(request,'rooms-quote.html')
def Home_Merchandising(request):
    return render(request,'home-merchandising.html')
def cleaning_kitchen(request):
    return render(request,'cleaning-kitchen.html')
def cleaning_bathroom(request):
    return render(request,'cleaning-bathroom.html')
def basic_package(request):
    return render(request,'basic-package.html')
def testing(request):
    return render(request,'renting&management.html')
def Contact(request):
    return render(request,'contact-us.html')
def Repair(request):
    return render(request,'repairs&management.html')
def homecleaning(request):
    return render(request,'home-cleaning.html')

def howitworks(request):
    return render(request,'howitworks.html')
def proj_delivered(request):
    return render(request,'proj-delivered.html')
def faqs(request):
    return render(request,'faqs.html')
def refrigerator(request):
    return render(request,'refrigerator.html')
def chimney(request):
    return render(request,'chimney.html')
def mwave(request):
    return render(request,'mwave.html')
def onebhk(request):
    return render(request,'onebhk.html')
def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #cheks for error
        if len(username) > 10:
            messages.success(request,"Username must not be more than 10 words ")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')


        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your accound has been successfully created")
        return redirect('/')

    else:
        return HttpResponse('404 - Not Found')
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username = loginusername,password = loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully Loggedin")
            return redirect('/')

        else:
            messages.success(request,'invalid user')
            return redirect('/')

def handleLogout(request):
        logout(request)
        messages.success(request,"successfully Loggedout")
        return redirect('/')
