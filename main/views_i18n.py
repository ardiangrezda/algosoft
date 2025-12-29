"""Custom i18n view with better error handling for language switching"""
import logging
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.utils import translation
from django.http import HttpResponseRedirect

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
        
        # Activate language for this request (optional)
        translation.activate(lang)
        
        logger.info(f"Successfully switched language to: {lang}")
        
        # Determine next URL and rewrite language prefix to selected lang
        next_url = (
            request.POST.get('next')
            or request.GET.get('next')
            or request.META.get('HTTP_REFERER')
            or '/'
        )

        try:
            # Normalize and rewrite prefix: /<lang>/...
            # Build list of language codes for prefix matching
            codes = [code for code, _ in settings.LANGUAGES]
            # Ensure leading slash
            if not next_url.startswith('/'):
                # keep scheme/host if full URL
                if '://' in next_url:
                    from urllib.parse import urlparse
                    parsed = urlparse(next_url)
                    path = parsed.path or '/'
                    next_url = path
                else:
                    next_url = '/' + next_url

            parts = next_url.split('/')[1:]  # drop leading empty segment
            if parts:
                if parts[0] in codes:
                    parts[0] = lang
                else:
                    parts.insert(0, lang)
            else:
                parts = [lang]
            rewritten = '/' + '/'.join(parts)
            # Always ensure trailing slash when original had it or at root
            if next_url.endswith('/') and not rewritten.endswith('/'):
                rewritten += '/'

            response = HttpResponseRedirect(rewritten)
            # Prefer cookie over session to avoid DB issues on Heroku
            # Use Django's LANGUAGE_COOKIE_NAME
            secure = True if request.is_secure() or request.META.get('HTTP_X_FORWARDED_PROTO') == 'https' else False
            response.set_cookie(
                key=getattr(settings, 'LANGUAGE_COOKIE_NAME', 'django_language'),
                value=lang,
                max_age=60*60*24*365,  # 1 year
                samesite='Lax',
                secure=secure,
            )
            return response
        except Exception:
            # Fallback to referrer/root
            return redirect(request.META.get('HTTP_REFERER', '/'))
    
    except Exception as e:
        logger.error(f"Error in set_language_custom view: {str(e)}", exc_info=True)
        # Fail gracefully - redirect back
        return redirect(request.META.get('HTTP_REFERER', '/'))




