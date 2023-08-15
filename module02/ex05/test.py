
from numpy import ndarray, array
from tinyStatistician import TinyStatistician

tstat = TinyStatistician()
# a = [1, 42, 300, 10, 59]
a = ndarray(shape=(5,), dtype=int, buffer=array([1, 42, 300, 10, 59]))
# a = [1, 42, 300, 10, 59]
print(tstat.mean(a))
# Expected result: 82.4
# 
print(tstat.median(a))
# Expected result: 42.0
# 
print(tstat.quartiles(a))
# Expected result: [10.0, 59.0]
# 
print(tstat.var(a))
# Expected result: 12279.439999999999
# 
print(tstat.std(a))
# Expected result: 110.81263465868862