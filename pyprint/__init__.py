def print_table(colnames, data, spaces_left=1, spaces_right=1, align='left', border=False, horizontal_char='-', vertical_char='|', corner_char='+'):

    lens = []

    for i, d in enumerate(colnames):
        lens.append(len(d))

    for i, d in enumerate(data):
        for y, x in enumerate(d):
            if len(str(x)) > lens[y]:
                lens[y] = len(str(x))

    format=''
    if align == 'left':
        multiplier = -1
    else:
        multiplier=1
    for i, col in enumerate(colnames):
        if border:
            if i != 0:
                format += f'{" "*spaces_left}%{(lens[i])*multiplier}s{" "*spaces_right}{vertical_char}'
            else:
                format += f'{vertical_char}{" "*spaces_left}%{(lens[i])*multiplier}s{" "*spaces_right}{vertical_char}'
        else:
            if i != 0:
                format += f'{" "*spaces_left}%{(lens[i])*multiplier}s{" "*spaces_right}'
            else:
                format += f'{" "*spaces_left}%{(lens[i])*multiplier}s{" "*spaces_right}'

    tmp = []

    for d in colnames:
        tmp.append(' ')
    
    top = format % tuple(tmp)

    if border:
        separator = horizontal_char*len(top)
        separator = list(separator)
        for i, w in enumerate(top):
            if w == vertical_char:
                separator[i]=corner_char
        separator = ''.join(separator)

    if border:
        print(separator)

    top = format % tuple(colnames)
    print(top)

    if border:
        print(separator)

    for row in data:
        print(format % tuple(row))

    if border:
        print(separator)

if __name__ == '__main__':

    print_table(['a|bc', 'def'], [[1,2],[3,4]], align='left', border=True, horizontal_char='-')

