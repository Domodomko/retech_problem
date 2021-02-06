# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# local Django
from .models import *


@admin.register(Vending)
class VendingAdmin(admin.ModelAdmin):
    model = Vending
    list_display = ('id', 'address', 'count')
    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    search_fields = ()
    fieldsets = (
        (None, {
            "fields": (
                'address',
                'max_size',
                'count',
                'total_sum',
                'id_key'
            ),
        }),
    )