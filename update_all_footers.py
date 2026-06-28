import os

def update_footers():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    old_nav = '<a href="contact.html"  data-i18n="nav_contact"  class="cinzel footer-link">Apply</a>'
    new_nav = '<a href="contact.html"  data-i18n="nav_contact"  class="cinzel footer-link">Apply</a>\n        <a href="privacy.html" class="cinzel footer-link">Privacy</a>'
    
    old_copy = '<p class="footer-copy jost">© 2025 The Soft Command. All rights reserved.</p>'
    new_copy = '<p class="footer-copy jost">© 2025 The Soft Command. All rights reserved. · 18+ only · All interactions are between consenting adults.</p>'

    for file_name in html_files:
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            
        updated = False
        if old_nav in content:
            content = content.replace(old_nav, new_nav)
            updated = True
        if old_copy in content:
            content = content.replace(old_copy, new_copy)
            updated = True
            
        if updated:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file_name}")

if __name__ == '__main__':
    update_footers()
