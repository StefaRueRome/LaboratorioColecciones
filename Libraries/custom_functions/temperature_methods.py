
def sum_lista(lista):
    suma = 0

    for temp in lista:
        suma += temp

    return suma


def mayor(lista):
    num_mayor=lista[0]

    for i in lista:
        if i>num_mayor:
            num_mayor=i
    return num_mayor


def calcula_promedio(lista):
    temp_sum =sum_lista(lista)
    temp_cont = len(lista)

    promedio_final = temp_sum / temp_cont

    return promedio_final


def mes_caliente(lista):
    temp_mas_caliente = mayor(lista)
    mes = []

    posicion = lista.index(temp_mas_caliente)

    if posicion == 0:
        mes.append("Enero")
    else:
        if posicion == 1:
            mes.append("Febrero")
        else:
            if posicion == 2:
                mes.append("Marzo")
            else:
                if posicion == 3:
                    mes.append("Abril")
                else:
                    if posicion == 4:
                        mes.append("Mayo")
                    else:
                        if posicion == 5:
                            mes.append("Junio")
                        else:
                            if posicion == 6:
                                mes.append("Julio")
                            else:
                                if posicion == 7:
                                    mes.append("Agosto")
                                else:
                                    if posicion == 8:
                                        mes.append("Septiembre")
                                    else:
                                        if posicion == 9:
                                            mes.append("Octubre")
                                        else:
                                            if posicion == 10:
                                                mes.append("Noviembre")
                                            else:
                                                if posicion == 11:
                                                    mes.append("Diciembre")
    return mes



def desv_estandar(lista):
    temp_sum = sum_lista(lista)
    temp_cont = len(lista)
    dif_temp = []
    suma = 0

    media = temp_sum / temp_cont

    for i in lista:
        i = i - media
        dif_temp.append((i ** 2) / temp_cont)

    for j in dif_temp:
        suma += j

    desviacion_estandar = suma ** (1 / 2)

    return desviacion_estandar
