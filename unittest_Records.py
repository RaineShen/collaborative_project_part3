#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
from Fittness.calories_burn import records as re


# In[1]:


class TestRecords(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        print('Set up class')
        
    def setUp(self):
        self.p1=re.Records("Mary","female",21,172,55)
        self.p2=re.Records("Mike","male",24,176,65)
        print('Set up')
        
    def test_init(self):
        print("test initialization")
        self.assertEqual(self.p1.gender,"female")
        self.assertEqual(self.p1.name,"Mary")
        self.assertEqual(self.p1.age,21)
        self.assertEqual(self.p1.height,172)
        self.assertEqual(self.p1.weight,55)
        self.assertEqual(self.p2.gender,"male")
        self.assertEqual(self.p2.name,"Mike")
        self.assertEqual(self.p2.age,24)
        self.assertEqual(self.p2.height,176)
        self.assertEqual(self.p2.weight,65)

        
        
        
        
    def test_BMI(self):
        print("test BMI")
        self.bmi1=self.p1.weight/(self.p1.height/100)**2
        self.bmi2=self.p2.weight/(self.p2.height/100)**2
        self.assertAlmostEqual(self.bmi1,18.59,2)
        self.assertAlmostEqual(self.bmi2,20.98,2)
        self.assertEqual(self.p1.BMI(),"Hello,Mary your BMI is 18.59 which is in normal range")
        self.assertEqual(self.p2.BMI(),"Hello,Mike your BMI is 20.98 which is in normal range")
    
    
    def test_display(self):
        print("test dispaly")
        self.assertEqual(self.p1.display(),"Name: Mary Age: 21 Gender:female Height: 172cm Wegiht: 55kg")
        self.assertEqual(self.p2.display(),"Name: Mike Age: 24 Gender:male Height: 176cm Wegiht: 65kg")
        self.assertNotEqual(self.p1.display(),"Name: Mary Age: 21 Gender:male Height: 172cm Wegiht: 55kg")
        self.assertNotEqual(self.p2.display(),"Name: Mike Age: 24 Gender:female Height: 176cm Wegiht: 65kg")
    
    def tearDown(self):
        print('Tear Down')
        
    @classmethod   
    def tearDownClass(cls):
        print("Tear Down Class")
unittest.main(argv=[''], verbosity=2, exit=False)  

