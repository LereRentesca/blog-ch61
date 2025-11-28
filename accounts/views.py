from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView): # POST request
    template_name = "registration/signup.html"

    #form_class is an attribute from the CreateView generic class that allow us to let django know from any another
    # form class to handle the creation of objects
    form_class = UserCreationForm
    success_url = reverse_lazy("home")