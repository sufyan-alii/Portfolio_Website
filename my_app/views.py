from django.shortcuts import render , redirect , HttpResponse
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'index.html')

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name','') 
        email = request.POST.get('email','')  # Update to the correct field name
        subject = request.POST.get('subject','')  # Update to the correct field name
        message = request.POST.get('message','')  # Update to the correct field name

         # Set the sender's email to the user's email
        from_email = email

         # Prepare HTML email body
        html_message = f"""
            <html>
                <head></head>
                <body>
                    <h2>Portfolio Form </h2>
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Subject:</strong> {subject}</p>
                    <p><strong>Message:</strong></p>
                    <p>{message}</p>
                </body>
            </html>
        """
        send_mail(
            subject,
            f"Name: {name}\nEmail: {email}\n\n{message}",
            from_email,      
            ['sufyan7586432@gmail.com'],
            fail_silently=False,
            html_message=html_message,
            )
        
        # Include a script in the response to show an alert and redirect to index
        return HttpResponse(f"""
            <script>
                alert('Your request has been submitted. We will contact you as soon as possible.');
                window.location.href = '/';
            </script>
        """)

    # Handle other cases, e.g., invalid request method
    return HttpResponse(f"""
        <script>
            alert('Invalid request method.');
            window.location.href = '/';
        </script>
    """)


