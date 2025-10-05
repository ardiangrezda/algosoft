#!/usr/bin/env python
"""
Test Email Sending for Algosoft II Contact Form
==============================================

This script tests if email sending is working properly.
"""

import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Algosoft.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

def test_email():
    print("=== TESTING EMAIL CONFIGURATION ===")
    print(f"Email Backend: {settings.EMAIL_BACKEND}")
    print(f"From Email: {settings.DEFAULT_FROM_EMAIL}")
    print(f"To Email: {settings.CONTACT_EMAIL}")
    print()
    
    try:
        # Test sending an email
        print("Attempting to send test email...")
        
        subject = "Test Email from Algosoft II Contact Form"
        message = """
This is a test email from your Algosoft II website contact form.

From: Test User
Email: test@example.com
Project Type: Testing
Message: This is a test message to verify email functionality.

If you receive this email, your contact form is working correctly!
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        print("✅ EMAIL SENT SUCCESSFULLY!")
        print(f"✅ Email sent from: {settings.DEFAULT_FROM_EMAIL}")
        print(f"✅ Email sent to: {settings.CONTACT_EMAIL}")
        print()
        print("CHECK YOUR EMAIL:")
        print(f"📧 Check: {settings.CONTACT_EMAIL}")
        print("📧 Check spam folder if not in inbox")
        
    except Exception as e:
        print(f"❌ EMAIL SENDING FAILED: {e}")
        print()
        print("TROUBLESHOOTING:")
        print("1. Check your Gmail App Password is correct")
        print("2. Ensure 2-factor authentication is enabled on Gmail")
        print("3. Check if Gmail is blocking the login attempt")

if __name__ == "__main__":
    test_email()
