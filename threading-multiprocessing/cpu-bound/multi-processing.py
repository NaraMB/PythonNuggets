from concurrent.futures import ProcessPoolExecutor
import multiprocessing

from utils import simulation_chunks, elapsed_seconds
from .cpu_bound_simulation import monte_carlo

# Using lower-level multiprocessing python module
@elapsed_seconds
def basic_mProcessing():

    process_pool = []
    for chunk in simulation_chunks:
        p = multiprocessing.Process(target=monte_carlo, args=[chunk])
        process_pool.append(p)
        p.start()

    for p in process_pool:
        p.join()


# 2. Using concurrent.futures - higher-level api
@elapsed_seconds
def pool_processing():
    with ProcessPoolExecutor() as executor:
        executor.map(monte_carlo, simulation_chunks)


if __name__ == "__main__":
    pool_processing()