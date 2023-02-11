from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate , login as login , logout
from home.forms import CertificateForm
from home.models import CERTIFICATE,Doctor



# Create your views here.
def home(request):
    return render(request, 'index.html')

def doctor(request):

    if(request.method=='GET'):
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request, 'doctor.html', context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)


            doctor = authenticate(username = username, password = password)
            if doctor is not None:
                login(request,doctor)
                return render(request, 'acceptApplication.html')
            
            else:
                form1 = AuthenticationForm()
                context = {
                    "form" : form1
                }
                return render(request, 'doctor.html', context=context)
        




def patient(request):
     if(request.method=='GET'):
        form2 = AuthenticationForm()
        context = {
            "form" : form2
        }
        return render(request, 'patient.html', context=context)
     else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                # return render(request, 'index.html')
                return redirect('applyCertificate')
            else:
                form1 = AuthenticationForm()
                context = {
                    "form" : form1
                }
                return render(request, 'patient.html', context=context)


def signup(request):

    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        # print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            # print(user)
            if user is not None:
                return redirect('patient')
            else:
                return HttpResponse('Somethig went wrong!!')
        else:
            return render(request , 'signup.html' , context=context)



def applyCertificate(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form3 = CertificateForm(request.POST)
        if form3.is_valid():
            print(form3.cleaned_data)
            certificate = form3.save(commit=False)
            certificate.user = user
            certificate.save()
            print(certificate)
            return redirect("applyCertificate")
        else: 
            return render(request , 'applyCertificate.html' , context={'form' : form3})




def signout(request):
    logout(request)
    return redirect('patient')
















