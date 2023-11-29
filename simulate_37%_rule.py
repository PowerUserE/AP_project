
import random
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("module did not install")


def simulate_37_percent_rule(num_papers, exploration_percentage):
    papers = [random.randint(1, 1000) for _ in range(num_papers)]
    random.shuffle(papers)

    exploration_threshold = int(exploration_percentage * num_papers)
    explored_papers = papers[:exploration_threshold]

    max_explored = max(explored_papers)
    remaining_papers = papers[exploration_threshold:]
    for p in remaining_papers:
        if p > max_explored:
            if p == max(papers):
                return True
            else:
                return False
    return False


def run_simulations(num_simulations, num_papers, exploration_percentage):
    success_rates = []

    for _ in range(num_simulations):
        if simulate_37_percent_rule(num_papers, exploration_percentage):
            success_rates.append(1)
        else:
            success_rates.append(0)

    cumulative_success_rates = [
        sum(success_rates[:i+1]) / (i+1) for i in range(num_simulations)]
    return cumulative_success_rates


# Example: Run 1000 simulations with 100 papers and 37% exploration
num_simulations = 1000
num_papers = 100
exploration_percentage = 0.37

success_rates = run_simulations(
    num_simulations, num_papers, exploration_percentage)
print("currently running")

# Plot the results on a line graph
plt.plot(range(1, num_simulations+1), success_rates)
plt.xlabel('Number of Simulations')
plt.ylabel('Cumulative Success Rate')
plt.title('37% Rule Simulation Results')
plt.show()
