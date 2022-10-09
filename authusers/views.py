from multiprocessing import context
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


class HomeView(TemplateView):
    template_name = 'authusers/index.html'

@login_required
def special(request):
    return render(request, 'authusers/special.html')
    
class SpecialView(TemplateView):
    template_name = 'authusers/special.html'



# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         REGISTER                  / */
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


def register(request):
    form = UserCreationForm(request.POST or None) # if request method== post ise deyip yapıyorduk, şimdi tek satırla yaptık
    if form.is_valid():
        form.save()
        # that creates a new user
        # after creation of the user, want to authenticate it
        username = form.cleaned_data['username']  # zorunda değiliz
        password = form.cleaned_data['password1']  # zorunda değiliz
        # inspect the page and see the first password is password1, import authenticate . 
        # from django.contrib.auth import authenticate,login
        user = authenticate(username=username, password=password) #zorunda değiliz

        # want user to login right after registered, import login
        login(request, user) #zorunda değiliz
        # want to redirect to home page, import redirect
        return redirect('authusers:home')
    context={
        'form':form
    }
    return render(request, 'registration/register.html',context)


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /         PASSWORD CHANGE            /*/
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

def password_change(request):
    if request.method == 'POST':
        # We will use user change form this time
        # Import it
        form = UserChangeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('authusers:home')
    else:
        form = UserChangeForm()

    context = {
        'form': form
    }
    return render(request, "registration/password_change.html", context)


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /                                    /*/
# /* /             LOGOUT                 /*/
# /* /                                    /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
def user_logout(request):
    messages.success(request, "You Logged out!")
    logout(request)
    return redirect('authusers:home')

