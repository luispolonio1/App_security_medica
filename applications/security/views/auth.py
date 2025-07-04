from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django .contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from applications.security.forms.registro import CustomUserCreationForm 

# ----------------- Cerrar Sesion -----------------
@login_required
def signout(request):
    logout(request)
    return redirect("security:signin")

# # ----------------- Iniciar Sesion -----------------
def signin(request):
    
    data = {"title": "Login",
            "title1": "Inicio de Sesión"}
    if request.method == "GET":
        # Obtener mensajes de éxito de la cola de mensajes
        success_messages = messages.get_messages(request)
        return render(request, "security/auth/signin.html", {
            "form": AuthenticationForm(),
            "success_messages": success_messages,  # Pasar mensajes de éxito a la plantilla
            **data
        })
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "security/auth/signin.html", {
                    "form": form,
                    "error": "El usuario o la contraseña son incorrectos",
                    **data
                })
        else:
            return render(request, "security/auth/signin.html", {
                "form": form,
                 "error": "Datos invalidos",
                **data
            })

# ----------------- Registrar Usuario -----------------
def signup(request):
    data = {
        "title": "Registro",
        "title1": "Crear Cuenta"
    }

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(4)
            user.save()
            login(request, user)
            return redirect("home")
        else:
            return render(request, "security/auth/signup.html", {"form": form, **data})
    else:
        form = CustomUserCreationForm()
        return render(request, "security/auth/signup.html", {"form": form, **data})


# grupos = {
#     "Administrador": 1,
#     "Gerente": 2,
#     "Vendedor": 3,
#     "Cliente": 4
# }