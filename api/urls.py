from django.urls import path
from . import views

urlpatterns = [
    path('', views.getEndpoints, name='get-routes'),
    path('medicines/', views.MedicineList.as_view(), name='all-medicine'),
    path('medicine/<int:id>', views.MedicineDetail.as_view(), name='medicine-detail'),


    # path('ngos/', views.getAllMedicines, name='all-medicines'),
    # path('ngo/<int:id>', views.getMedicine, name='all-medicines'),
    # path('suppliers/', views.getAllMedicines, name='all-medicines'),
    # path('supplier/<int:id>', views.getMedicine, name='all-medicines'),
]