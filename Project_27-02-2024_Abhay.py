#!/usr/bin/env python
# coding: utf-8

# In[5]:


def calculate_duration(age, time_unit):
    

    if time_unit not in ['years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds']:
        raise ValueError("Invalid time unit. Please choose from 'years', 'months', 'weeks', 'days', 'hours', 'minutes', or 'seconds'.")

  
    if time_unit == 'years':
        return age
    elif time_unit == 'months':
        return age * 12
    elif time_unit == 'weeks':
        return age * 52.142857 
    elif time_unit == 'days':
        return age * 365.2425
    elif time_unit == 'hours':
        return age * 365.2425 * 24
    elif time_unit == 'minutes':
        return age * 365.2425 * 24 * 60
    else:
        return age * 365.2425 * 24 * 60 * 60

# Example usage
age = int(input("Enter the person's age: "))
time_unit = input("Enter the desired time unit (years, months, weeks, days, hours, minutes, or seconds): ")

try:
    duration = calculate_duration(age, time_unit.lower())
    print(f"{age} years is equivalent to approximately {duration:.2f} {time_unit}.")
except ValueError as e:
    print(e)


# In[ ]:





# In[ ]:




