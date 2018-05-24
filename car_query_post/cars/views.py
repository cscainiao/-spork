from django.shortcuts import render

# Create your views here.
from cars.models import Car


def search(request):

    if request.method == 'GET':
        ctx = {
        }

    else:
        cp = request.POST.get('chepai')
        cars = Car.objects.filter(plate_number=cp)
        ctx = {
            # 'cars': Car.objects.all()
            'cars': cars
        }

    return render(request, 'search.html', context=ctx)