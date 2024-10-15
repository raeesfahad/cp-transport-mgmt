from django.db import models

# University choices
DEPARTMENT_NAME = [
    ('English', 'English'),
    ('Computer-Sci', 'Computer Science'),
    # Add more universities as needed
]

# Bus types
BUS_TYPES = [
    ('VAN', 'Van'),
    ('YOUTONG', 'Youtong Bus'),
    ('CARRY', 'Carry'),
]

# University days
UNIVERSITY_SHIFT= [
    ('MORNING', 'Morning'),
    ('EVENING', 'Evening'),
]

class Bus(models.Model):
    """
    Represents a bus with its details.
    """
    bus_number = models.CharField(max_length=10, unique=True)
    bus_type = models.CharField(max_length=10, choices=BUS_TYPES)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.bus_number} - {self.bus_type}"


class Route(models.Model):
    """
    Represents a bus route with its source, destination, and stops.
    """
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.source} to {self.destination}"


class Schedule(models.Model):
    """
    Represents a bus schedule with its departure and arrival times.
    """
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    university_shift = models.CharField(max_length=10, choices=UNIVERSITY_SHIFT)

    def __str__(self):
        return f"{self.bus} - {self.route} - {self.departure_time} to {self.arrival_time} on {self.university_shift}"


class Student(models.Model):
    """
    Represents a university student with their details.
    """
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=15)
    Department = models.CharField(max_length=20, choices=DEPARTMENT_NAME)

    def __str__(self):
        return f"{self.name} - {self.student_id} - {self.Department}"


class Pass(models.Model):
    """
    Represents a bus pass with its details.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.bus} - {self.route} - Valid from {self.start_date} to {self.end_date}"


class PassValidation(models.Model):
    """
    Represents a pass validation with its details.
    """
    pass_instance = models.ForeignKey(Pass, on_delete=models.CASCADE)
    validation_date = models.DateField()
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pass_instance} - Validated on {self.validation_date} - {self.is_valid}"
