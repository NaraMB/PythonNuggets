import random

from utils import elapsed_seconds

# Creating a normal distribution with 100k samples with mean 0 and std.dev = 2

# If you've scipy installed, defintiely use scipy for vectorized operation
# from scipy.stats import norm
# X = norm(loc=0, scale=2).rvs(size=100000)

X = [random.normalvariate(mu=0, sigma=2) for _ in range(100000)]

@elapsed_seconds
def monte_carlo(simulations):
    print(f"starting....{simulations} simulations")
    error = []
    for s in range(simulations):
        Rl=[]
        S = random.choice([1,-1])
        for i in range(3):
            N = random.choice(X)
            R = 1 if (S+N)>=0 else -1
            Rl.append(R)

        if S==1 and sum(Rl)<0:
            error.append(1)
        if S==-1 and sum(Rl)>0:
            error.append(1)
            
    print(f"completed... {simulations} simulations")
    return sum(error)/simulations