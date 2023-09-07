from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

class ClientHomeView(TemplateView):
    template_name = "clienthome.html"

class ClientSeviceView(TemplateView):
    template_name = "clientservice.html"

class ClientAboutView(ListView):
    template_name = "clientabout.html"
    model = Category
    context_object_name = 'categories'

class ClientContactView(TemplateView):
    template_name = "clientcontact.html"

class ClientNewsListView(ListView):
    template_name = "clientnewslist.html"
    model = News
    context_object_name = 'news'

class ClientNewsDetailView(DetailView):
    template_name = "clientnewsdetail.html"
    model = News
    context_object_name = 'newsdetail'

class AdminRequiredMixin(object):
    def dispatch (self, request, *args, **kwargs):
        try:
            self.user = request.user
            if self.user.is_superuser and self.user.is_active:
                print("Admin Only Passed")
            else:
                return redirect("everestapp: adminlogin"+"?next="+ request.get_full_patch())
        except Exception as e:
            print(e)
            return redirect("everestapp:adminlogin")
        return super().dispatch(request,*args, *kwargs)

class AdminLoginView(FormView):
    template_name = "adminlogin.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy("everestapp:clienthome")

    def form_valid(self,form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            try:
                username = user.username
                login(self.request, user)

            except Exception as e:
                print(e)
                return render(self.request,self.template_name,{"form":form,"error":"Invalid Credentials..."})
        else:
            return render(self.request,self.template_name, {"form": form,"error":"Invalid Credentials..."})

        return super().form_valid(form)

class AdminLogoutView (View):
    success_message = "Logged out successfully"

    def get(self,request,**kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect('everestapp:clienthome')
        else:
            pass


class ClientNewsCreateView(AdminRequiredMixin,CreateView):
    template_name = "clientnewscreate.html"
    form_class = ClientNewsCreateForm
    model = News
    success_url = reverse_lazy("everestapp:clienthome")

class ClientNewsUpdateView(AdminRequiredMixin,UpdateView):
    template_name= "clientnewscreate.html"
    form_class = ClientNewsCreateForm
    model = News
    success_url = reverse_lazy("everestapp:clienthome")

class ClientNewsDeleteView(AdminRequiredMixin,DeleteView):
    template_name = "clientnewsdelete.html"
    model = News
    context_object_name = "news"
    success_url = reverse_lazy("everestapp:clienthome")



