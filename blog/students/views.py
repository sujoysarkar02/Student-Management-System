from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# Create your views here.

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()  # Corrected key to 'students'
    })

def view_student(request, id):
    # Fetch the student object or return 404 if not found
    student = get_object_or_404(Student, pk=id)

    # Render the student's details using a template
    return render(request, 'students/view_student.html', {'student': student})

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new student
            form.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),  # Empty form for new addition
                'success': True
            })
    else:
        form = StudentForm()
    
    return render(request, 'students/add.html', {
        'form': form
    })
        
def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))