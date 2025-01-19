from django.http import Http404
from django.shortcuts import render
from todo.models import Todo


def todo_list(request):
    todo_list = Todo.objects.all().values_list('id', 'title')
    result = [{'id': todo[0], 'title': todo[1]} for i, todo in enumerate(todo_list)]

    return render(request, 'todo_list.html', {'data':result})


def todo_info(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
        info = {
            '제목': todo.title,
            '내용': todo.description,
            '시작 날짜': todo.start_date,
            '종료 날짜': todo.end_date,
            '완료 여부': todo.is_completed,
        }
        return render(request, 'todo_info.html', {'data':info})
    except Todo.DoesNotExist:
        return Http404('Todo does not exist')