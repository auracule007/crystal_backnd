from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # product & category url
    path('', views.index, name='index'),
    path('product_details/<slug:slug>/', views.product_details, name="product_details"),
    path('modal_details/<slug:slug>/', views.modal_details, name="modal_details"),
    path('categories/<slug:slug>/', views.categories, name="categories"),

    # Authentication Url
    path('userLogin/', views.userLogin, name="userLogin"),
    path('userReg/', views.userReg, name="userReg"),
    path('userSignout/', views.userSignout, name="userSignout"),
    path('profile/', views.profile, name="profile"),
    path('profile_update/', views.profile_update, name="profile_update"),

    #password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password/password_reset_form.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_complete.html"), name='password_reset_complete'),

    # SHopping url
    path('shopcart/<str:id>/', views.shopcart, name='shopcart'),
    path('cart/', views.cart, name='cart'),
    path('delete_cart/', views.delete_cart, name='delete_cart'),
    path('delallcart/', views.delallcart, name='delallcart'),
]
