from django.contrib import admin


from . models import Student
from . models import Contact
admin.site.register(Student)
admin.site.register(Contact)