import re

with open('rate-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

stack = []
for m in re.finditer(r'<div\b[^>]*>|</div>', html, re.IGNORECASE):
    tag = m.group(0).lower()
    if tag == '</div>':
        if stack:
            stack.pop()
        else:
            print('EXTRA </div> found at', m.start())
    else:
        # extract class
        cls_match = re.search(r'class=[\"\']([^\"\']+)[\"\']', m.group(0))
        cls = cls_match.group(1) if cls_match else 'no-class'
        stack.append(cls)

print('Unclosed divs at end:')
for cls in stack:
    print('  ', cls)
