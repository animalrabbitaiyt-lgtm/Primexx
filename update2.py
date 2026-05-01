import glob, re

for file in glob.glob('*.html'):
    if file == 'rate-list.html':
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'href="Pages/rate-list.html"' not in content:
        content = re.sub(
            r'(<a href="Pages/about\.html" class="nav-tab">About</a>)',
            r'\1\n                    <a href="Pages/rate-list.html" class="nav-tab">/Pages/rate-list.html</a>',
            content
        )
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Nav links successfully patched!")
