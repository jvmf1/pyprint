def print_table(colnames, data, spaces=2, align_left=True, border=False):

    lens = []

    for i, d in enumerate(colnames):
        lens.append(len(d))

    for i, d in enumerate(data):
        for y, x in enumerate(d):
            if len(str(x)) > lens[y]:
                lens[y] = len(str(x))

    format=''
    multiplier = 1
    if align_left:
        multiplier = -1
    for i, col in enumerate(colnames):
        if border:
            if i != 0:
                format += f'%{(lens[i]+spaces)*multiplier}s|'
            else:
                format += f'|%{(lens[i]+spaces)*multiplier}s|'
        else:
            format += f'%{(lens[i]+spaces)*multiplier}s '
    
    top = format % tuple(colnames)

    if border:
        separator = '-'*len(top)
        separator = list(separator)
        for i, w in enumerate(top):
            if w == '|':
                separator[i]='+'
        separator = ''.join(separator)

    if border:
        print(separator)

    print(top)

    if border:
        print(separator)

    for row in data:
        print(format % tuple(row))

    if border:
        print(separator)

if __name__ == '__main__':

    print_table(['abc', 'def'], [[1,2],[3,4]], align_left=True, border=True)

