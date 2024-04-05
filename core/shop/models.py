from django.db import models

class Color(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Size(models.Model):
    name=models.CharField(max_length=3)
    def __str__(self):
        return self.name

class Products(models.Model): 
    
    #model for products
    photo=models.ImageField(upload_to='products')
    photoTwo=models.ImageField(upload_to='products')
    photoThree=models.ImageField(upload_to='products')
    photoFour=models.ImageField(upload_to='products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    size=models.ManyToManyField(Size,blank=True)
    color=models.ManyToManyField(Color,blank=True)
    price = models.IntegerField()
    dummyPrice=models.IntegerField(null=True,blank=True)
    man=models.BooleanField(default=False)
    women=models.BooleanField(default=False)
    accessories=models.BooleanField(default=False)
    Others=models.BooleanField(default=False)
    featured=models.BooleanField(default=False)
    inStock=models.BooleanField(default=True)

    def price_difference_percentage(self):
        if self.dummyPrice is not None and self.dummyPrice > self.price:
            difference = self.dummyPrice - self.price
            percentage = (difference / self.dummyPrice) * 100
            return round(percentage, 2)
        else:
            return None




    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_list=models.TextField(null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100 ,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    CashOnDelivary=models.CharField(max_length=20, null=True,blank=True)
    online=models.CharField(max_length=20,null=True,blank=True)
    online_Sender_phone_number=models.CharField(max_length=20,null=True,blank=True)
    online_transaction_id=models.CharField(max_length=20,null=True,blank=True)
    Total_Payment=models.FloatField(default=0)
    OederPlaced=models.BooleanField(default=False,)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return "order: "+ self.name+" - "+self.phone
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    


class Banner(models.Model):
    image_one=models.ImageField(upload_to='banners')
    headline=models.CharField(max_length=64,null=True,blank=True)
    content=models.CharField( max_length=50,null=True,blank=True)
    offer=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
       return self.content 

class ShopInfo(models.Model):
    logo=models.ImageField(upload_to='banner',blank=True)
    Address=models.CharField(max_length=100,null=True)
    Phone=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    WorkingHour=models.CharField(max_length=100,null=True)
    onlinePaymentNumber=models.CharField(max_length=30,null=True)



