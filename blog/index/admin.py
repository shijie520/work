from django.contrib import admin
from index.models import date

# Register your models here.
class administer(admin.ModelAdmin):
	list_display = ('title','content','pub_time')
	list_filter = ('pub_time',)

admin.site.register(date,administer)

