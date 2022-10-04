from django.shortcuts import render


def homepageview(request):
    return render(request, 'index.html')


def roompageview(request):
    # the entered room number from the input in the index.html
    room_number = request.POST['room_number']
    name = request.POST['name']
    return render(request, 'room.html', {'room_number': room_number, 'name': name})
