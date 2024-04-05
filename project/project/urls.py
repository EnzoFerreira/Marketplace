from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from marketplace.views import *
from accounts.views import *


urlpatterns = [
    path('csmarket/',WeaponsListView.as_view(), name='weapons_list'),
    path('register/', register_view, name="register"),
    path('new_item/',new_market_item.as_view(), name='new_item'),
    path('login/', login_view , name='login'),
    path('logout/', logout_view, name='logout'),
    path('csmarket/<int:pk>/update/', Weapon_edit.as_view(), name='weapon_edit'),
    path('csmarket/<int:pk>/',Weapon_View.as_view() ,name="weapon_details"),
    path('csmarket/<int:pk>/delete/', Weapon_delete.as_view(), name="weapon_delete"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)