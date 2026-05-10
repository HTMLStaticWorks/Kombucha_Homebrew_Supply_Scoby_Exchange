import os
import re

files = [
    'index.html', 'home-niche.html', 'about.html', 'services.html', 
    'service-details.html', 'pricing.html', 'exchange.html', 
    'blog.html', 'blog-details.html', 'contact.html'
]

directory = r'c:\Users\prasa\OneDrive\Desktop\SF\May website 2026\Kombucha_Homebrew_Supply_Scoby_Exchange'

# Regex to find the Community div and replace it
# We look for a div containing a h4 with "Community" and then a ul
pattern = re.compile(r'<div>\s*<h4 class="font-bold mb-6 uppercase text-sm tracking-wider">Community</h4>\s*<ul class="space-y-3 text-gray-400 text-sm">.*?</ul>\s*</div>', re.DOTALL)

replacement = """<div>
                    <h4 class="font-bold mb-6 uppercase text-sm tracking-wider">Quick Links</h4>
                    <ul class="space-y-3 text-gray-400 text-sm">
                        <li><a href="index.html" class="hover:text-matcha transition-colors">Home</a></li>
                        <li><a href="about.html" class="hover:text-matcha transition-colors">About Us</a></li>
                        <li><a href="services.html" class="hover:text-matcha transition-colors">Our Supplies</a></li>
                        <li><a href="exchange.html" class="hover:text-matcha transition-colors">Scoby Exchange</a></li>
                        <li><a href="blog.html" class="hover:text-matcha transition-colors">Brewing Blog</a></li>
                    </ul>
                </div>"""

for filename in files:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub(replacement, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Could not find pattern in {filename}")
    else:
        print(f"File {filename} not found")
