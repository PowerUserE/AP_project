import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




def simulate_game(num_cards=100, num_repetitions=10000):
    hits = np.zeros(num_repetitions)
    for i in range(num_repetitions):
        # +1 because cards are numbered from 1 to 100
        deck = np.random.permutation(num_cards) + 1
        hits[i] = sum(deck[j] == j+1 for j in range(num_cards))
    return hits




hits = simulate_game()


# Calculate expectation (mean) and variance
expectation = np.mean(hits)
variance = np.var(hits)


print(f'Expectation: {expectation}')
print(f'Variance: {variance}')


# Plot histogram
plt.hist(hits, bins=range(int(min(hits)), int(
    max(hits)) + 2), alpha=0.7, edgecolor='black')
plt.title('Histogram of Hits')
plt.xlabel('Number of Hits')
plt.ylabel('Frequency')
plt.show()
