from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    ArticuloRopa, ClienteLavanderia, PedidoLavanderia,
    DetallePedidoLavanderia, EmpleadoLavanderia,
    MaquinaLavanderia, ReporteOperacional
)
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

# ===================== INICIO =====================
def inicio_mcdonalds(request):
    context = {
        'total_clientes': ClienteLavanderia.objects.count(),
        'total_pedidos': PedidoLavanderia.objects.count(),
    }
    return render(request, 'inicio.html', context)

# ===================== ARTÍCULOS =====================
def ver_articulos(request):
    articulos = ArticuloRopa.objects.select_related('cliente').all()
    return render(request, 'app_lavanderia27/articulos/ver_.html', {'articulos': articulos})

@csrf_protect
def agregar_articulo(request):
    clientes = ClienteLavanderia.objects.all()
    if request.method == 'POST':
        ArticuloRopa.objects.create(
            tipo_prenda=request.POST.get('tipo_prenda',''),
            color=request.POST.get('color',''),
            material=request.POST.get('material',''),
            tamano=request.POST.get('tamano',''),
            instrucciones_especiales=request.POST.get('instrucciones_especiales',''),
            costo_lavado_estandar=request.POST.get('costo_lavado_estandar') or 0,
            estado_articulo=request.POST.get('estado_articulo','En espera'),
            es_delicado=bool(request.POST.get('es_delicado')),
            cliente_id=request.POST.get('cliente') or None
        )
        return redirect('app_lavanderia:ver_articulos')
    return render(request, 'app_lavanderia27/articulos/agregar_.html', {'clientes': clientes})

@csrf_protect
def actualizar_articulo(request, id):
    art = get_object_or_404(ArticuloRopa, pk=id)
    clientes = ClienteLavanderia.objects.all()
    if request.method == 'POST':
        art.tipo_prenda = request.POST.get('tipo_prenda','')
        art.color = request.POST.get('color','')
        art.material = request.POST.get('material','')
        art.tamano = request.POST.get('tamano','')
        art.instrucciones_especiales = request.POST.get('instrucciones_especiales','')
        art.costo_lavado_estandar = request.POST.get('costo_lavado_estandar') or 0
        art.estado_articulo = request.POST.get('estado_articulo','En espera')
        art.es_delicado = bool(request.POST.get('es_delicado'))
        art.cliente_id = request.POST.get('cliente') or None
        art.save()
        return redirect('app_lavanderia:ver_articulos')
    return render(request, 'app_lavanderia27/articulos/actualizar_.html', {'art': art, 'clientes': clientes})

@csrf_protect
def borrar_articulo(request, id):
    art = get_object_or_404(ArticuloRopa, pk=id)
    if request.method == 'POST':
        art.delete()
        return redirect('app_lavanderia:ver_articulos')
    return render(request, 'app_lavanderia27/articulos/borrar_.html', {'art': art})

# ===================== CLIENTES =====================
def ver_clientes(request):
    clientes = ClienteLavanderia.objects.all()
    return render(request, 'app_lavanderia27/clientes/ver_.html', {'clientes': clientes})

@csrf_protect
def agregar_cliente(request):
    if request.method == 'POST':
        ClienteLavanderia.objects.create(
            nombre=request.POST.get('nombre',''),
            apellido=request.POST.get('apellido',''),
            telefono=request.POST.get('telefono',''),
            email=request.POST.get('email',''),
            direccion_recogida=request.POST.get('direccion_recogida',''),
            direccion_entrega=request.POST.get('direccion_entrega',''),
            notas_cliente=request.POST.get('notas_cliente',''),
            preferencias_lavado=request.POST.get('preferencias_lavado',''),
        )
        return redirect('app_lavanderia:ver_clientes')
    return render(request, 'app_lavanderia27/clientes/agregar_.html')

@csrf_protect
def actualizar_cliente(request, id):
    cliente = get_object_or_404(ClienteLavanderia, pk=id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre','')
        cliente.apellido = request.POST.get('apellido','')
        cliente.telefono = request.POST.get('telefono','')
        cliente.email = request.POST.get('email','')
        cliente.direccion_recogida = request.POST.get('direccion_recogida','')
        cliente.direccion_entrega = request.POST.get('direccion_entrega','')
        cliente.notas_cliente = request.POST.get('notas_cliente','')
        cliente.preferencias_lavado = request.POST.get('preferencias_lavado','')
        cliente.save()
        return redirect('app_lavanderia:ver_clientes')
    return render(request, 'app_lavanderia27/clientes/actualizar_.html', {'cliente': cliente})

@csrf_protect
def borrar_cliente(request, id):
    cliente = get_object_or_404(ClienteLavanderia, pk=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('app_lavanderia:ver_clientes')
    return render(request, 'app_lavanderia27/clientes/borrar_.html', {'cliente': cliente})

# ===================== PEDIDOS =====================
def ver_pedidos(request):
    pedidos = PedidoLavanderia.objects.select_related('cliente','empleado_recepcion').all()
    return render(request, 'app_lavanderia27/pedidos/ver_.html', {'pedidos': pedidos})

@csrf_protect
def agregar_pedido(request):
    clientes = ClienteLavanderia.objects.all()
    empleados = EmpleadoLavanderia.objects.all()
    if request.method == 'POST':
        cliente_id = request.POST.get('id_cliente')
        if not cliente_id:
            return render(request, 'app_lavanderia27/pedidos/agregar_.html', {
                'clientes': clientes,
                'empleados': empleados,
                'error': 'Debe seleccionar un cliente'
            })
        PedidoLavanderia.objects.create(
            cliente_id=cliente_id,
            fecha_entrega_estimada=request.POST.get('fecha_entrega_estimada') or None,
            estado_pedido=request.POST.get('estado_pedido','Recibido'),
            total_pedido=request.POST.get('total_pedido') or 0,
            metodo_pago=request.POST.get('metodo_pago',''),
            empleado_recepcion_id=request.POST.get('id_empleado_recepcion') or None,
            comentarios_cliente=request.POST.get('comentarios_cliente','')
        )
        return redirect('app_lavanderia:ver_pedidos')
    return render(request, 'app_lavanderia27/pedidos/agregar_.html', {'clientes': clientes, 'empleados': empleados})

@csrf_protect
def actualizar_pedido(request, id):
    pedido = get_object_or_404(PedidoLavanderia, pk=id)

    if request.method == 'POST':
        # Obtener el cliente seleccionado
        cliente_id = request.POST.get('cliente')
        if not cliente_id:
            # si no hay cliente seleccionado, puedes mostrar error o redirigir
            return render(request, 'app_lavanderia27/pedidos/actualizar_.html', {
                'pedido': pedido,
                'clientes': ClienteLavanderia.objects.all(),
                'empleados': EmpleadoLavanderia.objects.all(),
                'error': 'Debe seleccionar un cliente.'
            })
        pedido.cliente = get_object_or_404(ClienteLavanderia, pk=cliente_id)

        # Obtener empleado si se seleccionó
        empleado_id = request.POST.get('empleado_recepcion')
        if empleado_id:
            pedido.empleado_recepcion = get_object_or_404(EmpleadoLavanderia, pk=empleado_id)
        else:
            pedido.empleado_recepcion = None

        # Resto de campos
        pedido.fecha_entrega_estimada = request.POST.get('fecha_entrega_estimada') or None
        pedido.estado_pedido = request.POST.get('estado_pedido','Recibido')
        pedido.total_pedido = request.POST.get('total_pedido') or 0
        pedido.metodo_pago = request.POST.get('metodo_pago','')
        pedido.comentarios_cliente = request.POST.get('comentarios_cliente','')

        pedido.save()
        return redirect('app_lavanderia:ver_pedidos')

    clientes = ClienteLavanderia.objects.all()
    empleados = EmpleadoLavanderia.objects.all()
    return render(request, 'app_lavanderia27/pedidos/actualizar_.html', {'pedido': pedido, 'clientes': clientes, 'empleados': empleados})

@csrf_protect
def borrar_pedido(request, id):
    pedido = get_object_or_404(PedidoLavanderia, pk=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('app_lavanderia:ver_pedidos')
    return render(request, 'app_lavanderia27/pedidos/borrar_.html', {'pedido': pedido})

# ===================== DETALLES =====================
def ver_detalles(request):
    detalles = DetallePedidoLavanderia.objects.select_related('pedido','articulo').all()
    return render(request, 'app_lavanderia27/detalles/ver_.html', {'detalles': detalles})

@csrf_protect
def agregar_detalle(request):
    pedidos = PedidoLavanderia.objects.all()
    articulos = ArticuloRopa.objects.all()
    if request.method == 'POST':
        DetallePedidoLavanderia.objects.create(
            pedido_id=request.POST.get('pedido'),
            articulo_id=request.POST.get('articulo') or None,
            cantidad=request.POST.get('cantidad') or 1,
            tipo_servicio=request.POST.get('tipo_servicio','Lavado'),
            costo_servicio_individual=request.POST.get('costo_servicio_individual') or 0,
            subtotal_item=request.POST.get('subtotal_item') or 0,
            manchas_detectadas=request.POST.get('manchas_detectadas',''),
            instrucciones_item=request.POST.get('instrucciones_item','')
        )
        return redirect('app_lavanderia:ver_detalles')
    return render(request, 'app_lavanderia27/detalles/agregar_.html', {'pedidos': pedidos, 'articulos': articulos})

@csrf_protect
def actualizar_detalle(request, id):
    detalle = get_object_or_404(DetallePedidoLavanderia, pk=id)
    pedidos = PedidoLavanderia.objects.all()
    articulos = ArticuloRopa.objects.all()
    if request.method == 'POST':
        detalle.pedido_id = request.POST.get('pedido')
        detalle.articulo_id = request.POST.get('articulo') or None
        detalle.cantidad = request.POST.get('cantidad') or 1
        detalle.tipo_servicio = request.POST.get('tipo_servicio','')
        detalle.costo_servicio_individual = request.POST.get('costo_servicio_individual') or detalle.costo_servicio_individual
        detalle.subtotal_item = request.POST.get('subtotal_item') or detalle.subtotal_item
        detalle.manchas_detectadas = request.POST.get('manchas_detectadas','')
        detalle.instrucciones_item = request.POST.get('instrucciones_item','')
        detalle.save()
        return redirect('app_lavanderia:ver_detalles')
    return render(request, 'app_lavanderia27/detalles/actualizar_.html', {'detalle': detalle, 'pedidos': pedidos, 'articulos': articulos})

@csrf_protect
def borrar_detalle(request, id):
    detalle = get_object_or_404(DetallePedidoLavanderia, pk=id)
    if request.method == 'POST':
        detalle.delete()
        return redirect('app_lavanderia:ver_detalles')
    return render(request, 'app_lavanderia27/detalles/borrar_.html', {'detalle': detalle})

# ===================== EMPLEADOS =====================
def ver_empleados(request):
    empleados = EmpleadoLavanderia.objects.all()
    return render(request, 'app_lavanderia27/empleados/ver_.html', {'empleados': empleados})

@csrf_protect
def agregar_empleado(request):
    if request.method == 'POST':
        EmpleadoLavanderia.objects.create(
            nombre=request.POST.get('nombre',''),
            apellido=request.POST.get('apellido',''),
            cargo=request.POST.get('cargo',''),
            fecha_contratacion=request.POST.get('fecha_contratacion') or timezone.now().date(),
            salario=request.POST.get('salario') or 0,
            turno=request.POST.get('turno',''),
            telefono=request.POST.get('telefono',''),
            email=request.POST.get('email',''),
            dni=request.POST.get('dni','')
        )
        # Redirect para evitar duplicado al refrescar
        return redirect('app_lavanderia:ver_empleados')

    return render(request, 'app_lavanderia27/empleados/agregar_.html')

@csrf_protect
def actualizar_empleado(request, id):
    emp = get_object_or_404(EmpleadoLavanderia, pk=id)
    if request.method == 'POST':
        emp.nombre = request.POST.get('nombre','')
        emp.apellido = request.POST.get('apellido','')
        emp.cargo = request.POST.get('cargo','')
        emp.fecha_contratacion = request.POST.get('fecha_contratacion') or emp.fecha_contratacion
        emp.salario = request.POST.get('salario') or emp.salario
        emp.turno = request.POST.get('turno','')
        emp.telefono = request.POST.get('telefono','')
        emp.email = request.POST.get('email','')
        emp.dni = request.POST.get('dni','')
        emp.save()
        return redirect('app_lavanderia:ver_empleados')

    return render(request, 'app_lavanderia27/empleados/actualizar_.html', {'emp': emp})

@csrf_protect
def borrar_empleado(request, id):
    emp = get_object_or_404(EmpleadoLavanderia, pk=id)
    if request.method == 'POST':
        emp.delete()
        return redirect('app_lavanderia:ver_empleados')
    return render(request, 'app_lavanderia27/empleados/borrar_.html', {'emp': emp})

# ===================== MÁQUINAS =====================
def ver_maquinas(request):
    maquinas = MaquinaLavanderia.objects.all()
    return render(request, 'app_lavanderia27/maquinas/ver_.html', {'maquinas': maquinas})

@csrf_protect
def agregar_maquina(request):
    if request.method == 'POST':
        MaquinaLavanderia.objects.create(
            tipo_maquina=request.POST.get('tipo_maquina',''),
            marca=request.POST.get('marca',''),
            modelo=request.POST.get('modelo',''),
            capacidad_kg=request.POST.get('capacidad_kg') or None,
            estado_operativo=request.POST.get('estado_operativo',''),
            ultima_revision=request.POST.get('ultima_revision') or None,
            num_serie=request.POST.get('num_serie',''),
            es_lavadora=bool(request.POST.get('es_lavadora')),
            es_secadora=bool(request.POST.get('es_secadora')),
        )
        return redirect('app_lavanderia:ver_maquinas')
    return render(request, 'app_lavanderia27/maquinas/agregar_.html')

@csrf_protect
def actualizar_maquina(request, id):
    maq = get_object_or_404(MaquinaLavanderia, pk=id)
    if request.method == 'POST':
        maq.tipo_maquina = request.POST.get('tipo_maquina','')
        maq.marca = request.POST.get('marca','')
        maq.modelo = request.POST.get('modelo','')
        maq.capacidad_kg = request.POST.get('capacidad_kg') or maq.capacidad_kg
        maq.estado_operativo = request.POST.get('estado_operativo','')
        maq.ultima_revision = request.POST.get('ultima_revision') or maq.ultima_revision
        maq.num_serie = request.POST.get('num_serie','')
        maq.es_lavadora = bool(request.POST.get('es_lavadora'))
        maq.es_secadora = bool(request.POST.get('es_secadora'))
        maq.save()
        return redirect('app_lavanderia:ver_maquinas')
    return render(request, 'app_lavanderia27/maquinas/actualizar_.html', {'maq': maq})

@csrf_protect
def borrar_maquina(request, id):
    maq = get_object_or_404(MaquinaLavanderia, pk=id)
    if request.method == 'POST':
        maq.delete()
        return redirect('app_lavanderia:ver_maquinas')
    return render(request, 'app_lavanderia27/maquinas/borrar_.html', {'maq': maq})

# ===================== REPORTES =====================
# ===================== REPORTES =====================
def ver_reportes(request):
    # Seleccionamos todos los reportes con el empleado relacionado
    reportes = ReporteOperacional.objects.select_related('empleado').all()
    return render(request, 'app_lavanderia27/reportes/ver_.html', {'reportes': reportes})

@csrf_protect
def agregar_reporte(request):
    empleados = EmpleadoLavanderia.objects.all()
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado') or None
        ReporteOperacional.objects.create(
            empleado_id=empleado_id,
            num_pedidos_procesados=request.POST.get('num_pedidos_procesados') or 0,
            kg_ropa_procesada=request.POST.get('kg_ropa_procesada') or 0,
            tiempo_inactividad_maquinas=request.POST.get('tiempo_inactividad_maquinas') or 0,
            observaciones_turno=request.POST.get('observaciones_turno',''),
            consumo_agua_litros=request.POST.get('consumo_agua_litros') or 0
        )
        return redirect('app_lavanderia:ver_reportes')
    return render(request, 'app_lavanderia27/reportes/agregar_.html', {'empleados': empleados})

@csrf_protect
def actualizar_reporte(request, id):
    rep = get_object_or_404(ReporteOperacional, pk=id)
    empleados = EmpleadoLavanderia.objects.all()
    if request.method == 'POST':
        rep.empleado_id = request.POST.get('empleado') or rep.empleado_id
        rep.num_pedidos_procesados = request.POST.get('num_pedidos_procesados') or rep.num_pedidos_procesados
        rep.kg_ropa_procesada = request.POST.get('kg_ropa_procesada') or rep.kg_ropa_procesada
        rep.tiempo_inactividad_maquinas = request.POST.get('tiempo_inactividad_maquinas') or rep.tiempo_inactividad_maquinas
        rep.observaciones_turno = request.POST.get('observaciones_turno','')
        rep.consumo_agua_litros = request.POST.get('consumo_agua_litros') or rep.consumo_agua_litros
        rep.save()
        return redirect('app_lavanderia:ver_reportes')
    return render(request, 'app_lavanderia27/reportes/actualizar_.html', {'rep': rep, 'empleados': empleados})

@csrf_protect
def borrar_reporte(request, id):
    rep = get_object_or_404(ReporteOperacional, pk=id)
    if request.method == 'POST':
        rep.delete()
        return redirect('app_lavanderia:ver_reportes')
    return render(request, 'app_lavanderia27/reportes/borrar_.html', {'rep': rep})
