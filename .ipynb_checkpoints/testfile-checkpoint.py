from Fittness.calories_burn import monitoring
from Fittness.calories_burn import records




name = input("Please Enter name: ")
gender = input("Please Enter your gender (female or male): ")
age= int(input("Please Enter your age (integer): "))
height= int(input("Please Enter your height in cm: "  ))
weight= int(input("Please Enter your weight in kg: "))



P1=records.Records(name,gender,age,height,weight)
P1.display()
P1.BMI()
P1.BMR()
P1.totalcal()



print("You could calculate your burned calories for today from Records.totalcal")
calory=float(input("Please Enter your calory in cal: "))


M1=monitoring.Monitoring(name,gender,age,height,weight,calory)
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
M1.weight_change_plot()
M1.calory_change_plot()