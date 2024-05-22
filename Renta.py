from datetime import date
import Vista

def ajustarPeriodo(periodoInicial:date, periodoFinal:date)->int:
    """
    Metodo para ajustar 
    """
    años = periodoFinal.year - periodoInicial.year
    meses = periodoFinal.month - periodoInicial.month
    if meses < 0:
        años -= 1
        meses += 12
    total_meses = años * 12 + meses

    return total_meses

def calcularValor(tasa :float, cuotas:int, periodoInicial:date, periodoFinal:date)->float:
    """
    Metodo para calcular el valor del activo dado un periodo
    """
    periodo = ajustarPeriodo(periodoInicial, periodoFinal)
    valor = cuotas*((((1+tasa)**periodo)-1)/tasa)

    return valor

def calcularCuotas(valor:float, tasa:float,periodoInicial:date, periodoFinal:date)->float:
    """
    Metodo para calcular la cantidad de cuotas que tendra el proceso
    """
    periodo = ajustarPeriodo(periodoInicial, periodoFinal)
    cuotas=valor*(tasa/(((1+tasa)**periodo) -1))

    return cuotas

if __name__ == "__main__":
    Vista.run()