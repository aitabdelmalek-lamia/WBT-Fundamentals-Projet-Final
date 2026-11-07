#Parent Class
class DataSet:
    def __init__(self, data):
        self.data = data
        #calculating frequencies : fi
    def calculate_fi(self):
        frequency= {}

        for Xi in self.data:
            if Xi in frequency:
                 frequency[Xi] += 1
            else:
                frequency[Xi] = 1
        return frequency  

    
    #calculting cumulative frequency : Fi
    """
    Fi = f1 + f2 + f3 + ... + fi
    """
    def calculate_Fi(self, frequency):
        cumulative = {}
        total = 0
        for Xi in frequency:
            total += frequency[Xi]
            cumulative[Xi] = total
        return cumulative  

    #calculating relative frequency :fr =  fi/N ; N = number of individuals or the total number of observation
    def calculate_relative_frequency(self, frequency):
        N = sum(frequency.values())
        relative = {}
        for Xi in frequency:
            relative[Xi] = frequency[Xi] / N
        return relative 
       
    #calculating cumulative relative frequency : Fri = Fi / N
    def calculate_cum_rel_frequency(self, cumulative):
        N = list(cumulative.values())[-1] # N = the least cumulative frequency Fi
        Fri = {}
        for Xi in cumulative:
            Fri[Xi] = cumulative[Xi] / N
        return Fri


    #percentage  = fr * 10
    def calculate_percentage(self, relative):
        percentge = {}
        for Xi in relative:
            percentge[Xi] = relative[Xi] * 100
        return percentge


# Child Class 1
class QualitativeData(DataSet):

    def calculate_table(self):
        fi = self.calculate_fi()
        fr = self.calculate_relative_frequency(fi)
        percentage = self.calculate_percentage(fr)

        return fi, fr, percentage



# Child Class 2
class QuantitativeData(DataSet):

    def calculate_table(self):
        fi = self.calculate_fi()
        fi = dict(sorted(fi.items()))

        Fi = self.calculate_Fi(fi)
        fr = self.calculate_relative_frequency(fi)
        Fri = self.calculate_cum_rel_frequency(Fi)
        percentage = self.calculate_percentage(fr)

        return fi, Fi, fr, Fri, percentage






"""
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
""" 




def display_table(frequency, cumulative, relative, Fri, percentage):
    print("Xi\tfi\tFi\tfr\tFri\t%")
    for Xi in frequency:
        print(Xi, frequency[Xi], cumulative[Xi], relative[Xi], Fri[Xi], percentage[Xi], sep="\t")

display_table(fi, Fi, fr, Fri, percentage)







