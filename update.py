import os
import glob
import re

html_files = glob.glob('d:/CODING/primex/*.html')

top_bar_pattern = re.compile(
    r'<div class="top-bar-left">\s*<span>📍.*?</span>\s*<span>📞.*?</span>\s*<span>✉️.*?</span>\s*</div>',
    re.DOTALL
)

top_bar_replacement = """<div class="top-bar-left">
                <span>📞 +91 91409 33878</span>
                <span>✉️ the.primax.agency@gmail.com</span>
            </div>"""


footer_pattern = re.compile(
    r'<ul class="footer-links">\s*<li style="display: flex; gap: 12px; color: #cbd5e1; margin-bottom: 16px;">\s*<span>📍</span>[^<]*<br>[^<]*</li>\s*<li style="display: flex; gap: 12px; color: #cbd5e1; margin-bottom: 16px;">\s*<span>📞</span>[^<]*</li>\s*<li style="display: flex; gap: 12px; color: #cbd5e1;">\s*<span>✉️</span>[^<]*</li>\s*</ul>',
    re.DOTALL
)

footer_replacement = """<ul class="footer-links">
                        <li style="display: flex; gap: 12px; color: #cbd5e1; margin-bottom: 16px;">
                            <span>📞</span> +91 91409 33878
                        </li>
                        <li style="display: flex; gap: 12px; color: #cbd5e1;">
                            <span>✉️</span> the.primax.agency@gmail.com
                        </li>
                    </ul>"""

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = top_bar_pattern.sub(top_bar_replacement, content)
        new_content = footer_pattern.sub(footer_replacement, new_content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
            
    except Exception as e:
        print(f"Failed to process {file}: {e}")
