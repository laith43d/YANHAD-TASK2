from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router

from commerce.models import Product, Label, Merchant, Vendor, Category
from commerce.schemas import ProductCreate, MessageOut, LabelOut, MerchantOut, VendorOut, CategoryOut

commerce_controller = Router(tags=['products'])


@commerce_controller.put('product/{id}')
def update_product(payload: ProductCreate):
    pro = get_object_or_404(Product, id=id)
    for attr, value in payload.dict().items():
        setattr(pro, attr, value)
    pro.save()
    return {"success": True}


# bonus task
# create all crud operations for Label, Merchant, Vendor, Category

@commerce_controller.get('Label', response={
    200: List[LabelOut],
})
def list_label():
    label = Label.objects.all()
    # label = Label.filter(name='tshirt')
    return label


@commerce_controller.get('Label/{id}', response={
    200: LabelOut
})
def retrieve_Label():
    return get_object_or_404(Label, id=id)


@commerce_controller.post('Label', response={
    201: LabelOut,
    400: MessageOut
})
def create_Label(payload: LabelOut):
    try:
        label = Label.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, label


@commerce_controller.put('Label/{id}')
def update_employee(payload: LabelOut):
    label = get_object_or_404(Label, id=id)
    for attr, value in payload.dict().items():
        setattr(label, attr, value)
    label.save()
    return {"success": True}


@commerce_controller.delete('Label/{id}')
def delete_label():
    label = get_object_or_404(Label, id=id)
    label.delete()

    return {"success": True}


@commerce_controller.get('Merchants', response={
    200: List[MerchantOut],
})
def list_Merchants():
    merchants = Merchant.objects.all()
    return merchants


@commerce_controller.get('Merchants/{id}', response={
    200: MerchantOut
})
def retrieve_Merchant():
    return get_object_or_404(Merchant, id=id)


@commerce_controller.post('Merchants', response={
    201: MerchantOut,
    400: MessageOut
})
def create_Merchant(payload: MerchantOut):
    try:
        merchant = Merchant.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchant


@commerce_controller.put('Merchant/{id}')
def update_employee(payload: MerchantOut):
    merchant = get_object_or_404(Merchant, id=id)
    for attr, value in payload.dict().items():
        setattr(merchant, attr, value)
    merchant.save()
    return {"success": True}


@commerce_controller.delete('merchant/{id}')
def delete_merchant():
    merchant = get_object_or_404(Merchant, id=id)
    merchant.delete()

    return {"success": True}


@commerce_controller.get('Vendor', response={
    200: List[VendorOut],
})
def list_Vendors():
    vendors = Vendor.objects.all()
    return vendors


@commerce_controller.get('Vendors/{id}', response={
    200: VendorOut
})
def retrieve_Vendor():
    return get_object_or_404(Vendor, id=id)


@commerce_controller.post('Vendors', response={
    201: VendorOut,
    400: MessageOut
})
def create_Vendor( payload: VendorOut):
    try:
        vendor = Vendor.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendor


@commerce_controller.put('Vendor/{id}')
def update_employee(payload: VendorOut):
    vendor = get_object_or_404(Vendor, id=id)
    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return {"success": True}


@commerce_controller.delete('Vendor/{id}')
def delete_Vendor():
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()

    return {"success": True}


@commerce_controller.get('Categorys', response={
    200: List[CategoryOut],
})
def list_Categorys():
    categorys = Category.objects.all()
    # Categorys = Categorys.filter(name='tshirt')
    return categorys


@commerce_controller.get('Categorys/{id}', response={
    200: CategoryOut
})
def retrieve_Category():
    return get_object_or_404(Category, id=id)


@commerce_controller.post('Categorys', response={
    201: CategoryOut,
    400: MessageOut
})
def create_Category(payload: CategoryOut):
    try:
        category = Category.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category


@commerce_controller.put('Category/{id}')
def update_employee(payload: CategoryOut):
    category = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return {"success": True}


@commerce_controller.delete('Category/{id}')
def delete_Category():
    category = get_object_or_404(Category, id=id)
    category.delete()

    return {"success": True}
