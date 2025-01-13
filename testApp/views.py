from django.http import JsonResponse
from .models import Item
from .validators import ProductValidator
from pydantic import ValidationError


# Create your views here.

# Create Item
def create_item(request):
    if request.method == 'POST':
        data = {
           'name' : request.POST.get('name'), 
           'price' : request.POST.get('price')
        } 
        product = ProductValidator(**data)
        item = Item.objects.create(**product.dict())
        return JsonResponse({'message': f'Item {item.name} created'}, status=201)

# Read Item
def get_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        return JsonResponse({'name': item.name, 'price': str(item.price)}, status=200)
    except Item.DoesNotExist:
        return JsonResponse({'message': 'Item not found'}, status=404)
    
# Update Item
def update_item(request, item_id):
    item =  Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name', item.name)
        item.price = request.POST.get('price', item.price)
        item.save()
    return JsonResponse({'message': f'Item {item.name} updated'}, status=200)

# Delete Item
def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return JsonResponse({'message': 'Item deleted successfully!'}, status=204)