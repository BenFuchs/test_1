
import pandas 
from enum import Enum
data = []
CSV_file = 'data.csv'

# menu of options
class Actions(Enum):
    AVG = 1
    MAX = 2
    NUM_OF_IDEAL = 3
    COLOR = 4
    MID_PREMIUM = 5 
    AVG_CAR_PER_TYPE = 6
    AVG_PRICE_PER_COLOR = 7


def display_menu():
    for action in Actions:
        print(f'{action.name} - {action.value}')
    return int(input("Input selection: "))

#loading csv file
def load_file():
    data_frame =pandas.read_csv(CSV_file)
    data.append(data_frame)

#max price of diamonds
def max_price():
    df =pandas.read_csv(CSV_file)
    max = df['price'].max()
    print("the highest price for a diamond is: ",max)



#Average price of diamonds
def average_price():
    df =pandas.read_csv(CSV_file)
    total_sum =df['price'].sum()
    num_of_items = df['price'].count()
    print("The average price of all diamonds is: " , total_sum / num_of_items)
    
#num of 'ideal' cut diamonds
def num_of_ideal():
    df = pandas.read_csv(CSV_file)
    result=df[df['cut'] == 'Ideal']    
    count = result.shape[0]
    print("the number of ideal cut diamonds is: ",count)
    
#num of colors
def num_color():
    df = pandas.read_csv(CSV_file)
    n = len(pandas.unique(df['color']))
    print("Number of colors: ",n)

#color names
def color_names():
    df = pandas.read_csv(CSV_file)
    n = pandas.unique(df['color'])
    print("Color names: ",n)

#middle premium diamond
def middle_premium():
    df = pandas.read_csv(CSV_file)
    column = df[df['cut'] == 'Premium']
    middle_item = len(column) // 2
    middle_item_value = column.iloc[middle_item]
    print("The middle value for premium cut diamonds is:\n",middle_item_value)

#Carat average per cut type
def carat_average():
    df = pandas.read_csv(CSV_file)
    cut = df[df['cut'] == input("Input cut type (captial first letter) ")]
    average_carat = cut['carat'].mean()
    print("The average Carat for the chosen cut is: ",average_carat)

#Price average per color
def price_by_color():
    df = pandas.read_csv(CSV_file)
    result=df[df['color'] == input("Please input color type('E' 'I' 'J' 'H' 'F' 'G' 'D'): ")]    
    count = result.shape[0]
    price = result['price'].sum()
    avg_price = price / count
    print ("the average price for the chosen color is: " , avg_price)




if __name__ == '__main__':
    while True:
        user_input = display_menu() 
        if user_input == 1:
           average_price()
           exit()
        if user_input == 2: 
           max_price()
           exit()
        if user_input == 3: 
           num_of_ideal()
           exit()
        if user_input == 4:
         num_color()
         color_names()
         exit()
        if user_input == 5:
            middle_premium()
            exit()
        if user_input == 6:
            carat_average()
            exit()
        if user_input == 7:
            price_by_color()
            exit()