from django.shortcuts import render

# Create your views here.
# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from chat.models import Room

def index(request):
    # from channels.layers import get_channel_layer
    # from asgiref.sync import async_to_sync
    # channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.group_send)(
    #     "chat_lobby",
    #     {
    #         'type': 'chat.message',
    #         'message': "6666666yyyyy66666666"
    #     }
    # )

    # r = Room.objects.filter(id=46).update(name="33333333") #　如果信号中使用post＿save 此更新不会出发信号机制　　
    r = Room()
    r.name = "xiao"
    r.label = "qq "
    r.save()
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })