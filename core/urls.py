from django.urls import path
from .views import index, login, registro, rePass, register, tomadehoras, horastomadas, editarhora
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('login',login , name='login'),
    path('registro',registro , name='registro'),
    path('rePass',rePass , name='rePass'),
    path('tomadehoras',tomadehoras , name='tomadehoras'),
    path('horastomadas', horastomadas , name='horastomadas'),
    path('editarhora', editarhora , name='editarhora'),
    path('register/', register, name='register'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)