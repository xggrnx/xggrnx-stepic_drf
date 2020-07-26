from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from goods.models import Goods


@api_view(http_method_names=['GET'])
def goods_list(request):
    filters = {'min_price': 'price', 'min_weight': 'weight_grams'}

    if request.query_params:
        filter_key = list(request.query_params.keys())[0]
        filter_value = int(request.query_params.get(filter_key))
        if not filter_value or not filters.get(filter_key):
            return Response(status.HTTP_400_BAD_REQUEST)
        return Response(Goods.eq_gt_then(filters[filter_key], filter_value))

    return Response(Goods.all())


@api_view(http_method_names=['GET'])
def goods_detail(request, pk):
    recipient: dict = Goods.get_by_key('inner_id', pk)
    if recipient:
        return Response(recipient)
    return Response(status=status.HTTP_404_NOT_FOUND)
