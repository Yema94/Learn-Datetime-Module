projectslist = []
def addproject(project):
    projectslist.append(project)


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


taskcobj1 = Task("Name of Task one of project one", "Duration: 20 Days")

resourcecobj1 = Resource("Name of Person one working on project one", "Python Specialist")
resourcecobj2 = Resource("Name of Person two working on project one", "Data Science Specialist")

taskcobj1.addResource(resourcecobj1)
taskcobj1.addResource(resourcecobj2)

projectcobj.addTask(taskcobj1)

taskcobj2 = Task("Name of Task two of project one", "Duration: 20 Days")

taskcobj2.addResource(resourcecobj1)

projectcobj.addTask(taskcobj2)


addproject(projectcobj)


for eachprojectobj in projectslist:
    print(eachprojectobj.name, eachprojectobj.strdate, eachprojectobj.stopdate)
    for eachTaskobj in projectcobj.taskslist:
        print(" ",eachTaskobj.name, eachTaskobj.duration)
        for eachResourceobj in eachTaskobj.resourceslist:
            print("     ",eachResourceobj.name, eachResourceobj.skill)
