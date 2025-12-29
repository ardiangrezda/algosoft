"""Custom i18n view with better error handling for language switching"""
import logging
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

# Session key for storing language preference
LANGUAGE_SESSION_KEY = '_language'

@csrf_exempt  # Language switching is not a security-critical operation
@require_http_methods(["POST", "GET"])
def set_language_custom(request):
    """
    Handle language switching with proper error handling.
    
    Accepts language via:
    - POST parameter: 'language'
    - GET parameter: 'language'
    
    Redirects back to HTTP_REFERER or root.
    """
    try:
        # Get language from POST or GET
        lang = request.POST.get('language') or request.GET.get('language')
        
        if not lang:
            logger.warning("No language parameter provided in request")
            referer = request.META.get('HTTP_REFERER', '/')
            return redirect(referer)
        
        # Validate language is in configured languages
        valid_langs = [code for code, _ in settings.LANGUAGES]
        if lang not in valid_langs:
            logger.warning(f"Invalid language code requested: {lang}. Valid codes: {valid_langs}")
            referer = request.META.get('HTTP_REFERER', '/')
            return redirect(referer)
        
        # Activate language in session
        from django.utils import translation
        translation.activate(lang)
        request.session[LANGUAGE_SESSION_KEY] = lang
        
        # Use django's cookie approach too if configured
        from django.middleware.locale import LANGUAGE_COOKIE_NAME
        response = redirect(request.META.get('HTTP_REFERER', '/'))
        response.set_cookie(LANGUAGE_COOKIE_NAME, lang, 365*24*60*60)
        
        logger.info(f"Successfully switched language to: {lang}")
        return response
    
    except Exception as e:
        logger.error(f"Error in set_language_custom view: {str(e)}", exc_info=True)
        # Fail gracefully - redirect back
        referer = request.META.get('HTTP_REFERER', '/')
        return redirect(referer)



