import re

with open('public/logo-tc.svg', 'r') as f:
    content = f.read()

d = re.search(r'd="([^"]+)"', content).group(1)
subpaths = [p for p in d.replace(' M ', '|M ').split('|') if p.strip()]

sp10 = subpaths[10]
sp11 = subpaths[11]

def process(sp):
    nums = [float(x) for x in re.findall(r'-?\d+\.?\d*', sp)]
    xs = nums[::2]
    ys = nums[1::2]
    print(f"X: {min(xs):.1f} - {max(xs):.1f}, Y: {min(ys):.1f} - {max(ys):.1f}")
    
print("T shape:")
process(sp10)
print("C shape:")
process(sp11)

