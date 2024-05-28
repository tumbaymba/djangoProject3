import random
import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from djangoProject3.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, PasswordRecoveryForm
from users.models import User
from django.http import HttpResponseRedirect


class RegisterMessageView(TemplateView):
    template_name = 'users/register_message.html'


class PasswordRecoveryMessageView(TemplateView):
    template_name = 'users/password_recovery_message.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'users/user_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:register_message')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        token = "".join([str(random.randint(0, 9)) for i in range(10)])
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/register/email_confirm/{token}/'
        send_mail(
            'Подтверждение почты',
            f'Перейдите по ссылке для подтверждения почты {url}',
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return HttpResponseRedirect('/users/login/')


class PasswordRecoveryView(TemplateView):
    model = User
    template_name = 'users/recovery_password.html'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('users:recovery_message')

    code = secrets.token_hex(8)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        code = PasswordRecoveryView.code
        user.set_password(PasswordRecoveryView.code)
        user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/login/'

        send_mail(
            'Восстановление пароля',
            f'Ваш новый пароль {code}, перейдите по ссылке {url}',
            EMAIL_HOST_USER,
            [user.email],
        )
        return HttpResponseRedirect('/users/recovery_password/message/')
