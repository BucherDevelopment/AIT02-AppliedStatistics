import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameter
mu = 3.5
var = 2.9167
n_values = [1, 2, 5, 10, 50, 100]
n_simulations = 10000

fig, axes = plt.subplots(len(n_values), 2, figsize=(12, 4 * len(n_values)))

for i, n in enumerate(n_values):
    # Simulation
    rolls = np.random.randint(1, 7, size=(n_simulations, n))
    sn = np.sum(rolls - mu, axis=1) / np.sqrt(n * var)
    sn_sorted = np.sort(sn)
    
    # --- 1. Histogramm ---
    ax_hist = axes[i, 0]
    ax_hist.hist(sn, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')
    x = np.linspace(-4, 4, 100)
    ax_hist.plot(x, norm.pdf(x, 0, 1), 'r-', lw=2, label='N(0,1) PDF')
    ax_hist.set_title(f'Histogramm n={n}')
    ax_hist.legend()

    # --- 2. Empirische CDF ---
    ax_cdf = axes[i, 1]
    # Die empirische CDF berechnet man als (1..N) / N
    y_emp = np.arange(1, n_simulations + 1) / n_simulations
    ax_cdf.step(sn_sorted, y_emp, where='post', color='blue', label='Empirische CDF')
    
    # Theoretische CDF der Normalverteilung
    ax_cdf.plot(x, norm.cdf(x, 0, 1), 'r--', lw=2, label='Theoretische CDF')
    ax_cdf.set_title(f'Empirische CDF n={n}')
    ax_cdf.legend()
    ax_cdf.grid(alpha=0.3)

plt.tight_layout()
plt.show()