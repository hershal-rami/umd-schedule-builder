'''
UMD Schedule Builder
https://github.com/hershal-rami/umd-schedule-builder

Authors:
Hershal Rami
Ben Davidson

6/20/2020
'''

import requests
import Schedule

def query_by_Id(courseID):
    #Make call to umd.io to get all sections with given courseID
    r = requests.get('https://api.umd.io/v1/courses/' + courseID)
    return r

def generate_possibilities(schedule):
    #Brute force schedules, return some data structure containing of them
    pass

benSc = Schedule.Schedule()
hershSc = Schedule.Schedule()

benClasses = ['CMSC351', 'CMSC216', 'HACS200', 'MATH241', 'CMSC389O', 'GEOG170']
hershClasses = ['CMSC351', 'CMSC330', 'STAT400', 'HACS200', 'HACS208N', 'CMSC389O']

for c in benClasses:
    benSc.add_course(c)

for c in hershClasses:
    hershSc.add_course(c)

#print("Ben:")

#print("Hershal " + hershClasses)
