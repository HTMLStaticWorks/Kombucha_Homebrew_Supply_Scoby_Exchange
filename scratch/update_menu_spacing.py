import os
import re

files = [
    'index.html', 'home-niche.html', 'about.html', 'services.html', 
    'service-details.html', 'pricing.html', 'exchange.html', 
    'blog.html', 'blog-details.html', 'contact.html', 
    '404.html', 'coming-soon.html'
]

directory = r'c:\Users\prasa\OneDrive\Desktop\SF\May website 2026\Kombucha_Homebrew_Supply_Scoby_Exchange'

pattern = re.compile(r'<div class="space-y-2">\s*(<a href="index\.html".*?>Home 1</a>)\s*(<a href="home-niche\.html".*?>Home 2</a>)\s*</div>', re.DOTALL)

for filename in files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub(r'\1\n                \2', content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Could not find pattern in {filename}")
    else:
        print(f"File {filename} not found")
