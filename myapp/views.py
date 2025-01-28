from django.shortcuts import render,redirect
from django.contrib import messages
from .models import register,product,cart,hamper,inquiry,order,feedback
from django.db.models import Sum
# Create your views here.

def indexpage(request):
    return render(request,"index.html")

def loginpage(request):
    return render(request,"login.html")

def registerpage(request):
    return render(request,"register.html")

def checkoutpage(request):
    uid = request.session["id"]
    getdata = cart.objects.filter(user_id=uid,order_status=0)
    carttotal = cart.objects.filter(user_id=uid, order_id=0).aggregate(Sum("totalprice"))
    carttotal = carttotal.get("totalprice__sum")
    gethampers = hamper.objects.all()
    context = {
        'data':getdata,
        'hamper':gethampers,
        'total':carttotal
    }
    return render(request,"checkout.html",context)

def furniturepage(request):
    return render(request,"furniture.html")

def mailpage(request):
    return render(request,"mail.html")

def productspage(request):
    return render(request,"products.html")

def shoetcodespage(request):
    return render(request,"short-codes.html")

def categorywiseproduct(request,id):
    getdata = product.objects.filter(category_id=id)
    context = {
        'data':getdata
    }
    return render(request,"categorywiseproduct.html",context)



def singlepage(request,id):
    getdata = product.objects.get(id=id)
    context = {
        'data':getdata
    }
    return render(request,"single.html",context)

def feedbackpage(request):
    return render(request,"feedback.html")

def orderpage(request):
    uid=request.session["id"]
    data=order.objects.filter(user_id=uid)
    context={
        'data':data
    }
    return render(request,"order.html",context)

def singleorderpage(request,id):
    data=cart.objects.filter(order_id=id)
    context = {
        'data': data
    }
    return render(request,"singleorder.html", context)


def fetchdata(request):
    if request.method == 'POST':
        umail=request.POST.get("user_Emailid")

        try:
            userdetails = register.objects.get(user_Emailid=umail)
        except:
            userdetails = None

        if userdetails is not None:
            messages.success(request,"you are already registered")
            return render(request,"login.html")

        else:
            fname=request.POST.get("first_name")
            lname = request.POST.get("last_name")
            pswd = request.POST.get("password")
            mno = request.POST.get("mobile_no")
            add=request.POST.get("address")
            Eid = request.POST.get("user_Emailid")
            confpswd=request.POST.get("confirmpassword")


            if pswd==confpswd:
                insertdata = register(first_name=fname,last_name=lname,password=pswd,user_Emailid=Eid,mobile_no=mno,address=add)
                insertdata .save()
                messages.success(request,"Registered Successfully !")
                return render(request, "login.html")

            else:
                messages.error(request, 'Password and confirm password fields do not match')

    else:
        pass
    return render(request,"register.html")

def checklogindata(request):
    if request.method == 'POST':
        usermail=request.POST.get("user_Emailid")
        userpass=request.POST.get("password")
        try:
            userdetails = register.objects.get(user_Emailid=usermail,password=userpass)
            request.session["id"] = userdetails.id
            request.session["name"] = userdetails.first_name
            request.session.save()
        except:
            userdetails=None

        if userdetails is not None:
            messages.success(request,"Login Successfully")
        else:
            messages.success(request, "Incorrect Details !")
            return render(request,"login.html")
    else:
        pass
    return render(request,"index.html")

def addtocart(request):
    uid = request.session["id"]
    pid = request.POST.get("pid")
    price = request.POST.get("price")
    quantity = request.POST.get("quantity")
    price = int(price)
    quantity = int(quantity)
    tprice = price * quantity
    insertquery = cart(user_id=register(id=uid),product_id=product(id=pid),product_quantity=quantity,totalprice=tprice,order_id=0,order_status=0)
    insertquery.save()
    messages.success(request,"added to cart")
    return redirect(checkoutpage)


def hamperpage(request):
    # return render(request,"hamper.html")
    getdata = hamper.objects.all()
    context = {
        'data':getdata
    }
    return render(request,"hamper.html",context)

def singleHamperpage(request,id):
    getdata = hamper.objects.get(id=id)
    context = {
        'data':getdata
    }
    return render(request,"singleHamper.html",context)

def deleteproduct(request,id):
    querytoremove=cart.objects.get(id=id)
    querytoremove.delete()
    return redirect(checkoutpage)

def fetchinquiry(request):
    if request.method=='POST':
        cname=request.POST.get("iname")
        cmail= request.POST.get("mail")
        cmsg = request.POST.get("msg")

        insertdata=inquiry(name=cname,email=cmail,message=cmsg)
        insertdata.save()
        messages.success(request,"Your Inquiry is successfully Placed")

    else:
        pass
    return render(request, "mail.html")

def placeorder(request):
    uid = request.session["id"]
    if request.method == 'POST':
        hamper_id=request.POST.get("selectedHamper")
        print(hamper_id)
        selhamper=hamper.objects.get(id=hamper_id)
        hamperprice = selhamper.hamper_price
        del_date=request.POST.get("deldate")
        del_address=request.POST.get("address")

        carttotal = cart.objects.filter(user_id=uid, order_id=0).aggregate(Sum("totalprice"))
        carttotal = carttotal.get("totalprice__sum")

        print("hamper price")
        print(hamperprice)
        print("cart total price")
        print(carttotal)

        hamperorderprice = int(carttotal) + int(hamperprice)

        orderdata = order(user_id=register(id=uid),hamper_id=hamper(id=hamper_id), delivery_Address=del_address, order_totalprice=hamperorderprice,
                                  delivery_date=del_date)
        orderdata.save()

        lasstid = order.objects.latest('id')

        print(lasstid)

        objid = lasstid.id
        print(objid)


        obj = cart.objects.filter(user_id=uid, order_id=0)
        for object in obj:
            object.order_id = objid
            object.order_status = 1
            object.save()

        messages.success(request, "Order Placed")
        return render(request,"feedback.html")
    else:
        pass
    messages.error(request, "Order Failed")
    return render(request,"index.html")

def fetchfeedback(request):
    uid = request.session["id"]
    if request.method=='POST':
        desc=request.POST.get("des")
        rat=request.POST.get("rating")
        feedbackdata=feedback(user_id=register(id=uid),rating=rat,description=desc)
        feedbackdata.save()
        messages.success(request,"Your Feedback is successfully Placed")
        return render(request, "index.html")

    else:
        pass
    return render(request,"feedback.html")


