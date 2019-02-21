from django.contrib import admin
from .models import Profile,User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('id','email', 'username','admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email','username', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('active','staff','admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('admin',)
    filter_horizontal = ()

admin.site.register(Profile)
admin.site.register(User,UserAdmin)
