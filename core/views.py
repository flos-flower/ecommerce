from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Item, Profile
from .forms import ItemForm, AddressForm

def is_valid_queryparam(param):
    return param != '' and param is not None

class HomeView(ListView):
    model = Item
    paginate_by = 4
    template_name = "home.html"


    def get_queryset(self):
        cat_query = self.request.GET.get('category')
        query = self.request.GET.get('q')
        object_list = Item.objects.all()
        if is_valid_queryparam(query):        
            object_list = object_list.filter(title__icontains=query)
        if is_valid_queryparam(cat_query) and cat_query != 'Choose..':
            object_list = object_list.filter(category=cat_query)
        return object_list


class account_info(DetailView):
    model = Profile
    template_name = 'account_info.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'

def add_item(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        address_form = AddressForm(request.POST)
        if all((item_form.is_valid(), address_form.is_valid())):
            address = address_form.save()
            item = item_form.save(commit=False) 
            item.img = request.FILES.get('img', 'images/default.jpg')
            item.location = address
            item.user = request.user
            item.save()
            return redirect('core:home')
    else:
        item_form = ItemForm()
        address_form = AddressForm()
    context = {
        'items': Item.objects.all(),
        'item_form': item_form,
        'address_form': address_form
    }
    return render(request, 'item_create.html', context)

def delete_item(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return redirect('core:home')