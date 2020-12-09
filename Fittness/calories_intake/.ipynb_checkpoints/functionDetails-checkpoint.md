### **Subpackage - calories_intake**

This subpackage contains two modules: *__nutrients__* and *__visualization__*.

#### **nutrients** module:

- a super class **Nutrients** has self, name and amount attributes, and a display method. **Protein**, **Fat**, and **Carbohydrate** are 3 subclasses of **Nutrients** class, which inherent attributes and methods from **Nutrients** and also have attribute calPerGram (calories per gram of the nutrient) as well as their own method to calculate and display total calories. 

- **entry()** function obtains information from the user for daily protein, fat, and carbohydrate intakes in gram, as well as user's weight(kg), height(cm), age, sex, and activity level. 

- **calCalories(protI, fatI, carbI)** function takes the user inputs for protein, fat, and carbohydrate intakes and creates an object of each nutrients class to print the total calories from all three nutrients intake.

- **bodyNeeds(w, h, s, age, proAmt, fatAmt, carbAmt, fac)** function takes user's weight(g), height(cm), sex, age, and activity level (by choose one of the options) as well as daily protein, fat, and carbohydrate intake to print the summaries and suggestions for three different nutrients intake, and for the total calorie intake based on activity level and dietray intake.

#### **visualization** module:

- **entry()** function obtains amount of each of three nutrients daily intake in a certain of time period into a list. This function asks for 3 list input, each of them needs to be at least 7 elements long and all 3 lists need to have the same length. Otherwise, errors will be thrown. It also calculates the calories intake based on the 3 nutrients.

- **nutriTrack(lst1, lst2, lst3, lst4)** function takes all 3 lists of protein, fat, and carbohydrate intake, as well as the sequential number of days to show 3 linked plots. Each of the plot tracks the amount change of the nutrient over time in that particular period. 

- **calorieTrack(lst1, lst2, num)** function takes the list of daily calories intake calulated by the **entry()** function in a particular period, as well as the sequential number of days to show the graph of daily total calories intake over time. The calorie intake for a specific day can be obtained when hover on each point on the graph.