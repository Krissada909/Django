from django.shortcuts import render
from .models import Customer
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator




def customer_list(request):
    search_name = request.GET.get('search_name', '')
    search_status = request.GET.get('search_status', '')

    customers = Customer.objects.all()  # เริ่มต้นด้วยข้อมูลทั้งหมด

    if search_name:
        customers = customers.filter(customer_name__icontains=search_name)  # ค้นหาชื่อลูกค้า
    if search_status:
        customers = customers.filter(status__icontains=search_status)  # ค้นหาสถานะ

    # ใช้ paginator สำหรับการแบ่งหน้า
    paginator = Paginator(customers, 8)  # ปรับจำนวนที่จะแสดงในแต่ละหน้า
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'myapp/customer_list.html', {
        'page_obj': page_obj,
        'search_name': search_name,
        'search_status': search_status,
    })

@csrf_exempt
def delete_customers(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer_ids = data.get('ids', [])
            print("Received data:", data)
            print("Customer IDs to delete:", customer_ids)
            
            # ตรวจสอบว่า customer_ids ไม่ว่าง
            if customer_ids:
                # แปลง customer_ids เป็นรูปแบบที่เหมาะสม (เป็น list ของจำนวนเต็ม)
                customer_ids = [int(float(id)) for id in customer_ids]
                
                # ใช้ customer_id แทน id
                Customer.objects.filter(customer_id__in=customer_ids).delete()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'No customer IDs provided'})
        except Exception as e:
            print("Error occurred:", e)
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

