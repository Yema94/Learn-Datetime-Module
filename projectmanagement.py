# To manage multiple projects, tasks in those projects, and resources alloced for those tasks


# stores the objects of the project class
# len(projectslist) tells the number of projects
projectslist = []

def addproject(project):
    """This function takes the the obj of the project class as a paramenter and adds to the "projectlist"
     here number of objs == number of projects"""
    projectslist.append(project)

    
# ============================================Project Class============================================
class Project:
    """This Project class obj takes the name, startdate, and enddate of the project as initializing parameters """
    
    def __init__(self, name, strdate, stopdate):
        self.name = name # name of the project
        self.strdate = strdate # start date of the project
        self.stopdate = stopdate # end date of the project
        
        # stores the objs of the tasks class related to that particular project
        # len(taskslist) == number of Task class objs == number of tasks in that particular project
        self.taskslist = [] 

    def addTask(self, task):
    """This function takes the the obj of the Task class as a paramenter and adds to the "taskslist""""
        self.taskslist.append(task)
        
    def __del__(self):
        print("Destruction of Project Object!")

        
# ============================================Task Class============================================
class Task:
    """This Task class obj takes the name, and duration of the task as initializing parameters """    
    def __init__(self, name, duration):
        self.name = name # name of the task
        self.duration = duration # time duration of the task 
        
        # stores the objs of the resources allocated to this particular task
        # len(resourcelist) == number of resource class objs == number of persons working on that task
        self.resourceslist = [] 

    def addResource(self, resource):
        """This function takes the the obj of the Resource class as a paramenter and adds to the "resourceslist""""
        self.resourceslist.append(resource)
      
    def __del__(self):
        print("Destruction of Task Object!")

 
# ============================================Resource Class============================================
class Resource:
    """This Resource class obj takes the name, and skill of the employee allocated on a particular task as initializing parameters """  
    def __init__(self, name, skill):
        self.name = name # name of the employee
        self.skill = skill # skill set of this employee
        
    def __del__(self):
        print("Destruction of Resource Object!")        


# ============================================Main Program============================================        
if __name__=="__main__":

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
