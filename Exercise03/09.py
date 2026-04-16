import numpy as np

# Parameter der Aufgabe
n_trials = 2000
values = [1, 2, 3]
probabilities = [0.25, 0.15, 0.60]

# Simulation der Zufallsvariablen X
samples = np.random.choice(values, size=n_trials, p=probabilities)

# Berechnung der Schätzwerte (Estimation)
estimated_mean = np.mean(samples)
estimated_variance = np.var(samples)

print(f"Ergebnisse der Simulation (n={n_trials}):")
print(f"Geschätzter Erwartungswert: {estimated_mean:.4f}")
print(f"Geschätzte Varianz:         {estimated_variance:.4f}")

# Zum Vergleich mit den analytischen Werten
print("-" * 30)
print(f"Analytischer Erwartungswert: 2.3500")
print(f"Analytische Varianz:         0.7275")