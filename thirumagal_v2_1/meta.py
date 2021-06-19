import csv
a='chennai'     #String that you want to search
with open("meta_location.csv") as f_obj:
    reader = csv.reader(f_obj, delimiter=',')
    for line in reader:      #Iterates through the rows of your csv
        print(line)          #line here refers to a row in the csv
        if a in line:      #If the string you want to search is in the row
            print("String found in first row of csv")
            break