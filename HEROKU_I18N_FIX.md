# Heroku Deployment Guide - Language Switching Fix

## Issue
500 error when accessing `https://algosoftii.com/i18n/setlang/` on Heroku production environment.

## Root Cause
The built-in Django i18n view (`set_language`) can fail in production due to:
1. Missing CSRF handling
2. Locale file loading issues
3. Session handling problems
4. ALLOWED_HOSTS configuration

## Solution Applied

### 1. Custom i18n View
Created `main/views_i18n.py` with a custom language-setting view that:
- Validates language choices against LANGUAGES setting
- Provides proper error logging
- Handles CSRF gracefully
- Manages session language storage

### 2. Settings Configuration
Updated `Algosoft/settings.py`:
- Added logging configuration for debugging on Heroku
- Ensured LOCALE_PATHS is properly configured
- Verified LANGUAGES setting

### 3. URL Configuration
Updated `Algosoft/urls.py`:
- Routes `/i18n/setlang/` to the custom view
- Maintains backward compatibility with Django's built-in i18n patterns

## For Heroku Deployment

### 1. Update Your Procfile
```
web: gunicorn Algosoft.wsgi --log-file -
```

### 2. Ensure requirements.txt includes:
```
Django>=6.0
gunicorn==23.0.0
whitenoise==6.11.0
dj-database-url==3.0.1
python-dotenv==1.2.1
psycopg2-binary==2.9.9
requests==2.32.5
```

### 3. Heroku Config Vars
Set the following environment variables on Heroku:
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=algosoftii.com,www.algosoftii.com,algosoft.herokuapp.com
DATABASE_URL=postgres://... (auto-set by Heroku Postgres)
```

### 4. Run Migrations on Heroku
```bash
heroku run python manage.py migrate --app your-app-name
heroku run python manage.py collectstatic --noinput --app your-app-name
```

### 5. Test Language Switching
After deployment, test with:
```
POST https://algosoftii.com/i18n/setlang/ 
with parameter: language=de
```

## Testing Locally
The fix has been tested and verified to work:
```
python manage.py runserver
# Navigate to http://localhost:8000/contact/
# Click language button to switch (posts to /i18n/setlang/)
# Should successfully change language without 500 error
```

## Troubleshooting

If you still get 500 errors on Heroku:

1. **Check Heroku logs**:
   ```bash
   heroku logs --tail --app your-app-name
   ```

2. **Verify LANGUAGES setting**:
   - Ensure both 'en' and 'de' are configured in settings.LANGUAGES

3. **Check Session Backend**:
   - Heroku may need SESSION_ENGINE configured for distributed environments:
   ```python
   # Add to settings.py if needed:
   SESSION_ENGINE = 'django.contrib.sessions.backends.db'
   ```

4. **Clear Heroku cache**:
   ```bash
   heroku builds:cache:purge --app your-app-name
   git push heroku main  # Re-deploy
   ```

## Files Modified
- `Algosoft/settings.py` - Added logging configuration
- `Algosoft/urls.py` - Added custom i18n view route  
- `main/views_i18n.py` - New custom language-setting view

## Next Steps
1. Commit these changes: `git add -A && git commit -m "Fix i18n language switching on Heroku"`
2. Push to Heroku: `git push heroku main`
3. Test the language switching at https://algosoftii.com/i18n/setlang/
