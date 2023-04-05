from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *


# Create your views here.
@login_required
def dashboard(request):
    context = {}
    return render(request, 'home.html', context)


@login_required
def add_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        doc_form = DocumentForm(request.POST, request.FILES)
        if form.is_valid() and doc_form.is_valid():
            resource = form.save(commit=False)
            resource.created_by = request.user
            resource.save()
            document = doc_form.cleaned_data['document']
            resource.document = document
            resource.save()
            print(f"Resource {resource.pk} saved")
            return redirect('resource_detail', pk=resource.pk)
        else:
            print("Form is invalid")
            print(form.errors)
            print(doc_form.errors)
    else:
        form = ResourceForm()
        doc_form = DocumentForm()
    return render(request, 'add_resource.html', {'form': form, 'doc_form': doc_form})

@login_required
def edit_resource(request, pk):
    resource = get_object_or_404(AcademicResource, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        doc_form = DocumentForm(request.POST, request.FILES, instance=resource)
        if form.is_valid() and doc_form.is_valid():
            resource = form.save(commit=False)
            resource.created_by = request.user
            resource.save()

            # Check if a new document is uploaded
            new_document = doc_form.cleaned_data.get('document')
            if new_document:
                resource.document = new_document

            resource.save()

            messages.success(request, 'Resource updated successfully.')
            return redirect('my_files')
    else:
        form = ResourceForm(instance=resource)
        # Update the doc_form instance with the existing document
        doc_form = DocumentForm(instance=resource, initial={'document': resource.document})

    return render(request, 'edit_resource.html', {'form': form, 'doc_form': doc_form, 'resource': resource})


@login_required
def review_resource(request, pk):
    resource = get_object_or_404(AcademicResource, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Review.objects.create(user=request.user, resource=resource, text=text)
    return redirect('resource_detail', pk=resource.pk)


@login_required
def resource_detail(request, pk):
    resource = get_object_or_404(AcademicResource, pk=pk)
    reviews = Review.objects.filter(resource=resource)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.resource = resource
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully')
            return redirect('resource_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'resource_detail.html', {'resource': resource, 'reviews': reviews, 'form': form})


@login_required
def add_review(request, resource_id):
    resource = AcademicResource.objects.get(id=resource_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.resource = resource
            review.save()
            messages.success(request, 'Your review has been added successfully.')
            return redirect('dashboard:resource_detail', resource.id)
    else:
        form = ReviewForm()
    return render(request, 'dashboard/add_review.html', {'resource': resource, 'form': form})


# Resource List
def resource_list(request):
    query = request.GET.get('q')
    if query:
        resources = AcademicResource.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)  | Q(school__icontains=query)  
        )
    else:
        resources = AcademicResource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})


@login_required
def delete_resource(request, pk):
    resource = get_object_or_404(AcademicResource, pk=pk, created_by=request.user)
    if request.method == 'POST':
        resource.delete()
        messages.success(request, 'Resource deleted successfully.')
        return redirect('my_files')
    return render(request, 'delete_resource.html', {'resource': resource})



@login_required
def my_files(request):
    resources = AcademicResource.objects.filter(created_by=request.user)
    return render(request, 'my_files.html', {'resources': resources})
