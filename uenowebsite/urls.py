from django.urls import path
from uenowebsite import views

app_name = 'uenowebsite'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('enquiry/', views.enquiry, name='enquiry'),  # Add this line for the enquiry page
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),  # Add this line for the add page
    path('faq/', views.faq_view, name='faq'),

    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('president-message/', views.president_message, name='president_message'),


]
