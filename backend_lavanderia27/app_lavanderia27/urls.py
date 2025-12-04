from django.urls import path
from . import views

app_name = 'app_lavanderia'

urlpatterns = [
    # INICIO
    path('', views.inicio_mcdonalds, name='inicio'),

    # ARTÍCULOS
    path('articulos/', views.ver_articulos, name='ver_articulos'),
    path('articulos/agregar/', views.agregar_articulo, name='agregar_articulo'),
    path('articulos/editar/<int:id>/', views.actualizar_articulo, name='actualizar_articulo'),
    path('articulos/borrar/<int:id>/', views.borrar_articulo, name='borrar_articulo'),

    # CLIENTES
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # PEDIDOS
    path('pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedidos/editar/<int:id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/borrar/<int:id>/', views.borrar_pedido, name='borrar_pedido'),

    # DETALLES
    path('detalles/', views.ver_detalles, name='ver_detalles'),
    path('detalles/agregar/', views.agregar_detalle, name='agregar_detalle'),
    path('detalles/editar/<int:id>/', views.actualizar_detalle, name='actualizar_detalle'),
    path('detalles/borrar/<int:id>/', views.borrar_detalle, name='borrar_detalle'),

    # EMPLEADOS
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/editar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

    # MÁQUINAS
    path('maquinas/', views.ver_maquinas, name='ver_maquinas'),
    path('maquinas/agregar/', views.agregar_maquina, name='agregar_maquina'),
    path('maquinas/editar/<int:id>/', views.actualizar_maquina, name='actualizar_maquina'),
    path('maquinas/borrar/<int:id>/', views.borrar_maquina, name='borrar_maquina'),

    # REPORTES
    path('reportes/', views.ver_reportes, name='ver_reportes'),
    path('reportes/agregar/', views.agregar_reporte, name='agregar_reporte'),
    path('reportes/editar/<int:id>/', views.actualizar_reporte, name='actualizar_reporte'),
    path('reportes/borrar/<int:id>/', views.borrar_reporte, name='borrar_reporte'),
]
