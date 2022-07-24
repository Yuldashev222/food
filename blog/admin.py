from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


class CategoryMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'cat', 'date_cr',)
    inlines = [RecipeInline]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service', 'prep_time', 'cook_time', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryMPTTModelAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
