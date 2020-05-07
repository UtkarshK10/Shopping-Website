from django.shortcuts import render
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query=request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!=0:
           allProds.append([prod, range(1, nSlides), nSlides]) 
        

    
    params = {'allProds':allProds,"msg":""}
    if len(allProds)==0 or len(query)<3:
        params={"msg":"Please make sure to enter relevant serach query"}
    return render(request, 'shop/search.html', params)






def about(request):
    
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        
        
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        query=request.POST.get('query','')
        contact=Contact(name=name,email=email,phone=phone,query=query)
        contact.save()
        
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method=='POST':
        orderId=request.POST.get('orderId','')
        email=request.POST.get('email','')
        
        try:
            order=Orders.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    #converts object into json and json.loads() to object
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
            
    return render(request, 'shop/tracker.html')



def productview(request,myid):
    #Feth the prduct using id
    product=Product.objects.filter(id=myid)
    #without'' prod is variable and with is object we want to acces in our template
   
    return render(request, 'shop/productview.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        area=request.POST.get('area','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone,area=area)
        order.save()
        update=OrderUpdate(order_id=order.order_id, update_desc="The Order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')
        
    
    
    
