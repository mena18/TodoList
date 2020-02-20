from django.shortcuts import render,HttpResponse,get_object_or_404,redirect,reverse
from .models import Project,Folder,Task
from django.contrib import  messages
from django.utils import timezone
from django.views.generic import View,ListView
from .forms import TaskForm,ProjectForm,ListForm
import datetime
# Create your views here.


def home(request):
    today = datetime.date.today()
    delayed_tasks = Task.objects.filter(user=request.user,finished=False,deadline__lt=today).order_by('deadline')
    today_tasks = Task.objects.filter(user=request.user,finished=False,deadline=today)
    completed_tasks = Task.objects.filter(user=request.user,finished=True,completed_date=today)
    context = {'today':today_tasks,"delayed":delayed_tasks,"completed":completed_tasks}
    return render(request,"todo/home.html",context)


def toogle_finishing(request):
    pk = request.POST['pk'];
    task = get_object_or_404(Task,pk=pk);
    if(task.user!=request.user):
        messages.error(request,"forbiden")
        return redirect("todo:home")
    mes=""
    if(not task.finished):
        task.finished=True
        task.completed_date=datetime.date.today()
        mes="Task is completed"
    else:
        task.finished=False
        task.completed_date = None
        mes="Task is Marked and uncompleted"
    task.save()
    messages.success(request,mes)
    return redirect("todo:home")




"""  ----------------------- Tasks -----------------------  """
class CreateTask(View):

    def get(self,*args,**kwargs):
        form = TaskForm(user=self.request.user);
        context={'form':form,'head':"Create Task",'action':reverse("todo:create_task")}
        return render(self.request,"todo/form.html",context);

    def post(self,*args,**kwargs):
        form = TaskForm(self.request.POST,user=self.request.user);
        if(form.is_valid()):
            form.instance.user = self.request.user
            form.save()
            messages.success(self.request,"Task added")
            return redirect("todo:home")
        else:
            messages.error(self.request,"form isnot valid")
            return redirect("todo:home")


class EditTask(View):

    def get(self,*args,**kwargs):
        pk = kwargs['pk']
        task = get_object_or_404(Task,pk=pk)
        form = TaskForm(user=self.request.user,instance=task);
        context={'form':form,'head':"Edit Task",'action':reverse("todo:edit_task",kwargs={'pk':pk} )}
        return render(self.request,"todo/form.html",context);

    def post(self,*args,**kwargs):
        pk = kwargs['pk']
        task = get_object_or_404(Task,pk=pk)
        form = TaskForm(self.request.POST,user=self.request.user,instance=task);
        if(form.is_valid()):
            form.save()
            messages.success(self.request,"Task added")
            return redirect("todo:home")
        else:
            messages.error(self.request,"form isnot valid")
            return redirect("todo:home")


def DeleteTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if(task.user!=request.user):
        messages.error(request,"forbiden")
        return redirect("todo:home")
    task.delete()
    messages.success(request,"Deleted successfuly")
    return redirect("todo:home")



"""  ----------------------- End Tasks -----------------------  """




"""  ----------------------- Projects -----------------------  """
class CreateProject(View):

    def get(self,*args,**kwargs):
        form = ProjectForm(user=self.request.user);
        context={'form':form,'head':"Create Project",'action':reverse("todo:create_project")}
        return render(self.request,"todo/form.html",context);

    def post(self,*args,**kwargs):
        form = ProjectForm(self.request.POST,user=self.request.user);
        if(form.is_valid()):
            form.instance.user = self.request.user
            form.save()
            messages.success(self.request,"Task added")
            return redirect("todo:home")
        else:
            messages.error(self.request,"form isnot valid")
            return redirect("todo:home")


class EditProject(View):

    def get(self,*args,**kwargs):
        pk = kwargs['pk']
        project = get_object_or_404(Project,pk=pk)
        form = ProjectForm(user=self.request.user,instance=project);
        context={'form':form,'head':"Edit project",'action':reverse("todo:edit_project",kwargs={'pk':pk} )}
        return render(self.request,"todo/form.html",context);

    def post(self,*args,**kwargs):
        pk = kwargs['pk']
        project = get_object_or_404(Project,pk=pk)
        form = ProjectForm(self.request.POST,user=self.request.user,instance=project);
        if(form.is_valid()):
            form.save()
            messages.success(self.request,"project created")
            return redirect("todo:home")
        else:
            messages.error(self.request,"form isnot valid")
            return redirect("todo:home")


def DeleteProject(request,pk):
    project = get_object_or_404(Project,pk=pk)
    if(project.user!=request.user):
        messages.error(request,"forbiden")
        return redirect("todo:home")
    project.delete()
    messages.success(request,"Deleted successfuly")
    return redirect("todo:home")

def ViewProject(request,pk):
    project = get_object_or_404(Project,pk=pk)
    context = {"project":project}
    return render(request,"todo/view_project.html",context)


def ViewProjects(request):
    projects = Project.objects.filter(user=request.user)
    context={"projects":projects}
    return render(request,"todo/all_projects.html",context)

"""  ----------------------- End Projects -----------------------  """






"""  ----------------------- Lists -----------------------  """
class CreateList(View):

    def get(self,*args,**kwargs):
        form = ListForm();
        context={'form':form,'head':"Create List",'action':reverse("todo:create_list")}
        return render(self.request,"todo/form.html",context);

    def post(self,*args,**kwargs):
        form = ListForm(self.request.POST);
        if(form.is_valid()):
            form.instance.user = self.request.user
            form.save()
            messages.success(self.request,"list created")
            return redirect("todo:home")
        else:
            messages.error(self.request,"form isnot valid")
            return redirect("todo:home")


class EditList(View):

    def get(self,*args,**kwargs):
        pk = kwargs['pk']
        folder = get_object_or_404(Folder,pk=pk)
        form = ListForm(instance=folder);
        context={'form':form,'head':"Edit List",'action':reverse("todo:edit_list",kwargs={'pk':pk} )}
        return render(self.request,"todo/form.html",context);

    def post(self,*args,**kwargs):
        pk = kwargs['pk']
        folder = get_object_or_404(Folder,pk=pk)
        form = ListForm(self.request.POST,instance=folder);
        if(form.is_valid()):
            form.save()
            messages.success(self.request,"list changed")
            return redirect("todo:home")
        else:
            messages.error(self.request,"form isnot valid")
            return redirect("todo:home")


def DeleteList(request,pk):
    folder = get_object_or_404(Folder,pk=pk)
    if(folder.user!=request.user):
        messages.error(request,"forbiden")
        return redirect("todo:home")
    folder.delete()
    messages.success(request,"Deleted successfuly")
    return redirect("todo:home")

def ViewList(request,pk):
    folder = get_object_or_404(Folder,pk=pk)
    projects = Project.objects.filter(user=request.user,folder=folder)
    context={"projects":projects}
    return render(request,"todo/all_projects.html",context)


def ViewLists(request):
    lists = Folder.objects.filter(user=request.user)
    context={"lists":lists}
    return render(request,"todo/all_lists.html",context)


"""  ----------------------- End Lists -----------------------  """









tasks=[

{'name':"tasks operations",
"description":"",
"deadline":datetime.date(2020,2,19)
},
{'name':"project operations",
"description":"",
"deadline":datetime.date(2020,2,19)
},
{'name':"Folder operations",
"description":"",
"deadline":datetime.date(2020,2,19)
},
{'name':"Nice Design",
"description":"",
"deadline":datetime.date(2020,2,19)
},

]

def create_many(request):
    project = Project.objects.get(user=request.user,name='Todo')
    for task in tasks:
        Task.objects.create(name=task['name'],description=task['description'],deadline=task['deadline'],user=request.user,project=project)
    return redirect('todo:home')
