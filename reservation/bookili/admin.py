from django.contrib import admin
from .models import Structure,Staff,Servir,Service,Rdv,Demander,Client,CatergorieStructure
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

from .models import Proprietaire

# class ProprietaireInline(admin.StackedInline):
#     model = Proprietaire
#     can_delete = False
#     verbose_name_plural = 'proprietaire'

# Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProprietaireInline,)

# Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(Proprietaire)
admin.site.register(Structure)
admin.site.register(Staff)
admin.site.register(Servir)
admin.site.register(Service)
admin.site.register(Rdv)
admin.site.register(Demander)
admin.site.register(Client)
admin.site.register(CatergorieStructure)
