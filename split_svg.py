import re

with open('public/logo-tc.svg', 'r') as f:
    content = f.read()

match = re.search(r'd="([^"]+)"', content)
d = match.group(1)
subpaths = [p for p in d.replace(' M ', '|M ').split('|') if p.strip()]

for i, sp in enumerate(subpaths):
    nums = [float(x) for x in re.findall(r'-?\d+\.?\d*', sp)]
    if len(nums) < 2: continue
    xs = nums[::2]
    ys = nums[1::2]
    print(f"Subpath {i}: X {min(xs):.1f} - {max(xs):.1f}, Y {min(ys):.1f} - {max(ys):.1f}, cmds: {len(sp[:20])}")

