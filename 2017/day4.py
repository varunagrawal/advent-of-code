from collections import defaultdict

def valid_passphrases(x):
    """x is a list of phrases"""
    count = 0
    for ph in x:
        words = ph.split(' ')
        
        d = defaultdict(lambda: 0)
        for w in words:
            w = "".join(sorted(w))
            d[w] += 1
        
        valid = True
        for k, v in d.items():
            if v > 1:
                valid = False
                break
        if valid:
            count += 1

    return count

with open("day4.in", 'r') as f:
    inp = f.readlines() 

print(len(inp))
print(valid_passphrases(inp))