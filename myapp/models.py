from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class register(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=8)
    user_Emailid=models.EmailField()
    mobile_no=models.IntegerField()
    address=models.TextField()

    def __str__(self):
        return self.first_name

class category(models.Model):
    category_name=models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

class product(models.Model):
    product_name=models.CharField(max_length=25)
    category_id=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    product_price=models.IntegerField()
    product_description=models.TextField()
    product_image=models.ImageField(upload_to='photos')
    Product_status=models.BooleanField()


    def pro_img(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.product_image.url))


    def __str__(self):
        return self.product_name

class hamper(models.Model):
    hamper_name = models.CharField(max_length=50)
    hamper_price = models.BigIntegerField()
    hamper_image = models.ImageField(upload_to='photos')
    hamper_description = models.TextField()
    hamper_status = models.BooleanField()

    def hamp_img(self):
        return mark_safe('img src="{}" width="100" />'.format(self.hamper_image.url))

class order(models.Model):
    user_id=models.ForeignKey(register,on_delete=models.CASCADE,null=True)
    hamper_id = models.ForeignKey(hamper, on_delete=models.CASCADE, null=True)
    order_date=models.DateTimeField(auto_now_add=True)
    order_totalprice=models.IntegerField()
    delivery_date= models.DateTimeField(max_length=200)
    delivery_Address = models.TextField()


class cart(models.Model):
    user_id=models.ForeignKey(register,on_delete=models.CASCADE,null=True)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    product_quantity=models.BigIntegerField()
    totalprice = models.IntegerField(null=True)
    order_id = models.IntegerField(null=True)
    order_status = models.BooleanField()

class feedback(models.Model):
    user_id = models.ForeignKey(register,on_delete=models.CASCADE,null=True)
    rating=models.IntegerField(null=True)
    description=models.TextField()

class inquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)







