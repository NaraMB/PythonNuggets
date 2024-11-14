import time
from utils import elapsed_seconds

@elapsed_seconds
def io_bound_func(sec):
    print(f"started sleeping for {sec} seconds")
    time.sleep(sec)  # IO wait simulation
    print(f"Done sleeping for {sec} seconds")