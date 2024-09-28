from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Notification

class NotificationList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        notification_data = [
            {
                'id': notification.id,
                'actor': notification.actor.username,
                'verb': notification.verb,
                'timestamp': notification.timestamp,
                'is_read': notification.is_read,
            } for notification in notifications
        ]
        return Response(notification_data)
