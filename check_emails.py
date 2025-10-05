#!/usr/bin/env python
"""
Email Checker Script for Algosoft II Contact Form
================================================

This script helps you check if contact form emails are being generated.
"""

import os
import glob
from datetime import datetime

def check_emails():
    email_dir = "sent_emails"
    
    if not os.path.exists(email_dir):
        print("❌ Email directory not found!")
        print("Make sure you've submitted a contact form first.")
        return
    
    email_files = glob.glob(os.path.join(email_dir, "*.log"))
    
    if not email_files:
        print("📫 No emails found yet.")
        print("Submit a contact form to test the email system.")
        return
    
    print(f"📧 Found {len(email_files)} email(s):")
    print("-" * 50)
    
    for email_file in sorted(email_files):
        print(f"\n📄 File: {os.path.basename(email_file)}")
        with open(email_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        print("-" * 50)

def main():
    print("=== ALGOSOFT II EMAIL CHECKER ===")
    print()
    
    print("Current email setup:")
    print("✅ Backend: File-based (emails saved to files)")
    print("✅ Recipient: ardian.grezda@hotmail.com")
    print("✅ Directory: sent_emails/")
    print()
    
    check_emails()
    
    print()
    print("TO SEND REAL EMAILS:")
    print("1. Get a Gmail account")
    print("2. Generate an App Password")
    print("3. Update settings.py with SMTP configuration")
    print("4. Run setup_gmail.py for detailed instructions")

if __name__ == "__main__":
    main()
