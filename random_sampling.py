import random
def random_sampling_strategy_simulation(n, k, iterations):
   wins = 0
   for _ in range(iterations):
       # Phase 1: Random Sampling
       papers = list(range(1, n + 1))
       random.shuffle(papers)
       highest_encountered = max(papers[:k])

       # Phase 2: User's Maximum Hunt
       for number in papers[k:]:
           if number > highest_encountered:
               wins += 1
               break  # Exit the loop if a higher number is encountered

   # Calculate the success rate
   success_rate = wins / iterations
   print(f"Simulation Results (Iterations: {iterations}):")
   print(f"Success Rate: {success_rate:.4f}")
   return success_rate

# Example usage with n = 11, k = 7, and 10,000 iterations
n_value = 1000
sample_fraction = random.randint(1, n_value)
simulation_iterations = 10000
success_rate = random_sampling_strategy_simulation(
   n_value, sample_fraction, simulation_iterations)
