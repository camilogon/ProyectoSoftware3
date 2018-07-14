"""ProyectoSoftware3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
	path('Estudiante/',include('Apps.Estudiante.urls')),
	path('Acudiente/',include('Apps.Acudiente.urls')),
	path('Profesor/',include('Apps.Profesor.urls')),
	path('Curso/',include('Apps.Curso.urls')),
	path('Materia/',include('Apps.Materia.urls')),
	path('Tema/',include('Apps.Tema.urls')),
	path('Asignar/',include('Apps.Asignar.urls')),
	path('Actividad/',include('Apps.Actividad.urls')),
	path('Cuestionario/',include('Apps.Cuestionario.urls')),
	path('PreguntasCuestionario/',include('Apps.PreguntasCuestionario.urls')),
    path('admin/', admin.site.urls),
]
