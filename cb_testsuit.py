#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from unittest_Monitoring import TestMonitoring
from unittest_Records import TestRecords


# In[4]:



def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult() 
    suite.addTest(unittest.makeSuite(TestMonitoring)) 
    suite.addTest(unittest.makeSuite(TestRecords)) 
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
    
my_suite()

