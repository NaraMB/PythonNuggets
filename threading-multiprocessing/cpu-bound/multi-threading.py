import threading
from concurrent.futures import ThreadPoolExecutor

from utils import simulation_chunks, elapsed_seconds
from .cpu_bound_simulation import monte_carlo

# 1. using threading module
@elapsed_seconds
def basic_threading():

    thread_pool = []
    for chunk in simulation_chunks:
        t = threading.Thread(target=monte_carlo, args=[chunk])
        thread_pool.append(t)
        t.start()

    for t in thread_pool:
        t.join()


# 2. Using concurrent.futures - Higher level and generally preferred
@elapsed_seconds
def pool_threading():
    with ThreadPoolExecutor() as executor:
        executor.map(monte_carlo, simulation_chunks)  # returns generator and hence lazy in nature!
    
    # print([p for p in probs])


if __name__ == "__main__":
    pool_threading()
        