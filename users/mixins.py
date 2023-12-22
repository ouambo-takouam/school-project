from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class RedirectAuthenticatedUserMixin(AccessMixin):
    """
    Mixin pour rediriger un utilisateur déjà connecté.
    """
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # Redirection vers une autre URL si l'utilisateur est déjà connecté
            return redirect('school:home')
        return super().dispatch(request, *args, **kwargs)
