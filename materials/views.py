from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Material
from .forms import MaterialForm

def materials_list(request):
    materials = Material.objects.order_by('-created_at')
    return render(request, 'materials/materials_list.html', {'materials': materials})

def is_moderator_or_admin(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_moderator_or_admin)
def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.created_by = request.user
            material.save()
            return redirect('materials_list')
    else:
        form = MaterialForm()
    return render(request, 'materials/material_form.html', {'form': form, 'title': 'Додати матеріал'})

@login_required
@user_passes_test(is_moderator_or_admin)
def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('materials_list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'materials/material_form.html', {'form': form, 'title': 'Редагувати матеріал'})

@login_required
@user_passes_test(is_moderator_or_admin)
def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    material.delete()
    return redirect('materials_list')
