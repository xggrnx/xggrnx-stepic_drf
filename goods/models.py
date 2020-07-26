# Create your models here.

from lib.models import BaseModel


class GoodsModels(BaseModel):
    keys = ['name/title',
            'about/description',
            'price',
            'weight_grams/weight'
            ]


Goods = GoodsModels('goods')
