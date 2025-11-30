import pandas as pd
import matplotlib.pyplot as plt

def main():

    # Cargar dataset del autograder (columnas: year, month, day, temperature)
    df = pd.read_csv("phx.csv")

    # Crear columna de fecha
    df["Date"] = pd.to_datetime(df[["year", "month", "day"]])

    # Convertir Fahrenheit → Celsius
    df["Temperature_C"] = (df["temperature"] - 32) * 5 / 9

    # =====================================
    # Cálculos solicitados
    # =====================================

    # Índices
    idx_min = df["Temperature_C"].idxmin()
    idx_max = df["Temperature_C"].idxmax()

    # Datos mínimos
    fecha_min = df.loc[idx_min, "Date"]
    temp_min = df.loc[idx_min, "Temperature_C"]

    # Datos máximos
    fecha_max = df.loc[idx_max, "Date"]
    temp_max = df.loc[idx_max, "Temperature_C"]

    # Promedio
    temp_prom = df["Temperature_C"].mean()

    # =====================================
    # Impresiones EXACTAS para autograder
    # =====================================

    print(f"El día con la temperatura mínima en Phoenix fue: {fecha_min.date()}")
    print(f"La temperatura mínima registrada en Phoenix fue de: {temp_min:.2f} °C")

    print(f"El día con la temperatura máxima en Phoenix fue: {fecha_max.date()}")
    print(f"La temperatura máxima registrada en Phoenix fue de: {temp_max:.2f} °C")

    print(f"La temperatura promedio durante 2016 en Phoenix fue de: {temp_prom:.2f} °C")

    # =====================================
    # Gráfica
    # =====================================

    plt.figure(figsize=(10, 5))
    plt.scatter(df["Date"], df["Temperature_C"])
    plt.xticks(rotation=90)
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura (°C)")
    plt.title("Temperatura en Phoenix durante 2016")

    plt.tight_layout()
    plt.savefig("temperatura_phoenix_2016.png")
    plt.close()

    # Guardar CSV convertido
    df[["Date", "Temperature_C"]].to_csv("data_celsius.csv", index=False)


if __name__ == "__main__":
    main()
