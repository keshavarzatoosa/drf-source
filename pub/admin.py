from django.contrib import admin
from .models import Parameters
from django import forms


class ParametersAdminForm(forms.ModelForm):

    class Meta:
        model = Parameters
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ParametersAdminForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.parent:
            self.fields['type'].initial = self.instance.parent.type
            self.fields['type'].widget.attrs['readonly'] = True

class ParametersAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'parent', 'type')
    form = ParametersAdminForm

    # class Media:
    #     js = ('admin/js/parameters.js')

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.parent is not None:
            return ['type']
        return []
    
    # def save_model(self, request, obj, form, change):
    #     if obj.parent is not None:
    #         obj.type = obj.parent.type
    #     return super().save_model(request, obj, form, change)

admin.site.register(Parameters, ParametersAdmin)
