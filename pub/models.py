from django.db import models
from django.utils.translation import pgettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Parameters(models.Model):

    code = models.CharField(max_length=250, verbose_name=_("Parameters field", "Code"))
    name = models.CharField(max_length=250, verbose_name=_("Parameters field", "Name"))
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name=_("Parameters field", "Parent"))
    type = models.IntegerField(verbose_name=_("Parameters field", "Type"))
    sub_type = models.IntegerField(default=0, verbose_name=_("Parameters field", "Sub Type"))
    order_no = models.IntegerField(default=1, verbose_name=_("Parameters field", "Order Number"))
    info1 = models.IntegerField(default=0, verbose_name=_("Parameters field", "Info1"))
    info2 = models.IntegerField(default=0, verbose_name=_("Parameters field", "Info2"))
    info3 = models.IntegerField(default=0, verbose_name=_("Parameters field", "Info3"))
    info4 = models.IntegerField(default=0, verbose_name=_("Parameters field", "Info4"))
    description = models.CharField(max_length=250, verbose_name=_("Parameters field", "Description"))
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Parameters model", "Parameter")
        verbose_name_plural = _("Parameters model", "Parameters")

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Parameters)
def set_type_from_parent(sender, instance, **kwargs):
    if instance.parent is not None:
        instance.type = instance.parent.type

def params_get(type):
    items = Parameters.objects.filter(type=type, parent__isnull = False)
    return [(r.code, r.name) for r in items]