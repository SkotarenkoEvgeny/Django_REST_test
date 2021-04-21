from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView,
    UpdateView,
    )

from .models import Course


class HomePageView(ListView):
    template_name = 'courses_app/home.html'
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        rav_date = Course.objects.all()
        context['start_date'] = rav_date.values_list(
            'start_date', flat=True
            ).distinct()
        context['end_date'] = rav_date.values_list(
            'end_date', flat=True
            ).distinct()
        return context

    def get_queryset(self):
        queryset = Course.objects.all()
        search_name = self.request.GET.get("search_name", None)
        search_start_date = self.request.GET.get("search_start_date", None)
        search_end_date = self.request.GET.get("search_end_date", None)
        if search_name:
            queryset = queryset.filter(name__contains=search_name)
        if search_start_date:
            queryset = queryset.filter(
                start_date=datetime.strptime(
                    search_start_date, "%B %d, %Y"
                    ).date()
                )
        if search_end_date:
            queryset = queryset.filter(
                end_date=datetime.strptime(
                    search_end_date, "%B %d, %Y"
                    ).date()
                )

        return queryset


class CourseDetailView(DetailView):
    template_name = 'courses_app/detail.html'
    model = Course
    context_object_name = 'course'


class CourseUpdateView(UpdateView):
    template_name = 'courses_app/form.html'
    model = Course
    context_object_name = 'course'
    fields = '__all__'
    success_url = reverse_lazy('home')


class CourseCreateView(CreateView):
    template_name = 'courses_app/form.html'
    model = Course
    context_object_name = 'course'
    fields = '__all__'
    success_url = reverse_lazy('home')


class CourseDeleteView(DeleteView):
    success_url = reverse_lazy('home')
    model = Course
    context_object_name = 'course'
    fields = '__all__'
