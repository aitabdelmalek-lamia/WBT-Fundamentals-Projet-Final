#calculating frequencies : fi
def calculate_fi(data_set):
    frequency= {}

    for Xi in data_set:
        if Xi in frequency:
            frequency[Xi] += 1
        else:
            frequency[Xi] = 1
    return frequency    
#just for testing
"""
data = ["M", "L","M" , "S", "M","S","S","L"]
result = calculate_fi(data)
print(result)
"""





  



#calculting cumulative frequency : Fi
"""
Fi = f1 + f2 + f3 + ... + fi
"""
def calculate_Fi(frequency):
    cumulative = {}
    total = 0
    for Xi in frequency:
        total += frequency[Xi]
        cumulative[Xi] = total
    return cumulative    



    
#percentage  = fr * 100





#calculating relative frequency :fr =  fi/N ; N = number of individuals or the total number of observation
def calculate_relative_frequency(frequency):
    N = sum(frequency.values())
    relative = {}
    for Xi in frequency:
        relative[Xi] = frequency[Xi] / N
    return relative



#calculating cumulative relative frequency : Fri = Fi / N
def calculate_cum_rel_frequency(cumulative):
    N = list(cumulative.values())[-1] # N = the least cumulative frequency Fi
    Fri = {}
    for Xi in cumulative:
        Fri[Xi] = cumulative[Xi] / N
    return Fri




def calculate_percentage(relative):
    percentge = {}
    for Xi in relative:
        percentge[Xi] = relative[Xi] * 100
    return percentge



data = ["M", "L", "M", "S", "M", "S", "S", "L"]

fi = calculate_fi(data)
assert fi == {"M": 3, "L": 2, "S": 3}

Fi = calculate_Fi(fi)
assert Fi == {"M": 3, "L": 5, "S": 8}

fr = calculate_relative_frequency(fi)
assert fr == {"M": 3/8, "L": 2/8, "S": 3/8}

Fri = calculate_cum_rel_frequency(Fi)
assert Fri == {"M": 3/8, "L": 5/8, "S": 1}

percentage = calculate_percentage(fr)
assert percentage == {"M": 37.5, "L": 25.0, "S": 37.5}
print("All tests passed!")





def display_table(frequency, cumulative, relative, Fri, percentage):
    print("Xi\tfi\tFi\tfr\tFri\t%")
    for Xi in frequency:
        print(Xi, frequency[Xi], cumulative[Xi], relative[Xi], Fri[Xi], percentage[Xi], sep="\t")

display_table(fi, Fi, fr, Fri, percentage)