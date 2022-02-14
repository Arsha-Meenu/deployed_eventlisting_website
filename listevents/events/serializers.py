
from rest_framework import serializers
from .models import Event, UserEvent

class UserEventSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source ='event.title')
    description = serializers.CharField(source ='event.description')
    location = serializers.CharField(source ='event.location')
    start_date = serializers.CharField(source ='event.start_date')
    end_date = serializers.CharField(source ='event.end_date')
    categories = serializers.CharField(source ='event.categories')
    paid = serializers.CharField(source ='event.paid')
    
    class Meta:
         model = UserEvent
         fields = ['id',
                   'event_id',
                   'title',
                   'description',
                   'location',
                   'start_date',
                   'end_date',
                   'categories',
                   'paid'
                 ]



