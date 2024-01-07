# Tmax.py

import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(dt, T):
    t = np.arange(0, T+dt, dt)
    dW = np.sqrt(dt) * np.random.randn(len(t)-1)
    W = np.cumsum(dW)
    return t, W

# def estimate_proportion_positive(dt, T, num_paths):
#     count_positive = 0
#     for _ in range(num_paths):
#         t, W = brownian_motion(dt, T)
#         count_positive += np.sum(W > 0)
    
#     proportion_positive = count_positive / (num_paths * len(t))
#     return proportion_positive

def estimate_time_max_temperature(dt, T, num_paths):
    max_times = []
    for _ in range(num_paths):
        t, W = brownian_motion(dt, T)
        max_time = t[np.argmax(W)]
        max_times.append(max_time)
    
    return max_times

# Experiment with different values of dt
delta_ts = [0.0001]
num_paths = 10000

# # Plotting P
# plt.figure(figsize=(12, 5))
# plt.subplot(1, 2, 1)

# for dt in delta_ts:
#     P = estimate_proportion_positive(dt, 1, num_paths)
#     plt.bar(dt, P, width=0.0002, alpha=0.7, label=f'dt={dt}')

# plt.title('Distribution of P')
# plt.xlabel('dt')
# plt.ylabel('Proportion of Time with Positive Temperature')
# plt.legend()

# Plotting Tmax
plt.subplot(1, 2, 2)

for dt in delta_ts:
    Tmax = estimate_time_max_temperature(dt, 1, num_paths)
    plt.hist(Tmax, bins=30, density=True, alpha=0.5, label=f'dt={dt}', color = 'red')

plt.title('Distribution of Tmax')
plt.xlabel('Time')
plt.ylabel('Probability Density')
plt.legend()

plt.tight_layout()
plt.show()
