from django.db.models.signals import post_save
from django.dispatch import receiver
from chat.models import Room
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


@receiver(post_save, sender=Room)
def my_handler(sender, instance, created, **kwargs):

    async_to_sync(channel_layer.group_send)(
                # "chat_%s" % instance.id
                "chat_lobby",
                {
                    'type': 'chat.message',
                    'message': "6666666yyyyy66666666"
                }
            )
