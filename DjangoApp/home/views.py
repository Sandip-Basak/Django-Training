from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from home.forms import *
from home.models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect("/profile")
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                u=form.save()
                messages.success(request, "Account Created")
                return redirect("/signin")
            except Exception as e:
                print(e)
                messages.warning(request, "Some Error Occured")
    else:
        form = SignUpForm()
    data = {"form": form}
    return render(request, "form.html", data)

def signin(request):
    if request.user.is_authenticated:
        return redirect("/profile")
    
    if request.method == "POST":
        form = SignInForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/profile')
        else:
            messages.warning(request, "Invalid Login Credentials")
    else:
        form = SignInForm()
    data = {'form': form}
    return render(request, 'form.html', data)


@login_required(login_url='/signin')
def signout(request):
    logout(request)
    return redirect("/")


@login_required(login_url='/signin')
def profile(request):
    employee=Employee.objects.all()
    data={
        'employee': employee
    }
    return render(request,"profile.html",data)


@login_required(login_url='/signin')
def deleteEmployee(request,id):
    data=Employee.objects.get(eid=id)
    data.delete()
    return redirect("/profile")


@login_required(login_url='/signin')
def addEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EmployeeForm()

    return render(request, 'form.html', {'form': form})


@login_required(login_url='/signin')
def employeeUpdate(request, id):
    emp=get_object_or_404(Employee, eid=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=emp)
        if form.is_valid():
            form.save()
        return redirect("/profile")
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'form.html', {'form': form})