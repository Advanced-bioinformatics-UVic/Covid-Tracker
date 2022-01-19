import calendar
from datetime import timedelta
import time

Months=["january","february","march","april","may","june","july","august","september","october","novemeber","december"]
MonthDays=[31,28,31,30,31,30,31,31,30,31,30,31]#numeor dias mes. anys no bicsecs 


dicMonths={}
for month,day in zip(Months,MonthDays):
    dicMonths[month]=day

class Calendar:#creem classe.
    
    def __init__(self,year):#primer ffuncio es per iniciar. self es necessari al crear classe. i la segona, 3, ..seran els inputs.init es lo que automaticaent s'executa al cridar classe
        self.year=year#es guarda el any introduit en una varable dins a self. (self. es on es guarda tot i depres el nom atribut)
        self.monthsList=[]#creem atribut month list que sera llist de esos
        for month in Months:# per cada mes a month
            varName=month#es guarda variable mes
            varValue=Month(month,self.year)#creem la classe Month, fins ara tenim el nom domes. aixo ho
            #materialitza i defineix amb objectes el mes.Es ccrida class Month i se li dona atribut mes i any.
            self.monthsList.append(varValue)#definim llista on tenim tots els mesos definits com un atribut que es un llista
            setattr(self,varName,varValue)#funcio de Python que assigna a un atribut amb nom determinat (varName) a un objecte (self) un valor especific (varValue)
            
    def getFreeHours(self):#accedir dies lliures

        freeHours=[]
        for month in self.monthList:
            for day in month.days:
                for hour in day.hours:
                    if hour.disp:
                        freeHours.append(hour)
        #[[[[print(hour) for hour in day.hours],print()] for day in month.days] for month in self.monthsList]
        return freeHours
    
    def __repr__(self):
        return f'{self.year} vaccination calendar'

class Month:

    def __init__(self,month,year):
        self.year=year
        self.month=month
        self.nDays=dicMonths[self.month]
        
        if self.month==Months[1] and not self.year%4 and ( self.year%100 or not self.year%400):
            self.nDays+=1

        self.days=[Day(day+1,self.month) for day in range(self.nDays)]
        

    def __repr__(self):
        return f'{self.year} {self.month}\'s vaccination calendar '



class Day:

    def __init__(self,day,month):

        self.day = day
        self.month = month
        morningHours=[]
        eveningHours=[]
        for i in range(79):
            morningHours.append(str(timedelta(seconds=60*8+5*i))[2:])
            if i<50:
                eveningHours.append(str(timedelta(seconds=60*16+5*i))[2:])
                
        #morningHours=[str(timedelta(seconds=60*8+5*i))[2:] for i in range(79)]
        #eveningHours=[str(timedelta(seconds=60*16+5*i))[2:] for i in range(49)]

        #self.hours=[Hour(hora,self.day,self.month) for hora in morningHours+eveningHours]
        self.hours=[]
        for hora in morningHours+eveningHours:
            Hora=Hour(hora,self.day,self.month)
            self.hours.append(Hora)
        
    def __repr__(self):

        print( f'day {self.day}/{self.month}')
        return ''
    
class Hour:

    def __init__(self,hour,day,month):#
        
        self.hour = hour
        self.day= day
        self.month = month
        self.disp = True

    def reservation(self):

        if self.disp:

            self.disp=False

        else:

            print('Error. Hour already reserved, bitch')
    


    def annulate(self):

        if not self.disp:

            self.disp=True
        else:
            print('Error. Hour already free', end=', ')
            time.sleep(1)
            print('motherfucker')

    def __repr__(self):

        print( f'{self.day}/{self.month} - {self.hour} ({self.disp})')
        return ''
    

calendari=Calendar(2021)
