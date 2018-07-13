from django.shortcuts import render, get_object_or_404, redirect
from .models import Character
from .forms import CharacterForm

# Exibe todos os personagens
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'app/character_list.html', {'characters':characters})


# Exibe todos os detalhes de um personagem
def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'app/character_detail.html', {'character':character})


# Permite adicionar um novo personagem
def character_new(request):
    if request.method == "POST":
        form = CharacterForm(request.POST, request.FILES)

        if form.is_valid():
            #character = form.save(commit=False)
            #character.image = form.cleaned_data['image']
            #character.save()
            character = form.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()

    return render(request, 'app/character_new.html', {'form':form})


# Permite editar as informacoes de um personagem
def character_edit(request, pk):
    character = get_object_or_404(Character, pk=pk)

    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)

        if form.is_valid():
            character = form.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm(instance=character)

    return render(request, 'app/character_edit.html', {'form':form})

# Permite excluir personagem
def character_remove(request, pk):
    character = get_object_or_404(Character, pk=pk)
    character.delete()
    return redirect('character_list')