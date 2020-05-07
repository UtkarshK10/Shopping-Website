from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")
    
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=70,default="")
    phone=models.CharField(max_length=70,default="")
    query=models.CharField(max_length=70,default="")
    
    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zip_code=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    area=models.CharField(max_length=200)
    
    

    
class OrderUpdate(models.Model):
    
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc[0:7]+ "...."    
    
    
        