#imports libraries
import tkinter as tk
import random
from tkinter import filedialog
from tkinter import messagebox

class App(tk.Tk):
    #initialize the GUI
    def __init__(self, master=None):

        super().__init__()       

        self.geometry("400x400")
        self.title("Primality Checker")
        self.resizable(0,0)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=2)       

        
        self.create_widgets()

    #creatting widget for the GUI
    def create_widgets(self): 


        #label for numbers
        self.lbl_number = tk.Label(self, font=('arial', 10, "bold"), text="Number(s): ")
        self.lbl_number.grid(row=0, column=0, padx=5, pady=5)

        #input for numbers
        self.input_numbers = tk.StringVar()
        self.ent_number = tk.Entry(self, font=("arial", 10, "bold"), textvariable=self.input_numbers, insertwidth=4, bg="white", justify="left")
        self.ent_number.grid(row=0, column=1, columnspan=3, sticky="ew", padx=5, pady=5)

        #check button
        self.btn_check = tk.Button(self, activebackground="blue", command=self.GetNumbers, font=("arial", 10), pady=10, text="Check")
        self.btn_check.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        #load file button
        self.btn_loadFile = tk.Button(self, activebackground="blue", command=self.LoadFile, font=("arial", 10), pady=10, text="Load File")
        self.btn_loadFile.grid(row=2, column=2, columnspan=2, sticky="ew", padx=5, pady=5)

        #label for report
        self.lbl_report = tk.Label(self, font=("arial", 15, "bold"), text="REPORT")
        self.lbl_report.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

        #message box
        self.msg_report = tk.Text(self, font=("arial", 10), bg="white", height=12, width=10)
        self.msg_report.grid(row=6, column=0, columnspan=4, sticky="news", padx=5, pady=5)
        self.msg_report.config(state='disabled')

        #Adding scrollbar
        self.scrollBar = tk.Scrollbar(self, orient='vertical', command=self.msg_report.yview)
        self.scrollBar.grid(row=6, column=4, sticky='ns')
        self.msg_report.config(yscrollcommand=self.scrollBar.set)

        #save report button
        self.btn_save = tk.Button(self, activebackground="blue", command=self.SaveReport, font=("arial", 10), pady=10, text="Save")
        self.btn_save.grid(row=9, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        #new report button
        self.btn_newReport = tk.Button(self, activebackground="blue", command=self.NewReport, font=("arial", 10), pady=10, text="New Report")
        self.btn_newReport.grid(row=9, column=2, columnspan=1, sticky="ew", padx=5, pady=5)

        #cancel button
        self.btn_cancel = tk.Button(self, activebackground="blue", command=self.destroy, font=("arial", 10), pady=10, text="Cancel")
        self.btn_cancel.grid(row=9, column=3, columnspan=1, sticky="ew", padx=5, pady=5)

    #getting numbers inputed
    def GetNumbers(self):
        numbers = self.ent_number.get()
        listNumbers = numbers.split(",")
        self.CheckNumbers(listNumbers)

    #Function to check the numbers using the Fermat Check Primality function
    #Try/Catch to figure out with string and invalid integers.
    def CheckNumbers(self, listNumbers):               
        for number in listNumbers:
            try:                
                result = FermatCheckPrimality(int(number))                
                self.msg_report.config(state='normal')
                if(result):                
                    self.msg_report.insert('end', f'{number} - PRIME\n')
                else:
                    self.msg_report.insert('end', f'{number} - COMPOSITE\n')
            
                self.msg_report.config(state='disabled')
                self.input_numbers.set("")
            except ValueError:
                messagebox.showerror('Error!', f'"{number}" is not a valid number.')            

    #Function to save the report.
    def SaveReport(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file is None:
            return
        file_obj = open(file, 'w')
        file_obj.write(self.msg_report.get('1.0', 'end-1c'))
        file_obj.close()

    #Function to load a txt file and check the numbers.
    def LoadFile(self):
        file = filedialog.askopenfile(title='Open a file', initialdir='/', defaultextension='.txt')
        if file is None:
            return
        for line in file:
            listNumbers = [x.strip() for x in line.split(",")]
            self.CheckNumbers(listNumbers)
                

    #Function to erase the report and create a new one.
    def NewReport(self):
        self.ent_number.setvar("")
        self.msg_report.config(state='normal')
        self.msg_report.delete('1.0', 'end-1c')
        self.msg_report.config(state='disabled')

#function using the Fermat numbers to check if the numbers are prime or not.
def FermatCheckPrimality(number):
    
    if(number <= 1):
        return False

    elif(number > 3):
        k = 3
        
        while(k>0):
            a = random.randint(2,number-1)
            
            if((a**(number-1))%number != 1):
                return False
           
            k = k - 1

    return True

#initialize the app
if __name__ == "__main__":   
    
    app = App()
    app.mainloop()
