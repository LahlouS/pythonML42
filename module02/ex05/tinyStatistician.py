import math

class TinyStatistician:
    def __init__(self):
        pass
    
    def mean(self, lst):
        if not len(lst):
            return None
        work_lst = list(lst)
        ret = 0
        for elem in work_lst:
            ret += elem
        return ret / len(work_lst)
    
    def median(self, lst):
        if len(lst) > 0:
            work_lst = list(lst)
            work_lst.sort()
            return float(work_lst[(math.ceil( len(work_lst) / 2 )) - 1])
        return None
    
    def quartiles(self, lst):
        if not len(lst):
            return None
        work_lst = list(lst)
        work_lst.sort()
        q1 = work_lst[(math.ceil( len(work_lst) / 4 )) - 1]
        q3 = work_lst[(math.ceil( len(work_lst) * 3 / 4 )) - 1]
        return [float(q1), float(q3)]
    
    def var(self, lst):
        if not len(lst):
            return None
        work_lst = list(lst)
        mean = self.mean(work_lst)
        ret = 0
        for elem in work_lst:
            ret += (elem - mean)**2
        return ret / len(work_lst)
    
    def std(self, lst):
        if not len(lst):
            return None
        work_lst = list(lst)
        return math.sqrt(self.var(work_lst))

    
