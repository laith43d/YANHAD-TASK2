from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import Category, Label, Merchant, Product, Vendor
from commerce.schemas import CategoryCreate, CategoryOut, LabelCreate, LabelOut, MerchantCreate, MerchantOut, ProductOut, ProductCreate, MessageOut, VendorCreate, VendorOut

commerce_controller = Router(tags=['products'])

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

# all products
@commerce_controller.get('products', response={
    200: List[ProductOut],
})
def list_products(request):
    products = Product.objects.all()
    # products = products.filter(name='tshirt')
    return products

# product by id
@commerce_controller.get('products/{id}', response={
    200: ProductOut
})
def retrieve_product(request, id):
    return get_object_or_404(Product, id=id)

# add product
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

#update product
@commerce_controller.put('product/{id}',response={'200': ProductCreate})
def update_product(request, id, payload: ProductCreate):
    product = get_object_or_404(Product, id=id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    Product.save()
    # return {"updated": True}

#delete product
@commerce_controller.delete('product/{id}')
def delete_product(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()

# bonus task
# create all crud operations for Label, Merchant, Vendor, Category

# Label's crud operations

# all labels
@commerce_controller.get('label', response={
    200: List[LabelOut],
})
def list_labels(request):
    label = Label.objects.all()
    return label

# label by id
@commerce_controller.get('label/{id}', response={
    200: LabelOut
})
def retrieve_label(request, id):
    return get_object_or_404(Label, id=id)

# add label
@commerce_controller.post('label', response={
    201: LabelOut,
    400: MessageOut
})
def create_label(request, payload: LabelCreate):
    try:
        label = Label.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, label

#update label
@commerce_controller.put('label/{id}',response={'200': LabelCreate})
def update_label(request, id, payload: LabelCreate):
    label = get_object_or_404(Label, id=id)
    for attr, value in payload.dict().items():
        setattr(label, attr, value)
    Label.save()
    # return {"updated": True}

#delete product
@commerce_controller.delete('label/{id}')
def delete_label(request,id):
    label = get_object_or_404(Label, id=id)
    label.delete()


# Merchant's crud operations

# all Merchants
@commerce_controller.get('merchant', response={
    200: List[MerchantOut],
})
def list_merchants(request):
    merchant = Merchant.objects.all()
    return merchant

# Merchant by id
@commerce_controller.get('merchant/{id}', response={
    200: MerchantOut
})
def retrieve_merchant(request, id):
    return get_object_or_404(Merchant, id=id)

# add Merchant
@commerce_controller.post('merchant', response={
    201: MerchantOut,
    400: MessageOut
})
def create_merchant(request, payload: MerchantCreate):
    try:
        merchant = Merchant.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchant

#update Merchant
@commerce_controller.put('merchant/{id}',response={'200': MerchantCreate})
def update_merchant(request, id, payload: MerchantCreate):
    merchant = get_object_or_404(Merchant, id=id)
    for attr, value in payload.dict().items():
        setattr(merchant, attr, value)
    Merchant.save()
    # return {"updated": True}

#delete Merchant
@commerce_controller.delete('merchant/{id}')
def delete_merchant(request,id):
    merchant = get_object_or_404(Merchant, id=id)
    merchant.delete()


# Vendor's crud operations

# all vendors
@commerce_controller.get('vendor', response={
    200: List[VendorOut],
})
def list_vendor(request):
    vendor = Vendor.objects.all()
    return vendor

# Vendor by id
@commerce_controller.get('vendor/{id}', response={
    200: VendorOut
})
def retrieve_vendor(request, id):
    return get_object_or_404(Vendor, id=id)

# add Vendor
@commerce_controller.post('vendor', response={
    201: VendorOut,
    400: MessageOut
})
def create_vendor(request, payload: VendorCreate):
    try:
        vendor = Vendor.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendor

#update Vendor
@commerce_controller.put('vendor/{id}',response={'200': VendorCreate})
def update_vendor(request, id, payload: VendorCreate):
    vendor = get_object_or_404(Vendor, id=id)
    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    Vendor.save()
    # return {"updated": True}

#delete Vendor
@commerce_controller.delete('vendor/{id}')
def delete_vendor(request,id):
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()


# Category's crud operations

# all category
@commerce_controller.get('category', response={
    200: List[CategoryOut],
})
def list_category(request):
    category = Category.objects.all()
    return category

# Category by id
@commerce_controller.get('category/{id}', response={
    200: CategoryOut
})
def retrieve_category(request, id):
    return get_object_or_404(Category, id=id)

# add Category
@commerce_controller.post('category', response={
    201: CategoryOut,
    400: MessageOut
})
def create_category(request, payload: CategoryCreate):
    try:
        category = Category.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category

#update Category
@commerce_controller.put('category/{id}',response={'200': CategoryCreate})
def update_category(request, id, payload: CategoryCreate):
    category = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    Category.save()
    # return {"updated": True}

#delete Category
@commerce_controller.delete('category/{id}')
def delete_category(request,id):
    category = get_object_or_404(Category, id=id)
    category.delete()
