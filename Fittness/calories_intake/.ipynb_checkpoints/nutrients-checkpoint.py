class Nutrients:
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def display(self):
        print('You have consumed {:.2f} grams {} today.'.format(self.amount, self.name))


class Protein(Nutrients):
    
    def __init__(self, name, amount, calPerGram=4):
        Nutrients.__init__(self, name, amount)
        self.calPerGram = calPerGram
        
    def protCal(self):
        return self.amount * self.calPerGram
        
    def displaypCalories(self):
        Nutrients.display(self)
        toAmount = self.amount * self.calPerGram
        print('Calories intaken from protein is {:.2f}.'.format(toAmount))


class Fat(Nutrients):
    
    def __init__(self, name, amount, calPerGram=9):
        Nutrients.__init__(self, name, amount)
        self.calPerGram = calPerGram
        
    def fatCal(self):
        return self.amount * self.calPerGram
        
    def displayfCalories(self):
        Nutrients.display(self)
        toAmount = self.amount * self.calPerGram
        print('Calories intaken from fat is {:.2f}.'.format(toAmount))


class Carbohydrate(Nutrients):
    
    def __init__(self, name, amount, calPerGram=4):
        Nutrients.__init__(self, name, amount)
        self.calPerGram = calPerGram
        
    def carbCal(self):
        return self.amount * self.calPerGram
        
    def displaycCalories(self):
        Nutrients.display(self)
        toAmount = self.amount * self.calPerGram
        print('Calories intaken from carbohydrate is {:.2f}.'.format(toAmount))


def entry():
    
    try:
        proteinIntake = float(input('How many protein have you consumed in gram?'))
        fatIntake = float(input('How many fat have you consumed in gram?'))
        carbIntake = float(input('How many carbohydrate have you consumed in gram?'))
        
        weight = float(input('What is your weight in kg?'))
        height = float(input('What is your height in cm?'))
        age = int(input('What is your current age?'))
        sex = input('What is your gender? (m/f)')
        
    except ValueError as e:
        print('Please enter a valid value')
        entry()
        
    print('Choose your activity level:')
    print('1 - Sedentary (little or no exercise)')
    print('2 - Lightly active (exercise 1-3 days/week)')
    print('3 - Moderately active (exercise 3-5 days/week)')
    print('4 - Active (exercise 6-7 days/week)')
    print('5 - Very active (hard exercise 6-7 days/week)')
    answer = input()
    if answer == '1':
        act_fact = 1.2
    elif answer == '2':
        act_fact = 1.375
    elif answer == '3':
        act_fact = 1.55
    elif answer == '4':
        act_fact = 1.725
    elif answer == '5':
        act_fact = 1.9
    else:
        raise ValueError('Please choose a valid number')
        entry()
        
    calCalories(proteinIntake, fatIntake, carbIntake)
    bodyNeeds(weight, height, sex, age, proteinIntake, fatIntake, carbIntake, act_fact)
    
    
def calCalories(protI, fatI, carbI):
    prot = Protein('protein', protI, 4)
    fat = Fat('fat', fatI, 9)
    carb = Carbohydrate('carbohydrate', carbI, 4)
#     print('Summary:')
#     prot.displaypCalories()
#     fat.displayfCalories()
#     carb.displaycCalories()
    totalCalo = prot.protCal() + fat.fatCal() + carb.carbCal()
    return totalCalo
    
    
def bodyNeeds(w, h, s, age, proAmt, fatAmt, carbAmt, fac):
    prot = Protein('protein', proAmt, 4)
    fat = Fat('fat', fatAmt, 9)
    carb = Carbohydrate('carbohydrate', carbAmt, 4)
    totalCalo = prot.protCal() + fat.fatCal() + carb.carbCal()
    rdaPro = 0.8 * w
    rdaFat = 0.3 * totalCalo
    rdaCarb = 0.65 * totalCalo
    if s == 'f':
        bmr = (447.6 + 9.25 * w) + (3.10 * h) - (4.33 * age)
        amr = round(bmr * fac, 0)
    elif s == 'm':
        bmr = (88.4 + 13.4 * w) + (4.8 * h) - (5.68 * age)
        amr = round(bmr * fac, 0)
    if prot.amount < rdaPro:
        diffP = rdaPro - prot.protCal()
        print('You need to intake {:.2f} more calorie from protein!'.format(diffP))
    if fat.amount > rdaFat:
        diffF = fat.amount - rdaFat
        print('You need to cut your daily fat intake by {:.2f} grams!'.format(diffF))
    elif fat.amount < rdaFat and totalCalo <= bmr:
        diffF = rdaFat - fat.amount
        print('You need to intake {:.2f} more calorie from fat!'.format(diffF))
    if carb.amount > rdaCarb:
        diffC = carb.amount - rdaCarb
        print('You need to cut your daily carbohydrate intake by {:.2f} grams!'.format(diffC))
    elif carb.amount < 0.45 * totalCalo and totalCalo <= bmr:
        diffC = rdaCarb - carb.amount
        print('You need to intake {:.2f} more calorie from carbohydrate!'.format(diffC))
    
    if totalCalo > amr:
        diffCal = totalCalo - amr
        return 'You need to cut down your daily calorie intake or do more exercise!'
    elif totalCalo == amr:
        return 'You are doing great to maintain your weight!'
    else:
        diffCal = amr - totalCalo
        return 'You need to intake more calories daily!'
    