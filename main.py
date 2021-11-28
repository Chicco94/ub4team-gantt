#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mygantt import MyGantt
import gantt
import datetime

def main():
    r1 = gantt.Resource("Enrico")

    t1 = gantt.Task(name="test1", start=datetime.datetime.now(), duration=1)
    t2 = gantt.Task(name="test2", start=datetime.datetime.now(), duration=2, resources=[r1], depends_of=[t1])
    m1 = gantt.Milestone(name="m1", depends_of=[t1,t2])
    t3 = gantt.Task(name="test3", start=datetime.datetime.now(), duration=2, resources=[r1], depends_of=[m1])
    t3b = gantt.Task(name="test3", start=datetime.datetime.now(), duration=2, resources=[r1], depends_of=[m1])
    m2 = gantt.Milestone(name="m2", depends_of=[t3,t3b])
    t4 = gantt.Task(name="test4", start=datetime.datetime.now(), duration=4, resources=[r1], depends_of=[t3])
    m3 = gantt.Milestone(name="m2", depends_of=[t4])
    p1 = gantt.Project("project")
    p1.add_task(t1)
    p1.add_task(t2)
    p1.add_task(t3)
    p1.add_task(t3b)
    p1.add_task(t4)
    p1.add_task(m1)
    p1.add_task(m2)
    p1.add_task(m3)
    p1.make_svg_for_tasks(filename='project.svg', today=datetime.datetime.now(),scale=gantt.DRAW_WITH_DAILY_SCALE)

if __name__ == "__main__":
    main()