#Logica del programma

import pandas as pd
import csv

#lettura del dataset importato
def readCsv(title):
    dataset = pd.read_csv(title, sep=',')
    return dataset

#funzione per filtrare il dataset in base ai valori impostati nella gui
def createCsv(dataset, dict_values):
    with open('filteredcsv.csv', 'w', newline='') as csvfile:
        newfile = csv.writer(csvfile, delimiter=',')
        newfile.writerow(dataset.columns.values)
        for i in range(dataset.shape[0]):
            flag = True
            for key,value in dict_values.items():
                if(checkColType(dataset,key)=="int64"):
                    if(dataset[key][i]<value):
                        flag = False
                elif(checkColType(dataset,key)=="object"):
                    if(dataset[key][i]!=value):
                        flag = False
            if(flag):
                newfile.writerow(dataset.iloc[i])

#controllo del tipo della colonna considerata
def checkColType(dataset, column):
    # for key, value in dict_values.items():
    #     if(isinstance(value, str)):
    #         print(key + " è di tipo stringa!")
    #     elif (isinstance(value, int)):
    #         print(key + " è di tipo intero!")
    return dataset[column].dtype


# def main():
#     title = "Family Income and Expenditure.csv"
#     dataset = readCsv(title)
#     dict_values = {}
#     dict_values["Household Head Age"] = 40
#     dict_values["Total Number of Family members"] = 3
#     dict_values["Region"] = "CAR"
#     #createCsv(dataset, dict_values)
#     print(dataset["Region"].unique())
#
# main()