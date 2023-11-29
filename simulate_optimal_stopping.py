import random
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Matplotlib is not installed. Please install it to run this script.")


def simulate_exploration_rule(num_papers, exploration_percentage, value_range):
    papers = [random.randint(*value_range) for _ in range(num_papers)]
    random.shuffle(papers)

    # Determine the threshold for exploration
    # Set a minimum exploration threshold of 1
    exploration_threshold = max(1, int(exploration_percentage * num_papers))

    # Explore the first 'exploration_threshold' papers
    explored_papers = papers[:exploration_threshold]

    # Select the first paper with a number greater than any explored before
    max_explored = max(explored_papers)
    remaining_papers = papers[exploration_threshold:]

    for p in remaining_papers:
        if p > max_explored:
            if p == max(papers):
                return True
            else:
                return False
    return False


def run_simulations(num_simulations, num_papers, exploration_percentage, value_range):
    successful_selections = 0

    for _ in range(num_simulations):
        if simulate_exploration_rule(num_papers, exploration_percentage, value_range):
            successful_selections += 1

    success_rate = successful_selections / num_simulations
    return success_rate


# Run simulations for exploration percentages from 1% to 99%
exploration_percentages = range(1, 100)
success_rates = []

for exploration_percentage in exploration_percentages:
    exploration_percentage /= 100  # Convert to decimal
    success_rate = run_simulations(
        10000, 1000, exploration_percentage, (1, 10000))
    success_rates.append(success_rate)

# Find the exploration percentage with the maximum success rate
max_success_rate = max(success_rates)
max_index = success_rates.index(max_success_rate)
max_exploration_percentage = exploration_percentages[max_index]

# Plot the results
plt.plot(exploration_percentages, success_rates,
         marker='o', label='Success Rate')
plt.scatter(max_exploration_percentage, max_success_rate,
            color='red', label=f'Max: {max_success_rate:.2%}')
plt.title('Success Rate vs Exploration Percentage')
plt.xlabel('Exploration Percentage')
plt.ylabel('Success Rate')
plt.legend()  # Show legend with labels
plt.grid(True)
plt.show()
