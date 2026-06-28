import os
import re

html_files = [
    'index.html',
    'rules.html',
    'services.html',
    'tributes.html',
    'gallery.html',
    'contact.html'
]

replacement = """      <div class="footer-social">
        <a href="https://www.instagram.com/the.soft.command/" target="_blank" rel="noopener" class="social-link cinzel" aria-label="Instagram">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>
            <circle cx="12" cy="12" r="4"/>
            <circle cx="17.5" cy="6.5" r="0.5" fill="currentColor"/>
          </svg>
          <span>@the.soft.command</span>
        </a>
        <a href="https://www.instagram.com/the.soft.command.1/" target="_blank" rel="noopener" class="social-link cinzel" aria-label="Backup Instagram">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>
            <circle cx="12" cy="12" r="4"/>
            <circle cx="17.5" cy="6.5" r="0.5" fill="currentColor"/>
          </svg>
          <span>@the.soft.command.1</span>
        </a>
        <a href="mailto:thesoftcommand39@gmail.com" class="social-link cinzel" aria-label="Email">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
            <polyline points="22,6 12,13 2,6"></polyline>
          </svg>
          <span>Email</span>
        </a>
      </div>"""

# Define the regex pattern to match the <div class="footer-social"> block
pattern = re.compile(r'      <div class="footer-social">.*?</div>', re.DOTALL)

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the block
        new_content = pattern.sub(replacement, content)
        
        if content != new_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
        else:
            print(f"No changes needed for {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
