from csvLogic import *

from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import *



def main():

    #Funzioni

    def clicked():
        file = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
        txt0.insert(0,file)

    def send():
        dataset = readCsv(txt0.get())

        dict_values = {}
        dict_values[lbl2.cget("text")] = txt1.get()
        dict_values[lbl3.cget("text")] = combo1.get()
        dict_values[lbl4.cget("text")] = combo2.get()
        dict_values[lbl5.cget("text")] = combo3.get()
        dict_values[lbl6.cget("text")] = combo4.get()
        dict_values[lbl7.cget("text")] = combo5.get()
        dict_values[lbl8.cget("text")] = txt2.get()
        dict_values[lbl9.cget("text")] = combo6.get()
        dict_values[lbl10.cget("text")] = txt3.get()
        dict_values[lbl11.cget("text")] = txt4.get()
        dict_values[lbl12.cget("text")] = txt5.get()
        dict_values[lbl13.cget("text")] = combo7.get()

        createCsv(dataset,dict_values)



    #GUI

    window = Tk()
    window.title("Welcome to SmartADV app")
    window.geometry('500x500')

    #importa il path del file csv
    txt0 = Entry(window,width=10)
    txt0.grid(column=2, row=0)
    btn = Button(window, text="Importa il file csv", command=clicked)
    btn.grid(column=1, row=0)

    #text area
    lbl2 = Label(window, text="Household Head Age", font=("Arial", 12))
    lbl2.grid(column=1, row=1)
    txt1 = Entry(window,width=10)
    txt1.grid(column=2, row=1)

    #combobox
    lbl3 = Label(window, text="Household Head Class of Worker", font=("Arial", 12))
    lbl3.grid(column=1, row=2)
    combo1 = Combobox(window)
    combo1['values'] = ("Employer in own family-operated farm or business", "NA", "Self-employed wihout any employee", "Worked for government/government corporation", "Worked for private establishment", "Worked for private household","Worked with pay in own family-operated farm or business","Worked without pay in own family-operated farm or business")
    combo1.current(0)  # set the selected item
    combo1.grid(column=2, row=2)

    #combobox
    lbl4 = Label(window, text="Household Head Highest Grade Completed", font=("Arial", 12))
    lbl4.grid(column=1, row=3)
    combo2 = Combobox(window)
    combo2['values'] = ('Teacher Training and Education Sciences Programs',
     'Transport Services Programs', 'Grade 3', 'Elementary Graduate',
     'Second Year High School', 'Third Year High School',
     'Business and Administration Programs', 'First Year College',
     'High School Graduate',
     'Other Programs in Education at the Third Level, First Stage, of the Type that Leads to an Award not Equivalent to a First University or Baccalaureate Degree',
     'Humanities Programs', 'First Year High School', 'Grade 6', 'Grade 4',
     'Engineering and Engineering Trades Programs', 'Grade 2', 'Grade 5',
     'Social and Behavioral Science Programs',
     'Agriculture, Forestry, and Fishery Programs', 'Health Programs',
     'Fourth Year College', 'Engineering and Engineering trades Programs',
     'Second Year College', 'Third Year College', 'Grade 1', 'No Grade Completed',
     'Security Services Programs', 'Basic Programs', 'First Year Post Secondary',
     'Second Year Post Secondary', 'Post Baccalaureate',
     'Computing/Information Technology Programs',
     'Mathematics and Statistics Programs', 'Personal Services Programs',
     'Law Programs', 'Journalism and Information Programs',
     'Architecture and Building Programs',
     'Manufacturing and Processing Programs', 'Life Sciences Programs',
     'Other Programs of Education at the Third Level, First Stage, of the Type that Leads to a Baccalaureate or First University/Professional Degree (HIgher Education Level, First Stage, or Collegiate Education Level)',
     'Social Services Programs', 'Preschool', 'Physical Sciences Programs',
     'Arts Programs', 'Veterinary Programs', 'Environmental Protection Programs')
    combo2.current(0)  # set the selected item
    combo2.grid(column=2, row=3)

    #combobox
    lbl5 = Label(window, text="Household Head Marital Status", font=("Arial", 12))
    lbl5.grid(column=1, row=4)
    combo3 = Combobox(window)
    combo3['values'] = ("Annulled", "Divorced/Separated", "Married", "Single", "Unknown", "Widowed")
    combo3.current(0)  # set the selected item
    combo3.grid(column=2, row=4)

    #combobox
    lbl6 = Label(window, text="Household Head Sex", font=("Arial", 12))
    lbl6.grid(column=1, row=5)
    combo4 = Combobox(window)
    combo4['values'] = ("Male", "Female")
    combo4.current(0)  # set the selected item
    combo4.grid(column=2, row=5)

    #combobox
    lbl7 = Label(window, text="Main Source of Income", font=("Arial", 12))
    lbl7.grid(column=1, row=6)
    combo5 = Combobox(window)
    combo5['values'] = ("Enterpreneurial Activities", "Other source of Income","Wage/Salaries")
    combo5.current(0)  # set the selected item
    combo5.grid(column=2, row=6)

    #text area
    lbl8 = Label(window, text="Miscellaneous Goods and Services Expenditure", font=("Arial", 12))
    lbl8.grid(column=1, row=7)
    txt2 = Entry(window,width=10)
    txt2.grid(column=2, row=7)

    #combobox
    lbl9 = Label(window, text="Region", font=("Arial", 12))
    lbl9.grid(column=1, row=8)
    combo6 = Combobox(window)
    combo6['values'] = ("CAR", "Caraga", "VI - Western Visayas", "V - Bicol Region", "ARMM",
     "III - Central Luzon", "II - Cagayan Valley", "IVA - CALABARZON",
     "VII - Central Visayas", "X - Northern Mindanao", "XI - Davao Region",
     "VIII - Eastern Visayas", "I - Ilocos Region", "NCR", "IVB - MIMAROPA",
     "XII - SOCCSKSARGEN", "IX - Zasmboanga Peninsula")
    combo6.current(0)  # set the selected item
    combo6.grid(column=2, row=8)

    #text area
    lbl10 = Label(window, text="Total Income from Entrepreneurial Acitivites", font=("Arial", 12))
    lbl10.grid(column=1, row=9)
    txt3 = Entry(window,width=10)
    txt3.grid(column=2, row=9)

    #text area
    lbl11 = Label(window, text="Total Number of Family members", font=("Arial", 12))
    lbl11.grid(column=1, row=10)
    txt4 = Entry(window,width=10)
    txt4.grid(column=2, row=10)

    #text area
    lbl12 = Label(window, text="Total number of family members employed", font=("Arial", 12))
    lbl12.grid(column=1, row=11)
    txt5 = Entry(window,width=10)
    txt5.grid(column=2, row=11)

    #combobox
    lbl13 = Label(window, text="Type of Building/House", font=("Arial", 12))
    lbl13.grid(column=1, row=12)
    combo7 = Combobox(window)
    combo7['values'] = ("Commercial/industrial/agricultural building", "Duplex", "Institutional living quarter", "Multi-unit residential", "Other building unit (e.g. cave, boat)", "Single house")
    combo7.current(0)  # set the selected item
    combo7.grid(column=2, row=12)

    #importa il path del file csv
    btn2 = Button(window, text="Trasforma il file csv", command=send)
    btn2.grid(column=1, row=13)


    window.mainloop()

main()