from django.shortcuts import render, redirect

from CrudApp.models import Contact

# Create your views here.

def index(request):
    data = Contact.objects.all()
    return render(request, 'index.html', {'users': data})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, message=message)
        
        return redirect('/')
               
    return render(request, 'contact.html')


def deleteUser(request, id):
    user = Contact.objects.get(id=id)
    user.delete()
    return redirect('/')


def updateUser(request, id):
    contact = Contact.objects.get(id=id)
    
    if request.method == 'POST':
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.save()
        
        return redirect('/')

    return render(request, 'contact.html', {'contact': contact})