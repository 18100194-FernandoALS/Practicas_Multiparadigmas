"""webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import bienvenido,bienvenido2,bienvenido3, bienvenido4
from empleado.views import eliminarDept_Empl,editarDept_empl,nuevoDept_Empl,detalleDept_Empl,eliminarDepartamento,editarDepartamento,nuevoDepartamento,detalleDepartamento, nuevoEmpleado,editarEmpleado,eliminarEmpleado,detalleEmpleado,detalleJefeDepartamento,nuevoJefeDepartamento,editarJefeDepartamento,eliminarJefeDepartamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenido,name='index'),
    path('departamentos/',bienvenido2,name='indexdep'),
    path('jefedepartamento/',bienvenido3,name='indexjefe'),
    path('dept_empl/',bienvenido4,name='indexdept_empl'),

    path('detalle_empleado/<int:id>',detalleEmpleado),
    path('nuevo_empleado/',nuevoEmpleado),
    path('editar_empleado/<int:id>',editarEmpleado),
    path('eliminar_empleado/<int:id>',eliminarEmpleado),

    path('departamentos/detalle_departamento/<int:id>',detalleDepartamento),
    path('departamentos/nuevo_departamento/',nuevoDepartamento),
    path('departamentos/editar_departamento/<int:id>',editarDepartamento),
    path('departamentos/eliminar_departamento/<int:id>',eliminarDepartamento),

    path('jefedepartamento/detalle_jefedept/<int:id>',detalleJefeDepartamento),
    path('jefedepartamento/agregar_jefedept/',nuevoJefeDepartamento),
    path('jefedepartamento/editar_jefedept/<int:id>',editarJefeDepartamento),
    path('jefedepartamento/eliminar_jefedept/<int:id>',eliminarJefeDepartamento),

    path('dept_empl/detalle_dept_empl/<int:id>',detalleDept_Empl),
    path('dept_empl/nuevo_dept_empl/',nuevoDept_Empl),
    path('dept_empl/editar_dept_empl/<int:id>',editarDept_empl),
    path('dept_empl/eliminar_dept_empl/<int:id>',eliminarDept_Empl),
]
