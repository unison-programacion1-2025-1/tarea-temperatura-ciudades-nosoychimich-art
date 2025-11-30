import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# 1. FUNCIÓN PARA CONVERTIR K → C
# =====================================
def kelvin_to_celsius(k):
    return k - 273.15


def main():

    # =====================================
    # 2. CARGAR DATASET ORIGINAL
    # =====================================
    df = pd.read_csv("data.csv")

    # =====================================
    # 3. CONVERTIR TODAS LAS CIUDADES A °C
    # =====================================
    df_celsius = pd.DataFrame()
    df_celsius["Date"] = df["Date"]
    df_celsius["San Diego"] = df["San Diego"].apply(kelvin_to_celsius)
    df_celsius["Phoenix"] = df["Phoenix"].apply(kelvin_to_celsius)
    df_celsius["Toronto"] = df["Toronto"].apply(kelvin_to_celsius)

    # =====================================
    # 4. ANÁLISIS DE PHOENIX
    # =====================================

    idx_min = df_celsius["Phoenix"].idxmin()
    idx_max = df_celsius["Phoenix"].idxmax()

    fecha_min = df_celsius.loc[idx_min, "Date"]
    fecha_max = df_celsius.loc[idx_max, "Date"]

    temp_min = df_celsius.loc[idx_min, "Phoenix"]
    temp_max = df_celsius.loc[idx_max, "Phoenix"]

    temp_prom = df_celsius["Phoenix"].mean()

    print(f"El día con la temperatura mínima en Phoenix fue: {fecha_min}")
    print(f"La temperatura mínima registrada en Phoenix fue de: {temp_min:.2f} °C")

    print(f"El día con la temperatura máxima en Phoenix fue: {fecha_max}")
    print(f"La temperatura máxima registrada en Phoenix fue de: {temp_max:.2f} °C")

    print(f"La temperatura promedio durante 2016 en Phoenix fue de: {temp_prom:.2f} °C")

    # =====================================
    # 5. GRAFICAR DISPERSIÓN
    # =====================================

    plt.figure(figsize=(10, 5))
    plt.scatter(df_celsius["Date"], df_celsius["Phoenix"])
    plt.xticks(rotation=90)
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura (°C)")
    plt.title("Temperatura en Phoenix durante 2016")

    plt.tight_layout()
    plt.savefig("temperatura_phoenix_2016.png")
    plt.close()

    # =====================================
    # 6. EXPORTAR CSV
    # =====================================

    df_celsius.to_csv("data_celsius.csv", index=False)


if __name__ == "__main__":
    main()
