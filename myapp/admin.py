from pyexpat import model
from django.contrib import admin

from myapp.models import CustomUser
# from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser
# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     add_form=CustomUserCreationForm
#     form= CustomUserChangeForm
#     model= CustomUser
#     add_form=CustomUserCreationForm
#     list_display = ('email','is_staff','is_active')
#     list_filter= ('email','is_staff','is_active')

   
# fieldsets=(None, ({'fields',('email','password')})
# ('permissions'), {'fields',('is_staff','is_active')}
# )

# add_fieldsets=(
#     ( None,{ 'classes':('wide',),'fields':('email','password','is_staff','is_active'}),)


# search_fields=('email',)
# ordering=('email',)

# admin.site.register(CustomUser, CustomUserAdmin)


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'body',)
#     prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Post, PostAdmin)