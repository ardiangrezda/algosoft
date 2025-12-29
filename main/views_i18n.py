"""Custom i18n view with better error handling"""
import logging
from django.views.i18n import set_language
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

logger = logging.getLogger(__name__)

LANGUAGE_SESSION_KEY = '_language'

@require_http_methods(["POST", "GET"])
def set_language_custom(request):
    """
    Custom language setting view with better error handling.
    Works around potential issues with Django's built-in i18n view.
    """
    try:
        lang = request.POST.get('language') or request.GET.get('language')
        
        if not lang:
            logger.warning("No language parameter provided")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        
        # Validate language choice
        valid_langs = [code for code, _ in settings.LANGUAGES]
        if lang not in valid_langs:
            logger.warning(f"Invalid language: {lang}")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        
        # Store language in session
        request.session[LANGUAGE_SESSION_KEY] = lang
        request.session.save()
        
        logger.info(f"Language changed to: {lang}")
        
        # Return to referrer or home
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
    except Exception as e:
        logger.error(f"Error in set_language: {str(e)}", exc_info=True)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

