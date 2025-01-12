from django.contrib.auth import get_user_model,logout
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import redirect
class EmailBackend(ModelBackend):
    @staticmethod
    def authenticate(request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
    
    @staticmethod
    def ulogout(request):
        logout(request=request)
        return redirect('index')