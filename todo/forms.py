from django import forms
from .models import Task,Project,Folder

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'start_date',
            'deadline',
            'project',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['project']=forms.ModelChoiceField(queryset=Project.objects.filter(user=user))



class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'start_date',
            'deadline',
            'folder',
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['folder']=forms.ModelChoiceField(queryset=Folder.objects.filter(user=user))



class ListForm(forms.ModelForm):

    class Meta:
        model = Folder
        fields = [
            'name',
        ]
