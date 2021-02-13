from django.contrib import admin
from .models import  Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id', 'stuid', 'stuname', 'stuemail',)

#admin.site.register(Student, StudentAdmin)






