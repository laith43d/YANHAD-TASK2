from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import (Product,Category,Merchant,Label,Vendor)
from commerce.schemas import (ProductOut, ProductCreate,UpdateProduct, MessageOut,CategoryCreat,CategoryOut,LabelCreat,LabelOut,MerchantCreat,MerchantOut,VendorCreat,VendorOut)

commerce_controller = Router(tags=['CRUD'])

# @commerce_controller.get('products')
# def list_products(request, id: int = None):
#     return {'name': 'Ruaa  solved the task very late!!!!'}
#
#
# @commerce_controller.get('products/{id}')
# def retrieve_products(request, id: int):
#     return {'name': f'Ruaa  solved the task {id} days late '}
#
#
# @commerce_controller.post('products')
# def create_product(request, product_in: RuaaSchema):
#     return product_in.dict()


'''
/api/resource/{id}/

/api/resource?id=&name=&age=

{
    JSON
}
'''


@commerce_controller.get('products', response={
    200: List[ProductOut],
})
def list_products(request):
    products = Product.objects.all()
    # products = products.filter(name='tshirt')
    return products
#___________-category_______________
@commerce_controller.get('Category', response={
    200:list[CategoryOut],
})
def lists_category(request):
    category = Category.objects.all()
    
    return category
#__________label____________________

@commerce_controller.get('label', response={
    200: List[LabelOut],
})
def list_label(request):
    label = Label.objects.all()
    return label 
#_____________vendor_________________

@commerce_controller.get('vendor', response={
    200: List[VendorOut],
})
def list_vendor(request):
    vendor = Vendor.objects.all()
    return vendor

#----------MERCHANT--------------------

@commerce_controller.get('merchant', response={
    200: List[MerchantOut],
})
def list_merchant(request):
   merchant = Merchant.objects.all()
   return merchant 

#------Post---------------------------

@commerce_controller.post('products', response={
    201: ProductOut,
    400: MessageOut
})
def create_product(request, payload: ProductCreate):
    try:
        product = Product.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, product
#---------CATEGORY---------------
@commerce_controller.post('Category', response={
    201: CategoryOut,
    400: MessageOut
})
def create_Category(request, payload: CategoryCreat):
    try:
        category = Category.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category
#----------LABEL-----------------
@commerce_controller.post('label', response={
    201: LabelOut,
    400: MessageOut
})
def create_label(request, payload: LabelCreat):
    try:
       label = Label.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, label
#------------VENDOR----------------
@commerce_controller.post('vendor', response={
    201: VendorOut,
    400: MessageOut
})
def create_vendor(request, payload: LabelCreat):
    try:
       vendor = Vendor.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendor
#------------merchant-------
@commerce_controller.post('merchant', response={
    201: MerchantOut,
    400: MessageOut
})
def create_merchant(request, payload:MerchantCreat):
    try:
       merchant = Merchant.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchant

#__________________________________________-
#--------Update-------------------

@commerce_controller.put("product/{id}",response={
    202:ProductOut,
    400:MessageOut
})
def update_product(request, id: int, update: UpdateProduct):
    product_U = get_object_or_404(Product, id=id) #check if i have a product or not
    for attr, value in update.dict().items():
        setattr(update, attr, value)
    product_U.save()
    return product_U  

#------------category----------------
@commerce_controller.put("category/{id}",response={
    202:CategoryOut,
    400:MessageOut
})
def update_Category(request, id: int, update: CategoryCreat):
    category_U = get_object_or_404(Category, id=id) 
    for attr, value in update.dict().items():
        setattr(update, attr, value)
    category_U.save()
    return category_U 

#--------------label--------------------
@commerce_controller.put("label/{id}",response={
    202:LabelOut,
    400:MessageOut
})
def update_label(request, id: int, update: LabelCreat):
    label_U = get_object_or_404(Label, id=id) 
    for attr, value in update.dict().items():
        setattr(update, attr, value)
    label_U.save()
    return label_U
#-------------------vendor-----------
@commerce_controller.put("vendor/{id}",response={
    202:VendorOut,
    400:MessageOut
})
#--------------
schema
import datetime

from ninja import Schema
from pydantic import UUID4


class MessageOut(Schema):
    detail: str

class HumanQualities(Schema):
    age: int
    height: int


class RuaaSchema(Schema):
    name: str
    specs: HumanQualities

class CategoryOut(Schema):
    id: UUID4
    name: str
    description: str
    image: str
class CategoryCreat(Schema):
    id: UUID4
    name: str
    description: str
    image: str
    created:datetime.datetime
    is_active=bool
class LabelOut(Schema):
    id: UUID4
    name: str

class LabelCreat(Schema):
    id: UUID4
    name: str

class MerchantOut(Schema):
    id: UUID4
    name: str
    created: datetime.datetime
    updated: datetime.datetime

class MerchantCreat(Schema):
    id: UUID4
    name: str
    created: datetime.datetime
    updated: datetime.datetime

class VendorOut(Schema):
    id: UUID4
    name: str
    image: str

class VendorCreat(Schema):
    id: UUID4
    name: str
    image: str
    slug: str

class ProductOut(Schema):
    id: UUID4
    is_featured: bool
    name: str
    description: str
    qty: int
    price: int
    discounted_price: int
    category: CategoryOut
    vendor: VendorOut
    merchant: MerchantOut
    label: LabelOut
    created: datetime.datetime
    updated: datetime.datetime

class ProductCreate(Schema):
    is_featured: bool
    name: str
    description: str
    qty: int
    cost: int
    price: int
    discounted_price: int
    category_id: UUID4
    vendor_id: UUID4
    merchant_id: UUID4
    label_id: UUID4

class UpdateProduct(Schema):
    is_featured: bool
    name: str
    description: str
    qty: int
    cost: int
    price: int
    discounted_price: int
    updated: datetime.datetime
def update_vendor(request, id: int, update: VendorCreat):
    vendor_U = get_object_or_404(Vendor, id=id) 
    for attr, value in update.dict().items():
        setattr(update, attr, value)
    vendor_U.save()
    return vendor_U

#_______________merchant-------------------
@commerce_controller.put("Merchant/{id}",response={
    202:MerchantOut,
    400:MessageOut
})
def update_Merchant(request, id: int, update: VendorCreat):
    merchant_U = get_object_or_404(Merchant, id=id) 
    for attr, value in update.dict().items():
        setattr(update, attr, value)
    merchant_U.save()
    return merchant_U


   #________________________________- 
   #------Deleted------------------  
@commerce_controller.delete('product/{id}')
def delete_product(request,id):
    Deletedproduct = get_object_or_404(Product, id=id)
    Deletedproduct.delete()
    return {"success": True}

@commerce_controller.delete('Category/{id}')
def delete_Category(request,id):
    DeletedCategory = get_object_or_404(Category, id=id)
    DeletedCategory.delete()
    return {"success": True}

@commerce_controller.delete('label/{id}')
def delete_label(request,id):
    Deletedlabel = get_object_or_404(Label, id=id)
    Deletedlabel.delete()
    return {"success": True}

@commerce_controller.delete('Vendor/{id}')
def delete_Vendor(request,id):
    DeletedVendor = get_object_or_404(Vendor, id=id)
    DeletedVendor.delete()
    return {"success": True}

@commerce_controller.delete('Merchant/{id}')
def delete_Merchant(request,id):
    DeletedMerchant = get_object_or_404(Merchant, id=id)
    DeletedMerchant.delete()
    return {"success": True}
    
    

