from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  # เปลี่ยนเป็น primary key ของคุณ
    customer_name = models.CharField(max_length=255)
    business_type = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    date_of_status = models.DateField(null=True, blank=True)
    responsible_by = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'Customer'

