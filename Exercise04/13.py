import numpy as np

# Parameter der Grundgesamtheit
mu_true = 2
sigma_true = np.sqrt(3)
var_true = 3

sizes = [100, 1000, 10000]

print(f"{'n':>7} | {'Mittelwert (Schätzer)':>22} | {'Varianz (Schätzer)':>20}")
print("-" * 55)

for n in sizes:
    # Erzeuge Stichprobe aus N(mu, sigma)
    sample = np.random.normal(mu_true, sigma_true, n)
    
    # Berechne Punktschätzer
    mean_est = np.mean(sample)
    var_est = np.var(sample, ddof=1) # ddof=1 für n-1 Korrektur
    
    print(f"{n:7d} | {mean_est:22.4f} | {var_est:20.4f}")