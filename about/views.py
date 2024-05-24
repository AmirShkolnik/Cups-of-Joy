from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm
# Create your views here.


def about_me(us):
    """
    Renders the most recent information on the website author
    and allows user collaboration uss.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
        ``contact_form``
            An instance of :form:`about.contactForm`.
    **Template**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()
    if us.method == "POST":
        contact_form = ContactForm(data=us.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.read = False
            contact.save()
            messages.add_message(
                us, messages.SUCCESS,
                'We got your message! '
                'We endeavor to respond within 2 working days.'
            )
            contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm()

    return render(
        us,
        "about/about.html",
        {"about": about, "contact_form": contact_form},
    )
