import time

def ft_progress(listy):
    i = 0
    start_time = time.time()
    diff = 0
    while i < len(listy):
        progress_bar = '=' * int(i / len(listy) * 20) + '>'
        formatted_output = 'ETA: %.2fs [%d%s][%s] %d/%d | elapsed time %.3f' %((time.time() - (start_time + diff)) * len(listy), (i / len(listy) * 100) + 1, '%', progress_bar.ljust(21, ' '), i + 1, len(listy), time.time() - start_time)
        if (len(listy) - 1 != i):
            print(formatted_output, end='\r')
        else:
            print(formatted_output, end='\n')
        diff = time.time() - start_time
        yield listy[i]
        e = 0
        i += 1

listy = range(1000)
ret = 0
for elem in ft_progress(range(1000)):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
