"""babytilly2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import TemplateView

from commercial.views import ArticleListView, AddToCartView, OrderListView, edit_cart

urlpatterns = [
    path('cart/', edit_cart, {}, 'commercial_edit_cart'),
    path('commerce/addtocart/<int:id>/', AddToCartView.as_view(), name='commercial_addto_cart_one'),
    path('commerce/addtocart/<int:id>/<int:count>/', AddToCartView.as_view(),
                      name='commercial_addto_cart'),
    path('commerce/orders/', OrderListView.as_view(), name='commercial_order_list'),
    path('commerce/category/<int:id>/', ArticleListView.as_view(), name='category_detail_url'),
    path('', login_required(TemplateView.as_view(template_name='index.html'))),
] + staticfiles_urlpatterns()