from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router
from commerce.models import Product
from commerce.schemas import ProductOut, ProductCreate, MessageOut

commerce_controller = Router(tags=['products'])



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
def update_product(request,id,payload:ProductCreate):
    updateProduct=get_object_or_404(Product,id=id)
    for attr,value in payload.dict().items():
        setattr(updateProduct, attr, value)       
    updateProduct.save()  


@commerce_controller.delete('product/{id}')
def delete_product(request):
    get_object_or_404(Product,id=id)
    Product.delete()


