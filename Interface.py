

from tkinter import messagebox
import tkinter as tk
import ctypes as ty
from calendario import Calendar
import datetime as dt


now=dt.datetime.now()
Any,Mes,Dia,Hora,Minut=now.year,now.month,now.day,now.hour,now.minute
calendari=Calendar(Any)


amplada, altura=ty.windll.user32.GetSystemMetrics(0), ty.windll.user32.GetSystemMetrics(1)

windows=tk.Tk()


windows.geometry(f'{amplada}x{altura-3}')
windows.title("Welcome to Covid Tracker app")
windows.configure(background="#4aacc5")

class dayCalendar(tk.Toplevel):

    def __init__(self,dia,master= None, *args, **kwargs):
        super().__init__(master = master)
        nday=dia.day
        if nday==1:
            sufix="st"
        elif nday==2:
            sufix="nd"
        elif nday==3:
            sufix="rd"
        else:
            sufix="th"

        header=f'{dia.month} {nday}{sufix}'
        self.dayLabel=tk.Label(self,text=header)
        self.dayLabel.grid(row=0)

        row=1
        for hour in dia.hours:

       
            if hour.disp:
                
                temp=tk.Button(self,text=hour.hour,foreground="black",command=lambda mem=hour:self.reservate(mem))
            else:
                temp=tk.Label(self,text=hour.hour,foreground="grey")

            temp.grid(row=row)
            row+=1

    def reservate(self,hour):

        ask=messagebox.askokcancel(title="Reservation confirmation",message="Do you wish to reserve?")

        if ask:
            hour.reservation()
            
class monthCalendar(tk.Toplevel):

    def __init__(self,mes,master= None, *args, **kwargs):

        super().__init__(master = master)
        self.monthLabel=tk.Label(self,text=mes.month)
        self.monthLabel.grid(row=0,columnspan=7)
        nD=1

        for setmana in range(5):

            for dia in range(7):

                if nD>mes.nDays:
                    temp=tk.Label(self,text="")

                else:
                    if nD<10:
                        
                        temp=tk.Button(self,text=" "+str(nD)+" ",command=lambda mem=mes.days[nD-1]:dayCalendar(mem))
                    else:
                        temp=tk.Button(self,text=nD,command=lambda mem=mes.days[nD-1]:dayCalendar(mem))
                        
                temp.grid(row=setmana+1,column=dia)
                nD+=1
        



class yearCalendar(tk.Toplevel):

    def __init__(self,master=None):
        super().__init__(master = master)
        self.yearLabel=tk.Label(self,text=Any)
        self.yearLabel.grid(columnspan=4)

        nM=0
        for row in range(1,4):
            for column in range(4):
                mes=calendari.monthsList[nM]
                temp=tk.Button(self,text=mes.month,command=lambda mem=mes : monthCalendar(mem))
                temp.grid(row=row,column=column,sticky="news")
                nM+=1
        
    

titleFrame=tk.Frame(windows,width=0.9*amplada,height=0.10*altura,background="#012160")
calendarFrame=tk.Frame(windows,width=0.4*amplada,height=0.10*altura,background="#8064a1")
casesFrame=tk.Frame(windows,width=0.4*amplada,height=0.10*altura,background="#b4d69b")
symptomsFrame=tk.Frame(windows,width=0.4*amplada,height=0.10*altura,background="#1f477c")
settingsFrame=tk.Frame(windows,width=0.4*amplada,height=0.10*altura,background="#f79646")

title=tk.Label(titleFrame,text="Covid Tracker", background="#012160", foreground="#ffffff")


calendar=tk.Button(calendarFrame, text="                     Calendar                  ", background="#8064a1", foreground="#ffffff",command=yearCalendar)
cases=tk.Button(casesFrame, text="                 Covid Cases               ", background="#b4d69b", foreground="#ffffff")
symptoms=tk.Button(symptomsFrame, text="                 Symptoms                  ", background="#1f477c", foreground="#ffffff")
settings=tk.Button(settingsFrame, text="                   Settings                    ", background="#f79646", foreground="#ffffff")

titleFrame.place(x=0.05*amplada, y=0.1*altura)
titleFrame.pack_propagate(0)
title.config(font=("Times New Roman",35))
title.pack()

calendarFrame.place(x=0.55*amplada, y=0.35*altura)
calendarFrame.pack_propagate(0)
calendar.config(font=("Times New Roman",30))
calendar.pack()

casesFrame.place(x=0.05*amplada, y=0.35*altura)
casesFrame.pack_propagate(0)
cases.config(font=("Times New Roman",30))
cases.pack()

symptomsFrame.place(x=0.55*amplada, y=0.7*altura)
symptomsFrame.pack_propagate(0)
symptoms.config(font=("Times New Roman",30))
symptoms.pack()

settingsFrame.place(x=0.05*amplada, y=0.7*altura)
settingsFrame.pack_propagate(0)
settings.config(font=("Times New Roman",30))
settings.pack()

windows.mainloop()




