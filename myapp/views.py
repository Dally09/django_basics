from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    scores = [
        {
            "names": "Jaden Vaughn",
            "english": 57,
            "maths": 37,
            "chemistry": 48,
            "biology": 56
        },
        {
            "names": "Sigourney Brewer",
            "english": 31,
            "maths": 21,
            "chemistry": 82,
            "biology": 83
        },
        {
            "names": "Kirestin Goff",
            "english": 45,
            "maths": 31,
            "chemistry": 58,
            "biology": 75
        },
        {
            "names": "Britanni Ray",
            "english": 43,
            "maths": 66,
            "chemistry": 41,
            "biology": 67
        },
        {
            "names": "Penelope Clarke",
            "english": 40,
            "maths": 38,
            "chemistry": 72,
            "biology": 64
        },
        {
            "names": "Imelda Mejia",
            "english": 65,
            "maths": 36,
            "chemistry": 83,
            "biology": 66
        },
        {
            "names": "Aidan Erickson",
            "english": 70,
            "maths": 70,
            "chemistry": 46,
            "biology": 84
        },
        {
            "names": "Sebastian West",
            "english": 57,
            "maths": 29,
            "chemistry": 77,
            "biology": 57
        },
        {
            "names": "Keelie Craig",
            "english": 55,
            "maths": 62,
            "chemistry": 69,
            "biology": 79
        },
        {
            "names": "Kerry Brown",
            "english": 56,
            "maths": 32,
            "chemistry": 55,
            "biology": 81
        }
    ]
    data = {
      "scores": scores,
    }
    return render(request, 'about.html', data)


def products(request):
    age = 27
    weight = 69.09
    subjects = ["Maths", "Science", "Engineering"]
    isDisabled = False
    name = "Jack Doe"

    # packing into a dictionary
    data = {
        'age': age,
        'weight': weight,
        'subjects': subjects,
        'isDisabled': isDisabled,
        'name': 'Jack Doe'
    }

    return render(request, 'products.html', data)
