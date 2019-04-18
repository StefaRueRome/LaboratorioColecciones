from custom_functions import temperature_methods


lista_temp_santander=[]

for i in range(0, 12):
	temperaturas_santander=int(input("Ingrese la temperatura del mes {} del departamento de santander:".format(i+1)))

	lista_temp_santander.append(temperaturas_santander)


prom_temp_santander=int(temperature_methods.calcula_promedio(lista_temp_santander))
print("El promedio de las temperaturas del departamento de santander es de {}°C".format(prom_temp_santander))

mes_caliente_santander=temperature_methods.mes_caliente(lista_temp_santander)
print("El mes mas caliente en el departamento de santander fue:", mes_caliente_santander)

temp_mayor_santander=temperature_methods.mayor(lista_temp_santander)

sum_temp_santander=temperature_methods.sum_lista(lista_temp_santander)

desv_estandar_santander=temperature_methods.desv_estandar(lista_temp_santander)




lista_temp_narinno=[]

for i in range(0, 12):
	temperaturas_narinno=int(input("Ingrese la temperatura del mes {} del departamento de Nariño:".format(i+1)))

	lista_temp_narinno.append(temperaturas_narinno)

prom_temp_narinno=int(temperature_methods.calcula_promedio(lista_temp_narinno))
print("El promedio de las tempertauras del departamento de Nariño es de {}°C:".format(prom_temp_narinno))

mes_caliente_narinno=temperature_methods.mes_caliente(lista_temp_narinno)
print("El mes mas caliente en el departamento de Nariño fue:", mes_caliente_narinno)

temp_mayor_narinno=temperature_methods.mayor(lista_temp_narinno)

sum_temp_narinno=temperature_methods.sum_lista(lista_temp_narinno)

desv_estandar_narinno=temperature_methods.desv_estandar(lista_temp_narinno)




lista_temp_guajira=[]

for i in range(0, 12):
	temperaturas_guajira=float(input("Ingrese la temperatura del mes {} del departamento de la Guajira:".format(i+1)))

	lista_temp_guajira.append(temperaturas_guajira)

prom_temp_guajira=int(temperature_methods.calcula_promedio(lista_temp_guajira))
print("El promedio de las temperaturas del departamento de la Guajira es de {}°C:".format(prom_temp_guajira))

mes_caliente_guajira=temperature_methods.mes_caliente(lista_temp_guajira)
print("El mes mas caliente en el departamento de la Guajira fue:", mes_caliente_guajira)

temp_mayor_guajira=temperature_methods.mayor(lista_temp_guajira)

sum_temp_guajira=temperature_methods.sum_lista(lista_temp_guajira)

desv_estandar_guajira=temperature_methods.desv_estandar(lista_temp_guajira)



'''Promedio de la temperatura a nivel nacional'''

prom_nacional=int((sum_temp_santander+sum_temp_narinno+sum_temp_guajira)/36)
print("El promedio de las temperaturas a nivel nacional es de {}°C".format(prom_nacional))

''' Promedio de las temperaturas de los meses mas calientes de los tres departamentos'''

prom_temp_3dprts=int((temp_mayor_santander+temp_mayor_narinno+temp_mayor_guajira)/3)
print("El promedio de las temperaturas de los meses mas calientes de los tres departamentos es de {}°C".format(prom_temp_3dprts))

'''cual promedio de los tres departamentos fue mayor'''

if prom_temp_santander>prom_temp_narinno and prom_temp_santander>prom_temp_guajira:
	print("Del promedio de los tres departamento el mayor fue el del departamento de Santander con {}°C".format(prom_temp_santander))
else:
	if prom_temp_narinno>prom_temp_santander and prom_temp_narinno>prom_temp_guajira:
		print("Del promedio de los tres departamento el mayor fue el del departamento de Nariño con {}°C".format(prom_temp_narinno))
	else:
		if prom_temp_guajira>prom_temp_santander and prom_temp_guajira>prom_temp_narinno:
			print("Del promedio de los tres departamento el mayor fue el del departamento de la Guajira con {}°C".format(prom_temp_guajira))

'''Cual fue la temperatura mas caliente en todo el año, en que mes se presentó y en que departamento'''

if temp_mayor_santander>temp_mayor_narinno and temp_mayor_santander>temp_mayor_guajira:
	print("La temperatura mas caliente que se presentó en todo el año fue {}°C, se presentó en el mes de {} en el departamento de Santander".format(temp_mayor_santander,mes_caliente_santander))
else:
	if temp_mayor_narinno>temp_mayor_santander and temp_mayor_narinno>temp_mayor_guajira:
		print("La temperatura mas caliente que se presentó en todo el año fue {}°C, se presentó en el mes de {} en el departamento de Nariño".format(temp_mayor_narinno,mes_caliente_narinno))
	else:
		if temp_mayor_guajira>temp_mayor_santander and temp_mayor_guajira>temp_mayor_narinno:
			print("La temperatura mas caliente que se presentó en todo el año fue {}°C, se presentó en el mes de {} en el departamento de La Guajira".format(temp_mayor_guajira,mes_caliente_guajira))

'''Desviacion estandar de los tres departamentos'''

print("La desviacion estándar del departamento de Santander es:", desv_estandar_santander)

print("La desviacion estándar del departamento de Nariño es:", desv_estandar_narinno)

print("La desviacion estándar del departamento de la Guajira es:", desv_estandar_guajira)