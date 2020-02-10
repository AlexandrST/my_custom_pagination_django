from django.contrib import admin
from .models import full_data

#admin.site.register(full_data)
@admin.register(full_data)
class full_dataAdmin(admin.ModelAdmin):
	list_display = ('id_file', 'date_file', 'country_id')

# Register your models here.
