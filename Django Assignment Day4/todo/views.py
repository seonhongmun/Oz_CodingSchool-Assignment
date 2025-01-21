from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from todo.forms import TodoForm, TodoUpdateForm #Form 파일 생성 잊지 말기~
from todo.models import Todo

@login_required
def todo_list(request):
    todo_list = Todo.objects.filter(user=request.user).order_by('created_at')
    q = request.GET.get('q') # GET 요청으로부터 q에 담긴 쿼리 파라미터를 가져온다.
    # 페이지네이션
    if q:
        todo_list = todo_list.filter(Q(title__icontains=q)|Q(description__icontains=q))
    paginator = Paginator(todo_list, 10) # 한 페이지당 10개씩 가져온다.
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        'page_object': page_object
    }
    print(page_object)
    return render(request, 'todo_list.html', context)


@login_required
def todo_info(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    context ={
        'todo': todo.__dict__
    }
    return render(request, 'todo_info.html', context)

@login_required
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect(reverse('todo_info', kwargs={'todo_id':todo.pk}))
    context = {
        'form': form,
    }
    return render(request, 'todo_create.html', context)


@login_required
def todo_update(request, todo_id):
    todo = get_object_or_404(Todo , id=todo_id, user=request.user)
    form = TodoUpdateForm(request.POST or None, instance=todo)
    if form.is_valid():
        todo = form.save()
        return redirect(reverse('todo_info', kwargs={'todo_id':todo.pk}))
    context = {
        'form': form
    }
    return render(request, 'todo_update.html', context)

@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect(reverse('todo_list'))