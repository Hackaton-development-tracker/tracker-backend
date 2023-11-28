from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    pass


class ProjectMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Course(models.Model):
    pass


class CourseEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Specializtion(models.Model):
    pass


class SpecializationRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)


class Skill(models.Model):
    pass


class SkillProficiency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class User(models.Model):
    pass
