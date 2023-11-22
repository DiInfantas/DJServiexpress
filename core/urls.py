from django.urls import path
from .views import index, login, registro, rePass, tomadehoras
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('login',login , name='login'),
    path('registro',registro , name='registro'),
    path('rePass',rePass , name='rePass'),
    path('tomadehoras',tomadehoras , name='tomadehoras'),

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)