from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import Product, Label, Merchant, Vendor, Category
from commerce.schemas import ProductOut, ProductCreate, MessageOut, LabelOut, MerchantOut, VendorOut, CategoryOut, \
    CategoryIn, VendorIn, MerchantIn,LabelIn

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


@commerce_controller.get('products', response={
    200: List[ProductOut],
})
def list_products(request):
    products = Product.objects.all()
    # products = products.filter(name='tshirt')
    return products


@commerce_controller.get('products/{id}', response={
    200: ProductOut
})
def retrieve_product(request, id):
    return get_object_or_404(Product, id=id)


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


@commerce_controller.put('product/{id}')
def update_product(request, id, payload: ProductCreate):
    product = get_object_or_404(Product, id=id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}


@commerce_controller.delete('product/{id}')
def delete_product(request, id):
    employee = get_object_or_404(Product, id=id)
    Product.delete()
    return {"success": True}

# bonus task
# create all crud operations for Label, Merchant, Vendor, Category
@commerce_controller.get('labels', response={
    200: List[LabelOut],
})
def list_labels(request):
    label = Label.objects.all()
    return label

@commerce_controller.get('labels/{id}', response={
    200: LabelOut
})
def retrieve_label(request, id):
    return get_object_or_404(Label, id=id)


@commerce_controller.post('labels', response={
    201: LabelOut,
    400: MessageOut
})
def create_label(request, payload: LabelIn):
    try:
        label = Label.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, label

@commerce_controller.put('label/{id}')
def update_label(request,id,payload:LabelIn):
    label = get_object_or_404(Label, id=id)
    for attr, value in payload.dict().items():
        setattr(label, attr, value)
    label.save()
    return {"success": True}


@commerce_controller.delete('label/{id}')
def delete_label(request,id):
    label = get_object_or_404(Label, id=id)
    label.delete()
    return {"success": True}


@commerce_controller.get('merchants', response={
    200: List[MerchantOut],
})
def list_merchants(request):
    merchant = Merchant.objects.all()
    return merchant


@commerce_controller.get('merchants/{id}', response={
    200: MerchantOut
})
def retrieve_merchant(request, id):
    return get_object_or_404(Merchant, id=id)


@commerce_controller.post('merchants', response={
    201: MerchantOut,
    400: MessageOut
})
def create_merchant(request, payload: MerchantIn):
    try:
        merchant = Merchant.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchant


@commerce_controller.put('merchant/{id}')
def update_merchant(request,id,payload:MerchantIn):
    merchant = get_object_or_404(Merchant, id=id)
    for attr, value in payload.dict().items():
        setattr(merchant, attr, value)
    merchant.save()
    return {"success": True}


@commerce_controller.delete('merchant/{id}')
def delete_merchant(request,id):
    merchant = get_object_or_404(Merchant, id=id)
    merchant.delete()
    return {"success": True}


@commerce_controller.get('vendors', response={
    200: List[VendorOut],
})
def list_vendors(request):
    vendor = Vendor.objects.all()
    return vendor


@commerce_controller.get('vendors/{id}', response={
    200: VendorOut
})
def retrieve_vendor(request, id):
    return get_object_or_404(Vendor, id=id)


@commerce_controller.post('vendors', response={
    201: VendorOut,
    400: MessageOut
})
def create_vendor(request, payload: VendorIn):
    try:
        vendor = Vendor.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendor


@commerce_controller.put('vendor/{id}')
def update_vendor(request,id,payload:VendorIn):
    vendor = get_object_or_404(Vendor, id=id)
    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return {"success": True}


@commerce_controller.delete('vendor/{id}')
def delete_vendor(request,id):
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()
    return {"success": True}


@commerce_controller.get('categorys', response={
    200: List[CategoryOut],
})
def list_category(request):
    category = Category.objects.all()
    return category


@commerce_controller.get('categorys/{id}', response={
    200: CategoryOut
})
def retrieve_category(request, id):
    return get_object_or_404(Category, id=id)


@commerce_controller.post('categorys', response={
    201: CategoryOut,
    400: MessageOut
})
def create_category(request, payload: CategoryIn):
    try:
        category = Category.objects.create(**payload.dict(),is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category


@commerce_controller.put('category/{id}')
def update_category(request,id,payload:CategoryIn):
    category = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return {"success": True}


@commerce_controller.delete('category/{id}')
def delete_category(request,id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return {"success": True}
