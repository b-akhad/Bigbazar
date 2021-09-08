from django.urls import path

from ecom.views import *

urlpatterns = [
    path('', home, name="home"),
    path('<int:pk>', detail, name="detail"),
    path('shoe/', shoe_link, name="shoe"),
    path('bags/', bags_link, name="bag"),
    path('dress/', dress_link, name="dress"),
    path('treasure/', treasure_link, name="treasure"),
    path('hijab/', hijab_link, name="hijab"),
    path('romol/', romol_link, name="romol"),
    path('shoe/<int:pk>', sh_detail, name="sh-detail"),
    path('dress/<int:pk>', d_detail, name="d-detail"),
    path('bag/<int:pk>', b_detail, name="b-detail"),
    path('treasure/<int:pk>', t_detail, name="t-detail"),
    path('hijab/<int:pk>', h_detail, name="h-detail"),
    path('romol/<int:pk>', romol_detail, name="detail-r"),



]