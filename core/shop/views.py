from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User
from django .contrib.auth import authenticate,login,logout
from django .contrib.auth import login as auth_login
from django.contrib import messages
# Create your views here.

def home(request):
    sort_by = request.GET.get('sort_by', 'newest')  # Default sorting by newest

    if sort_by == 'price_asc':
        products = Products.objects.order_by('price').filter(featured=True)
    elif sort_by == 'price_desc':
        products = Products.objects.order_by('-price').filter(featured=True)
    else:
        products = Products.objects.all().filter(featured=True)  # Default sorting by newest

    banner = Banner.objects.all()

    context = {
        'banner': banner,
        'products': products,
        'sort_by': sort_by
    }
    return render(request, 'home.html', context)



def  man(request):
    sort_by = request.GET.get('sort_by', 'newest')  # Default sorting by newest

    if sort_by == 'price_asc':
        products = Products.objects.order_by('price').filter(man=True)
    elif sort_by == 'price_desc':
        products = Products.objects.order_by('-price').filter(man=True)
    else:
        products = Products.objects.all().filter(man=True)  # Default sorting by newest

    context= {'products':products}
    return render ( request, 'man.html',context)


def  women(request):
    sort_by = request.GET.get('sort_by', 'newest')  # Default sorting by newest

    if sort_by == 'price_asc':
        products = Products.objects.order_by('price').filter(women=True)
    elif sort_by == 'price_desc':
        products = Products.objects.order_by('-price').filter(women=True)
    else:
        products = Products.objects.all().filter(women=True)  # Default sorting by newest

    context= {'products':products}
    return render ( request, 'womens.html',context)


def  accessories(request):
    sort_by = request.GET.get('sort_by', 'newest')  # Default sorting by newest

    if sort_by == 'price_asc':
        products = Products.objects.order_by('price').filter(accessories=True)
    elif sort_by == 'price_desc':
        products = Products.objects.order_by('-price').filter(accessories=True)
    else:
        products = Products.objects.all().filter(accessories=True)  # Default sorting by newest
    context= {'products':products}
    return render ( request, 'accessories.html',context)


def  others(request):
    sort_by = request.GET.get('sort_by', 'newest')  # Default sorting by newest

    if sort_by == 'price_asc':
        products = Products.objects.order_by('price').filter(Others=True)
    elif sort_by == 'price_desc':
        products = Products.objects.order_by('-price').filter(Others=True)
    else:
        products = Products.objects.all().filter(Others=True)  # Default sorting by newest
    context= {'products':products}
    return render ( request, 'others.html',context)


def  cart(request):
    

    
    return render ( request, 'shop-cart.html')


def  productDetails(request , id): #viw all the details of the selected product 
    #similarProducts= Products.objects.filter(category__in=Products.objects.filter(id=id).values("category"))[:4]  
    product=Products.objects.get(id = id)
    context={'product':product,
             'image_url': product.photo.url,
             }
    return render ( request, 'product-details.html',context)



def  login(request):
    if request.method ==  "POST":
        data=request.POST

        username=data.get('email')
        password=data.get('password')


        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            print("logged in")
           
            return redirect('home')
        
        
        
        else:
            messages.error(request,'Username or Password is incorrect')
            print("not in")

            return redirect('login')
    return render ( request, 'login.html')





def register(request):
    if request.method == 'POST':
        data = request.POST

        username = data.get('inputEmailAddress')
        first_name = data.get('inputName')
        email = data.get('inputEmailAddress')
        mobile = data.get('inputmobile')
        password = data.get('inputChoosePassword')
        agreement = data.get('agreementChecked')

        errors = []

        if User.objects.filter(username=username).exists():
            errors.append('Username is already taken.')
        if User.objects.filter(email=email).exists():
            errors.append('Email is already registered.')

        if errors:
            return render(request, 'register.html', {'errors': errors})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.mobile = mobile
        user.agreement = agreement
        user.save()

        messages.success(request, 'Sign up successful.')
        return redirect('login')

    return render(request, 'register.html')


def handlelogout(request):
    logout(request)
    return redirect('home')

def checkOut(request):
    if  request.method=='POST':
        data=request.POST
        itemsJSON=data.get('itemsJson', '')
        Name=data.get('fname', '')
        email=data.get('email', '')
        phone=data.get('phone', '')
        state=data.get('state', '')
        city=data.get('city', '')
        address=data.get('address', '')
        paymentCOD=data.get('payment_type', '')
        paymentOnline=data.get('payment_typeOnline', '')
        online_Sender_phone_number=data.get('send_phone_number', '')
        online_transaction_id=data.get('transaction_number', '')
        Total_Payment=float(request.POST.get('price', 0))


        order =Orders.objects.create(
            items_list=itemsJSON,
            name=Name,
            email=email,
            phone=phone,
            state=state,
            city=city,
            address=address,
            CashOnDelivary=paymentCOD,
            online=paymentOnline,
            online_Sender_phone_number=online_Sender_phone_number,
            online_transaction_id=online_transaction_id,
            Total_Payment=Total_Payment,

        )
        order.save()
        return redirect('checkOutMsg')
    return render ( request, 'checkout.html')


def checkOutMsg(request):
    
    return render ( request, 'checkoutMsg.html')

def privacy(request):
    return render(request,'privacy.html')


