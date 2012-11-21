from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from client.models import UserProfile

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'tariff and domains'
    fieldsets = (
        (None, {
            'fields': ('tariff', 'domains')
        }),
    )
    readonly_fields = ('domains', 'tariff')

# Define a new User admin
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permisions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )
    inlines = (UserProfileInline, )
    list_display = ('username', 'email', 'is_active', 'tariff')
    list_filter = ('is_active', 'is_staff')

    def tariff(self, instance):
        return instance.get_profile().tariff
    tariff.short_description = 'Tariff'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)