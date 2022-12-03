import unittest
import sys
sys.path.append('..')
from calculation import Calculation

cal = Calculation()
class Test(unittest.TestCase):
    
  def test_add(self):
      val1=5
      val2=3
      predict=8
      self.assertEqual(cal.add(val1, val2), predict)


  # def test_multiply(self):
  #     val1=3
  #     val2=100
  #     predict=300
  #     self.assertEqual(cal.multiply(val1, val2), predict)

  # def input_str(self):
  #     with self.assertRaises(TypeError):
  #       cal.add(1, "vaijosf")


if __name__ == "__main__":
    unittest.main()