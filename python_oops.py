# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:21:07 2020

@author: Dinesh.Choudhary
"""
        
class Player:
    def __init__(self):
        self.type=self.__class__.__name__


class Terrorist(Player):             
    def __init__(self):
        self.type=f'{Player.__name__}:{self.__class__.__name__}'
        
class Counter_Terrorist(Player):             
    def __init__(self):
        self.type=f'{Player.__name__}:{self.__class__.__name__}'


        
class T1(Terrorist):             
    def __init__(self):
        self.type=f'{Player. __name__}:{Terrorist.__name__}:{self.__class__.__name__}'
        
class T2(Terrorist):             
    def __init__(self):
        self.type=f'{Player. __name__}:{Terrorist.__name__}:{self.__class__.__name__}'
        
class CT1(Counter_Terrorist):             
    def __init__(self):
        self.type=f'{Player. __name__}:{Counter_Terrorist.__name__}:{self.__class__.__name__}'
        
class CT2(Counter_Terrorist):             
    def __init__(self):
        self.type=f'{Player. __name__}:{Counter_Terrorist.__name__}:{self.__class__.__name__}'
    



class Gun:
    def __init__(self):
        self.type=self.__class__.__name__
     
        
class Pistol(Gun):
    def __init__(self):
        self.type=f'{Gun.__name__}:{self.__class__.__name__}'

class Rifle(Gun):
    def __init__(self):
       self.type=f'{Gun.__name__}:{self.__class__.__name__}'



class Flare_Gun(Pistol):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Pistol.__name__}:{self.__class__.__name__}'
    
class Deagle(Pistol):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Pistol.__name__}:{self.__class__.__name__}'      

class Skorpion(Pistol):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Pistol.__name__}:{self.__class__.__name__}'      

class Assault_Rifle(Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{self.__class__.__name__}'
 
class Sniper(Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{self.__class__.__name__}'
        
class Shotgun(Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{self.__class__.__name__}'

class Machinegun(Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{self.__class__.__name__}'        
        
class Groza(Assault_Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Assault_Rifle.__name__}:{self.__class__.__name__}'
        
class AK47(Assault_Rifle):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Assault_Rifle.__name__}:{self.__class__.__name__}'
        
class AWM(Sniper):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Sniper.__name__}:{self.__class__.__name__}'

class M24(Sniper):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Sniper.__name__}:{self.__class__.__name__}'   
        
class DBS(Shotgun):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Shotgun.__name__}:{self.__class__.__name__}'
  
class S686(Shotgun):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Shotgun.__name__}:{self.__class__.__name__}'  
        
class MG42(Machinegun):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Machinegun.__name__}:{self.__class__.__name__}' 
  
class ThompsonMG(Machinegun):
    def __init__(self):
        self.type=f'{Gun. __name__}:{Rifle.__name__}:{Machinegun.__name__}:{self.__class__.__name__}'   
        


player=Player()
terrorist=Terrorist()
counter_terrorist=Counter_Terrorist()   
t1=T1()
t2=T2()
ct1=CT1()
ct2=CT2()


gun=Gun()

pistol=Pistol()
rifle=Rifle()

flare_gun=Flare_Gun()
deagle=Deagle()
skorpion=Skorpion()
assault_rifle=Assault_Rifle()
sniper=Sniper()
shotgun=Shotgun()
machinegun=Machinegun()

groza=Groza()
ak47=AK47()
awm=AWM()
m24=M24()
dbs=DBS()
s686=S686()
mg42=MG42()
thompsonmg=ThompsonMG()





#main

print("Enter the player: (Terrorist)(Counter Terrorist)")
player_input=input()

print("Enter the player type: (T1)(T2)(CT1)(CT2)")
player_type_input=input()

print("Enter the gun: (Pistol)(Rifle)")
gun_input=input()

print("Enter the gun type: (Flare gun)(Deagle)(Skorpion)(Assault Rifle)(Sniper)(Shotgun)(Machine gun)")
gun_type_input=input()

print("Enter the gun sub type: (Groza)(AK47)(M24)(AWM)(DBS)(S686)((MG42)(Thompson MG)")
gun_subtype_input=input()



if(player_input=='Terrorist'):
    if (player_type_input=='T1'):
        print(t1.type)
        
        if(gun_input=='Pistol'):
            if (gun_type_input=='Flare Gun'):
                print(flare_gun.type)
            elif (gun_type_input=='Deagle'):
                print(deagle.type) 
            elif (gun_type_input=='Skorpion'):
                print(skorpion.type) 
        elif (gun_input=='Rifle'):   
            if (gun_type_input=='Assault Rifle'):
                print(assault_rifle.type)
            if (gun_type_input=='Sniper'):
                print(sniper.type) 
            if (gun_type_input=='Shotgun'):
                print(shotgun.type)
            if (gun_type_input=='Machinegun'):
                print(machinegun.type)         
        
    elif (player_type_input=='T2'):
        print(t2.type) 
        
        if(gun_input=='Pistol'):
            if (gun_type_input=='Flare Gun'):
                print(flare_gun.type)
            elif (gun_type_input=='Deagle'):
                print(deagle.type) 
            elif (gun_type_input=='Skorpion'):
                print(skorpion.type) 
        elif (gun_input=='Rifle'):   
            if (gun_type_input=='Assault Rifle'):
                print(assault_rifle.type)
            if (gun_type_input=='Sniper'):
                print(sniper.type) 
            if (gun_type_input=='Shotgun'):
                print(shotgun.type)
            if (gun_type_input=='Machinegun'):
                print(machinegun.type)         
        
elif(player_input=='Counter Terrorist'):
    if (player_type_input=='CT1'):
        print(ct1.type)
        
        if(gun_input=='Pistol'):
            if (gun_type_input=='Flare Gun'):
                print(flare_gun.type)
            elif (gun_type_input=='Deagle'):
                print(deagle.type) 
            elif (gun_type_input=='Skorpion'):
                print(skorpion.type) 
        elif (gun_input=='Rifle'):   
            if (gun_type_input=='Assault Rifle'):
                print(assault_rifle.type)
            if (gun_type_input=='Sniper'):
                print(sniper.type) 
            if (gun_type_input=='Shotgun'):
                print(shotgun.type)
            if (gun_type_input=='Machinegun'):
                print(machinegun.type)         
        
    elif (player_type_input=='CT2'):
        print(ct2.type) 
        
        if(gun_input=='Pistol'):
            if (gun_type_input=='Flare Gun'):
                print(flare_gun.type)
            elif (gun_type_input=='Deagle'):
                print(deagle.type) 
            elif (gun_type_input=='Skorpion'):
                print(skorpion.type) 
        elif (gun_input=='Rifle'):   
            if (gun_type_input=='Assault Rifle'):
                print(assault_rifle.type)
            if (gun_type_input=='Sniper'):
                print(sniper.type) 
            if (gun_type_input=='Shotgun'):
                print(shotgun.type)
            if (gun_type_input=='Machinegun'):
                print(machinegun.type)         

































