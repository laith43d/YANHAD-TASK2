from typing import List
from pydantic import UUID4

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import Product, Category, Merchant, Vendor, Label
from commerce.schemas import CreateCategory, CreateLabel, CreateMerchant, CreateVendor, ProductOut, ProductCreate, MessageOut, MerchantOut, UpdateProduct, VendorOut, LabelOut, CategoryOut

commerce_controllers = {'products': Router(tags=['products']), 'merchant': Router(tags=['merchant']), 'vendor': Router(
    tags=['vendor']), 'label': Router(tags=['label']), 'category': Router(tags=['category']), }


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


@commerce_controllers['products'].get('products', response={
    200: List[ProductOut],
})
def list_products(request):
    products = Product.objects.all()
    # products = products.filter(name='tshirt')
    return products


@commerce_controllers['products'].get('products/{id}', response={
    200: ProductOut
})
def retrieve_product(request, id):
    return get_object_or_404(Product, id=id)


@commerce_controllers['products'].post('products', response={
    201: ProductOut,
    400: MessageOut
})
def create_product(request, payload: ProductCreate):
    try:
        product = Product.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, product


@commerce_controllers['products'].put('product/{id}', response={200: UpdateProduct})
def update_product(request, id: UUID4, payload: UpdateProduct):
    product = get_object_or_404(Product, id=id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()


@commerce_controllers['products'].delete('product/{id}')
def delete_product(request, id: UUID4):
    product = get_object_or_404(Product, id=id)
    product.delete()


# bonus task
# create all crud operations for Label, Merchant, Vendor, Category

# merchant CRUD
@commerce_controllers['merchant'].get('merchant/{id}', response={
    200: MerchantOut
})
def retrieve_merchant(request, id):
    return get_object_or_404(Merchant, id=id)


@commerce_controllers['merchant'].post('merchant', response={
    201: MerchantOut,
    400: MessageOut
})
def create_merchant(request, payload: CreateMerchant):
    try:
        merchant = Merchant.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchant


@commerce_controllers['merchant'].put('merchant/{id}', response={'200': CreateMerchant})
def update_merchant(request, id: UUID4, payload: CreateMerchant):
    merchant = get_object_or_404(Merchant, id=id)
    for attr, value in payload.dict().items():
        setattr(merchant, attr, value)
    merchant.save()


@commerce_controllers['merchant'].delete('merchant/{id}')
def delete_merchant(request, id: UUID4):
    merchant = get_object_or_404(Merchant, id=id)
    merchant.delete()

# Vendor CRUD


@commerce_controllers['vendor'].get('vendor/{id}', response={
    200: VendorOut
})
def retrieve_vendor(request, id):
    return get_object_or_404(Vendor, id=id)


@commerce_controllers['vendor'].post('vendor', response={
    201: VendorOut,
    400: MessageOut
})
def create_vendor(request, payload: CreateVendor):
    try:
        vendor = Vendor.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendor


@commerce_controllers['vendor'].put('vendor/{id}', response={'200': CreateVendor})
def update_vendor(request, id: UUID4, payload: CreateVendor):
    vendor = get_object_or_404(Vendor, id=id)
    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    vendor.save()


@commerce_controllers['vendor'].delete('vendor/{id}')
def delete_vendor(request, id: UUID4):
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()


# Label CRUD


@commerce_controllers['label'].get('label/{id}', response={
    200: LabelOut
})
def retrieve_label(request, id):
    return get_object_or_404(Label, id=id)


@commerce_controllers['label'].post('label', response={
    201: LabelOut,
    400: MessageOut
})
def create_label(request, payload: CreateLabel):
    try:
        label = Label.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, label


@commerce_controllers['label'].put('label/{id}', response={'200': CreateLabel})
def update_label(request, id: UUID4, payload: CreateLabel):
    label = get_object_or_404(Label, id=id)
    for attr, value in payload.dict().items():
        setattr(label, attr, value)
    label.save()


@commerce_controllers['label'].delete('label/{id}')
def delete_label(request, id: UUID4):
    label = get_object_or_404(Label, id=id)
    label.delete()


# category CRUD


@commerce_controllers['category'].get('category/{id}', response={
    200: CategoryOut
})
def retrieve_category(request, id):
    return get_object_or_404(Category, id=id)


@commerce_controllers['category'].post('category', response={
    201: CategoryOut,
    400: MessageOut
})
def create_category(request, payload: CreateCategory):
    try:
        category = Category.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category


@commerce_controllers['category'].put('category/{id}', response={'200': CreateCategory})
def update_category(request, id: UUID4, payload: CreateCategory):
    category = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()


@commerce_controllers['category'].delete('category/{id}')
def delete_category(request, id: UUID4):
    category = get_object_or_404(Category, id=id)
    category.delete()


''
