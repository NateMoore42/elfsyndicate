from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Auth.models import User, Profile
from Auth.forms import ProfileForm, RegisterForm, UserForm, ProfileCreate

class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important Dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password')
        }),
    )
    form = UserForm
    add_form = RegisterForm
    list_display = ('email', 'username', 'last_login', 'date_joined', 'is_staff')
    search_fields = ('email', 'username', 'last_login', 'date_joined')
    order = ('email',)

admin.site.register(User, UserAdmin)

class CharactersInline(admin.TabularInline):
    model = Profile.characters.through

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('user', 'first_name', 'last_name', 'gender', 'description', 'dob', 'profile_picture')}),
    )
    inlines = [
        CharactersInline,
    ]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'gender', 'description', 'dob', 'profile_picture')
        }),
    )
    form = ProfileForm
    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'

    list_display = ['user', 'first_name', 'last_name', 'gender', 'dob',]

admin.site.register(Profile, ProfileAdmin)
