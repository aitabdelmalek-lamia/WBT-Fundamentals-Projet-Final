#Parent Class
class DataSet:
    def __init__(self, data):
        #check if data is empty
        if not data:
            raise ValueError("Data set cannot be empty")
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

    #calculating relative frequency :fr =  fi/N ; N = number of individuals,total frequency or the total number of observation
    def calculate_relative_frequency(self, frequency):
        N = sum(frequency.values())
        if N == 0:
            raise ZeroDivisionError("Total frequency cannot be zero")
        relative = {}
        for Xi in frequency:
            relative[Xi] = frequency[Xi] / N
        return relative 
       
    #calculating cumulative relative frequency : Fri = Fi / N
    def calculate_cum_rel_frequency(self, cumulative):
        if not cumulative:
            raise ValueError("Cumulative frequency is empty")
        N = list(cumulative.values())[-1] # N = the least cumulative frequency Fi
        if N == 0:
                    raise ZeroDivisionError("Total frequency cannot be zero")
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

        #check if all values are numeric
        for Xi in self.data:
            if not isinstance(Xi, (int, float)) or isinstance(Xi, bool):
                raise ValueError("Quantitative data must contain numbers")
        try:

            fi = self.calculate_fi()
            fi = dict(sorted(fi.items()))
        except TypeError:
            raise ValueError("Invalid quantitative data")
        Fi = self.calculate_Fi(fi)
        fr = self.calculate_relative_frequency(fi)
        Fri = self.calculate_cum_rel_frequency(Fi)
        percentage = self.calculate_percentage(fr)

        return fi, Fi, fr, Fri, percentage

try:
    dataset = QuantitativeData([])
    result = dataset.calculate_table()
    print(result)

except (ValueError, ZeroDivisionError, TypeError) as error:
    print("Error:", error)

