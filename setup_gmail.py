#!/usr/bin/env python
"""
Gmail Setup Script for Algosoft II Contact Form
===============================================

This script helps you set up Gmail to send emails from your contact form.

STEPS TO SET UP GMAIL EMAIL SENDING:

1. CREATE OR USE A GMAIL ACCOUNT:
   - You can create a dedicated Gmail account like: algosoftii.contact@gmail.com
   - Or use an existing Gmail account

2. ENABLE 2-FACTOR AUTHENTICATION:
   - Go to: https://myaccount.google.com/security
   - Turn on "2-Step Verification"

3. CREATE AN APP PASSWORD:
   - Go to: https://support.google.com/accounts/answer/185833
   - Generate an "App Password" for "Mail"
   - You'll get a 16-character password like: "abcd efgh ijkl mnop"

4. UPDATE SETTINGS:
   - Replace 'algosoftii.contact@gmail.com' with your Gmail address
   - Replace 'your_gmail_app_password_here' with your 16-character app password

5. TEST THE SETUP:
   - Submit a contact form on your website
   - Check if email arrives at ardian_grezda@outlook.com

ALTERNATIVE - QUICK TEST MODE:
If you want to test without setting up Gmail, change this in settings.py:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

This will print emails to your terminal instead of sending them.
"""

import os
import sys

def main():
    print("=== ALGOSOFT II EMAIL SETUP ===")
    print()
    print("Current email configuration:")
    print("- FROM: algosoftii.contact@gmail.com")
    print("- TO: ardian_grezda@outlook.com")
    print("- METHOD: Gmail SMTP")
    print()
    print("TO COMPLETE SETUP:")
    print("1. Create Gmail account: algosoftii.contact@gmail.com")
    print("2. Enable 2-factor authentication")
    print("3. Generate App Password")
    print("4. Update settings.py with your App Password")
    print()
    print("Need help? Check the comments in this file!")

if __name__ == "__main__":
    main()
