from django.http import HttpResponse
from django.shortcuts import render
from .models import Pedido, ProductoComprado
from .forms import PedidoForm, ActualizaPedido

# Create your views here.
def view_pedidos(request):
    pedido_details = Pedido.objects.only('id','usuario','dir_entrega','estado')
    context = {
        'pedidos' : pedido_details
    }
    return render(request, "pedidos.html", context)

def pedido_form(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            print(request.path_info)
            new_pedido = Pedido()
            new_pedido.usuario = form.cleaned_data['usuario']
            new_pedido.dir_entrega = form.cleaned_data['dir_entrega']
            new_pedido.forma_pago = form.cleaned_data['forma_pago']
            new_pedido.productos = form.cleaned_data['productos']
            new_pedido.estado = "Gestionado"
            if request.path_info == '/pedidos/pedido_form':
                new_pedido.gestionado = 1
            new_pedido.save()
            context = {
                'operacion' : "ingresado"
            }
            return render(request, "pedido_success.html", context)
        else:
            return HttpResponse("Ha ocurrido un error en el formulario")
    else:
        form = PedidoForm()

    return render(request, "pedido_form.html", {"form": form})

def pedido_detail(request,id):
    if request.method != "POST":
        pedido_details = Pedido.objects.only('id','usuario','dir_entrega','forma_pago','estado','gestionado').filter(id=id)
        print(pedido_details[0].id)
        pedido_productos = ProductoComprado.objects.all().filter(pedido=pedido_details[0].id)
        print(pedido_productos[0].pedido)
        form = ActualizaPedido(initial={'estado': pedido_productos[0].pedido.estado})
        context = {
            'pedido' : pedido_details,
            'productos' : pedido_productos,
            'form': form
        }
        return render(request, "pedido_detail.html", context)
    else:
        form = ActualizaPedido(request.POST)
        if form.is_valid():
            updated_pedido = Pedido.objects.all().get(id=form.cleaned_data['id'])
            updated_pedido.estado = form.cleaned_data['estado']
            updated_pedido.save()
        context = {
            'operacion' : "actualizado"
        }
        return render(request, "pedido_success.html", context)