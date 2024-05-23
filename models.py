from django.db import models

class Room(models.Model):
    ID_Room = models.AutoField(primary_key=True)
    scheme = models.TextField()

    def __str__(self):
        return f"Room {self.ID_Room}"

class Building(models.Model):
    ID_Building = models.AutoField(primary_key=True)
    address = models.TextField()
    name = models.TextField()
    reception_time = models.TextField()
    building = models.TextField()
    station = models.TextField()
    scheme = models.ImageField(upload_to='building_schemes/')

    def __str__(self):
        return self.name


class Property(models.Model):
    ID_Property = models.AutoField(primary_key=True)
    category = models.TextField()
    image = models.ImageField(upload_to='property_images/')
    conditions = models.BooleanField()
    ID_Building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.TextField()
    ID_Room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category} - {self.ID_Building.name} {self.floor}-{self.ID_Room.ID_Room}"
    


class Employee(models.Model):
    ID_Employee = models.AutoField(primary_key=True)
    category = models.TextField()
    image = models.ImageField(upload_to='employee_images/')
    post = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()

    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.post}"


class User(models.Model):
    ID_User = models.AutoField(primary_key=True)
    role = models.TextField()
    email = models.TextField()
    password = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()
    image = models.ImageField(upload_to='user_images/')

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class History(models.Model):
    ID_Epoch = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    ID_Property = models.ForeignKey(Property, on_delete=models.CASCADE)
    ID_Employee = models.IntegerField()

    def __str__(self):
        return f"Дата {self.date}"
