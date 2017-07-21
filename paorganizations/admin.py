from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import Organization, Assignment, Person, TelephoneNumber


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'email_domain', 'parent')
    list_per_page = 20
    list_max_show_all = 40
    search_fields = ('title', 'email_domain')


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'organization', 'person', 'email',
                    'out_telephone_numbers')
    list_per_page = 20
    list_max_show_all = 40
    search_fields = ('organization__title', 'organization__email_domain',
                     'person__first_name', 'person__last_name',
                     'person__user__username')

    def out_telephone_numbers(self, obj):
        numbers = obj.telephone_numbers.all()
        if len(numbers):
            return ', '.join(
                ["{} [{}]".format(tn.number, tn.type)for tn in numbers])
        return ''
    out_telephone_numbers.short_description = _('Telephone numbers')


class AssignmentInline(admin.StackedInline):
    model = Assignment
    extra = 2


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline]
    list_display = ('pk', 'first_name', 'last_name', 'register_number')
    list_per_page = 20
    list_max_show_all = 40
    search_fields = ('first_name', 'last_name', 'user__username')


@admin.register(TelephoneNumber)
class TelephoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'type')
    list_per_page = 20
    list_max_show_all = 40
    search_fields = ('number', 'type')


