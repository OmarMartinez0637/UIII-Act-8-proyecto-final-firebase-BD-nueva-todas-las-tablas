from django.contrib import admin
from .models import (
    ClienteLavanderia, EmpleadoLavanderia, ArticuloRopa,
    PedidoLavanderia, DetallePedidoLavanderia, MaquinaLavanderia, ReporteOperacional
)

class DetalleInline(admin.TabularInline):
    model = DetallePedidoLavanderia
    extra = 0

@admin.register(ClienteLavanderia)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente','nombre','apellido','telefono','email','fecha_registro')

@admin.register(EmpleadoLavanderia)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado','nombre','apellido','cargo','fecha_contratacion')

@admin.register(ArticuloRopa)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id_articulo','tipo_prenda','color','material','tamano','estado_articulo','es_delicado')

@admin.register(PedidoLavanderia)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido','cliente','fecha_recepcion','estado_pedido','total_pedido')
    inlines = [DetalleInline]

@admin.register(DetallePedidoLavanderia)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ('id_detalle','pedido','articulo','tipo_servicio','cantidad','subtotal_item')

@admin.register(MaquinaLavanderia)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('id_maquina','tipo_maquina','marca','modelo','estado_operativo')

@admin.register(ReporteOperacional)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('id_reporte','fecha_reporte','empleado','num_pedidos_procesados')
