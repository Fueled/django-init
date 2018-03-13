# Third Party Stuff
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm

from .models import User


# Forms
# ----------------------------------------------------------------------------
class MyUserCreationForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class MyUserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


# ModelAdmins
# ----------------------------------------------------------------------------
@admin.register(User)
class UserAdmin(AuthUserAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined', 'last_login')
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_superuser', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
