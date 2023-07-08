from django.http import HttpResponse
from django.shortcuts import render
from .models import Pedido
from .forms import PedidoForm

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
            return render(request, "pedido_success.html")
        else:
            return HttpResponse("Ha ocurrido un error en el formulario")
    else:
        form = PedidoForm()

    return render(request, "pedido_form.html", {"form": form})

def pedido_detail(request,id):
    pedido_details = Pedido.objects.only('usuario','dir_entrega','productos','forma_pago','estado','gestionado').filter(id=id)
    context = {
        'pedido' : pedido_details
    }
    return render(request, "pedido_detail.html", context)