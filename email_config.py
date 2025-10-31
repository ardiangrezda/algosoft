# Email Configuration Instructions for Contact Form
# ================================================

# TO ENABLE EMAIL SENDING:
# 1. You need a Gmail account to send emails through SMTP
# 2. Enable 2-factor authentication on your Gmail account
# 3. Generate an "App Password" for this application
# 4. Update the settings.py file with your credentials

# OPTION 1: Using Gmail SMTP (Recommended)
# ========================================
# Replace these values in settings.py:

EMAIL_SETTINGS_GMAIL = {
    'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_HOST': 'smtp.gmail.com',
    'EMAIL_PORT': 587,
    'EMAIL_USE_TLS': True,
    'EMAIL_HOST_USER': 'your_gmail@gmail.com',  # Your Gmail address
    'EMAIL_HOST_PASSWORD': 'your_16_char_app_password',  # Gmail App Password (not your regular password)
    'DEFAULT_FROM_EMAIL': 'your_gmail@gmail.com',
}

# OPTION 2: Using Outlook/Hotmail SMTP
# ====================================
EMAIL_SETTINGS_OUTLOOK = {
    'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_HOST': 'smtp-mail.outlook.com',
    'EMAIL_PORT': 587,
    'EMAIL_USE_TLS': True,
    'EMAIL_HOST_USER': 'your_email@hotmail.com',  # Your Outlook/Hotmail address
    'EMAIL_HOST_PASSWORD': 'your_password',  # Your Outlook password
    'DEFAULT_FROM_EMAIL': 'your_email@hotmail.com',
}

# TESTING WITHOUT EMAIL (Current Setup)
# =====================================
# If you want to test without setting up email, the form will work
# but emails won't be sent. Messages will be printed to console instead.

# STEPS TO SET UP GMAIL:
# ======================
# 1. Go to https://myaccount.google.com/security
# 2. Enable 2-Step Verification
# 3. Go to "App passwords" and generate a new app password
# 4. Use that 16-character password in EMAIL_HOST_PASSWORD
# 5. Update EMAIL_HOST_USER with your Gmail address
# 6. The emails will be sent to: ardian_grezda@outlook.com

print("Email configuration instructions loaded.")
print("Check this file for setup instructions.")
