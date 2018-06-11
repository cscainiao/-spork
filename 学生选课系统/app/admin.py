from django.contrib import admin

# Register your models here.
from app.models import Grade, Student

class GradeAdmin(admin.ModelAdmin):
    list_display = ('g_name', 'g_create_time')
    search_fields = ('g_name', )


class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_name', 's_create_time', 's_operate_time', 'g')
    search_fields = ('s_name', )


admin.site.register(Grade, GradeAdmin)
admin.site.register(Student, StudentAdmin)
