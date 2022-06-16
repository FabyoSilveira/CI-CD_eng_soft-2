from unittest import TestCase
from Calculator import Calculator

class CalculatorTest(TestCase):
  
  def setUp(self):
    self.calc = Calculator()

  def test_sum(self):
    self.assertEqual(9, self.calc.sum(4,5))

  def test_sub(self):
    self.assertEqual(-1, self.calc.sub(4,5))

  def test_mult(self):
    self.assertEqual(16, self.calc.mult(4,4))
  
  def test_div(self):
    self.assertEqual(2, self.calc.div(4,2))

  def test_sum_after_mult(self):
    multResutl = self.calc.mult(4,5)

    self.assertEqual(24, self.calc.sum(4,multResutl))

