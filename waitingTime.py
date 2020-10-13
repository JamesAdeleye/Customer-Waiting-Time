#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
This code is developed to calculate the time a customer will wait for agent or staff to attend to him/her. 
It takes the email and name of the customer as input and give position of the customer on the waiting list and time of waiting.
"""

import re
def waitingTime():
    
    # The code takes the email of the customer here and confirm if it is a valid email address
    email = input("Please, put your email address here: ")
    pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]{2,3})"
    if re.search(pattern, email):
        print(email)
    else:
        print("email invalid")
        return 
    # The code takes the name of the customer and use it to compute the waiting time based on the available staffs and agents
    
    my_name = input("what is your name?" )
    agents = 4 # This takes the number of agents at work- NOTE: you can change the figure
    other_customers = ("Boye, Tolu, Shola, Seun, Wumi, Kemi, Comfort, Ade, Wale, Dada, Ojo, Iyanu") #This line can take a list of other customers, which can be changed
    customer_names = my_name+' '+other_customers
    customer_names_list = customer_names.split(' ')
    customer_names_list = sorted([o.lower() for o in customer_names_list])
    n_count = len(customer_names_list)
    my_position = (customer_names_list.index(my_name.lower())) + 1
    group_time_position = my_position/agents
    if my_position%agents == 0:
        waiting_time = (my_position/agents) * 20
    else: 
        waiting_time = (my_position//agents * 20) + 20
    print("Your position on the waiting list is", my_position)
    print("Please, you have to wait for " + str(waiting_time) + " minutes to be attended to, thank you")

