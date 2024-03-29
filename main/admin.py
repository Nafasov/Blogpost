from django.contrib import admin


from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_date')
    search_fields = ('name', )
    list_per_page = 7
