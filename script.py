import matplotlib.pyplot as plt


class CalculadoraHipoteca:
    def __init__(self, principal, años, tasa_interes):
        self.principal = principal
        self.años = años
        self.tasa_interes = tasa_interes
        self.pagos_capital = []
        self.pagos_interes = []
        self.saldo_restante = []

    def calcular_pago_mensual(self):
        meses = self.años * 12
        tasa_mensual = self.tasa_interes / 12
        if tasa_mensual == 0:
            return self.principal / meses
        return (
            self.principal
            * tasa_mensual
            * (1 + tasa_mensual) ** meses
            / ((1 + tasa_mensual) ** meses - 1)
        )

    def calcular_amortizacion(self):
        meses_totales = self.años * 12
        tasa_mensual = self.tasa_interes / 12
        saldo = self.principal
        pago_mensual = self.calcular_pago_mensual()

        for _ in range(meses_totales):
            interes = saldo * tasa_mensual
            capital = pago_mensual - interes
            saldo -= capital
            self.pagos_capital.append(capital)
            self.pagos_interes.append(interes)
            self.saldo_restante.append(saldo)

    def graficar_resultados(self):
        meses = list(range(1, self.años * 12 + 1))

        plt.figure(figsize=(12, 8))
        plt.plot(meses, self.pagos_capital, label="Pago al Capital")
        plt.plot(meses, self.pagos_interes, label="Pago de Intereses")
        plt.plot(meses, self.saldo_restante, label="Saldo Restante")
        plt.xlabel("Meses")
        plt.ylabel("Monto en $")
        plt.title("Desglose del Pago de la Hipoteca")
        plt.legend()
        plt.grid(True)
        plt.show()


# Funciones para obtener valores del usuario
def obtener_valor_numerico(prompt, tipo=float, min_valor=None, max_valor=None):
    while True:
        try:
            valor = tipo(input(prompt))
            if (min_valor is not None and valor < min_valor) or (
                max_valor is not None and valor > max_valor
            ):
                print(f"Por favor, ingrese un valor entre {min_valor} y {max_valor}.")
            else:
                return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


# Entrada del usuario
P = obtener_valor_numerico("Ingrese el principal del préstamo: ", float, 0)
y = obtener_valor_numerico("Ingrese el número de años: ", int, 1)
r = obtener_valor_numerico(
    "Ingrese la tasa de interés anual (en decimal, por ejemplo, 0.04 para 4%): ",
    float,
    0,
)

# Crear instancia de CalculadoraHipoteca y realizar cálculos
calculadora = CalculadoraHipoteca(P, y, r)
calculadora.calcular_amortizacion()

# Calcular y mostrar el pago mensual
pago_mensual = calculadora.calcular_pago_mensual()
print(f"El pago mensual es: ${pago_mensual:.2f}")

# Graficar resultados
calculadora.graficar_resultados()
