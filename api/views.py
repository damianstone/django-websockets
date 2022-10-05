from django.shortcuts import render
from .models import ChatModel


def homepageview(request):
    return render(request, 'index.html')


def roompageview(request):
    # the entered room number from the input in the index.html
    room_number = request.POST['room_number']
    name = request.POST['name']
    messages = []
    for chat in ChatModel.objects.filter(room_number=room_number):
        messages.append(chat.message)

    return render(
        request, 'room.html',
        {
            'room_number': room_number,
            'name': name,
            'messages': messages
        }
    )
