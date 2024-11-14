import time

from utils import simulation_chunks, elapsed_seconds
from .cpu_bound_simulation import monte_carlo

# Sequential way
@elapsed_seconds
def sequential_exec(simulation_chunks):

    start_time = time.time()

    for sims in simulation_chunks:
        monte_carlo(sims)
        
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Total time: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    sequential_exec(simulation_chunks)