from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            request.session['first_name'] = form.cleaned_data['first_name']
            request.session['last_name'] = form.cleaned_data['last_name']
            request.session['college_id'] = form.cleaned_data['college_id']
            request.session['branch'] = form.cleaned_data['branch']
            request.session['college_name'] = form.cleaned_data['college_name']
            username = request.user.username if request.user.is_authenticated else "Anonymous"
            return redirect('student_info', username=username)
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_info(request, username):
    first_name = request.session.get('first_name', '')
    last_name = request.session.get('last_name', '')
    college_id = request.session.get('college_id', '')
    branch = request.session.get('branch', '')
    college_name = request.session.get('college_name', '')

    return render(request, 'student_info.html', {
        'first_name': first_name,
        'last_name': last_name,
        'college_id': college_id,
        'branch': branch,
        'college_name': college_name,
        'message': f"Inserted by {username}"
    })
