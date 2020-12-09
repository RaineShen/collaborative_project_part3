from monitoring import Monitoring
from  records import Records


# name = input("Please Enter name: ")
# weight= int(input("Please Enter your weight in kg: "))
# calories=int(input("Please Enter your burned calory in kcal: "))



M1=Monitoring("yuxuan","female",22,174,55,1778)
M1.new_weight(55)
M1.new_calory(1893)
M1.new_weight(56.4)
M1.new_calory(1993)
M1.new_weight(57.4)
M1.new_calory(1893)
M1.new_weight(58.4)
M1.new_calory(1893)
M1.new_weight(58.4)
M1.weight_calory_plot()
