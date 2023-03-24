from django import template
from mainApp.models import Product
register = template.Library()


@register.filter('cartQuantity')
def cartQuantity(request,id):
    cart = request.session.get("cart",None)
    for key,value in cart.items():
        if(key==str(id)):
            return value    

@register.filter('cartFinal')
def cartFinal(request,id):
    cart = request.session.get("cart",None)
    for key,value in cart.items():
        if(key==str(id)):
            p = Product.objects.get(id=id)
            return value*p.finalPrice   
@register.filter("checkoutDelete")
def checkoutDelete(request,num):
    if(num==1):
        return True
    else:
        return False

@register.filter("paymentMode")
def paymentMode(request,num):
    if(num==1):
        return "COD"
    else:
        return "Net Banking"
@register.filter("paymentStatus")
def paymentStatus(request,num):
    if(num==1):
        return "Pending"
    else:
        return "Done"

@register.filter("orderStatus")
def orderStatus(request,num):
    if(num==1):
        return "Not Packed"
    elif(num==2):
        return "Packed"
    elif(num==3):
        return "Out for Delivery"
    else:
        return "Delivered"

@register.filter("products")
def products(arg):
    arg=arg[0:len(arg)-1]
    item = arg.split(",")
    return item

@register.filter("productName")
def productName(arg):
    try:
        item = arg.split(":")
        if(item[0]!=''):
            item=int(item[0])
            p = Product.objects.get(id=item)
            return p.name
        else:
            return ""
    except:
        return ""

@register.filter("productImage")
def productImage(arg):
    try:
        item = arg.split(":")
        if(item[0]!=''):
            item=int(item[0])
            p = Product.objects.get(id=item)
            return p.pic1.url
        else:
            return ""
    except:
        return ""

@register.filter("productPrice")
def productPrice(arg):
    try:
        item = arg.split(":")
        if(item[0]!=''):
            item=int(item[0])
            p = Product.objects.get(id=item)
            return p.finalPrice
        else:
            return ""
    except:
        return ""

@register.filter("productColor")
def productColor(arg):
    try:
        item = arg.split(":")
        if(item[0]!=''):
            item=int(item[0])
            p = Product.objects.get(id=item)
            return p.color
        else:
            return ""
    except:
        return ""

@register.filter("productSize")
def productSize(arg):
    try:
        item = arg.split(":")
        if(item[0]!=''):
            item=int(item[0])
            p = Product.objects.get(id=item)
            return p.size
        else:
            return ""
    except:
        return ""