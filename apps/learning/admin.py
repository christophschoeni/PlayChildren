from django.contrib import admin
from .models import Learn, Category


# Register your models here.
# @admin.register(Learn)
# class AuthorAdmin(admin.ModelAdmin):
#     pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')



@admin.register(Learn)
class LearnAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


