
# coding: utf-8

# ### Login System
# 
# Creating a basic login system which will ask for username and password and will match it up with the one's existing in the database.
# 
# STEP-1
import getpass
# Setting a default username and password
username="admin"
password="thenewdogwillbite"

# Taking the input of username
u=input("Username: ")

if u==username:
    
# Taking password as input
    p=getpass.getpass('Password: ')
    if p==password:
        print("Logged in sucessfully!")
    else:
        print("Incorrect password")
    
else:
    print('Invalid Username')
