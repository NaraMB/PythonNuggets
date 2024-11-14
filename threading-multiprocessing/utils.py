import time
from functools import wraps

# 10M simulations in-total for cpu-bound tasks. You can play with inputs to understand.
simulation_chunks = [1000_000, 1000_000, 1000_000, 2000_000, 2000_000, 3000_000]

# 6 i/o bound tasks for simulations.You can play with inputs to understand.
seconds = [3, 3, 2, 2, 4, 4]

def elapsed_seconds(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time 
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds\n")
        return result
    return wrapper