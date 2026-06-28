import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'CashApp' in content or 'Venmo' in content:
        content = re.sub(r'\s*<span class="payment-badge cinzel">CashApp</span>', '', content)
        content = re.sub(r'\s*<span class="payment-badge cinzel">Venmo</span>', '', content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
