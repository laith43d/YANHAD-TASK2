from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import Category, Label, Merchant, Product, Vendor
from commerce.schemas import CategoryCreate, CategoryOut, CategoryUpdate, LabelCreate, LabelOut, LabelUpdate, MerchantCreate, MerchantOut, MerchantUpdate, ProductOut, ProductCreate, MessageOut, ProductUpdate, VendorCreate, VendorOut, VendorUpdate

commerce_controller = {'products': Router(tags=['products']),'label': Router(tags=['label']), 'merchant': Router(tags=['merchant']), 'vendor': Router(
    tags=['vendor']),'category': Router(tags=['category']), }

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
@commerce_controller['products'].get('products', response={
    200: List[ProductOut],
})
def list_products(request):
    products = Product.objects.all()
    # products = products.filter(name='tshirt')
    return products

# product by id
@commerce_controller['products'].get('products/{id}', response={
    200: ProductOut
})
def retrieve_product(request, id):
    return get_object_or_404(Product, id=id)

# add product
@commerce_controller['products'].post('products', response={
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
@commerce_controller['products'].put("product/{id}", response={200: ProductUpdate, 404: MessageOut})
def update_product(request, product_id, data: ProductUpdate):
    product = get_object_or_404(Product, id=product_id)
    for attr, value in data.dict().items():
        setattr(product, attr, value)
    product.save()
    return product

#delete product
@commerce_controller['products'].delete('product/{id}')
def delete_product(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()

# bonus task
# create all crud operations for Label, Merchant, Vendor, Category

# Label's crud operations

# all labels
@commerce_controller['label'].get('label', response={
    200: List[LabelOut],
})
def list_labels(request):
    label = Label.objects.all()
    return label

# label by id
@commerce_controller['label'].get('label/{id}', response={
    200: LabelOut
})
def retrieve_label(request, id):
    return get_object_or_404(Label, id=id)

# add label
@commerce_controller['label'].post('label', response={
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
@commerce_controller['label'].put("label/{id}", response={200: LabelUpdate, 404: MessageOut})
def update_label(request, id, data: LabelUpdate):
    label = get_object_or_404(Label, id=id)
    for attr, value in data.dict().items():
        setattr(label, attr, value)
    label.save()
    return label
    # return {"updated": True}

#delete label
@commerce_controller['label'].delete('label/{id}')
def delete_label(request,id):
    label = get_object_or_404(Label, id=id)
    label.delete()


# Merchant's crud operations

# all Merchants
@commerce_controller['merchant'].get('merchant', response={
    200: List[MerchantOut],
})
def list_merchants(request):
    merchant = Merchant.objects.all()
    return merchant

# Merchant by id
@commerce_controller['merchant'].get('merchant/{id}', response={
    200: MerchantOut
})
def retrieve_merchant(request, id):
    return get_object_or_404(Merchant, id=id)

# add Merchant
@commerce_controller['merchant'].post('merchant', response={
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

@commerce_controller['merchant'].put("merchant/{id}", response={200: MerchantUpdate, 404: MessageOut})
def update_merchant(request, id, data: MerchantUpdate):
    merchant = get_object_or_404(Merchant, id=id)
    for attr, value in data.dict().items():
        setattr(merchant, attr, value)
    merchant.save()
    return merchant


#delete Merchant
@commerce_controller['merchant'].delete('merchant/{id}')
def delete_merchant(request,id):
    merchant = get_object_or_404(Merchant, id=id)
    merchant.delete()


# Vendor's crud operations

# all vendors
@commerce_controller['vendor'].get('vendor', response={
    200: List[VendorOut],
})
def list_vendor(request):
    vendor = Vendor.objects.all()
    return vendor

# Vendor by id
@commerce_controller['vendor'].get('vendor/{id}', response={
    200: VendorOut
})
def retrieve_vendor(request, id):
    return get_object_or_404(Vendor, id=id)

# add Vendor
@commerce_controller['vendor'].post('vendor', response={
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


@commerce_controller['vendor'].put("vendor/{id}", response={200: VendorUpdate, 404: MessageOut})
def update_vendor(request, id, data: VendorUpdate):
    vendor = get_object_or_404(Vendor, id=id)
    for attr, value in data.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return vendor

#delete Vendor
@commerce_controller['vendor'].delete('vendor/{id}')
def delete_vendor(request,id):
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()


# Category's crud operations

# all category
@commerce_controller['category'].get('category', response={
    200: List[CategoryOut],
})
def list_category(request):
    category = Category.objects.all()
    return category

# Category by id
@commerce_controller['category'].get('category/{id}', response={
    200: CategoryOut
})
def retrieve_category(request, id):
    return get_object_or_404(Category, id=id)

# add Category
@commerce_controller['category'].post('category', response={
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

@commerce_controller['category'].put("category/{id}", response={200: CategoryUpdate, 404: MessageOut})
def update_category(request, id, data: CategoryUpdate):
    category = get_object_or_404(Category, id=id)
    for attr, value in data.dict().items():
        setattr(category, attr, value)
    category.save()
    return category

#delete Category
@commerce_controller['category'].delete('category/{id}')
def delete_category(request,id):
    category = get_object_or_404(Category, id=id)
    category.delete()
