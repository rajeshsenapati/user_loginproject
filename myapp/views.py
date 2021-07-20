from django.shortcuts import render, redirect
from myapp.forms import UserForm
from myapp.models import UserModel
from django.contrib import messages

# Create your views here.


def showLoginpage(request):
    if request.method == "POST":
        try:
            detail = UserModel.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['email'] = detail.email
            return render(request, 'detail.html', {"data": detail})
        except UserModel.DoesNotExist as e:
            messages.success(request, 'Email or Password Invalid.....')
    return render(request, 'login.html')


def showSignuppage(request):
    if request.method == "POST":
        formvalidation = UserForm(request.POST)
        if formvalidation.is_valid():
            name = request.POST.get('Name')
            email = request.POST.get('Email')
            password = request.POST.get('Password')
            address = request.POST.get('Address')
            UserModel(username=name, email=email, password=password, address=address).save()
            return render(request, 'login.html', {"message": "Sucessfully Signuped."})
        else:
            return render(request, 'sginup.html', {"message": "Password doest not match..", "form": UserForm()})

    else:
        return render(request, 'sginup.html', {"form": UserForm()})



def showDetail(request):
    return render(request, 'detail.html')


def showDelete(request, email):
    data = UserModel.objects.get(email=email)
    if request.method == "POST":
        data.delete()
        return render(request, 'login.html', {"delete": "Data Deleted Successfully"})
    else:
        return redirect('detail')


def showUpdate(request, email):
    update_data = UserModel.objects.get(email=email)
    if request.method == "POST":
        update_data.username = request.POST.get('name')
        update_data.email = request.POST.get('email')
        update_data.address = request.POST.get('address')
        updated_data = update_data.save()
        return render(request, 'login.html', {"update_sucess": "Update Sucessfully"})
    else:
        return render(request, 'update.html', {"data": update_data})
