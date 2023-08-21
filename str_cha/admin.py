from django.contrib import admin
from str_cha.models import Producto
from django.utils.html import format_html

# Register your models here.

class AdminProductos(admin.ModelAdmin):
    list_display = ('foto', 'get_nombre', 'get_precio')

    def foto(self, object):
        return format_html('<img src={} width="120" height="100" />', object.img.url)

admin.site.register(Producto, AdminProductos)