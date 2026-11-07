            # ┌─────────────────┐
            #   │ Start Program │
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Enter Xi data │
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Find modalities │
            #   │ Xi │
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Calculate fi │
            #   │ (frequency) │
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Calculate N │
            #   │ total │
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Relative freq. │
            #   │ fi / N │
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Cumulative freq.│
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Cumulative │
            #   │ relative freq. │
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Pie angle │
            #   │ fi/N × 360° │
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Statistical │
            #   │ Table │
            #   └────────┬────────┘
            #            ↓
            #   ┌─────────────────┐
            #   │ Graphs │
            #   │ Pie / Bar / ... │
            #   └─────────────────┘
import pandas as pd
def load_data(file_path):
    #check the file extension
    if file_path.endswith(".csv"):
        data = pd.read_csv(file_path)

    elif file_path.endswith(".xlsx"):
        data = pd.read_excel(file_path)

    else:
        raise ValueError("Unsupported file format")
    
    return data
def input_data():
    values = input("Enter your data separated by commas: ")
    data = values.split(",")
    data = [value.strip() for value in data]
    return pd.DataFrame({"Values": data })













#calculating frequencies : fi
def calculate_fi(data):
    frequency= {}

    for Xi in data:
        if Xi in frequency:
            frequency[Xi]+= 1
        else:
            frequency[Xi] = 1
    for Xi in frequency:
        print(f"{Xi}: {calculate_Fi[Xi]}")
        return 


 
    



#calculating relative frequencies : fi/n ; n= number of individuals 
def calculate_relative_frequency(frequencies):
    pass
#calculting cumulative frequency : Fi
def calculate_Fi(fi):
    pass
#percentage













while True:
    variable_type= input("What type of variable do you have? ")
    if variable_type == "qualitative":



def analize(data):
    data = input("Enter your data: ")
    







import turtle
#create the screen
screen = turtle.Screen()
screen.bgcolor("#FFFFFF")
screen.title("StatEasy")
turtle.color("DarkBlue")
turtle.penup()
turtle.goto(0, 100)
turtle.write(
    "StatEasy",
    align="center",
    font=("Arial", 30, "bold")
)
turtle.done()














