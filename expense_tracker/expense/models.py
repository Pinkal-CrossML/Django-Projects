from django.db import models



class ExpenseCategories(models.Model):
    OPTIONS = [('TR','travel'), 
    ('ED','education'), 
    ('GD','gift_donation'), 
    ('BU','bill_utilities'), 
    ('FD','food_dining'),
    ('HF','health_fitness'),
    ('PC','Personal_care'),
    ('FC','fees_charges')]
    category = models.CharField(max_length=200, choices=OPTIONS,default=OPTIONS[-1])

    def __str__(self):
        return self.category



class Expense(models.Model):
    travel = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    gift_donations = models.CharField(max_length=200)
    bills_utilities = models.CharField(max_length=200)
    food_dining = models.CharField(max_length=200)
    health_fitness = models.CharField(max_length=200)
    personal_care = models.CharField(max_length=200)
    fees_charges = models.CharField(max_length=200)

