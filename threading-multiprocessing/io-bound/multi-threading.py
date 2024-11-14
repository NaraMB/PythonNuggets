from utils import elapsed_seconds, seconds
from concurrent.futures import ThreadPoolExecutor
from .io_bound_simulation import io_bound_func

@elapsed_seconds
def pool_threading():
    # print(simulation_chunks)
    with ThreadPoolExecutor() as executor:
        executor.map(io_bound_func, seconds)


if __name__ == "__main__":
    pool_threading()
