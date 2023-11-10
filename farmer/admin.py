from django.contrib import admin
from farmer.models import UserInformation
from .models import ResponseLog
from django import forms
from .models import Farmer_details

from .models import CustomUser
@admin.register(CustomUser)
class YourModelAdmin(admin.ModelAdmin):
    search_fields = ('uname', 'uplace')  # Replace 'field1' and 'field2' with the fields you want to search on

# Register your model with the custom admin class
admin.site.register(UserInformation, YourModelAdmin)

class ModelAdmin(admin.ModelAdmin):
    search_fields = ('your_name','mobile_number')  # Replace 'field1' and 'field2' with the fields you want to search on

# Register your model with the custom admin class
admin.site.register(Farmer_details, ModelAdmin)

@admin.register(ResponseLog)
class ResponseLogAdmin(admin.ModelAdmin):
    list_display = ('content', 'timestamp')




