from django.contrib import admin
from django.urls import path, include
from CRM_Main import views as CRM_Main_views
from Leads import views as Leads_views
from django.contrib.auth import views as auth_v
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',CRM_Main_views.Home_Page,name='home'),
    path('',CRM_Main_views.Landing_Page, name='landing'),
    path('login/',auth_v.LoginView.as_view(template_name='CRM_Main/login.html'),name="login"),
    path('logout/',auth_v.LogoutView.as_view(template_name='CRM_Main/logout.html'),name="logout"),
    path('leads/',Leads_views.leads,name='leads'),
    path('agents/',Leads_views.agents,name='agents'),
    path('leads/create_lead',Leads_views.create_lead,name='create_lead'),
    path('agents/create_agent',Leads_views.create_agent,name='create_agent'),
    path('leads/<int:pk>',Leads_views.leads_detail,name='leads_detail'),
    path('leads/<int:pk>/edit',Leads_views.leads_edit,name='leads_edit'),       
    path('agents/<int:pk>',Leads_views.agents_detail,name='agents_detail'),
    path('agents/<int:pk>/edit',Leads_views.agents_edit,name='agents_edit'), 
]

handler404="CRM_Main.views.handler404"

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)