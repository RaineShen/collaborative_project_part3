#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pygal
import unittest
import inputcheck
from Fittness.calories_burn import records as re
from Fittness.calories_burn import monitoring 


# In[7]:


class TestMonitoring(unittest.TestCase):

    @classmethod
     
    def setUpClass(cls):
        cls.re_p1=re.Records("Mary","female",21,172,55)
        cls.re_p2=re.Records("Mike","male",24,176,65)
        print('Set up class')
        
        
    def setUp(self):
        self.M1=monitoring.Monitoring("Mary","female",21,172,55,1390)
        self.M2=monitoring.Monitoring("Mike","male",24,176,65,2340)
        # incorrect set up
        self.M3=monitoring.Monitoring("M2","male",-1,1.76,650,-2340)
        print('Set up')
        
        
    def test_init(self):
        print("test initialization")
        self.assertEqual(self.M1.calories,1390)
        self.assertEqual(self.M2.calories,2340)
        self.assertEqual(self.M1.name,self.re_p1.name)
        self.assertEqual(self.M2.name,self.re_p2.name)
        self.assertEqual(self.M1.age,self.re_p1.age)
        self.assertEqual(self.M2.age,self.re_p2.age)
        try:
            if self.M3.age <0:
                raise inputcheck.Ageerror()

        except inputcheck.Ageerror:
            print ("age should greater than 0")
        
        try:
            if self.M3.height>200 or self.M3.height<100:
                raise inputcheck.Heighterror()

        except inputcheck.Heighterror:
            print ("please enter your height in cm")


    
    def test_new_weight(self):
        self.assertEqual(self.M1.new_weight(55.7),self.M1.weight_list)
        self.assertEqual(self.M1.new_weight(54.9),self.M1.weight_list)
        self.assertEqual(self.M2.new_weight(65.7),self.M2.weight_list)
        self.assertEqual(self.M2.new_weight(64.9),self.M2.weight_list)
        self.assertEqual(self.M3.new_weight(-65.7),self.M3.weight_list)
        self.assertEqual(self.M3.new_weight(-900),self.M3.weight_list)
        try:
            if self.M3.weight_list[-1]>200 or self.M3.weight_list[-1]<25:
                raise inputcheck.weightterror()

        except inputcheck.weightterror:
            print ("please enter your weight in kg")




    def test_new_calory(self):
        self.assertEqual(self.M1.new_calory(1229),self.M1.calories_list)
        self.assertEqual(self.M1.new_calory(1567),self.M1.calories_list)
        self.assertEqual(self.M2.new_calory(1892),self.M2.calories_list)
        self.assertEqual(self.M2.new_calory(1233),self.M2.calories_list)
        self.assertEqual(self.M3.new_calory(-1),self.M3.calories_list)
        try:
            if self.M3.calories_list[-1]<0:
                raise ValueError("invalid calories")

        except ValueError:
            print ("please enter a valid calorties number")
       
        
        
     
    def tearDown(self):
        print('Tear Down')
        
    @classmethod   
    def tearDownClass(cls):
        print("Tear Down Class")
unittest.main(argv=[''], verbosity=2, exit=False)    

