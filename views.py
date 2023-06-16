from django.shortcuts import render
from .models import Class1, Class2, Class3
from .forms import Class1Form, Class2Form, Class3Form

def insert_data(request):
    if request.method == 'POST':
        form1 = Class1Form(request.POST)
        form2 = Class2Form(request.POST)
        form3 = Class3Form(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
    else:
        form1 = Class1Form()
        form2 = Class2Form()
        form3 = Class3Form()
    
    return render(request, 'insert_data.html', {'form1': form1, 'form2': form2, 'form3': form3})

def search_data(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        # Realiza la búsqueda en la base de datos según tus necesidades
        # y devuelve los resultados
    else:
        query = ''
    
    return render(request, 'search_data.html', {'query': query})
