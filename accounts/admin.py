from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile


class ProfileInline(admin.StackedInline):
    ''' Profile admin'''
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'  # The OneToOneField name
    fields = ('full_name', 'country', 'about', 'image', )  # Customize fields shown


class CustomUserAdmin(UserAdmin):
    ''' custom user admin '''
    inlines = (ProfileInline,)
    # Add fields to user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    # Show profile fields in user list view
    list_display = (
        'username', 'email', 'get_full_name', 'is_staff', 'is_superuser',
        'is_active', 'otp', 'refresh_token', 'last_login', 'date_joined',
    )

    def get_full_name(self, obj):
        return obj.profile.full_name if hasattr(obj, 'profile') else ''
    get_full_name.short_description = 'Full Name'

    # Handle saving of profile when user is saved
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not hasattr(obj, 'profile'):
            Profile.objects.create(user=obj)


admin.site.register(User, CustomUserAdmin)
