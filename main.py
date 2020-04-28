
import numpy as np
from alrgorism import do
from os import system

class Nonogram:

    cell = ['□', '■', '◇']

    def __init__(self, size):
        # -> (ver_arr)
        # V  (hori_arr)
        self.space = [[0] * size] * size
        self.size = size

        #가로
        self.hori_arr = [[]] * self.size
        #세로
        self.ver_arr  = [[]] * self.size

    def arr_input(self):

        print("가로줄을 입력")
        for i in range(self.size):
            self.hori_arr[i] = list(map(int, input().split(" ")))
            print(self.hori_arr)

        print("세로줄을 입력")
        for i in range(self.size):
            self.ver_arr[i]  = list(map(int, input().split(" ")))
            print(self.ver_arr)

    def current_info(self):

        x = system('cls')
        
        for i in self.space:
            for j in i:
                print(self.cell[j], end='')
            print()

    def getVerline(self, idx):
        result = []
        for i in self.space:
            result.append(i[idx])
        return result

    def ls_ver(self, idx):
        line = self.getVerline(idx)
        arr = self.ver_arr[idx]

        dline = do(line, arr)

        for num, i in enumerate(dline):
            
            self.space[num][idx] = i

        if dline != line:
            self.current_info()

        return [x for x in line if x == 0]
    
    def ls_hori(self, idx):
        line = self.space[idx]
        arr = self.hori_arr[idx]

        dline = do(line, arr)

        self.space[idx] = dline

        if dline != line:
            self.current_info()

        return [x for x in line if x == 0]

    def main(self):
        varr = [True] * self.size
        harr = [True] * self.size

        while any(varr) or any(harr):

            for num, i in enumerate(harr):
                if i: 
                    harr[num] = self.ls_hori(num)

            for num, i in enumerate(varr):
                if i: 
                    varr[num] = self.ls_ver(num)
            

if __name__ == "__main__":
    a = Nonogram(15)
    a.hori_arr = [
        [6],
        [1, 6],
        [4, 5],
        [7, 4],
        [1, 2, 3, 2],
        [1, 1, 4, 1],
        [1, 1, 5],
        [2, 1, 2, 2],
        [2, 1, 1, 2, 1],
        [1, 1, 1, 3, 1],
        [1, 1, 2, 4, 2],
        [4, 1, 4, 1],
        [2, 7],
        [3, 3],
        [5]
    ]

    a.ver_arr = [
        [2, 4, 1],
        [1, 1, 2, 1, 1],
        [1, 6, 1, 1],
        [1, 2, 3, 1],
        [1, 7, 1, 1],
        [2, 2, 3],
        [1, 1, 5],
        [1, 5, 1],
        [1, 4, 4],
        [1, 3, 5],
        [2, 8],
        [2, 6],
        [2, 2],
        [3, 3, 2],
        [4, 4]
    ]
    a.main()
    