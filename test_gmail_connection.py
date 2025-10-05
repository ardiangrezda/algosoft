#!/usr/bin/env python
"""
Test Gmail Connection for Algosoft II
====================================
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
import smtplib

def test_gmail_connection():
    print("=== TESTING GMAIL CONNECTION ===")
    print(f"Email Host: {settings.EMAIL_HOST}")
    print(f"Email Port: {settings.EMAIL_PORT}")
    print(f"Email User: {settings.EMAIL_HOST_USER}")
    print(f"Email Password: {'*' * len(settings.EMAIL_HOST_PASSWORD) if hasattr(settings, 'EMAIL_HOST_PASSWORD') else 'NOT SET'}")
    print()
    
    # Test 1: Direct SMTP connection
    try:
        print("Testing direct SMTP connection...")
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.quit()
        print("✅ Direct SMTP connection successful!")
    except Exception as e:
        print(f"❌ Direct SMTP connection failed: {e}")
        return False
    
    # Test 2: Django send_mail with simple content
    try:
        print("Testing Django send_mail...")
        send_mail(
            'Test Email from Algosoft II',
            'This is a test email to verify Gmail setup.',
            settings.EMAIL_HOST_USER,
            ['ardian.grezda@hotmail.com'],
            fail_silently=False,
        )
        print("✅ Django send_mail successful!")
        return True
    except Exception as e:
        print(f"❌ Django send_mail failed: {e}")
        return False

if __name__ == "__main__":
    success = test_gmail_connection()
    if success:
        print("\n🎉 Gmail setup is working correctly!")
        print("📧 Check ardian.grezda@hotmail.com for test email")
    else:
        print("\n⚠️ Gmail setup needs attention")
        print("Check your Gmail App Password and account settings")
