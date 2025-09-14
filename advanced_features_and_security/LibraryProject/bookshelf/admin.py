from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import  CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth')
    fieldsets =UserAdmin.fieldsets +  (
            (None, {
                'fields':('date_of_birth', 'prophile_photo')
                }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
            (None, {
                'fields':('date_of_birth', 'prophile_photo')
                }),
            )

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
