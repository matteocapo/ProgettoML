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

        dict_values = dict()
        dict_values[lbl2.cget("text")] = txt1.get()
        dict_values[lbl3.cget("text")] = combo1.get()

        if combo2.get() != "null":
            dict_values[lbl4.cget("text")] = combo2.get()

        marital = []
        if chk_state2.get() == 1:
            marital.append("Annulled")
        if chk_state3.get() == 1:
            marital.append("Divorced/Separated")
        if chk_state4.get() == 1:
            marital.append("Married")
        if chk_state5.get() == 1:
            marital.append("Single")
        if chk_state6.get() == 1:
            marital.append("Unknown")
        if chk_state7.get() == 1:
            marital.append("Widowed")

        if marital:
            dict_values[lbl5.cget("text")] = marital

        sex = []
        if chk_state.get() == 1 and chk_state1.get() == 1:
            sex.append("Male")
            sex.append("Female")
        else:
            if chk_state.get() == 1:
                sex.append("Male")
            if chk_state1.get() == 1:
                sex.append("Female")
        if sex:
            dict_values[lbl6.cget("text")] = sex

        main = []
        if chk_state8.get() == 1:
            marital.append("Enterpreneurial Activities")
        if chk_state9.get() == 1:
            marital.append("Other source of Income")
        if chk_state10.get() == 1:
            marital.append("Wage/Salaries")
        if main:
            dict_values[lbl7.cget("text")] = main

        dict_values[lbl8.cget("text")] = txt2.get()

        if combo6.get() != "null":
            dict_values[lbl9.cget("text")] = combo6.get()

        dict_values[lbl10.cget("text")] = txt3.get()
        dict_values[lbl11.cget("text")] = txt4.get()
        dict_values[lbl12.cget("text")] = txt5.get()

        house=[]
        if chk_state11.get() == 1:
            marital.append("Commercial/industrial/agricultural building")
        if chk_state12.get() == 1:
            marital.append("Duplex")
        if chk_state13.get() == 1:
            marital.append("Institutional living quarter")
        if chk_state14.get() == 1:
            marital.append("Multi-unit residential")
        if chk_state15.get() == 1:
            marital.append("Other building unit (e.g. cave, boat)")
        if chk_state16.get() == 1:
            marital.append("Single house")
        if house:
            dict_values[lbl13.cget("text")] = house

        print (dict_values)

        createCsv(dataset,dict_values)

        print("Il csv è stato filtrato!")



    #GUI

    window = Tk()
    window.title("Welcome to SmartADV app")
    window.geometry('1135x500')

    #importa il path del file csv
    txt0 = Entry(window,width=10)
    txt0.grid(column=3, row=0)
    btn = Button(window, text="Importa il file csv", command=clicked)
    btn.grid(column=2, row=0)

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
    combo2['values'] = ('null', 'Teacher Training and Education Sciences Programs',
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


    #chekbox
    lbl5 = Label(window, text="Household Head Marital Status", font=("Arial", 12))
    lbl5.grid(column=1, row=4)
    chk_state2 = BooleanVar()
    chk_state3 = BooleanVar()
    chk_state4 = BooleanVar()
    chk_state5 = BooleanVar()
    chk_state6 = BooleanVar()
    chk_state7 = BooleanVar()

    chk_state2.set(False)
    chk_state3.set(False)
    chk_state4.set(False)
    chk_state5.set(False)
    chk_state6.set(False)
    chk_state7.set(False)

    chk2 = Checkbutton(window, text='Annulled', var=chk_state2)
    chk3 = Checkbutton(window, text='Divorced/Separated', var=chk_state3)
    chk4 = Checkbutton(window, text='Married', var=chk_state4)
    chk5 = Checkbutton(window, text='Single', var=chk_state5)
    chk6 = Checkbutton(window, text='Unknown', var=chk_state6)
    chk7 = Checkbutton(window, text='Widowed', var=chk_state7)

    chk2.grid(column=2,row=4)
    chk3.grid(column=3,row=4)
    chk4.grid(column=4, row=4)
    chk5.grid(column=5, row=4)
    chk6.grid(column=6, row=4)
    chk7.grid(column=7, row=4)

    #chekbox
    lbl6 = Label(window, text="Household Head Sex", font=("Arial", 12))
    lbl6.grid(column=1, row=5)
    chk_state = BooleanVar()
    chk_state1 = BooleanVar()

    chk_state.set(False)
    chk_state1.set(False)

    chk = Checkbutton(window, text='Male', var=chk_state)
    chk1 = Checkbutton(window, text='Female', var=chk_state1)

    chk.grid(column=2,row=5)
    chk1.grid(column=3,row=5)


    #chekbox
    lbl7 = Label(window, text="Main Source of Income", font=("Arial", 12))
    lbl7.grid(column=1, row=6)
    chk_state8 = BooleanVar()
    chk_state9 = BooleanVar()
    chk_state10 = BooleanVar()

    chk_state8.set(False)
    chk_state9.set(False)
    chk_state10.set(False)

    chk8 = Checkbutton(window, text='Enterpreneurial Activities', var=chk_state8)
    chk9 = Checkbutton(window, text='Other source of Income', var=chk_state9)
    chk10 = Checkbutton(window, text='Wage/Salaries', var=chk_state10)

    chk8.grid(column=2,row=6)
    chk9.grid(column=3,row=6)
    chk10.grid(column=4,row=6)


    #text area
    lbl8 = Label(window, text="Miscellaneous Goods and Services Expenditure", font=("Arial", 12))
    lbl8.grid(column=1, row=7)
    txt2 = Entry(window,width=10)
    txt2.grid(column=2, row=7)

    #combobox
    lbl9 = Label(window, text="Region", font=("Arial", 12))
    lbl9.grid(column=1, row=8)
    combo6 = Combobox(window)
    combo6['values'] = ("null", "CAR", "Caraga", "VI - Western Visayas", "V - Bicol Region", "ARMM",
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




    #chekbox
    lbl13 = Label(window, text="Type of Building/House", font=("Arial", 12))
    lbl13.grid(column=1, row=13)
    chk_state11 = BooleanVar()
    chk_state12 = BooleanVar()
    chk_state13 = BooleanVar()
    chk_state14 = BooleanVar()
    chk_state15 = BooleanVar()
    chk_state16 = BooleanVar()


    chk_state11.set(False)
    chk_state12.set(False)
    chk_state13.set(False)
    chk_state14.set(False)
    chk_state15.set(False)
    chk_state16.set(False)

    chk11 = Checkbutton(window, text='Commercial/industrial/agricultural building', var=chk_state11)
    chk12 = Checkbutton(window, text='Duplex', var=chk_state12)
    chk13 = Checkbutton(window, text='Institutional living quarter', var=chk_state13)
    chk14 = Checkbutton(window, text='Multi-unit residential', var=chk_state14)
    chk15 = Checkbutton(window, text='Other building unit (e.g. cave, boat)', var=chk_state15)
    chk16 = Checkbutton(window, text='Single house', var=chk_state16)

    chk11.grid(column=2,row=12)
    chk12.grid(column=3,row=12)
    chk13.grid(column=2,row=14)
    chk14.grid(column=2,row=13)
    chk15.grid(column=3,row=13)
    chk16.grid(column=3,row=14)

    #importa il path del file csv
    btn2 = Button(window, text="Trasforma il file csv", command=send)
    btn2.grid(column=1, row=15)

    window.mainloop()

main()