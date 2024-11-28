import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def benford_distribution(n_digits=9):
    """Genera la distribución teórica de la Ley de Benford."""
    return np.array([np.log10(1 + 1 / d) for d in range(1, n_digits + 1)])

def first_digit_analysis(series):
    """Analiza la distribución del primer dígito en una serie de números."""
    first_digits = series.astype(str).str[0].astype(int)
    counts = first_digits.value_counts(normalize=True).sort_index()
    return counts

def compare_with_benford(counts, expected):
    """Compara la distribución observada con la Ley de Benford."""
    observed = np.array([counts.get(d, 0) for d in range(1, len(expected) + 1)])
    chi_square = np.sum((observed - expected) ** 2 / expected)
    return chi_square

# Leer datos desde el archivo Excel
file_path = "Data.xlsx"
data = pd.read_excel(file_path)

# Comprobar que la columna necesaria existe
if "Followers" not in data.columns:
    raise ValueError("El archivo debe contener una columna llamada 'Followers'.")

# Distribución teórica de Benford
benford_expected = benford_distribution()

# Análisis de la columna de seguidores
followers = data["Followers"]
distribution = first_digit_analysis(followers)

# Comparación con Benford
chi_square_stat = compare_with_benford(distribution, benford_expected)
print(chi_square_stat)
# Determinar si alguna cuenta podría ser un bot
threshold = 0.5  # Valor crítico de chi-cuadrado para 8 grados de libertad (al 95% de confianza)
if chi_square_stat > threshold:
    print("La distribución no sigue la Ley de Benford. Podría haber cuentas sospechosas.")
else:
    print("La distribución sigue la Ley de Benford.")

# Graficar la comparación
plt.bar(range(1, 10), distribution, alpha=0.7, label="Observada")
plt.plot(range(1, 10), benford_expected, 'ro-', label="Benford", linewidth=2)
plt.xticks(range(1, 10))
plt.xlabel("Primer Dígito")
plt.ylabel("Frecuencia Relativa")
plt.title("Comparación con la Ley de Benford")
plt.legend()
plt.show()
