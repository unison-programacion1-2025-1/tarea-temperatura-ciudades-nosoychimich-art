import pandas as pd

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    # 1. Leer el archivo original
    df = pd.read_csv("data.csv")

    # 2. Agregar columnas convertidas
    df["Temperatura_C"] = df["Temperatura_K"].apply(kelvin_to_celsius)
    df["Temperatura_F"] = df["Temperatura_K"].apply(kelvin_to_fahrenheit)

    # 3. Obtener estadísticas
    prom = df["Temperatura_C"].mean()
    ciudad_caliente = df.loc[df["Temperatura_C"].idxmax(), "Ciudad"]
    ciudad_fria = df.loc[df["Temperatura_C"].idxmin(), "Ciudad"]

    print("=== Estadísticas ===")
    print(f"Temperatura promedio (°C): {prom:.2f}")
    print(f"Ciudad más caliente: {ciudad_caliente}")
    print(f"Ciudad más fría: {ciudad_fria}")

    # 4. Guardar archivo convertido
    df.to_csv("temperaturas_convertidas.csv", index=False)

if __name__ == "__main__":
    main()


