from django.db import models
from django.utils import timezone


class Task(models.Model):
    """
    Task to do.
    """
    name = models.CharField(max_length=30)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField(null=True)
    memo = models.CharField(max_length=200, null=True)
    status = models.IntegerField(default=0)

    __TODO_IDX = 0
    __DOING_IDX = 1
    __DONE_IDX = 2
    __STATUS = {
        __TODO_IDX : 'ToDo',
        __DOING_IDX : 'Doing',
        __DONE_IDX : 'Done'
    }

    def create(self):
        self.startTime = timezone.now()
        self.status = self.__TODO_IDX

    def getId(self):
        return self.id

    def getName(self):
        try:
            return self.name
        except NameError:
            return False

    def setName(self, name):
        if name is None:
            raise TypeError('invalid name')
        self.name = name
        self.save()

    def getStartTime(self):
        try:
            return self.startTime
        except NameError:
            return False

    def getEndTime(self):
        try:
            if self.endTime is None:
                return ''
            return self.endTime
        except NameError:
            return False

    def getMemo(self):
        try:
            return self.memo
        except NameError:
            return False

    def setMemo(self, memo):
        if memo is not None:
            self.memo = memo
            self.save()

    def isToDo(self):
        return self.status == self.__TODO_IDX

    def setToDo(self):
        self.status = self.__TODO_IDX
        self.save()

    def isDoing(self):
        return self.status == self.__DOING_IDX

    def setDoing(self):
        self.status = self.__DOING_IDX
        self.save()

    def isDone(self):
        return self.status == self.__DONE_IDX

    def setDone(self):
        self.endTime = timezone.now()
        self.status = self.__DONE_IDX
        self.save()

    def Done(self):
        self.endTime = timezone.now()
        self.save()

    def getStatus(self):
        try:
            return self.status
        except NameError:
            return False

    def getStatusName(self):
        return self.__STATUS[self.getStatus()]

    def setStatus(self, status):
        self.status = status
        self.save()
