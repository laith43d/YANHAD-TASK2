
from typing import List
from uuid import UUID

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import Product, Category, Vendor, Merchant, Label
from commerce.schemas import ProductOut, ProductCreate, MessageOut, CategoryOut, CategoryIn, VendorOut, VendorIn, MerchantOut, MerchantIn, LabelOut, LabelIn

commerce_controller = Router(tags=['products'])
commerce_controller2 = Router(tags=['category'])
commerce_controller3 = Router(tags=['Vendor'])
commerce_controller4 = Router(tags=['Merchant'])
commerce_controller5 = Router(tags=['Label'])

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
def update_product(request,id, payload: ProductCreate):
        productUpdate = get_object_or_404(Product, id=id)
        for attr, value in payload.dict().items():
            setattr(productUpdate, attr, value)
        productUpdate.save()
        return {"success": True}




@commerce_controller.delete('product/{id}')
def delete_product(request ,id):
    productDelete = get_object_or_404(Product, id=id)
    productDelete.delete()
    return {"success": True}




@commerce_controller2.get('Category', response={
    200: List[CategoryOut],
})
def list_categories(request):
    categories = Category.objects.all()
    return categories


@commerce_controller2.get('categories/{id}', response={
    200: CategoryOut
})
def retrieve_category(request, id):
    return get_object_or_404(Category, id=id)


@commerce_controller2.post('category', response={
    201: CategoryOut,
    400: MessageOut
})
def create_category(request, payload: CategoryIn):
    try:
        category = Category.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category


@commerce_controller2.put('category/{id}')
def update_category(request,id, payload: CategoryIn):
        categoryUpdate = get_object_or_404(Category, id=id)
        for attr, value in payload.dict().items():
            setattr(categoryUpdate, attr, value)
        categoryUpdate.save()
        return {"success": True}




@commerce_controller2.delete('category/{id}')
def delete_category(request ,id):
    categoryDelete = get_object_or_404(Category, id=id)
    categoryDelete.delete()
    return {"success": True}


@commerce_controller3.get('Vendor', response={
    200: List[VendorOut],
})
def list_vendor(request):
    vendors = Vendor.objects.all()
    return vendors


@commerce_controller3.get('vendors/{id}', response={
    200: VendorOut
})
def retrieve_vendor(request, id):
    return get_object_or_404(Vendor, id=id)


@commerce_controller3.post('createVendor', response={
    201: VendorOut,
    400: MessageOut
})
def create_vendor(request, payload: VendorIn):
    try:
        vendorCreate = Vendor.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendorCreate


@commerce_controller3.put('vendor/{id}')
def update_vendor(request,id, payload: VendorIn):
        vendorUpdate = get_object_or_404(Vendor, id=id)
        for attr, value in payload.dict().items():
            setattr(vendorUpdate, attr, value)
        vendorUpdate.save()
        return {"success": True}




@commerce_controller3.delete('vender/{id}')
def delete_vender(request ,id):
    venderDelete = get_object_or_404(Vendor, id=id)
    venderDelete.delete()
    return {"success": True}

@commerce_controller4.get('Merchant', response={
    200: List[MerchantOut],
})
def list_merchant(request):
    merchants = Merchant.objects.all()
    return merchants


@commerce_controller4.get('Merchants/{id}', response={
    200: MerchantOut
})
def retrieve_merchant(request, id):
    return get_object_or_404(Merchant, id=id)


@commerce_controller4.post('createMerchant', response={
    201: MerchantOut,
    400: MessageOut
})
def create_merchant(request, payload: MerchantIn):
    try:
        merchantCreate = Merchant.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchantCreate


@commerce_controller4.put('updateMerchant/{id}')
def update_merchant(request,id, payload: MerchantIn):

            merchantUpdate = get_object_or_404(Merchant, id=id)
            for attr, value in payload.dict().items():
                setattr(merchantUpdate, attr, value)
            merchantUpdate.save()
            return {"success": True}





@commerce_controller4.delete('DeleteMerchant/{id}')
def delete_merchant(request ,id):
    merchantDelete = get_object_or_404(Merchant, id=id)
    merchantDelete.delete()
    return {"success": True}



@commerce_controller5.get('Label', response={
    200: List[LabelOut],
})
def list_label(request):
    labels = Label.objects.all()
    return labels


@commerce_controller5.get('Labels/{id}', response={
    200: LabelOut
})
def retrieve_label(request, id):
    return get_object_or_404(Label, id=id)


@commerce_controller5.post('label', response={
    201: LabelOut,
    400: MessageOut
})
def create_label(request, payload: LabelIn):
    try:
        labelCreat = Label.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, labelCreat


@commerce_controller5.put('label/{id}')
def update_label(request,id, payload: LabelIn):
        labelUpdate = get_object_or_404(Label, id=id)
        for attr, value in payload.dict().items():
            setattr(labelUpdate, attr, value)
        labelUpdate.save()
        return {"success": True}




@commerce_controller5.delete('label/{id}')
def delete_label(request ,id):
    labelDelete = get_object_or_404(Label, id=id)
    labelDelete.delete()
    return {"success": True}





# bonus task
# create all crud operations for Label, Merchant, Vendor, Category
