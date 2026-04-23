import random

def simulate_coin_tosses(n_simulations=100_000):
    # 0 steht für Kopf (Heads), 1 steht für Zahl (Tails)
    count_condition_met = 0  # Wie oft tritt Bedingung A (mind. 2x Kopf) ein?
    count_event_and_condition = 0  # Wie oft tritt Bedingung A UND Ereignis B ein?

    for _ in range(n_simulations):
        # Simuliere 3 Münzwürfe
        tosses = [random.choice(['H', 'T']) for _ in range(3)]
        # print(f"Würfe: {tosses}")  # Debug-Ausgabe der Würfe
        # Bedingung A: Mindestens 2-mal Kopf ('H')
        heads_count = tosses.count('H')
        
        if heads_count >= 2:
            count_condition_met += 1
            
            # Ereignis B: Zahl ('T') beim dritten Wurf
            if tosses[2] == 'T':
                count_event_and_condition += 1

    # Schätzung der bedingten Wahrscheinlichkeit
    if count_condition_met > 0:
        estimated_prob = count_event_and_condition / count_condition_met
        return estimated_prob
    return 0

# Ausführung
n = 100000
result = simulate_coin_tosses(n)

print(f"Simulation mit {n} Durchläufen:")
print(f"Geschätzte bedingte Wahrscheinlichkeit: {result:.4f}")
print(f"Theoretischer Wert: {1/4}")