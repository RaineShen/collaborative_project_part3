from bokeh.plotting import figure, output_file, show
from bokeh.layouts import row, gridplot
from bokeh.models import HoverTool, ColumnDataSource
        
def entry():
    
    """
    This function is for the user to enter information of the amount of each nutrient
    consumed daily for a certain period of time, in order to track nutrients and calorie
    intake during this period by using bokeh graphs.
    
    """
        
    try:        
        entry_proteins = input('Enter your daily protein intake in gram, separated by spaces')
        lstA = entry_proteins.split(' ')
        protList = [float(x) for x in lstA]
        protCount = len(protList)
        
        entry_fats = input('Enter your daily fat intake in gram, separated by spaces')
        lstB = entry_fats.split(' ')
        fatList = [float(x) for x in lstB]
        fatCount = len(fatList)
        
        entry_carbs = input('Enter your daily carbohydrate intake in gram, separated by spaces')
        lstC = entry_carbs.split(' ')
        carbList = [float(x) for x in lstC]
        carbCount = len(carbList)
        
    except ValueError as e:
        print('Please enter valid values')
        entry()
    
    length = len(protList)
    if (protCount or fatCount or carbCount) < 7:
        raise ValueError('We need records for at least a week')
        entry()
    
    elif not all(len(lst) == length for lst in [protList, fatList, carbList]):
        raise ValueError('Number of records for all 3 nutrients need to be the same')
        entry()
        
    else:
        protSum = sum(protList)
        fatSum = sum(fatList)
        carbSum = sum(carbList)
        total_carlo = (protSum+carbSum)*4 + fatSum*9
        avg_carlo = total_carlo / len(protList)
    
        dayList = [x+1 for x in range(length)]
        protListC = [x*4 for x in protList]
        fatListC = [x*9 for x in fatList]
        carbListC = [x*4 for x in carbList]
        multiLists = [protListC, fatListC, carbListC]
        caloList = [sum(k) for k in zip(*multiLists)]
    
    nutriTrack(protList, fatList, carbList, dayList)
    calorieTrack(caloList, dayList, avg_carlo)
    
    return caloList
        
        
def nutriTrack(lst1, lst2, lst3, lst4):
    
    """
    Description of the Function

    Parameters:
    lst1 (list): a list of daily protein intake(g) in a certain time period provided by the user
    lst2 (list): a list of daily fat intake(g) in a certain time period provided by the user
    lst3 (list): a list of daily carbohydrate intake(g) in a certain time period provided by the user
    lst4 (list): a list of sequential days for a certain time period obtained from the user

    Returns:
    show linked plotting graphs of three nutrients intake for a certain time period
    
    """
    
#     print('Summary:')
#     print('Your average daily protein intake in {:.0f} days is {:.2f} g'.format(len(lst1), sum(lst1)/len(lst1)))
#     print('Your average daily fat intake in {:.0f} days is {:.2f} g'.format(len(lst2), sum(lst2)/len(lst2)))
#     print('Your average daily carbohydrate intake in {:.0f} days is {:.2f} g'.format(len(lst3), sum(lst3)/len(lst3)))
    
#     output_file('nutrients.html')
    s1 = figure(plot_width=450, plot_height=350, title="Daily Protein Intake", x_axis_label='Days', y_axis_label='Protein(g)')
    s1.circle(lst4, lst1, size=10, color='navy', alpha=0.5)
    s2 = figure(plot_width=450, plot_height=350, x_range=s1.x_range, y_range=s1.y_range,
               title="Daily Fat Intake", x_axis_label='Days', y_axis_label='Fat(g)')
    s2.triangle(lst4, lst2, size=10, color='firebrick', alpha=0.5)
    s3 = figure(plot_width=450, plot_height=350, x_range=s1.x_range, y_range=s1.y_range,
               title="Daily Carbohydrate Intake", x_axis_label='Days', y_axis_label='Carbohydrate(g)')
    s3.square(lst4, lst3, size=10, color='olive', alpha=0.5)
    
    p = gridplot([[s1, s2, s3]], toolbar_location=None)
#     return type(p)
#     show(p)

    
def calorieTrack(lst1, lst2, num):
    
    """
    Description of the Function

    Parameters:
    lst1 (list): a list of daily calorie intake in a certain time period calculated by info provided by the user
    lst2 (list): a list of sequential days for a certain time period obtained from the user
    num (float): average calorie intake for a certain period of time

    Returns:
    show the graph of the total daily calorie intake for a certain period of time
    
    """
    
#     print('Your average calorie intake in {:.0f} days is {:.2f}'.format(len(lst2), num))
    
#     output_file('calories.html')
    source = ColumnDataSource(data=dict(x = lst2, y = lst1))
    hover = HoverTool(tooltips=[('index', '$index'), ('y', '@y')])
    p = figure(plot_width =750, plot_height =500, tools=[hover], title='Daily Calorie Intake',
              x_axis_label='Days', y_axis_label='Calorie')
    p.line('x', 'y', line_width=3, source=source)
    p.circle('x', 'y', size=20, source=source)
#     show(p)
    
#     return type(hover)