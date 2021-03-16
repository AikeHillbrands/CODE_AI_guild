################################################################################
# Problem Setup: You want the perfect bread
# What influences this?
#  - how long do you toast it?
#  - how long after toasting do you eat the bread?
#  - Do you have power? And how much? 
#  - Which toaster do you use?
################################################################################

import math
import numpy as np

################################################################################
# the function you are supposed to optimize.
# It has the following input:
#  toast_duration: duration of toasting in seconds. It is supposed to be an integer between 1 and 100
#  wait_duration: duration of waiting after toasting in seconds. It's supposed to be an integer between 1 and 100
#  toaster: the number of the toaster you want to use. It's supposed to be an integer, between 1 and 10.
#  power: how much power the toaster has (it's supposed to be a floating point number between 0 and 2)
################################################################################
def utility(toast_duration, wait_duration, power = 1.0,toaster = 1):
    # handle input errors
    if (not type(toast_duration) is int) or not (1 <= toast_duration <= 100):
        raise ValueError("toast_duration is not an integer")
    if (not type(wait_duration) is int) or not (1 <= wait_duration <= 100):
        raise ValueError("wait_duration is not an integer")
    if (not type(toaster) is int) or not (1 <= toaster <= 10):
        raise ValueError("toaster is not an integer or is not in a valid range")
    if (not type(power) is float) or not (0.0 <= power <= 2.0):
        raise ValueError("power is not a float or not in the valid range")

    # get toaster specific configuration
    hpt = [10,8,15,7,9,2,9,19,92,32][toaster-1]
    hpw = [1,4,19,3,20,3,1,4,1,62][toaster-1]
    toaster_utility = [1,0.9,0.7,1.3,0.3,0.8,0.5,0.8,3,0.2][toaster-1]

    # calculate values
    toast_utility = -0.1*(toast_duration-hpt)**2+1
    wait_utility = -0.01*(wait_duration-hpw)**2+1
    overall_utility = (toast_utility + wait_utility) * toaster_utility

    # apply modifier based on electricity
    power_factor = math.sin(10*power+math.pi/2 -10) + power*0.2
    overall_utility *= power_factor

    return overall_utility


################################################################################
# Writing this function is your homework. 
# The function should return the tuple of parameters that optmizes the function.
# 
# You can implement it in multiple difficulty levels:
# easy: 
#     - implement it with only two parameters: toast_duration and wait_duration
#     - e.g., utility(2,3)
#     - Implement the function by testing all possible values for these variables.
#     - (This state space has only 10000 values, so it shouldn't take too long)
#
# medium: 
#    - same as easy, but implement hill climbing
#    - see pseudo code
# hard: 
#    - also use the parameter power
#    - e.g., utility(2,3,1.2)
#    - this introduces the following complications:
#        - multiple maxima
#        - a continuous parameter
#    - implement gradient ascent
# very hard:
#    - Same as hard, but use repeated search to find all maxima. 
#    - repeated search: 
#        - apply gradient descent from different starting points.
#    - I think there are 5 maxima. But I'm not sure :-P
# prepare to cry:
#    - find the optimum for all four parameters
#    - define your own algorithm!
def find_maximum_easy():
    params = np.zeros((100,100))
    for x in range(100):
        for y in range(100):
            params[x,y] = utility(x,y)

    return

def random_args():
    return (np.random.randint(99)+1,np.random.randint(99)+1,np.random.randint(200)/100)

def next_best_step(args,lr = 0.1,toaster = 1):
    max_val = utility(*args,toaster=toaster)
    max_arg = args
    finished = True
    for arg1 in [-1,0,+1]:
        for arg2 in  [-1,0,+1]:
            for arg3 in  [-1,0,+1]:
                a= (
                        args[0] + arg1,
                        args[1] + arg2,
<<<<<<< HEAD
                        args[2] + arg3 * lr
=======
                        args[2] + arg3*lr
>>>>>>> 4422dbc (add verbose to toaster optimisation)
                    )
                try:
                    val  = utility(*a,toaster=toaster)

                    if val > max_val:
                        max_val = val
                        max_arg = a
                        finished = False
                except:
                    pass
    
    return max_arg,finished

<<<<<<< HEAD
def find_max_extreme(toaster = 1, verbose = 0):
=======
def find_max_extreme(toaster = 1,verbose = 0):
>>>>>>> 4422dbc (add verbose to toaster optimisation)
    params = random_args()

    finished = False

    lr = 0.1

    while not finished:
        params,finished = next_best_step(params,lr,toaster)
<<<<<<< HEAD
        if verbose:
            print(f"Score: {np.round(utility(*params,toaster=toaster),10)} with params: {params}")  
=======

        if verbose:
            print(f"Score {utility(*params)} for params {params}")

>>>>>>> 4422dbc (add verbose to toaster optimisation)
        if finished and lr > 1e-10:
            lr *=0.1
            finished = False
             

    return params

find_max_extreme(verbose=1)

<<<<<<< HEAD
best_toaster = None
best_val = None
best_params = None

optimum = find_max_extreme(verbose=1)

for toaster in range(1,11):
    print(f"Checking toaster: {toaster}")
    for i in range(200):
        optimum = find_max_extreme()
        val = utility(*optimum,toaster=toaster)
=======
# for toaster in range(1,11):

#     res = {}

#     for i in range(400):
#         optimum = find_max_extreme(verbose=1)
#         res[optimum] = utility(*optimum,toaster=toaster)
>>>>>>> 4422dbc (add verbose to toaster optimisation)

        if best_val is None or val > best_val:
            best_toaster = toaster
            best_val = val
            best_params = optimum

<<<<<<< HEAD
    print(f"Best score so far: Score: {best_val} with toaster: {best_toaster} and params: {best_params}")
print(f"Score: {best_val} with toaster: {best_toaster} and params: {best_params}")
#Score: 2740.9903781640137 with toaster: 9 and params: (1, 100, 0.055522069999999965)
=======
#     [print("Toaster",toaster,i) for i in res.items()]
>>>>>>> 4422dbc (add verbose to toaster optimisation)
