from django.shortcuts import render, redirect
from blog.forms import ProfileDetailForms
from blog.models import ProfileDetails

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from blog.decorators import allowed_users

# Create your views here.


@login_required(login_url='login')
@allowed_users(allowed_roles=['author', 'basic'])
def Profile(request):

    author = request.user

    profile = ProfileDetails.objects.get(user=author)

    if profile:

        form = ProfileDetailForms(instance=profile)
        if request.method == 'POST':
            form = ProfileDetailForms(
                request.POST, request.FILES, instance=profile)

            if form.is_valid():

                form = form.save(commit=False)
                form.user = request.user
                form.save()
                messages.success(
                    request, 'Updated Profile Details Successfully')

                return redirect('status')

        else:
            form = ProfileDetailForms(instance=profile)

            context = {
                "form": form, "profile": profile
            }

            return render(request, 'account/profile.html', context)

    else:

        form = ProfileDetailForms()

        if request.method == 'POST':
            form = ProfileDetailForms(
                request.POST, request.FILES)

            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user.author
                form.save()
                messages.success(
                    request, 'Updated Profile Details Successfully')

                return redirect('status')

        context = {
            "form": form, "profile": profile
        }

        return render(request, 'account/profile.html', context)
