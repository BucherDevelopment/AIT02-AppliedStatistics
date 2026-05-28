import numpy as np

# Parameter definieren
m_true = 100      # Der wahre, unbekannte Wert
n = 30            # Stichprobengröße
reitertions = 10000 # Wie oft wir das Experiment wiederholen

# Simulation: Ziehe 10.000 Mal eine Stichprobe der Größe 30
samples = np.random.randint(1, m_true + 1, size=(reitertions, n))

# Berechne das Stichprobenmittel (x-quer) für jede der 10.000 Stichproben
x_bar = np.mean(samples, axis=1)

# Berechne den Schätzer m_hut = 2 * x_bar - 1
m_hats = 2 * x_bar - 1

# Durchschnitt aller Schätzungen
mean_m_hat = np.mean(m_hats)

print(f"Wahrer Wert m: {m_true}")
print(f"Durchschnitt der Schätzer aus der Simulation: {mean_m_hat:.2f}")