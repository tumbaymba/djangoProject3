from django.contrib.auth.models import User
u = User.objects.get(username='tumba')
u.set_password('admin')
u.save()
