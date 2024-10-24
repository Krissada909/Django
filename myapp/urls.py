from django.urls import path
from .views import customer_list, delete_customers  # นำเข้าทั้งสองฟังก์ชัน

urlpatterns = [
    path('customers/', customer_list, name='customer_list'),  # URL สำหรับรายการลูกค้า
    path('delete_customers/', delete_customers, name='delete_customers'),  # URL สำหรับลบลูกค้า
]
