from PIL import Image

def analyze_logo(filepath):
    img = Image.open(filepath).convert('L')
    width, height = img.size
    pixels = img.load()
    
    # helper: find black segments in a given row or col
    def get_black_segments(arr):
        segs = []
        start = None
        for i, val in enumerate(arr):
            if val < 128:  # black
                if start is None: start = i
            else:
                if start is not None:
                    segs.append((start, i-1))
                    start = None
        if start is not None: segs.append((start, len(arr)-1))
        return segs

    # Analyze some rows to find T and C
    print(f"Size: {width}x{height}")
    
    # Top bar row (say, y = 20)
    print("Row 20:", get_black_segments([pixels[x, 20] for x in range(width)]))
    # Mid row (say, y = height // 2)
    print(f"Row {height//2}:", get_black_segments([pixels[x, height//2] for x in range(width)]))
    # Bottom row of stem (say, y = height - 20)
    print(f"Row {height-20}:", get_black_segments([pixels[x, height-20] for x in range(width)]))
    
    # Center of C?
    # For a row cutting through the wheel, say height//2
    row = [pixels[x, height//2] for x in range(width)]
    print(f"Wheel cutting row {height//2}:", get_black_segments(row))

analyze_logo('public/logo-tc.png')
