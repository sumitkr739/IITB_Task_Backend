from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.title

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, related_name='instances', on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.course.title} - {self.year} - Semester {self.semester}"
