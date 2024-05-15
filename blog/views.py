from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.models import Blogpost


class BlogpostCreateView(CreateView):
    model = Blogpost
    fields = ('title', 'content', 'publication', 'preview')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
        return super().form_valid(form)


class BlogpostListView(ListView):
    model = Blogpost


class BlogpostUpdateView(UpdateView):
    model = Blogpost
    fields = ('title', 'content', 'publication', 'preview')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse_lazy('blog:view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновление блога'
        return context


class BlogpostDetailView(DetailView):
    model = Blogpost
    success_url = reverse_lazy('blog:blogpost_detail')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object
        return context


class BlogpostDeleteView(DeleteView):
    model = Blogpost
    success_url = reverse_lazy('blog:blog_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление блога'
        return context
