import os
from statistics import median
from PIL import Image

# Code39 patterns
CODE39_PATTERNS = {
    '111221211': '0', '211211112': '1', '112211112': '2', '212211111': '3',
    '111221112': '4', '211221111': '5', '112221111': '6', '111211212': '7',
    '211211211': '8', '112211211': '9',
    '211112112': 'A', '112112112': 'B', '212112111': 'C', '111122112': 'D',
    '211122111': 'E', '112122111': 'F', '111112212': 'G', '211112211': 'H',
    '112112211': 'I', '111122211': 'J',
    '211111122': 'K', '112111122': 'L', '212111121': 'M', '111121122': 'N',
    '211121121': 'O', '112121121': 'P', '111111222': 'Q', '211111221': 'R',
    '112111221': 'S', '111121221': 'T',
    '221111112': 'U', '122111112': 'V', '222111111': 'W', '121121112': 'X',
    '221121111': 'Y', '122121111': 'Z',
    '121111212': '-', '221111211': '.', '122111211': ' ', '121212111': '$',
    '121211121': '/', '121112121': '+', '111212121': '%', '121121211': '*'
}

def trim_zeros(lst):
    start = 0
    end = len(lst) - 1
    while start <= end and lst[start] == 0:
        start += 1
    return lst[start:]

def binarize_row(row, threshold=128):
    return [1 if pixel < threshold else 0 for pixel in row]

def get_run_lengths(binary_row):
    if not binary_row:
        return []
    
    run_lengths = []
    current = binary_row[0]
    count = 1

    for bit in binary_row[1:]:
        if bit == current:
            count += 1
        else:
            run_lengths.append(count)
            current = bit
            count = 1
    run_lengths.append(count)
    return run_lengths

def normalize_widths(Lst):
    L=sorted(Lst, reverse=True)
    med = [L[0],L[1],L[2]]
    here=[2 if w in med else 1 for w in Lst]
    #print(here)
    return here

def group_by_9_elements(elements):
    return [elements[i:i+9] for i in range(0, len(elements) - 8, 9)]

def pattern_to_string(pattern):
    #for t in pattern :
    #    print(str(t), end="")
    key = ''.join(str(d) for d in pattern)
    return CODE39_PATTERNS.get(key, '?')
    #print(" ")

def try_find(L):
    ans=[]
    i=0
    while(i<len(L)-9):
        curr=L[i:i+9]
        normalized=normalize_widths(curr)
        converted=pattern_to_string(normalized)
        if(converted!='?'):
            #print(normalized)
            ans.append(converted)
            i+=10
        else :
            i+=1
    #print(ans)
    return ans
        
# === MAIN ===
image_path = input()

if os.path.isfile(image_path):
    img = Image.open(image_path).convert('L')  # Grayscale
    width, height = img.size
    mid_y = height // 2

    row = [img.getpixel((x, mid_y)) for x in range(width)]
    binary_row = binarize_row(row)
    binary_row=trim_zeros(binary_row)
    run_lengths = get_run_lengths(binary_row)
    
    #print(binary_row)
    #print(run_lengths)
    #normalized = normalize_widths(run_lengths)
    chars=[]
    chars=try_find(run_lengths)
    if chars and chars[0] == '*' and chars[-1] == '*':
        chars = chars[1:-1]
    print(''.join(chars))
