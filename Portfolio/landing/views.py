from django.shortcuts import render
from django.http import HttpResponse

from .models import HeaderHome, ContentSlidebar, ContensBar, ContentServices, \
                    ContentWorks, SettingSidebar, ContentFooter

from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
'''def index(request):
    return render(request, 'landing/index.html')'''

class Index(ListView):
    model = HeaderHome
    #context_object_name = 'header_home'
    template_name = 'landing/index.html'
#    queryset = HeaderHome.objects.all()[0:1]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['header_home'] = HeaderHome.objects.all()[0:1]

        context['contens_bar'] = ContensBar.objects.all()[0:1]

        context['content_services'] = ContentServices.objects.all()[0:1]

        #Тут надо будет выбрать 5 проектов с галочкой публикации
        context['content_works'] = ContentWorks.objects.filter(publication__exact=True)[0:4]

        #Заголовок слайд бара
        context['setting_sidebar'] = SettingSidebar.objects.all()[0:1]

        #слайды слайд бара если публикация
        context['сontent_sidebar'] = ContentSlidebar.objects.filter(publication__exact=True)

        #контент футера
        context['сontent_footer'] = ContentFooter.objects.all()[0:1]

        return context

"""class Index(ListView):
    model = HeaderHome
    #context_object_name = 'header_home'
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['header_home'] = HeaderHome.objects.all()[:0]
        return context    """

class Work(DetailView):
    model = ContentWorks
    template_name = 'landing/works_details.html'
    context_object_name = 'work_item'


class Works(ListView):
    model = ContentWorks
    template_name = 'landing/works.html'
    context_object_name = 'works'
    paginate_by = 2
    allow_empty = False

    #def get_queryset(self):
    #    return ContentWorks.objects.filter(tags__slug=self.kwargs['pk'])