from django.http  import HttpResponse,Http404
from django.shortcuts import render, redirect
from .forms import NewPostForm, UserUpdateForm, ProfileUpdateForm
from .models import Image
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def home(request):
    all_posts = Image.all_images()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                 request.FILES, 
                                 instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'your profile has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'all_posts': all_posts
    }
    return render(request, 'index.html', context)

def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.image_poster = request.user
            image.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'post_image.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                 request.FILES, 
                                 instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request, f'your profile has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)