from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import Product, Label, Merchant, Vendor, Category
from commerce.schemas import ProductOut, ProductCreate, MessageOut, ProductUpdate, LabelOut, LabelCreate, MerchantOut, \
    MerchantCreate, VendorCreate, VendorOut, CategoryOut, CategoryCreate

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
        return 201, product
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.put('product/{id}', response={
    200: ProductUpdate,
    400: MessageOut
})
def update_product(request, pid, payload: ProductUpdate):
    try:
        Product.objects.filter(id=pid).update(**payload.dict(), id=pid)
        return 200, {"status": "ok"}
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.delete('product/{id}')
def delete_product(request, pid):
    try:
        Product.objects.get(id=pid).delete()
        return 200, {"status": "deleted"}
    except:
        return 400, {"detail": "something went wrong !"}


# bonus task
# create all crud operations for Label, Merchant, Vendor, Category


# Label model
@commerce_controller.get('label', response={
    200: List[LabelOut],
})
def list_labels(request):
    labels = Product.objects.all()
    return labels


@commerce_controller.get('label/{id}', response={
    200: LabelOut
})
def retrieve_label(request, id):
    return get_object_or_404(Label, id=id)


@commerce_controller.post('label', response={
    201: LabelOut,
    400: MessageOut
})
def create_label(request, payload: LabelCreate):
    try:
        label = Label.objects.create(**payload.dict(), is_active=True)
        return 201, label
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.put('label/{id}', response={
    200: LabelCreate,
    400: MessageOut
})
def update_label(request, pid, payload: LabelCreate):
    try:
        Label.objects.filter(id=pid).update(**payload.dict(), id=pid)
        return 200, {"status": "ok"}
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.delete('label/{id}')
def delete_label(request, pid):
    try:
        Label.objects.get(id=pid).delete()
        return 200, {"status": "deleted"}
    except:
        return 400, {"detail": "something went wrong !"}


# Merchant model
@commerce_controller.get('merchant', response={
    200: List[MerchantOut],
})
def list_merchant(request):
    merchant = Merchant.objects.all()
    return merchant


@commerce_controller.get('merchant/{id}', response={
    200: MerchantOut
})
def retrieve_merchant(request, id):
    return get_object_or_404(Label, id=id)


@commerce_controller.post('merchant', response={
    201: MerchantOut,
    400: MessageOut
})
def create_merchant(request, payload: MerchantCreate):
    try:
        merchant = Merchant.objects.create(**payload.dict(), is_active=True)
        return 201, merchant
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.put('merchant/{id}', response={
    200: MerchantCreate,
    400: MessageOut
})
def update_merchant(request, pid, payload: MerchantCreate):
    try:
        Merchant.objects.filter(id=pid).update(**payload.dict(), id=pid)
        return 200, {"status": "ok"}
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.delete('merchant/{id}')
def delete_merchant(request, pid):
    try:
        Merchant.objects.get(id=pid).delete()
        return 200, {"status": "deleted"}
    except:
        return 400, {"detail": "something went wrong !"}


# Vendor model
@commerce_controller.get('vendor', response={
    200: List[VendorOut],
})
def list_merchant(request):
    vendor = Vendor.objects.all()
    return vendor


@commerce_controller.get('vendor/{id}', response={
    200: VendorOut
})
def retrieve_vendor(request, id):
    return get_object_or_404(Vendor, id=id)


@commerce_controller.post('vendor', response={
    201: VendorOut,
    400: MessageOut
})
def create_vendor(request, payload: VendorCreate):
    try:
        vendor = Vendor.objects.create(**payload.dict(), is_active=True)
        return 201, vendor
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.put('vendor/{id}', response={
    200: VendorCreate,
    400: MessageOut
})
def update_vendor(request, pid, payload: VendorCreate):
    try:
        Vendor.objects.filter(id=pid).update(**payload.dict(), id=pid)
        return 200, {"status": "ok"}
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.delete('vendor/{id}')
def delete_vendor(request, pid):
    try:
        Vendor.objects.get(id=pid).delete()
        return 200, {"status": "deleted"}
    except:
        return 400, {"detail": "something went wrong !"}


# Category model
@commerce_controller.get('category', response={
    200: List[CategoryOut],
})
def list_category(request):
    category = Category.objects.all()
    return category


@commerce_controller.get('category/{id}', response={
    200: CategoryOut
})
def retrieve_category(request, id):
    return get_object_or_404(Category, id=id)


@commerce_controller.post('category', response={
    201: CategoryOut,
    400: MessageOut
})
def create_category(request, payload: CategoryCreate):
    try:
        category = Category.objects.create(**payload.dict(), is_active=True)
        return 201, category
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.put('category/{id}', response={
    200: CategoryCreate,
    400: MessageOut
})
def update_category(request, pid, payload: CategoryCreate):
    try:
        Category.objects.filter(id=pid).update(**payload.dict(), id=pid)
        return 200, {"status": "ok"}
    except:
        return 400, {"detail": "something went wrong !"}


@commerce_controller.delete('category/{id}')
def delete_category(request, pid):
    try:
        Category.objects.get(id=pid).delete()
        return 200, {"status": "deleted"}
    except:
        return 400, {"detail": "something went wrong !"}
