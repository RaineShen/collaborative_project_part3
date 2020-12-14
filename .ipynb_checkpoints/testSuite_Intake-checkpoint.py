import unittest
from test_nutrients import TestNutrients
from test_visualization import TestVisualization

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestNutrients))
    suite.addTest(unittest.makeSuite(TestVisualization))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
my_suite()