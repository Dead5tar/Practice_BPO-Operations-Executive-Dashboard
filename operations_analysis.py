import pandas as pd

# 1. Simulacion de un Dataset que combina operaciones de BPO y Confección/Manufactura
data = {
    'employee_id': [101, 102, 103, 104, 105, 106, 107, 108],
    'sector': ['BPO', 'BPO', 'Manufacturing', 'Manufacturing', 'BPO', 'BPO', 'Manufacturing', 'Manufacturing'],
    'shift': ['Night', 'Day', 'Day', 'Night', 'Night', 'Day', 'Day', 'Night'],
    'idle_time_minutes': [45, 12, 10, 35, 50, 15, 8, 40],
    'units_or_calls_processed': [120, 310, 450, 280, 110, 290, 470, 260],
    'resigned_within_3_months': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)

print("--- DATOS ORIGINALES CARGADOS ---")
print(df.head())

# 2. Análisis con Pandas: Promedio de Tiempos Muertos por Sector y Turno
print("\n--- PROMEDIO DE TIEMPOS MUERTOS (IDLE TIME) POR SECTOR Y TURNO ---")
summary = df.groupby(['sector', 'shift'])['idle_time_minutes'].mean().reset_index()
print(summary)

# 3. Filtrar el riesgo: Empleados con alto tiempo muerto (> 30 mins) que terminaron renunciando
print("\n--- ALERTA: EMPLEADOS CON ALTO TIEMPO MUERTO Y RIESGO DE RENUNCIADA ---")
high_risk = df[(df['idle_time_minutes'] > 30) & (df['resigned_within_3_months'] == 'Yes')]
print(high_risk[['employee_id', 'sector', 'shift', 'idle_time_minutes']])
