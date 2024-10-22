from django.contrib import admin

# Register your models here.
from.models import Aadhar,User,Department
admin.site.register(Aadhar)
admin.site.register(User)
admin.site.register(Department)