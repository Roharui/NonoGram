

import numpy as np

cell = ['□', '■', '◇']

def do(line, arr):
    result = [line]
    starts = [0]
    start = 0
    
    for arr_num in arr:
        result2 = []
        starts2 = []
        for line_num in range(len(result)):

            c = result[line_num]
            start = starts[line_num]
            
            if start + arr_num > len(line): continue

            for i in range(0, len(line) + 1 - arr_num - start):

                tf = False
                cline = c[:]

                for j in range(arr_num):

                    ele = c[start + i + j]

                    if(ele == 2):
                        tf = True
                        break

                    cline[start + i + j] = 1

                if tf:
                    continue
                result2.append(cline)
                starts2.append(i + arr_num + 1)
        
        result = result2
        starts = starts2

    result = [zeroTwo(i) for i in result if inside(arr, i)]

    if not result:
        return line

    if __name__ == "__main__":
        for i in result:
            print_line(i)
    
    return rt_result(result)

def inside(arr, cline):
    result = []
    num = 0
    for i in cline:
        if i == 1: num += 1
        if i != 1 and num != 0: 
            result.append(num)
            num = 0
    if num != 0: result.append(num)
    return arr == result


def rt_result(r):
    result = r[0]
    for i in r[1:]:
        for num, j in enumerate(i):
            if result[num] == j:
                pass
            else:
                result[num] = 0
    return result

def zeroTwo(line):
    result = []
    for i in line:
        if i == 0:
            result.append(2)
        else:
            result.append(i)
    return result

def print_line(st):
    for i in st:
        print(cell[int(i)], end='')
    print()


if __name__ == "__main__":
    line = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    #line = [0] * 15
    arr = [2, 5]

    print(do(line, arr))