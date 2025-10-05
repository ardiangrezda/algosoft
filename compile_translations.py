#!/usr/bin/env python3
"""
Simple compilation of .po files to .mo files using Python's msgfmt
"""
import os
import polib

def compile_po_to_mo(po_file_path, mo_file_path):
    """Compile .po file to .mo file using polib"""
    try:
        po = polib.pofile(po_file_path, encoding='utf-8')
        po.save_as_mofile(mo_file_path)
        return True
    except Exception as e:
        print(f"Error compiling {po_file_path}: {e}")
        return False

if __name__ == '__main__':
    # Try to install polib if not available
    try:
        import polib
    except ImportError:
        print("Installing polib...")
        os.system("pip install polib")
        import polib
    
    # Compile German translations
    success_de = compile_po_to_mo('locale/de/LC_MESSAGES/django.po', 'locale/de/LC_MESSAGES/django.mo')
    if success_de:
        print("Compiled German translations")
    
    # Compile English translations  
    success_en = compile_po_to_mo('locale/en/LC_MESSAGES/django.po', 'locale/en/LC_MESSAGES/django.mo')
    if success_en:
        print("Compiled English translations")
