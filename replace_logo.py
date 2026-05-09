import os
import re

directory = r'c:\Users\prasa\OneDrive\Desktop\SF\May website 2026\Kombucha_Homebrew_Supply_Scoby_Exchange'

favicon_pattern = re.compile(r'<link rel="icon" type="image/png" href="assets/images/logo\.png">')
favicon_replacement = r'<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍄</text></svg>">'

# Header logo pattern
header_logo_pattern = re.compile(r'<img src="assets/images/logo\.png" alt="[^"]+" class="w-10 h-10 rounded-full object-cover group-hover:rotate-12 transition-transform shadow-sm">')
header_logo_replacement = r'<div class="w-10 h-10 rounded-full bg-matcha/20 text-matcha flex items-center justify-center text-xl shadow-sm group-hover:rotate-12 transition-transform">🍄</div>'

# Footer logo pattern
footer_logo_pattern = re.compile(r'<img src="assets/images/logo\.png" alt="Logo" class="w-8 h-8 rounded-full object-cover">')
footer_logo_replacement = r'<div class="w-8 h-8 rounded-full bg-matcha/20 text-matcha flex items-center justify-center text-lg">🍄</div>'

# Auth logo pattern
auth_logo_pattern = re.compile(r'<img src="assets/images/logo\.png" alt="Logo" class="w-16 h-16 rounded-full object-cover group-hover:rotate-12 transition-transform shadow-lg shadow-matcha/20">')
auth_logo_replacement = r'<div class="w-16 h-16 rounded-full bg-matcha/20 text-matcha flex items-center justify-center text-3xl shadow-lg shadow-matcha/20 group-hover:rotate-12 transition-transform">🍄</div>'

# Coming soon logo pattern
coming_soon_logo_pattern = re.compile(r'<img src="assets/images/logo\.png" alt="Logo" class="w-20 h-20 mx-auto rounded-full object-cover mb-6 shadow-inner border border-white/30">')
coming_soon_logo_replacement = r'<div class="w-20 h-20 mx-auto rounded-full bg-matcha/20 text-matcha flex items-center justify-center text-4xl mb-6 shadow-inner border border-white/30">🍄</div>'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = favicon_pattern.sub(favicon_replacement, content)
        new_content = header_logo_pattern.sub(header_logo_replacement, new_content)
        new_content = footer_logo_pattern.sub(footer_logo_replacement, new_content)
        new_content = auth_logo_pattern.sub(auth_logo_replacement, new_content)
        new_content = coming_soon_logo_pattern.sub(coming_soon_logo_replacement, new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
