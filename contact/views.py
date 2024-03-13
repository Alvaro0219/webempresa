from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    #RECIBIR MENSAJES ENVIADOS POR FORMULARIO
    if request.method == "POST":
        #carga los datos
        contact_form = ContactForm(data=request.POST)
        #validando datos
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            mail = request.POST.get('mail', '')
            content = request.POST.get('content', '')

            #Creamos el correo
            mail = EmailMessage(
                "La sabrosa: nuevo mensaje de contacto", #asunto
                "De {} {}\n\nEscribió:\n\n{}".format(name,mail,content), #mensaje
                "LaSabrosa.com", #email de origen - dominio de web
                ["alvaroconti05@gmail.com"], #Email de destino
                reply_to=[mail]
            )

            #Enviamos y redireccionamos
            try:
                mail.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")

    return render(request, 'contact/contact.html', {'form': contact_form})