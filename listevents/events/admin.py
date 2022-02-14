from multiprocessing import Event
from django.contrib import admin

from events.models import CustomUser,Event, UserEvent

admin.site.register(CustomUser)

class EventAdmin(admin.ModelAdmin):
           list_display = ['id','title','description','start_date','end_date','categories','paid','published']
admin.site.register(Event,EventAdmin)

admin.site.register(UserEvent)

