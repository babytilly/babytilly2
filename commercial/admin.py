from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from mptt.admin import MPTTModelAdmin

from commercial.models import Profile, CategoryProperties


class ProfileAdmin(admin.TabularInline):
    model = Profile
    autocomplete_fields = ['department']
    can_delete = False
    min_num = 1
    max_num = 1


class CategoryPropertyAdmin(admin.StackedInline):
    model = CategoryProperties
    min_num = 1


class DepartamentAdmin(admin.ModelAdmin):
    list_display = ['country', 'email']
    search_fields = ['country']


class CategoryAdmin(MPTTModelAdmin):
    inlines = [CategoryPropertyAdmin]
    list_display = ['id']


class UserAdmin(DefaultUserAdmin):
    inlines = [ProfileAdmin]
