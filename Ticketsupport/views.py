from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm
from django.template.loader import get_template
from .upload import handle_uploaded_file



def home(request):
    if request.method == 'POST' :
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            catagory = request.POST.get('catagory')
            comments = request.POST.get('comments')




            template= get_template('contact_template.txt')
            context = {
            'name': name,
            'email': email,
            'catagory': catagory,
            'comments': comments

            }
            content = template.render(context)

            email = EmailMessage(
            catagory,
            content,
            'support@btcz.rocks',
            ['support@btcz.rocks'],
            headers = {'Reply-to': email}
            )
            email.send()
            return render(request, 'thanks.html')





    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
