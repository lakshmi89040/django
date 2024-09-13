from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Client

# List all doctors
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'client': clients})

# Create a new patient
def client_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        disease = request.POST['disease']
        age = request.POST['age']
        # Corrected 'patient' to 'Patient'
        Client.objects.create(name=name, disease=disease, age=age)
        return redirect('client_list')
    return render(request, 'client_form.html')

# Update an existing doctor
def client_update(request, id):
    client = Client.objects.get(id=id)
    if request.method == 'POST':
        client.name = request.POST['name']
        client.disease = request.POST['disease']
        client.age = request.POST['age']
        client.save()
        return redirect('client_list')
    return render(request, 'client_form.html', {'client': client})

# Delete a doctor
def client_delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('client_list')