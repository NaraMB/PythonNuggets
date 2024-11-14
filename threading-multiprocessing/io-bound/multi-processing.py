from utils import elapsed_seconds, seconds
from concurrent.futures import ProcessPoolExecutor
from .io_bound_simulation import io_bound_func

@elapsed_seconds
def pool_processing():
    # print(simulation_chunks)
    with ProcessPoolExecutor() as executor:
        executor.map(io_bound_func, seconds)


if __name__ == "__main__":
    # import sys
    # print(sys.path)
    pool_processing()
