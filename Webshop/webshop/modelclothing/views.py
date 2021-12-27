from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ClothingForm
from .models import Clothing


def all_clothing_list(request):
    all_clothes = Clothing.objects.all()
    context = {'all_the_clothing': all_clothes}
    return render(request, 'clothing-list.html', context)


def clothing_list_filtered(request, **kwargs):
    filter = kwargs['pk']
    all_clothes_filtered = Clothing.objects.all().filter(type = filter);
    context = {'all_the_clothing': all_clothes_filtered}
    return render(request, 'clothing-list.html', context)


def clothing_detail(request, **kwargs):
    clothing_id = kwargs['pk']
    detailed_clothing = Clothing.objects.get(id=clothing_id)
    context = {'that_clothing': detailed_clothing}
    return render(request, 'clothing-detail.html', context)


def clothing_create(request):
    if request.method == 'POST':
        create_clothing_form = ClothingForm(request.POST)
        create_clothing_form.instance.user = request.user
        if create_clothing_form.is_valid():
            create_clothing_form.save()
        else:
            pass
        return redirect('clothing-list')

    else: 
        create_clothing_form = ClothingForm()
        context = {'form': create_clothing_form}
        return render(request, 'clothing-create.html', context)


def clothing_delete(request, **kwargs):
    clothing_id = kwargs['pk']
    Clothing.objects.filter(id=clothing_id).delete()
    return redirect('clothing-list')