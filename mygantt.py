#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import gantt

class MyGantt():
    def __init__(self):
        self.df = []
        # Change font default
        gantt.define_font_attributes(fill='black', stroke='black', stroke_width=0, font_family="Verdana")
        self.resources = {}
    
    def add_resources(self,resource:str):
        '''Add resource'''
        self.resources[resource] = (gantt.Resource(resource))

    def add_vacation(self,datefrom:datetime,dateto:datetime=None,resource:str=None):
        '''Add vacations'''
        if (resource is None):
            # add vacation to everyone
            return gantt.add_vacations(dfrom=datefrom,dto=dateto)
        else:
            self.resources[resource].add_vacations(dfrom=datefrom,dto=dateto)
            return 

    def is_resource_available(self,date:datetime,resource:str)->bool:
        '''Test if this resource is  avalaible for some dates'''
        return  self.resources[resource].is_available(date)

    def add_task(self,name:str,start_date:datetime=None,end_date:datetime=None,percent_done:int=0,duration:float=0,resources:list=[],depends_of:list=None,color:str=None):
        if (start_date is None): start_date = datetime.datetime.now()
        if (resources is []): return None
        if (duration == 0 and end_date is None): return None
        if (duration == 0): return gantt.Task(name=name, start=start_date, duration=end_date-start_date, percent_done=percent_done,depends_of=depends_of, resources=[r for r in self.resources], color=color)
        return gantt.Task(name=name, start=start_date, duration=duration, percent_done=percent_done,depends_of=depends_of, resources=[r for r in self.resources], color=color)

    def create_project(self,name:str):
        self.projects[name] = gantt.Project(name=name)

    def add_task_to_project(self,project,task_or_subproject):
        '''Add tasks/subproject/milestones to this project'''
        self.projects[project].add_task(task_or_subproject)

    def create_milestone(self,name:str,depends_of:list=[]):
        return gantt.Milestone(name=name, depends_of=depends_of)

    def print_project(self,project:str,focus:datetime=None,start:datetime=None,end:datetime=None):
        self.projects[project].make_svg_for_tasks(filename=f'{project}.svg', today=focus, start=start, end=end, scale=gantt.DRAW_WITH_WEEKLY_SCALE)