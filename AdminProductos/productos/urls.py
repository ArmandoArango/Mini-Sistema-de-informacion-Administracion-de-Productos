from django.conf.urls import url
from productos.views import ListadoProducto
from productos.views import VisualizarProducto
from productos.views import AdicionarProducto
from productos.views import ModificarProducto
from productos.views import EliminarProducto
from productos.views import ReporteExcel

urlpatterns = [
    url(r'^listar-producto/', ListadoProducto.as_view(), name='listar_producto'),
    url(r'^visualizar-prodcuto/(?P<id_producto>\w+)', VisualizarProducto.as_view(), name='visualizar_producto'),
    url(r'^modificar-prodcuto/(?P<id_producto>\w+)', ModificarProducto.as_view(), name='modificar_producto'),
    url(r'^eliminar-prodcuto/(?P<id_producto>\w+)', EliminarProducto.as_view(), name='eliminar_producto'),
    url(r'^adicionar-prodcuto/', AdicionarProducto.as_view(), name='adicionar_producto'),
    url(r'^reporte-prodcuto/', ReporteExcel.as_view(), name='reporte_producto'),
]