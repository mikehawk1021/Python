# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 14:59:44 2018

@author: HP
"""
#Method 1
def Genre(name):
    Output = "Song Genre: Blues"
    return Output

def Rating(Number):
    Output = "Music Rating: 4.5"
    return Output

def Artist(ArtNames):
    Output = "Artist Name: Adele"
    return Output

v1 = 0
var2 = Genre(v1)
var3 = Rating(v1)
var4 = Artist(v1)
print(var4)
print(var3)
print(var2)


#Method 2


def Genre():
    print('Genre: Blues')
    
def Artist():
    print('Artist Name: Adele')
    
def Rating():
    print('Rating: 4.5')
    
Artist()
Genre()
Rating()