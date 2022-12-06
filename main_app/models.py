from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

gender=(
    ('M','Male'),
    ('F','Female')
)

active =(
    ('1','Little or no exercise'),
    ('2','1-3 workouts/week'),
    ('3','4-5 workouts/week'),
    ('4','6-7 workouts/week')
)


fitnessgoal=(
    ('L','Loss Wieght'),
    ('G','Gain Muscle'),
    ('M','Maintain Weight')
)


class PersonFitness(models.Model):
    #1---What is your Fitness goal ? 
    goal=models.CharField(
        max_length=1 ,
        choices=fitnessgoal,
        default=fitnessgoal[0][0]
    )
    #2---Current [weight,height] & target weight 
    current_weight = models.IntegerField()
    height = models.IntegerField()
    target_weight = models.IntegerField()
    Gender=models.CharField(
        max_length=1 ,
        choices=gender,
        default=gender[0][0]
    ) 
    #3---Whats your gender ?  
    Active=models.CharField(
        max_length=1 ,
        choices=active,
        default=active[0][0]
    )
    #4---How Active are you ? 
    Dont_eat = models.TextField()

















# class FitnessGoal(models.Model):
#     goal=models.CharField(
#         max_length=1 ,
#         choices=fitnessgoal,
#         default=fitnessgoal[0][0]
#     )

    
# #2---Current [weight,height] & target weight 
# class Weight_Height(models.Model):
#     currentweight = models.IntegerField()
#     height = models.IntegerField()
#     targetweight = models.IntegerField()

# #3---Whats your gender ?



# class Gender(models.Model):
#     g=models.CharField(
#         max_length=1 ,
#         choices=gender,
#         default=gender[0][0]
#     )
    
    
# #4---How Active are you ? 



# class Active(models.Model):
#     a=models.CharField(
#         max_length=1 ,
#         choices=active,
#         default=active[0][0]
#     )
    
    
# #5---What do you not eat ? 
# class dontEat(models.Model):
#     donteat = models.TextField()

