# Create your controllers here.
from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import Product, Category, Label, Vendor, Merchant
from commerce.schemas import ProductOut, ProductCreate, MessageOut, CategoryOut, CategoryCreate, LabelOut, LabelCreate, \
    VendorCreate, VendorOut, MerchantOut, MerchantCreate, ProductIn, CategoryIn, LabelIn, VendorIn, MerchantIn

commerce_controller = Router(tags=['products'])

"""
# three ways to send information to server with: path parameter, query parameter, body
required path parameter /api/resource/{id}
dynamic query parameter /api/resource/id=&name=
body { json }

# operation
# @commerce_controller.get('products')
# def list_products(request, id: int = 1):
#     return {
#         "name": "Taha"
#     }


# @commerce_controller.get('products/{id}')
# def list_products_by_id(request, id):
#     return {
#         "name": f"Taha {id}"
#     }


# @commerce_controller.post('products')
# def create_product(request, product_in: TahaSchema):
#     results = {
#         "name": product_in.name,
#         "specs": product_in.specs
#     }
#     return results


"""


@commerce_controller.get('products', response={200: List[ProductOut]})
def list_products(request):
    products = Product.objects.all()
    return products


@commerce_controller.get('products/{product_id}', response={200: ProductOut})
def retrieve_products(request, product_id: str):
    return get_object_or_404(Product, product_id=product_id)


@commerce_controller.post('products', response={201: ProductOut, 400: MessageOut})
def create_products(request, payload: ProductCreate):
    try:
        product = Product.objects.create(**payload.dict(), is_active=True, is_featured=True)
    except:
        return 400, {'detail': 'something wrong happened'}
    return 201, product


@commerce_controller.put('products/{product_id}')
def update_products(request, product_id: str, payload: ProductIn):
    product = get_object_or_404(Product, id=product_id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}


@commerce_controller.delete("products/{product_id}")
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True}


@commerce_controller.get('categories', response={200: List[CategoryOut]})
def list_categories(request):
    categories = Category.objects.all()
    return categories


@commerce_controller.get('categories/{category_id}', response={200: CategoryOut})
def retrieve_categories(request, category_id: str):
    return get_object_or_404(Category, category_id=category_id)


@commerce_controller.post('categories', response={201: CategoryOut, 400: MessageOut})
def create_categories(request, payload: CategoryCreate):
    try:
        category = Category.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened'}
    return 201, category


@commerce_controller.put('categories/{category_id}')
def update_categories(request, category_id: str, payload: CategoryIn):
    category = get_object_or_404(Category, id=category_id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return {"success": True}


@commerce_controller.delete("categories/{category_id}")
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {"success": True}


@commerce_controller.get('labels', response={200: List[LabelOut]})
def list_labels(request):
    labels = Label.objects.all()
    return labels


@commerce_controller.get('labels/{label_id}', response={200: LabelOut})
def retrieve_labels(request, label_id: str):
    return get_object_or_404(Label, label_id=label_id)


@commerce_controller.post('labels', response={201: LabelOut, 400: MessageOut})
def create_labels(request, payload: LabelCreate):
    try:
        label = Label.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened'}
    return 201, label


@commerce_controller.put('labels/{label_id}')
def update_labels(request, label_id: str, payload: LabelIn):
    label = get_object_or_404(Label, id=label_id)
    for attr, value in payload.dict().items():
        setattr(label, attr, value)
    label.save()
    return {"success": True}


@commerce_controller.delete("labels/{label_id}")
def delete_label(request, label_id):
    label = get_object_or_404(Label, id=label_id)
    label.delete()
    return {"success": True}


@commerce_controller.get('vendors', response={200: List[VendorOut]})
def list_vendors(request):
    vendors = Vendor.objects.all()
    return vendors


@commerce_controller.get('vendors/{vendor_id}', response={200: VendorOut})
def retrieve_vendors(request, vendor_id: str):
    return get_object_or_404(Vendor, vendor_id=vendor_id)


@commerce_controller.post('vendors', response={201: VendorOut, 400: MessageOut})
def create_vendors(request, payload: VendorCreate):
    try:
        vendor = Vendor.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened'}
    return 201, vendor


@commerce_controller.put('vendors/{vendor_id}')
def update_vendors(request, vendor_id: str, payload: VendorIn):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return {"success": True}


@commerce_controller.delete("vendors/{vendor_id}")
def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    vendor.delete()
    return {"success": True}


@commerce_controller.get('merchants', response={200: List[MerchantOut]})
def list_merchants(request):
    merchants = Merchant.objects.all()
    return merchants


@commerce_controller.get('merchants/{merchant_id}', response={200: MerchantOut})
def retrieve_merchants(request, merchant_id: str):
    return get_object_or_404(Merchant, merchant_id=merchant_id)


@commerce_controller.post('merchants', response={201: MerchantOut, 400: MessageOut})
def create_merchants(request, payload: MerchantCreate):
    try:
        merchant = Merchant.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened'}
    return 201, merchant


@commerce_controller.put('merchants/{merchant_id}')
def update_merchants(request, merchant_id: str, payload: MerchantIn):
    merchant = get_object_or_404(Merchant, id=merchant_id)
    for attr, value in payload.dict().items():
        setattr(merchant, attr, value)
    merchant.save()
    return {"success": True}


@commerce_controller.delete("merchants/{merchant_id}")
def delete_merchant(request, merchant_id):
    merchant = get_object_or_404(Merchant, id=merchant_id)
    merchant.delete()
    return {"success": True}
