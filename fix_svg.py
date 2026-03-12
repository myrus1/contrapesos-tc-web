import re

with open('public/logo-tc.svg', 'r') as f:
    content = f.read()

match = re.search(r'd="([^"]+)"', content)
if match:
    d = match.group(1)
    
    # Split the subpaths separated by M or m (but here it's M)
    subpaths = []
    # add a marker to split easily
    d_marked = d.replace(' M ', '|M ')
    for sp in d_marked.split('|'):
        if sp.strip():
            subpaths.append(sp.strip())
            
    # Subpath 0-9 are text. Subpath 10+ are the logo.
    logo_subpaths = subpaths[10:]
    new_d = ' '.join(logo_subpaths)
    
    new_content = content.replace(d, new_d)
    
    # Optional: adjust viewBox or just shift it.
    # The logo occupies X: 26 to 257. Y: 40 to 202.
    # We can shift everything by -26 in X and -40 in Y, or just leave it.
    # Let's adjust the viewBox to zoom in perfectly.
    # minX = 26, minY = 40, width = 257 - 26 = 231, height = 202 - 40 = 162
    
    new_content = re.sub(
        r'viewBox="0 0 278 216"',
        r'viewBox="26 40 231 162"',
        new_content
    )
    new_content = re.sub(
        r'width="278" height="216"',
        r'width="231" height="162"',
        new_content
    )
    
    with open('public/logo-tc-icon.svg', 'w') as f:
        f.write(new_content)
    print("Created public/logo-tc-icon.svg")

