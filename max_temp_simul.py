import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def simulate_max_temperature_time(num_simulations, delta_t):
    max_temperature_times = []

    for _ in range(num_simulations):
        # Initialize temperature at time 0
        temperature = 0
        max_temperature = temperature
        max_temperature_time = 0

        # Corrected usage of np.arange function
        for t in np.arange(0, 1, delta_t):
            # Update temperature using normal distribution
            temperature_change = np.random.normal(
                loc=0, scale=np.sqrt(delta_t), size=1)
            temperature += temperature_change

            # Update max temperature and time
            if temperature > max_temperature:
                max_temperature = temperature
                max_temperature_time = t

        # Store the time at which temperature is maximum
        max_temperature_times.append(max_temperature_time)

    return max_temperature_times


# Experiment with different delta_t values
delta_t_values = [0.01, 0.005, 0.001, 0.0001, 0.00001]
num_simulations = 10000

print("starting")

# Create subplots for each delta_t
fig, axs = plt.subplots(len(delta_t_values), 2, figsize=(
    12, 2 * len(delta_t_values)), sharex=True, constrained_layout=True)

# Define colors for each delta_t
colors = ['blue', 'orange', 'green', 'red', 'purple']


# Perform Monte Carlo simulation for each delta_t and plot histograms and kernel density plots
for i, (delta_t, color) in enumerate(zip(delta_t_values, colors)):
    print("starting", delta_t, color)
    max_temperature_times = simulate_max_temperature_time(
        num_simulations, delta_t)
    print("almost complete", "just finished", delta_t, color)
    # Plot histogram
    axs[i, 0].hist(max_temperature_times, bins=50,
                   alpha=0.5, color=color, density=True)
    axs[i, 0].set_title(f'Histogram (Delta_t = {delta_t})')
    axs[i, 0].set_xlabel('Time at Max Temperature')
    axs[i, 0].set_ylabel('Density')

    # Plot kernel density plot
    sns.kdeplot(max_temperature_times, color=color, ax=axs[i, 1])
    axs[i, 1].set_title(f'Kernel Density Plot (Delta_t = {delta_t})')
    axs[i, 1].set_xlabel('Time at Max Temperature')
    axs[i, 1].set_ylabel('Density')
print("completed")
plt.show()
print("done")
