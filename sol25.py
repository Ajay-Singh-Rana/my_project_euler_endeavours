# h3avren
import time

# to calculate execution time
exec_start = time.perf_counter()

start = 1
successor = 1
index = 2
digits = 1
while digits != 1000:
    next = start + successor
    start = successor
    successor = next
    index += 1
    digits = len(str(next))

end = time.perf_counter()

print(index,f"Execution time: {end - exec_start}", sep = "\n")
