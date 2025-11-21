from django.contrib import admin

from Users.models import Note, user

@admin.register(user)
class user(admin.ModelAdmin):
    search_fields = ["phone_number"]

@admin.register(Note)
class Note(admin.ModelAdmin):
    search_fields = ["title"]

# Register your models here.6