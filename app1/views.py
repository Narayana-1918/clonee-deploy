from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# from django.contrib.auth import authenticate
 
def userregister(request):
    if request.method=="POST":
        print("sdfgh")
        user=New_user.objects.filter(username=request.POST['username'])
        if user.exists():
            messages.info(request,"User Already Exist")
            return redirect('/userregister/')
        form=UserForm(request.POST)
        if form.is_valid():
            print("hello")
            form.save()
            return redirect('/userlogin/')
        else:
            print('hi')
            print(form.errors)
            return render(request,'userregister.html',{'form':form})
        
    return render(request,'userregister.html')

def userlogin(request):
    print(request.user)
    if request.method=='POST':
        form=UserloginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect('//')
            else:
                messages.info(request,"username or password is invalid")
                return redirect('/userlogin/')
    return render(request,'userlogin.html')



@login_required(login_url='userlogin')
def home(request):
    return render(request,'home.html')


@login_required(login_url='userlogin')
def userlogout(request):
    logout(request)
    return redirect('/userlogin/')

@login_required(login_url='userlogin')
def hotel_list(request):
    data=Restaurant.objects.all()
    return render(request,'hotel_list.html',{'data':data})
            


@login_required(login_url='userlogin')
def menu_list(request,id):
    menus=Menu.objects.filter(restaurant_id=id)
    return render(request,'menu.html',{'menus':menus})


@login_required(login_url='userlogin')


@login_required(login_url='login')
def create_order(request):
    
    cart = Cart_items.objects.filter(user=request.user)

    if cart:
        total_price = sum(item.menu.item_price * item.quantity for item in cart)

        order = Order.objects.create(user=request.user, total_price=total_price)

        for item in cart:
            OrderItem.objects.create(order=order, product=item.menu, quantity=item.quantity)

        cart.delete()
    else:
        return redirect('/hotel_list/')

    return redirect('order_detail', order_id=order.id) 

def order_detail(request, order_id):
    order =Order.objects.get( id=order_id, user=request.user)

    return render(request, 'order_detail.html', {'order': order})


#user addtocart

@login_required(login_url='userlogin')  
def profile(request):
    if request.user:
        user=New_user.objects.filter(id=request.user.id)
        print(user)
    return render(request,'profile.html',{'data':user})

def view_cart(request):
    cart_items=Cart_items.objects.filter(user=request.user)
    total_price=sum(i.menu.item_price * i.quantity for i in cart_items)
    return render(request,'cart.html',{'cart_items':cart_items,'total_price':total_price})


@login_required(login_url='userlogin')
def add_to_cart(request,id):
    menu=Menu.objects.get(menu_id=id)
    cart_item,created=Cart_items.objects.get_or_create(menu=menu,user=request.user)
    cart_item.quantity+=1
    cart_item.save()
    return redirect('/hotel_list/')

@login_required(login_url='userlogin')
def remove_from_cart(request,id):   
    cart_item=Cart_items.objects.get(id=id)
    print(cart_item)
    if cart_item.quantity>1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('/view_cart/')

def delete_item(request,id):
    cart_item=Cart_items.objects.get(id=id)
    cart_item.delete()
    return redirect('/view_cart/')


# def buy_now(request,id):
#     product=Menu.objects.get(menu_id=id)
#     cart_item,created=Cart_items.objects.get_or_create(product=product,user=request.user)
#     cart_item.quantity+=1
#     cart_item.save()
#     return redirect('/view_cart/')

@login_required(login_url='userlogin')
def search_view(request):
    query=request.GET.get('q')
    obj=Restaurant.objects.filter(restaurant_name__icontains=query)
    print(obj)
    # if obj:
    #     redirect('searchview/')
    return render(request,'data.html',{'filter':obj})

@login_required(login_url='userlogin')
def menu_search(request):
    query1=request.GET.get('r')
    obj1=Menu.objects.filter(item_name__icontains=query1)
    # if obj1:
    #     redirect('menu_search/')
    return render(request,'data1.html',{'filter1':obj1})

@login_required(login_url='userlogin')
def addetail(request):
    if request.method=='POST':
        form=AddetailForm()
        if form.is_valid():
            # form.save()
            return redirect('/order/')
    return render(request,'address.html')

# @login_required(login_url='userlogin')
# def menu_detail(request,id):
#     menu=Menu.objects.get(menu_id=id)
#     return render(request,'order.html',{'menu':menu})

@login_required(login_url='userlogin')
def success(request):
    return render(request,'succeed.html')




