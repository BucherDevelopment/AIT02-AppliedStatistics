import numpy as np

def simulate_car_rental(n_days=100_000):
    # Inventar der Station
    inventory = {1: 5, 2: 6, 3: 6}
    
    # Wahrscheinlichkeiten für die Autotypen
    car_types = [1, 2, 3]
    probabilities = [0.25, 0.35, 0.40]
    
    success_days = 0
    
    for _ in range(n_days):
        # 1. Anzahl der Kunden für diesen Tag simulieren
        # Normalverteilung (mean=16, std=2), gerundet auf Ganzzahl
        n_customers = int(round(np.random.normal(16, 2)))
        
        # Falls n_customers negativ wäre (theoretisch möglich), setzen wir es auf 0
        n_customers = max(0, n_customers)
        
        # 2. Wünsche der Kunden generieren
        customer_choices = np.random.choice(car_types, size=n_customers, p=probabilities)
        
        # 3. Zählen, wie oft jeder Typ gewünscht wurde
        unique, counts = np.unique(customer_choices, return_counts=True)
        requests = dict(zip(unique, counts))
        
        # 4. Überprüfen, ob alle Wünsche erfüllt werden können
        possible = True
        for car_type in inventory:
            # Wie viele Autos dieses Typs wurden angefragt? (0 falls nicht in requests)
            needed = requests.get(car_type, 0)
            if needed > inventory[car_type]:
                possible = False
                break
        
        if possible:
            success_days += 1
            
    return success_days / n_days

# Simulation starten
prob_success = simulate_car_rental()
print(f"Geschätzte Wahrscheinlichkeit, dass alle Kunden bedient werden: {prob_success:.4f}")