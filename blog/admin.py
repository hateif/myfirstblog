from django.contrib import admin
from .models import Post, ExamInfo, User

# Register your models here.
admin.site.register(Post)

admin.site.register(ExamInfo)
admin.site.register(User)

#class ExamInfoAdmin(admin.ModelAdmin):
    #list_display = ['name', 'level']
#admin.site.register(ExamInfo, ExamInfoAdmin)
