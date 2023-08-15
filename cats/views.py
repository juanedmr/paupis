from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from cats.models import Cat, Breed
from cats.forms import BreedForm

# Create your views here.


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Breed.objects.all().count()
        al = Cat.objects.all()
        
        ctx = {'make_count': mc, 'cat_list': al}
        print(ctx)
        return render(request, 'cats/cats_list.html', ctx)


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Breed.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'cats/make_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/make_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request):
        form = BreedForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        make = form.save()
        return redirect(self.success_url)


# BreedUpdate has code to implement the get/post/validate/store flow
# CatUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/make_form.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=make)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance=make)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)


class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/make_confirm_delete.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=make)
        ctx = {'make': make}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview