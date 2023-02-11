from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate , login as login , logout
from .forms import CertificateForm
from .models import CERTIFICATE,Doctor
from . import models

hospital = ''

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
                all_task = models.CERTIFICATE.objects.filter(doctorName=username)
                hospital=username
                context = {'name': all_task,'doctor':username}


                return render(request,'acceptApplication.html',context=context)

                #     return redirect('doctor')
                # else:
                #     print('failed')
                #
                # if request.POST=='POST':
                #     print("Hello2")
                #     username = request.POST.get('username')
                #     ticketid=request.POST.get('ticketid')
                #     if models.CERTIFICATE.objects.filter(username=username,ticketid=ticketid).exists():
                #         print("Hello")
                #         models.CERTIFICATE.objects.filter(username=username, ticketid=ticketid).update(isverified=True)
                #
            # return render(request, 'acceptApplication.html',context=context)
            
        else:
            form1 = AuthenticationForm()
            context = {
                "form" : form1
            }
            return render(request, 'doctor.html', context=context)
        

def patient(request):
     username=""
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
                if request.method=='POST':
                    all_task = models.CERTIFICATE.objects.filter(username=user)
                    context = {'name': all_task}
                return render(request,'applyCertificate.html',context=context)
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

def acceptApplication(request):
     dname=''
     if request.POST=='POST':
        print("Hello2")
        doctorname=request.POST.get('doctorname')
        dname=doctorname
        username = request.POST.get('username')
        ticketid=request.POST.get('ticketid')
        if models.CERTIFICATE.objects.filter(username=username,ticketid=ticketid).exists():
            print("Hello")
            models.CERTIFICATE.objects.filter(username=username, ticketid=ticketid).update(isverified=True)

        all_task = models.CERTIFICATE.objects.filter(doctorName=doctorname)
        context = {'name': all_task, 'doctor':doctorname}
        return render(request, 'acceptApplication.html', context=context)

     else:
        print(dname)
        all_task = models.CERTIFICATE.objects.filter(doctorName=dname)
        context = {'name': all_task, 'doctor':dname}
        return render(request, 'acceptApplication.html', context=context)





def signout(request):
    logout(request)
    return redirect('patient')
















