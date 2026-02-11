from django.http import HttpResponseForbidden


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return HttpResponseForbidden("У вас нет прав!")
        return super().dispatch(request, *args, **kwargs)
