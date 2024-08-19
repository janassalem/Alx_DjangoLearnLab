from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def view_content(request):
    # View logic here
    return render(request, 'bookshelf/view_content.html')

@permission_required('bookshelf.can_create', raise_exception=True)
def create_content(request):
    # Create logic here
    return render(request, 'bookshelf/create_content.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_content(request):
    # Edit logic here
    return render(request, 'bookshelf/edit_content.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_content(request):
    # Delete logic here
    return render(request, 'bookshelf/delete_content.html')