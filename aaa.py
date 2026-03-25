grid = [["X","Y","."],["Y",".","."]]
from typing import List

class Solution:

    def numberOfX(self,array: List[str]):
        if "X" in array:
            return True
        else:
            return False

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        for i in grid:
            for l in i:
                print(l)