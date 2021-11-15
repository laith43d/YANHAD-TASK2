import datetime

from ninja import Schema
from pydantic import UUID4


class MessageOut(Schema):
    detail: str

class HumanQualities(Schema):
    age: int
    height: int


class RuaaSchema(Schema):
    name: str
    specs: HumanQualities

class CategoryOut(Schema):
    id: UUID4
    name: str
    description: str
    image: str

class LabelOut(Schema):
    id: UUID4
    name: str

class MerchantOut(Schema):
    id: UUID4
    name: str
    created: datetime.datetime
    updated: datetime.datetime

class VendorOut(Schema):
    id: UUID4
    name: str
    image: str


class ProductOut(Schema):
    id: UUID4
    is_featured: bool
    name: str
    description: str
    qty: int
    price: int
    discounted_price: int
    category: CategoryOut
    vendor: VendorOut
    merchant: MerchantOut
    label: LabelOut
    created: datetime.datetime
    updated: datetime.datetime

class ProductCreate(Schema):
    is_featured: bool
    name: str
    description: str
    qty: int
    cost: int
    price: int
    discounted_price: int
    category_id: UUID4
    vendor_id: UUID4
    merchant_id: UUID4
    label_id: UUID4

class ProductUpdate(Schema):
    is_featured: bool
    name: str
    description: str
    qty: int
    cost: int
    price: int
    discounted_price: int

class LabelCreate(Schema):
    id: UUID4
    name: str
class LabelUpdate(Schema):
    name: str

class MerchantCreate(Schema):
    id: UUID4
    name: str
    image: str
    slug: str

class MerchantUpdate(Schema):
    name: str

class VendorCreate(Schema):
    id: UUID4
    name: str

class VendorUpdate(Schema):
    name: str

class CategoryCreate(Schema):
    id: UUID4
    name: str
    description: str
    image: str
    is_active: bool

class CategoryUpdate(Schema):
    name: str
    description: str
    image: str
    is_active: bool