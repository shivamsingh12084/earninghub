from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AuthenticationPageView(TemplateView): # new
    template_name = 'authentication_page.html'

class SearchPageView(TemplateView):
    template_name = 'search.html'