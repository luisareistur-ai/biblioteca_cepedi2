from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("apps.core.urls")),
    path('alunos/', include('apps.alunos.urls', namespace='alunos')),
    path('livros/', include('apps.livros.urls', namespace='livros')),
    path('emprestimos/', include('apps.emprestimos.urls', namespace='emprestimos')),
<<<<<<< HEAD
    path('editoras/', include('apps.editoras.urls', namespace='editoras')),
    path('autores/', include('apps.autores.urls', namespace='autores')),
=======
>>>>>>> dec613af3560ee40193b9f197de6e822329538d0
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)