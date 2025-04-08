from django.shortcuts import render, get_object_or_404, redirect
import markdown
from django.utils.safestring import mark_safe
import os
from .models import Todo
from .forms import TodoForm

# Create your views here.
def mainpage(request):
    md_file_path = 'main/Week2_Study.md'

    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()

    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
    
    context = {
        'generation': 13,
        'info': {'weather': '좋음', 'feeling': '배고픔(?)', 'note': '아기사자 화이팅!'},
        'shortKeys': [
            '들여쓰기: Tab',
            '내어쓰기: Shift + Tab',
            '주석 처리: 윈도우 - Ctrl + /, 맥 - command + /',
            '자동 정렬: Shift + Alt + F or Ctrl + K + F',
            '한 줄 이동: Alt + 방향키(위/아래)',
            '한 줄 삭제: Ctrl + Shift + k or Ctrl + x',
            '같은 단어 전체 선택: Ctrl + Shift + L'
        ],
        'content':mark_safe(html_content)
    }

    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')

def todo_list(request):
    form = TodoForm()
    todos = Todo.objects.filter(is_done=False).order_by('-created_at')
    done_tasks = Todo.objects.filter(is_done=True).order_by('-created_at')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secondpage')
        
    return render(request, 'main/secondpage.html', {
        'form': form,
        'todos': todos,
        'done_tasks': done_tasks
    })

def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.is_done = True
    todo.save()
    return redirect('secondpage')

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo,  id=todo_id)
    todo.delete()
    return redirect('secondpage')