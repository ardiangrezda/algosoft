from django.shortcuts import render
from django.utils.translation import gettext as _
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.utils import translation


def homepage(request):
    return render(request = request, template_name='home.html')

def about(request):
    return render(request = request, template_name='about.html')

def services(request):
    return render(request = request, template_name='services.html')

def servicesoftware(request):
    return render(request = request, template_name='services software.html')

def servicedata(request):
    return render(request = request, template_name='services data services.html')

def contact(request):
    if request.method == 'POST':
        print("=== CONTACT FORM SUBMITTED ===")
        # Get form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        
        # Basic validation
        if name and email and message:
            try:
                # Import required modules
                from django.conf import settings
                import os
                from datetime import datetime
                
                # Clean all input data to remove any special characters
                clean_name = ''.join(c for c in name if ord(c) < 128)
                clean_email = ''.join(c for c in email if ord(c) < 128)
                clean_subject = ''.join(c for c in (subject if subject else "General Inquiry") if ord(c) < 128)
                clean_message = ''.join(c for c in message if ord(c) < 128)
                
                # Create email subject
                email_subject = "Contact Form: " + clean_subject
                
                # Create email message with only ASCII characters
                lines = []
                lines.append("New contact form submission:")
                lines.append("")
                lines.append("Name: " + clean_name)
                lines.append("Email: " + clean_email)
                lines.append("Project Type: " + clean_subject)
                lines.append("")
                lines.append("Message:")
                lines.append(clean_message)
                lines.append("")
                lines.append("---")
                lines.append("Sent from Algosoft II contact form")
                
                email_message = "\n".join(lines)
                
                print("=== SAVING EMAIL ===")
                print(f"Subject: {email_subject}")
                print(f"From: {settings.DEFAULT_FROM_EMAIL}")
                print(f"To: {settings.CONTACT_EMAIL}")
                
                # Save email to file (for backup)
                emails_dir = os.path.join(settings.BASE_DIR, 'sent_emails')
                os.makedirs(emails_dir, exist_ok=True)
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"contact_form_{timestamp}.txt"
                filepath = os.path.join(emails_dir, filename)
                
                full_email = f"""Subject: {email_subject}
From: {settings.DEFAULT_FROM_EMAIL}
To: {settings.CONTACT_EMAIL}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{email_message}"""
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(full_email)
                
                print(f"=== EMAIL SAVED TO: {filename} ===")
                
                # Also try to send real email with completely clean content
                try:
                    from django.core.mail import send_mail
                    
                    # Create ultra-clean content using only basic letters and numbers
                    safe_subject = "Contact Form Submission from Algosoft Website"
                    safe_message = (
                        "New contact form submission:\n\n" +
                        "Name: " + ''.join(c if c.isalnum() or c.isspace() or c in '.-@_' else '' for c in clean_name) + "\n" +
                        "Email: " + ''.join(c if c.isalnum() or c in '.-@_' else '' for c in clean_email) + "\n" +
                        "Project Type: " + ''.join(c if c.isalnum() or c.isspace() else '' for c in clean_subject) + "\n\n" +
                        "Message:\n" + ''.join(c if c.isalnum() or c.isspace() or c in '.,!?-' else '' for c in clean_message) + "\n\n" +
                        "---\n" +
                        "Sent from Algosoft II contact form"
                    )
                    
                    print("=== ATTEMPTING TO SEND CLEAN EMAIL ===")
                    print(f"Safe subject: {safe_subject}")
                    print(f"Safe message length: {len(safe_message)}")
                    
                    # Send with ultra-clean content
                    send_mail(
                        safe_subject,
                        safe_message,
                        'algosoftii.contact@gmail.com',
                        ['ardian.grezda@hotmail.com'],
                        fail_silently=False,
                    )
                    print("=== REAL EMAIL SENT SUCCESSFULLY ===")
                except Exception as e:
                    print(f"=== REAL EMAIL FAILED (saved to file instead): {e} ===")
                    print(f"Error type: {type(e).__name__}")
                
                messages.success(request, _('Thank you for your message! We will get back to you soon.'))
                
            except Exception as e:
                # If email fails, still show success to user but log the error
                print(f"=== EMAIL SENDING FAILED ===")
                print(f"Error: {e}")
                messages.success(request, _('Thank you for your message! We will get back to you soon.'))
            
            return HttpResponseRedirect(reverse('contact'))
        else:
            messages.error(request, _('Please fill in all required fields.'))
    
    return render(request, 'contact.html')

