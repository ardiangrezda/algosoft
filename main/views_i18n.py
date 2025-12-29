"""Custom i18n view with better error handling for language switching"""
import logging
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.utils import translation

logger = logging.getLogger(__name__)

@csrf_exempt  # Language switching is not a security-critical operation
@require_http_methods(["POST", "GET"])
def set_language_custom(request):
    """
    Handle language switching with proper error handling.
    
    Accepts language via POST or GET parameter: 'language'
    Redirects back to HTTP_REFERER or root.
    """
    try:
        # Get language from POST or GET
        lang = request.POST.get('language') or request.GET.get('language')
        
        if not lang:
            logger.warning("No language parameter provided in request")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        # Validate language is in configured languages
        valid_langs = [code for code, _ in settings.LANGUAGES]
        if lang not in valid_langs:
            logger.warning(f"Invalid language code requested: {lang}. Valid codes: {valid_langs}")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        # Activate and store language in session
        translation.activate(lang)
        request.session['django_language'] = lang
        request.session.save()
        
        logger.info(f"Successfully switched language to: {lang}")
        
        # Redirect back to referrer
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    except Exception as e:
        logger.error(f"Error in set_language_custom view: {str(e)}", exc_info=True)
        # Fail gracefully - redirect back
        return redirect(request.META.get('HTTP_REFERER', '/'))




