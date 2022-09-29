'''
tablamult.py
Autor: Javier Spina
Agosto 2022
ECyT UNSAM - Programación 1
'''

row_format = '%4d ' * 10

def print_row(n):
    n_str = str(n) + ':'
    print(f'{n_str:<4s}', end='')
    if not n:
        print(row_format % ((0,) * 10) )
    else:
        print(row_format % tuple(range(0, 10*n, n)))

for n in range(0, 10):
    if not n:
        print(' ' * 4, end='')
        print(row_format % tuple(range(0, 10)))
        print('-' * 54)
        print_row(n)
        continue
    print_row(n)

'''
stdout:
    
       0    1    2    3    4    5    6    7    8    9 
------------------------------------------------------
0:     0    0    0    0    0    0    0    0    0    0 
1:     0    1    2    3    4    5    6    7    8    9 
2:     0    2    4    6    8   10   12   14   16   18 
3:     0    3    6    9   12   15   18   21   24   27 
4:     0    4    8   12   16   20   24   28   32   36 
5:     0    5   10   15   20   25   30   35   40   45 
6:     0    6   12   18   24   30   36   42   48   54 
7:     0    7   14   21   28   35   42   49   56   63 
8:     0    8   16   24   32   40   48   56   64   72 
9:     0    9   18   27   36   45   54   63   72   81
'''