# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:21:07 2020

@author: Dinesh.Choudhary
"""

class gun:
    def __init__(self):
        self.name='GUN:'

class pistol(gun):
    def __init__(self):
        self.name='PISTOL-'
    def printguntype(self):
        super().__init__()
        G1=self.name  + 'PISTOL-'
        print(G1)   
    

class rifle(gun):
    def __init__(self):
        self.name='RIFLE-'
    def printguntype(self):
        super().__init__()
        G2=self.name  + 'RIFLE-'
        print(G2) 
        

class flare_gun(pistol):
    def __init__(self):
        self.name='FLARE GUN' 
    def printgunsubtype(self):
        super().printguntype()
        G3= Pistol.G1  + 'FLARE GUN-'
        print(G3) 

class deagle(pistol):
    def __init__(self):
        self.name='DEAGLE'            
        

class assault_rifle(rifle):
    def __init__(self):
        self.name='ASSAULT RIFLE-'
 
class sniper(rifle):
    def __init__(self):
        self.name='SNIPER-'
        
        
        
Gun=gun()
Pistol=pistol()
Rifle=rifle()
Flare_Gun=flare_gun()
Deagle=deagle()
Assault_Rifle=assault_rifle()
Sniper=sniper()


print("Enter the gun: (Pistol)(Rifle)")
Gun=input()

print("Enter the gun type: (Flare gun)(Deagle)(Skorpion)(Assault Rifle)(Sniper)(Shotgun)(Machine gun)")
Gun_type=input()


if((Gun=='Pistol') ):
    if(Gun_type=='Flare gun'):
        Flare_Gun.printgunsubtype()
        

         
        
elif ((Gun=='Rifle') ) :    
    Rifle.printguntype()







                        
#class flare_gun(pistol):
#    def __init__(self):
#        self.name='FLARE GUN'        
#        
#class skorpion(pistol):
#    def __init__(self):
#        self.name='SKORPION'
#        
#class deagle(pistol):
#    def __init__(self):
#        self.name='DEAGLE'       
#        
#
#
#class assault_rifle(rifle):
#    def __init__(self):
#        self.name='ASSAULT RIFLE-'
# 
#class sniper(rifle):
#    def __init__(self):
#        self.name='SNIPER-'
#        
#class shotgun(rifle):
#    def __init__(self):
#        self.name='SHOTGUN-'
#
#class machinegun(rifle):
#    def __init__(self):
#        self.name='MACHINEGUN-'
#        
#class groza(assault_rifle):
#    def __init__(self):
#        self.name='GROZA-'
#        
#class AK47(assault_rifle):
#    def __init__(self):
#        self.name='AK47-'
#        
#class AWM(sniper):
#    def __init__(self):
#        self.name='AWM-'
#
#class M24(sniper):
#    def __init__(self):
#        self.name='M24-'   
#        
#class DBS(shotgun):
#    def __init__(self):
#        self.name='DBS-'   
#  
#class S686(shotgun):
#    def __init__(self):
#        self.name='S686-'   
#        
#class MG42(machinegun):
#    def __init__(self):
#        self.name='MG42-'   
#  
#class ThompsonMG(machinegun):
#    def __init__(self):
#        self.name='THOMPSONMG-'   
#        
#        
#class Player:
#    def __init__(self):
#        self.name='Player-'
#        print(self.name)
#
#class Terrorist(Player):             
#    def __init__(self):
#        self.name='Terrorist-'
#        
#class T1(Terrorist):             
#    def __init__(self):
#        self.name='T1-'
#        
#class T2(Terrorist):             
#    def __init__(self):
#        self.name='T2-'
#        
#class Counter_Terrorist(Player):             
#    def __init__(self):
#        self.name='Counter_Terrorist-'   
#        print(self.name)
#    
#class CT1(Counter_Terrorist):             
#    def __init__(self):
#        self.name='CT1-'
#        print(self.name)
#
#class CT2(Counter_Terrorist):             
#    def __init__(self):
#        self.name='CT2-'    
#    
#P=Player()
#T=Terrorist()
#CT=Counter_Terrorist()   
#T1=T1()
#T2=T2()
#CT1=CT1()
#CT2=CT2()
#Gun=gun()
#Pistol=pistol()
#Rifle=rifle()






#main

#print("Enter the player name: (Terrorist)(Counter-Terrorist)")
#Player_name=input()
#
#print("Enter the player type: (T1)(T2)(CT1)(CT2)")
#Player_type=input()


#print("Enter the gun sub type: (Groza)(AK47)(M24)(AWM)(DBS)(S686)((MG42)(Thompson MG)")
#Gun_subtype=input()
#

#if((Player_name=='Counter-Terrorist') & (Player_type=='CT1')):
#    print(CT1.name)
#else: 
#    print('scheme')
#    


























