from django.contrib import admin
from .models import Parameters


class ParametersAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.parent is not None:
            return ['type']
        return []
    
    # def save_model(self, request, obj, form, change):
    #     if obj.parent is not None:
    #         obj.type = obj.parent.type
    #     return super().save_model(request, obj, form, change)

admin.site.register(Parameters, ParametersAdmin)
