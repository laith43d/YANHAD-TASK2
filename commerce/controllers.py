from typing import List
from uuid import UUID

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import Product, Merchant, Category, Label, Vendor
from commerce.schemas import ProductOut, ProductCreate, MessageOut, ProductUpdate
import commerce.schemas as  all_schemas

commerce_controller = Router(tags=['products'])

bonus_create_controller = Router(tags=['bonus / create'])
bonus_controller = Router(tags=['bonus / retrieve'])
bonus_update_controller = Router(tags=['bonus / update'])
bonus_remove_controller = Router(tags=['bonus / remove'])


# order_controller =Router(tags=['Order'])

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


@commerce_controller.get('product/{id}', response={
    200: ProductOut
})
def retrieve_product(request, id):
    return get_object_or_404(Product, id=id)


@commerce_controller.post('create_product', response={
    201: ProductOut,
    400: MessageOut
})
def create_product(request, payload: ProductCreate):
    try:
        product = Product.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, product




@commerce_controller.put('product/{product_id}', response={
    200: ProductOut,
    400: MessageOut
})
def update_product(request, product_id, payload: ProductUpdate):
    product = get_object_or_404(Product, id=product_id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return product

@commerce_controller.delete('product/delete/{id}')
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return {"success": True}


# bonus task
# create all crud operations for Label, Merchant, Vendor, Category

# * list of Label, Merchant, Vendor, Category
@bonus_controller.get('get_label', response={
    200: List[all_schemas.LabelOut],
})
def list_label(request):
    label = Label.objects.all()
    return label

@bonus_controller.get('get_merchant', response={
    200: List[all_schemas.MerchantOut],
})
def list_merchant(request):
    merchant = Merchant.objects.all()
    return merchant

@bonus_controller.get('get_vendor', response={
    200: List[all_schemas.VendorOut],
})
def list_vendor(request):
    vendor = Vendor.objects.all()
    return vendor



@bonus_controller.get('get_category', response={
    200: List[all_schemas.CategoryOut],
})
def list_category(request):
    category = Category.objects.all()
    return category

# done retrive


# * creation of Label, Merchant, Vendor, Category

@bonus_create_controller.post('create_label', response={
    201: all_schemas.LabelOut,
    400: MessageOut
})
def create_label(request, payload: all_schemas.LabelCreate):
    try:
        label = Label.objects.create(**payload.dict())
    except Label.DoesNotExist:
        return 400, {'detail': 'something wrong happened!'}

    return 201, label

@bonus_create_controller.post('create_merchant', response={
    201: all_schemas.MerchantOut,
    400: MessageOut
})
def create_merchant(request, payload: all_schemas.MerchantCreate):
    try:
        merchant = Label.objects.create(**payload.dict())
    except Merchant.DoesNotExist:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchant


@bonus_create_controller.post('create_vendor', response={
    201: all_schemas.LabelOut,
    400: MessageOut
})
def create_vendor(request, payload: all_schemas.VendorCreate):
    try:
        vendor = Vendor.objects.create(**payload.dict())
    except Vendor.DoesNotExist:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendor

@bonus_create_controller.post('create_category', response={
    201: all_schemas.CategoryOut,
    400: MessageOut
})
def create_category(request, payload: all_schemas.CategoryCreate):
    try:
        category = Category.objects.create(**payload.dict())
    except Category.DoesNotExist:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category




# the end of creation


@bonus_update_controller.put('label/{label_id}', response={
    200: all_schemas.LabelOut,
    400: MessageOut
})
def update_label(request, label_id, payload: all_schemas.LabelCreate):
    label = get_object_or_404(Label, id=label_id)
    for attr, value in payload.dict().items():
        setattr(label, attr, value)
    label.save()
    return label
@bonus_update_controller.put('merchant/{merchant_id}', response={
    200: all_schemas.MerchantOut,
    400: MessageOut
})
def update_merchant(request, merchant_id, payload: all_schemas.MerchantCreate):
    merchant = get_object_or_404(Merchant, id=merchant_id)
    for attr, value in payload.dict().items():
        setattr(merchant, attr, value)
    merchant.save()
    return merchant

@bonus_update_controller.put('vendor/{vendor_id}', response={
    200: all_schemas.VendorOut,
    400: MessageOut
})
def update_vendor(request, vendor_id, payload: all_schemas.VendorCreate):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return vendor


@bonus_update_controller.put('category/{category_id}', response={
    200: all_schemas.CategoryOut,
    400: MessageOut
})
def update_category(request, category_id, payload: all_schemas.CategoryCreate):
    category = get_object_or_404(Category, id=category_id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return category

# end of update

# * update of Label, Merchant, Vendor, Category
@bonus_remove_controller.delete('label/{id}')
def delete_label(request, id):
    label = get_object_or_404(Label, id=id)
    label.delete()
    return {"success": True}


@bonus_remove_controller.delete('merchant/{id}')
def delete_merchant(request, id):
    merchant = get_object_or_404(Merchant, id=id)
    merchant.delete()
    return {"success": True}


@bonus_remove_controller.delete('vendor/{id}')
def delete_vendor(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()
    return {"success": True}


@bonus_remove_controller.delete('category/{id}')
def delete_categoryr(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return {"success": True}
