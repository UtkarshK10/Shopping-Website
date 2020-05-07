from django.contrib import admin
from .models import Product,Orders,OrderUpdate
from .models import Contact
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
# Register your models here.
