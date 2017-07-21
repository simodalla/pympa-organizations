from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Organization, Assignment, Person


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'email_domain', 'parent')
    search_fields = ('title', 'email_domain')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'organization', 'person', 'email')
    search_fields = ('organization__title', 'organization__email_domain',
                     'person__first_name', 'person__last_name',
                     'user__username')


class AssignmentInline(admin.StackedInline):
    model = Assignment
    extra = 2


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline]
    list_display = ('pk', 'first_name', 'last_name', 'register_number')
    search_fields = ('first_name', 'last_name', 'user__username')
