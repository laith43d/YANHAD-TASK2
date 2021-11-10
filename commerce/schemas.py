from pydantic import UUID4

from ninja import Schema


# class OrderOut(Schema):
#     id: UUID4
#     user_id: UUID4
#     address_id: UUID4
#     total: int
#     status_id: UUID4
#     note: str
#     ref_code: str
#     ordered: bool
#     # items = models.ManyToManyField('commerce.Item', verbose_name='items', related_name='order')


# class ItemOut(Schema):
#     id: UUID4
#     user_id: UUID4
#     product_id: UUID4
#     item_qty: int
#     ordered: bool


# class OrderStatusOut(Schema):
#     id: UUID4
#     title: str
#     #     models.CharField('title', max_length=255, choices=[
#     #     (NEW, NEW),
#     #     (PROCESSING, PROCESSING),
#     #     (SHIPPED, SHIPPED),
#     #     (COMPLETED, COMPLETED),
#     #     (REFUNDED, REFUNDED),
#     # ])
#     is_default: bool


# class ProductImageOut(Schema):
#     id: UUID4
#     image: str
#     is_default_image: bool
#     product_id: UUID4


# class CityOut(Schema):
#     id: UUID4
#     name: str


# class AddressOut(Schema):
#     id: UUID4
#     user_id: UUID4
#     work_address: bool
#     address1: str
#     address2: str
#     city_id: UUID4
#     phone: str

class MessageOut(Schema):
    detail: str


class MerchantOut(Schema):
    id: UUID4
    name: str


class MerchantCreate(Schema):
    name: str


class MerchantIn(Schema):
    name: str


class VendorOut(Schema):
    id: UUID4
    name: str
    image: str


class VendorCreate(Schema):
    name: str
    image: str


class VendorIn(Schema):
    name: str
    image: str


class LabelOut(Schema):
    id: UUID4
    name: str


class LabelIn(Schema):
    name: str


class LabelCreate(Schema):
    name: str


class CategoryOut(Schema):
    id: UUID4
    name: str
    description: str
    image: str
    is_active: bool


class CategoryIn(Schema):
    name: str
    description: str
    image: str
    is_active: bool


class CategoryCreate(Schema):
    name: str
    description: str
    image: str
    is_active: bool


class ProductOut(Schema):
    id: UUID4
    name: str
    qty: int
    description: str
    cost: int
    price: int
    discounted_price: int
    vendor: VendorOut
    category: CategoryOut
    merchant: MerchantOut
    label: LabelOut


class ProductIn(Schema):
    name: str
    qty: int
    description: str
    cost: int
    price: int
    discounted_price: int


class ProductCreate(Schema):
    name: str
    qty: int
    description: str
    cost: int
    price: int
    discounted_price: int
    vendor_id: UUID4
    category_id: UUID4
    merchant_id: UUID4
    label_id: UUID4
