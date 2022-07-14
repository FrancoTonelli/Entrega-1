import email
from django.shortcuts import render
from App_mvt.forms import ClienteFormulario, ClienteBusquedaFormulario
from App_mvt.forms import CoinFormulario, CoinBusquedaFormulario
from App_mvt.forms import OperacionFormulario, OperacionBusquedaFormulario
from App_mvt.models import Cliente, Coin, Operacion


# Create your views here.

def mostrar_index(request):
    context ={}
    return render(request, 'App_mvt/index.html',context)


def cargar_cliente(request):
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)
    
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente (nombre=informacion['nombre'], apellido = informacion['apellido'] ,edad = informacion['edad'], email = informacion ['email'])
            cliente.save()

            return render (request, 'App_mvt/index.html')

    else:
        miFormulario = ClienteFormulario()

    return render (request,'App_mvt/cliente-forms.html',{"miFormulario": miFormulario})


def buscar_cliente(request):
    formulario = ClienteBusquedaFormulario()
    clientes = "a"

    if request.GET:
        criterio = request.GET
        criterio=criterio['nombre']
        clientes = Cliente.objects.filter(nombre__icontains=criterio)

    return render(request, "App_mvt/cliente-search.html",{"formulario": formulario, "clientes":clientes})
 

def cargar_coin(request):
    if request.method == 'POST':
        miFormulario = CoinFormulario(request.POST)
        print(miFormulario)
    
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            coin = Coin(nombre=informacion['nombre'], ticker = informacion['ticker'] ,precio = informacion['precio'])
            coin.save()

            return render (request, 'App_mvt/index.html')

    else:
        miFormulario = CoinFormulario()

    return render (request,'App_mvt/coin-forms.html',{"miFormulario": miFormulario})


def buscar_coin(request):
    formulario = CoinBusquedaFormulario()
    coins = "a"

    if request.GET:
        criterio = request.GET
        criterio=criterio['ticker']
        coins = Coin.objects.filter(ticker__icontains=criterio)

    return render(request, "App_mvt/coin-search.html",{"formulario": formulario, "coins":coins})


def cargar_operacion(request):
    if request.method == 'POST':
        miFormulario = OperacionFormulario(request.POST)
        print(miFormulario)
    
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            operacion = Operacion(tipo=informacion['tipo'], activo = informacion['activo'] ,precio = informacion['precio'], cantidad = informacion ['cantidad'], fecha = informacion['fecha'])
            operacion.save()

            return render (request, 'App_mvt/index.html')

    else:
        miFormulario = OperacionFormulario()

    return render (request,'App_mvt/operacion-forms.html',{"miFormulario": miFormulario})


def buscar_operacion(request):
    formulario = OperacionBusquedaFormulario()
    operaciones = "a"

    if request.GET:
        criterio = request.GET
        criterio=criterio['activo']
        operaciones = Operacion.objects.filter(activo__icontains=criterio)

    return render(request, "App_mvt/operacion-search.html",{"formulario": formulario, "operaciones":operaciones})