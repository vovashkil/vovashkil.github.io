#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue">A Calendar Application Example
# AWS CLOUD INSTITUTE: PROVIDED FOR EDUCATIONAL INSTRUCTIONAL PURPOSES ONLY.

# # A Schedule Calendar Application
# We'll **combine** some of the **data structures** we **discussed** to create a simple **scheduling calendar application**. The class will maintain **appointments at the granularity of one hour**. The class will support:
# - **Adding appointments**
# - **Deleting appointments**
# - **Listing monthly appointments**
# - **Retrieving a specific appoint**
# - **Returning the next few appointments** based on current time

# The **class will use multiple data structures**:
# - A **three dimensional array** to maintain the appointments
# - A **one dimensional array** to maintain the max days in each month
# - **Tuples** to return multiple values in a function
# - A **list of tuples** to represent a list of combined values

# ## MyCalendar Class

# In[ ]:


# use the datetime class to get current time
import datetime

class MyCalendar:
    '''
    This class will implement a calendar application, which will maintain appointments for a year. It will
    take the year in the constructor, so that a new one can be used every year, similar to paper calendars.
    The class will use a three dimension array to track appoints for each month, day, and hour.
    It will support methods to add appointments, review appointments, and check for upcoming appointments.
    '''

    # This class variable uses an array to maintain the maximum number of days in each month
    # Since the index starts at 0, we put a dummy value for month = 0
    # for simplicity, we assume every year is a leap year, and give February 20 days
    max_days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # This is a simple mapping of month numbers to names
    month_names = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    def __init__(self, year):
        '''
        The constructor will initialize the calendar for the given year, with all appointments set None.
        '''

        # initizlize years
        self.year = year

        # Initialize the 3 dimensional array to None.
        # So that we don't always have to offset the months and days by one, we make the array one day and month bigger
        # That way we can us the [month][day] indexes without having to subtract one
        self.appointments = [[[None for hour in range(24)] for day in range(32)] for month in range(13)]

    def add_appointment(self, month, day, hour, appointment):
        '''
        This method will add an appointment to the calendar for the given month, day, and hour.
        '''

        # raise an exception for an invalid date or time
        if not(1 <= month <= 12 and 1 <= day <= self.max_days_in_month[month]  and 0 <= hour < 24):
            raise ValueError("Invalid month, day, or hour")

        # if there is already an appoint at that time, raise an exception for a conflicting appointment
        if self.appointments[month][day][hour]:
            raise ValueError("Appointment conflict")

        # set the appointment
        self.appointments[month][day][hour] = appointment

    def delete_appointment(self, month, day, hour):
        '''
        This method will delete an appointment to the calendar for the given month, day, and hour.
        
        return:
            The deleted appointment, or None if there was none
        '''

        # raise an exception for an invalid date or time
        if not(1 <= month <= 12 and 1 <= day <= self.max_days_in_month[month]  and 0 <= hour < 24):
            raise ValueError("Invalid month, day, or hour")

        # get the appointment value for this time
        appointment = self.appointments[month][day][hour]
        
        # if there is already an appoint at that time, updated it to None   
        if appointment:
            self.appointments[month][day][hour] = None

        # return the appointment cleared
        return appointment

    def get_appointment(self, month, day, hour):
        '''
        This method retrieve the appointment to the calendar for the given month, day, and hour.
        
        return:
            The retrieved appointment, or None if there was none
        '''

        # raise an exception for an invalid date or time
        if not(1 <= month <= 12 and 1 <= day <= self.max_days_in_month[month]  and 0 <= hour < 24):
            raise ValueError("Invalid month, day, or hour")

        # get the appointment value for this time
        return self.appointments[month][day][hour]

    def monthly_appointments(self, month):
        '''
        This method will return the appointments for the given month.

        return:
            A list of tuples with the format: (month, day, hour, appointment)
        '''
        # raise an exception for an invalid month
        if not(0 <= month < 12):
            raise ValueError("Invalid month")

        # initialize the result apointments list
        result = []
        
        # loop through each day and hour in that month
        for day in range(31):
            for hour in range(24):
                # if there is an appointment at this hour, add it to result
                if self.appointments[month][day][hour]:
                    result.append((month, day, hour, self.appointments[month][day][hour]))

        # return appointments result
        return result

    def get_next_appointments(self, num_appointments = 1):
        '''
        This method will return the appointments after the current time. The num_appointments argument specifies how many to return,
        and defaults to 1.

        return:
            A list of tuples with the format: (month, day, hour, appointment)
        '''

        # get the current date and time using utility static method
        curr_month, curr_day, curr_hour = self.get_current_hour()

        # initialize the result apointments list
        result = []
        
        # set the day and hour we'll start to search as the current day
        start_day = curr_day
        start_hour = curr_hour + 1
        
        # loop through each month, day, and hour starting from the current date and time
        for month in range(curr_month, 13):
            # loop through remaining days in the month        
            for day in range(curr_day, self.max_days_in_month[month]):
                # loop through remaining hours in the day
                for hour in range(start_hour, 24):
                    # if there was an appointment at this day and hour, add tuple with appointment details to result list
                    if self.appointments[month][day][hour]:
                        result.append((month, day, hour, self.appointments[month][day][hour]))

                        # if we've reached the maximum number of appointments requested, return result imediately
                        if len(result) == num_appointments:
                            return result
                            
                # since we finished a day, reset the start hour to 0 for the next day
                start_hour = 0
            
            # since we finieshed a month, reset day to 1 for the next month
            start_day = 1

        # return list of appointments
        return result

    @staticmethod
    def get_current_hour():
        '''
        This static method will return a tuple containing the current month, day, and hour
        '''
        # get current time from datetime module
        now = datetime.datetime.now()

        # return tuple with month, day, and hour
        return (now.month, now.day, now.hour)

    def __str__(self):
        '''
        This method will return a string representation of the calendar object
        '''
        return f"Calendar for {self.year}"


# ## Test

# ### Create an calendar object for the current year

# In[ ]:


my_cal = MyCalendar(2024)
print(my_cal)


# ### Add some appointments

# #### Some appointments this week

# In[ ]:


# Add appointment for 10/14 at 12pm
my_cal.add_appointment(10, 14, 12, "DF2 - Week 3 - Advanced Data Structures - Stand up - Session 1")

# Add appointment for 10/14 at 13hr (1pm)
my_cal.add_appointment(10, 14, 13, "Walk Tucker and Moose")

# and a few more ...
my_cal.add_appointment(10, 14, 14, "DF2 - Week 3 - Advanced Data Structures - Stand up - Session 2")
my_cal.add_appointment(10, 14, 15, "Delivery Team Meeting")
my_cal.add_appointment(10, 14, 16, "DF2 - Week 3 - Advanced Data Structures - Stand up - Session 3")
my_cal.add_appointment(10, 14, 17, "Feed Tucker and Moose")


# In[ ]:


# Add appointment for 10/15 at 12pm
my_cal.add_appointment(10, 15, 12, "DF2 - Week 3 - Advanced Data Structures - Focus Session p1 - Session 1")

# Add appointment for 10/15 at 13hr (1pm)
my_cal.add_appointment(10, 15, 13, "Walk Tucker and Moose")

# and a few more ...
my_cal.add_appointment(10, 15, 14, "DF2 - Week 3 - Advanced Data Structures - Focus Session p1 - Session 2")
my_cal.add_appointment(10, 15, 16, "DF2 - Week 3 - Advanced Data Structures - Focus Session p1 - Session 3")
my_cal.add_appointment(10, 15, 17, "Feed Tucker and Moose")


# In[ ]:


# Add appointment for 10/16 at 12pm
my_cal.add_appointment(10, 16, 12, "DF2 - Week 3 - Advanced Data Structures - Focus Session p2 - Session 1")

# Add appointment for 10/16 at 13hr (1pm)
my_cal.add_appointment(10, 16, 13, "Walk Tucker and Moose")

# and a few more ...
my_cal.add_appointment(10, 16, 14, "DF2 - Week 3 - Advanced Data Structures - Focus Session p2 - Session 2")
my_cal.add_appointment(10,16, 16, "DF2 - Week 3 - Advanced Data Structures - Focus Session p2 - Session 3")
my_cal.add_appointment(10, 16, 17, "Feed Tucker and Moose")


# In[ ]:


# Add appointment for 10/17 at 12pm
my_cal.add_appointment(10, 17, 12, "DF2 - Week 3 - Advanced Data Structures - Labology - Session 1")

# Add appointment for 10/17 at 13hr (1pm)
my_cal.add_appointment(10, 17, 13, "Walk Tucker and Moose")

# and a few more ...
my_cal.add_appointment(10, 17, 14, "DF2 - Week 3 - Advanced Data Structures - Labology - Session 2")
my_cal.add_appointment(10, 17, 16, "DF2 - Week 3 - Advanced Data Structures - Labology - Session 3")
my_cal.add_appointment(10, 17, 17, "Feed Tucker and Moose")


# In[ ]:


# Add appointment for 10/18 at 12pm
my_cal.add_appointment(10, 18, 12, "Walk Tucker and Moose")

# Add appointment for 10/18 at 13hr (1pm)
my_cal.add_appointment(10, 18, 13, "One on one with manager")

# and a few more ...
my_cal.add_appointment(10, 18, 15, "Development Fundamentals Team meeting")


# #### Some appointments next month and beyond

# In[ ]:


# Add appointment for 11/4 at 12pm
my_cal.add_appointment(11, 4, 12, "DF2 - Week 6 - Algorithms - Stand up - Session 1")

# and a few more ...
my_cal.add_appointment(11, 4, 14, "DF2 - Week 6 - Algorithms - Stand up - Session 2")
my_cal.add_appointment(11, 4, 15, "Delivery Team Meeting")
my_cal.add_appointment(11, 4, 16, "DF2 - Week 6 - Algorithms - Stand up - Session 3")


# In[ ]:


# Add appointment for 11/21 at 4am
my_cal.add_appointment(11, 21, 9, "Fernando's birthday")

# Add appointment for 11/25 at 9am
my_cal.add_appointment(11, 25, 9, "Begin Thanksgiving break")


# In[ ]:


# Add appointment for 12/2 at 7am
my_cal.add_appointment(12, 2, 7, "Fernando starting Disney vacation")

# Add appointment for 12/8 at 7pm
my_cal.add_appointment(12, 8, 19, "Fernando returns to New Jersey")

# Add appointment for 12/19 at 4pm
my_cal.add_appointment(12, 19, 16, "Last DF2 session of the year")


# ### Retrieve appointments

# #### Get specific appointments

# In[ ]:


# get appointment for 10/15 at 14hr
month = 10
day = 15
hour = 14
appointment = my_cal.get_appointment(month, day, hour)

# print appointment if there is one
if appointment:
    print(f"On {month}/{day} at {hour}hrs --> {appointment}")
else:
    print(f"You have no appointments at {month}/{day} at {hour}")


# In[ ]:


# get appointment (non-existent) for 9/18 at 9am
month = 9
day = 18
hour = 9
appointment = my_cal.get_appointment(month, day, hour)

# print appointment if there is one
if appointment:
    print(f"On {month}/{day} at {hour}hrs --> {appointment}")
else:
    print(f"You have no appointments at {month}/{day} at {hour}")


# #### Get all appointments this month

# In[ ]:


# get appointment for specified month
month = 10
appointments = my_cal.monthly_appointments(month)

# print a header using class variable to get month name
print(f"Appointments for {MyCalendar.month_names[month]}:")

# iterate through list of appointments, and get each tuple with appointment info
for appt_info in appointments:
    # assign variables to each specific item in the tuple
    month, day, hour, appointment = appt_info

    # print appointment details
    print(f"    On {month}/{day} at {hour}hrs --> {appointment}")


# #### Get upcoming appointments

# In[ ]:


# get next upcoming appointment based on current time
appointments = my_cal.get_next_appointments()

# iterate through list of appointments, and get each tuple with appointment info
for appt_info in appointments:
    # assign variables to each specific item in the tuple
    month, day, hour, appointment = appt_info

    # print appointment details
    print(f"On {month}/{day} at {hour}hrs --> {appointment}")


# In[ ]:


# get next 5 upcoming appointment based on current time
appointments = my_cal.get_next_appointments(5)

# iterate through list of appointments, and get each tuple with appointment info
for appt_info in appointments:
    # assign variables to each specific item in the tuple
    month, day, hour, appointment = appt_info

    # print appointment details
    print(f"On {month}/{day} at {hour}hrs --> {appointment}")


# ### Delete appointments

# In[ ]:


# get appointment for 10/8 at 14hr
month = 10
day = 7
hour = 14
appointment = my_cal.get_appointment(month, day, hour)

# print appointment
print(f"On {month}/{day} at {hour}hrs --> {appointment}")

# delete the appointment
print("Deleting appointment ...")
my_cal.delete_appointment(month, day, hour)

# try to retrieve and print appointment
appointment = my_cal.get_appointment(month, day, hour)
print(f"On {month}/{day} at {hour}hrs --> {appointment}")


# ### Validation and error handling
# If we look at the code, we see that most **methods perform validations** up front, **and generate exceptions for invalid cases**.

# #### Retrieving an appointment with an invalid date

# In[ ]:


# try to retrieve an appointment for February 30th, which is an invalid day
month = 2
day = 30
hour = 2

appointment = my_cal.get_appointment(month, day, hour)
print(f"On {month}/{day} at {hour}hrs --> {appointment}")


# #### Trying to add an appoint when there is already one
# In a simple calendar, we only allow one appoint per slot

# In[ ]:


month = 10
day = 15
hour = 16

# Show there is an appointment already at this time
appointment = my_cal.get_appointment(month, day, hour)
print(f"On {month}/{day} at {hour}hrs --> {appointment}")

# Try to add an appointment at the same time
print(f"Trying to add an appointment on {month}/{day} at {hour}hrs ...")
my_cal.add_appointment(month, day, hour, "Team meeting")
print("Appointment added successfully")


# # More ideas
# **This was** a **simple implementation** to **show** a few **different data structures**. We could use more data structures, object-oriented programming, and Python code to make a **lot more enhancements ...**
# - Support appointments with flexible begin and end times
# - Support a multi-year calandar
# - Print formatted calendars
# - Maintain some appointments in a high priority queue
# - Etc, etc, etc
# 
# Maybe we'll come to it in the future, or maybe you can add some of your own.
