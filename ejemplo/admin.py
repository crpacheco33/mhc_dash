from django.contrib import admin
from .models import Member, CustomerFoo

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname")
  
admin.site.register(Member, MemberAdmin)


class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname")
  
admin.site.register(CustomerFoo, MemberAdmin)