import unittest
from custom_functions import temperature_methods

class TestCollectionMethods(unittest.TestCase):

	def prueba_calcula_promedio(self):

		temp_lista = [27, 30, 28, 29, 32, 31, 34, 35, 32, 31, 27, 26]
		prom = temperature_methods.calcula_promedio(temp_lista)

		self.assertEqual(prom, 30.16)

	def prueba_mes_caliente(self):

		temp_lista = [27, 30, 23, 29, 32, 31, 34, 37, 32, 31, 27, 25]
		mes=temperature_methods.mes_caliente(temp_lista)

		self.assertListEqual(mes, ['Agosto'])

	def prueba_sum_lista(self):

		temp_lista = [26, 30, 24, 29, 32, 31, 34, 36, 32, 35, 27, 25]
		suma=temperature_methods.sum_lista(temp_lista)

		self.assertEqual(suma, 361)

	def prueba_mayor(self):

		temp_lista = [27, 26, 28, 29, 30, 31, 34, 40, 32, 31, 27, 26]
		mayor=temperature_methods.mayor(temp_lista)

		self.assertEqual(mayor, 40)

	def prueba_desv_estandar(self):

		temp_lista = [27, 26, 28, 29, 30]
		result = temperature_methods.desv_estandar(temp_lista)

		self.assertEqual(result, 1.41)


if __name__ == '__main__':
	unittest.main()


