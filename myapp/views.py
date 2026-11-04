from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    age = 27
    weight = 69.09
    subjects = ["Maths", "Science", "Engineering"]
    isDisabled = False
    name = "Jack Doe"

    #packing into a dictionary
    data = {
        'age': age,
        'weight': weight,
        'subjects': subjects,
        'isDisabled': isDisabled,
        'name': 'Jack Doe'
    }

    return render(request, 'products.html', data)