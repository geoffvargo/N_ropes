from unittest import TestCase
from n_ropes import *


class Test(TestCase):
	def setUp(self) -> None:
		self.test_1 = [4, 3, 2, 6]
		self.test_2 = [4, 3, 2, 6, 5, 7, 12]
		self.test_3 = [1, 1, 1, 1, 1, 1]
		self.result_1 = 29
		self.result_2 = 103
		self.result_3 = 2
	
	def test_n_ropes__1(self):
		print(f'input = {self.test_1}')
		print(f'expected output = {self.result_1}')
		output_1 = n_ropes(self.test_1)
		print(f'actual output = {output_1}')
		self.assertEqual(output_1, self.result_1)
		print()
	
	def test_n_ropes__2(self):
		print(f'input = {self.test_2}')
		print(f'expected output = {self.result_2}')
		output_2 = n_ropes(self.test_2)
		print(f'actual output = {output_2}')
		self.assertEqual(output_2, self.result_2)
		print()
	
	def test_n_ropes__3(self):
		print(f'input = {self.test_3}')
		print(f'expected output = {self.result_3}')
		output_3 = n_ropes(self.test_3)
		print(f'actual output = {output_3}')
		self.assertEqual(output_3, self.result_3)
		print()
