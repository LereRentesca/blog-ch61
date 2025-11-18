from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView): #Class Based View
    #OOP - Inheritance 
    template_name = "pages/home.html" #Link our view to the html


class AboutPageView(TemplateView):
    template_name = "pages/about.html"