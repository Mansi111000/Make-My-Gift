from django.contrib import admin
from .models import register
from .models import category
from .models import product
from .models import order
from .models import hamper
from .models import cart
from .models import feedback
from .models import inquiry



# Register your models here.
class showregister(admin.ModelAdmin):
    list_display = ('first_name','last_name','password','user_Emailid','mobile_no','address')

class showcategory(admin.ModelAdmin):
    list_display = ('id','category_name',)


class showproduct(admin.ModelAdmin):
    list_display=('product_name','category_id','product_price','product_description','product_image')

class showorder(admin.ModelAdmin):
    list_display = ('user_id','order_date','order_totalprice','delivery_date','delivery_Address')

class showhamper(admin.ModelAdmin):
    list_display=('hamper_name','hamper_price','hamper_image','hamper_description','hamper_status')

class showcart(admin.ModelAdmin):
    list_display = ('user_id','product_id','product_quantity','order_id','order_status')

class showfeedback(admin.ModelAdmin):
    list_display=('user_id','rating','description')

class showinquiry(admin.ModelAdmin):
    list_display = ('name','email','message','timestamp')




admin.site.register(register,showregister)
admin.site.register(category,showcategory)
admin.site.register(product,showproduct)
admin.site.register(order,showorder)
admin.site.register(hamper,showhamper)
admin.site.register(cart,showcart)
admin.site.register(feedback,showfeedback)
admin.site.register(inquiry,showinquiry)
