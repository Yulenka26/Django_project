from django.shortcuts import render
from project.feedback_app.forms import FeedbackForm
from project.feedback_app.models import Feedback
from django.shortcuts import redirect

def feedback_page(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Feedback.objects.create(**data)

            return redirect("blog:index")
    else:
        form = FeedbackForm()

    return render(request, "feedback_app/feedback_page.html", context={"form": form})
