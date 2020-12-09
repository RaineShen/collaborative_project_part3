#!/usr/bin/env python
# coding: utf-8

# In[164]:


import pygal
from IPython.display import SVG, display
class Records:
    def __init__(self,name,age,gender,height,weight):
        
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height  
        self.weight=weight   
        self.weight_list=[]
        self.weight_list.append(weight)
        
    
    def add_weight(self, new_weight):
        self.weight_list.append(new_weight)
        if new_weight < self.weight_list[-1]:
            d=self.weight_list[-1]-new_weight
            print("Congrats! You lost {} kg, Keep up!".format(d))
        else:
            print("Today's weight is {} kg".format(new_weight))
            
            
    def weight_change_plot(self):
        line_chart = pygal.Line()
        line_chart.title = 'Weight Changes '
        line_chart.x_title='Day'
        line_chart.y_title='kg'
        line_chart.add(self.name, self.weight_list)
        line_chart.x_labels = map(str, range(0,len(self.weight_list)))
        display(SVG(line_chart.render (disable_xml_declaration=True)))
    
    def display(self):
        print("Name: {} Age: {} Genger: {} Height: {} Wegiht:{} ".format(self.name,self.age,self.gender,self.height,self.weight))
        print("weight list{}".format(self.weight_list))



# class Exercise(Records):
#     def __init__(self,name,age,gender,height,weight,time):
#         Records.__init__(self,name,age,gender,height,weight)
#         self.time=time
#         self.time_list=[]
#         self.time_list.append(time)
        
#     def display(self):
#         print("Today's excerise time {}".format(self.time))
        
        
    


# In[184]:


class KPI(Records):
    """
    Basal metabolic rate is a measurement 
    of the number of calories needed to perform 
    your body's most basic (basal) functions, 
    like breathing, circulation and cell production. 
    BMR is most accurately measured in a lab setting under very restrictive conditions
    
    """

    """
    https://www.bmi-calculator.net/bmr-calculator/bmr-formula.php
    Harris-Benedict Equation
    Women: BMR = 655 + (9.6 x weight in kg) + (1.8 x height in cm) - (4.7 x age in years)
    Men: BMR = 66 + (13.7 x weight in kg) + (5 x height in cm) - (6.8 x age in years)
    """
    def __init__(self,name,age,gender,height,weight):
        Records.__init__(self,name,age,gender,height,weight)
    def BMR(self):
        if self.gender=="female":
            bmr= 655 + (9.6 * self.weight) + (1.8* self.height- (4.7* self.age))
        else:
            bmr= 66 + (13.7*self.weight) + (5*self.height) - (6.8*self.age)
        return bmr
            
            
            
    

    


# In[186]:


P1=Records('Yuxuan',22,'female',175,55)
P2=Records('Rain',22,'female',165,50)
P1.add_weight(50)
P1.add_weight(40)
P1.add_weight(65)
P1.weight_change_plot()
K1=KPI('Yuxuan',22,'female',175,55)

P11=Exercise('Yuxuan',22,'female',175,55,10)
P11.display()


# In[ ]:




