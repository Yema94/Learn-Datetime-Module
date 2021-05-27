class Project:
    def __init__(self, name, strdate, stopdate):
        self.name = name
        self.strdate = strdate
        self.stopdate = stopdate
        self.taskslist = []

    def addTask(self, task):
        self.taskslist.append(task)


class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.resourceslist = []

    def addResource(self, resource):
        self.resourceslist.append(resource)


class Resource:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill


projectcobj = Project("Name of Project one", "Starting Date: 1st June 2021", "Ending Date: 1st Sept 2021")
taskcobj = Task("Name of Task one of project one", "Duration: 20 Days")
resourcecobj = Resource("Name of Person one working on project one", "Python Specialist")
task.addResource(resourcecobj)
project.addTask(taskcobj)


for eachTaskobj in project.taskslist:
    print(eachTaskobj.name, eachTaskobj.duration)
    for eachResourceobj in eachTaskobj.resourceslist:
        print(eachResourceobj.name, eachResourceobj.skill)
