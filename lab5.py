import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.
#in data file

# Part 2
   # The function for Part 2 should be within the class in data.py.
#in data file

# Part 3
#Purpose is to add two different time object and as a result create a new time object with it being added
#Input is the time object in (hrs.minutes,seconds)  Ex. (3,4,5) and (4,5,6)
# Output is the new time object (7,9,11)
def time_add(time1:data.Time, time2:data.Time)->data.Time:
    seconds=time1.second + time2.second #Add seconds together
    minutes=time1.minute + time2.minute+(seconds//60)  #Add minutes together with an integer division for seconds
    hours=time1.hour+time2.hour+(minutes//60) #Add hours together with an integer division for minutes
    new_sec=seconds%60  #Get remainder for seconds and minutes
    new_min=minutes%60
    return data.Time(hours,new_min,new_sec) #New object

# Part 4
#Purpose of the function is to return a boolean value depending on if the list is in descending order
#Input is the list like [7,6,5,4]
#Output is the value which in the example above would be true
def is_descending(lst:list[float])->bool:
    for i in range(1,len(lst)): #A loop to check each index on the list from a range between1 to the length of the list
        if lst[i]>= lst[i-1]: #if statement to check to see if the index is less than the index before it
            return False
    return True
# Part 5
#Purpose is to find the index that is the largest between the lower and upper integers
#Input is the list and lower and upper numbers Ex. [788,55,4400] lower:0 upper:2
#Output is based on the lower and upper values and it returns the index that has the largest number   Ex. max_idx=2
def largest_between(lst:list[int],lower:int,upper:int):
    if lower>upper: #To filter out if lower is greater than upper because the rest of the function won't work.
        return None
    if lower < 0: #To filter out if lower is less than 0.
        lower = 0
    if upper >= len(lst): # Upper has to be within the bounds of the length of the list
        upper=len(lst)-1
    if lower>upper: #To filter out if lower is greater than upper because the rest of the function won't work.
        return None
    max_idx=lower
    for i in range(lower,upper +1): # A for loop with an if statement to find the index that is greater than lower and less than upper in the list.
        if lst[i]>lst[max_idx]:
            max_idx=i
    return max_idx

# Part 6
#Purpose is to find the index with the largest distance from the origin
#Input is the list of data points like [Point(20,2),Point(1,4),Point(2,2)
#Output is the the index with the largest distance like for example furthest_idx= 0
def furthest_from_origin(point:list[data.Point])->int:
    def distance_formula_with_origin(points:data.Point): #This function will be used to calculate the distance formula by squaring and adding the x and y coordinates and taking the square root of that.
        x_squared=points.x**2
        y_squared=points.y**2
        add=x_squared+y_squared
        return add**(0.5)
    furthest_idx=0
    furthest_distance=distance_formula_with_origin(point[0]) #Start off with these two variables, and it will be used in the for loop area.
    for i in range(1,len(point)): #For loop to check each index on the list with a range from 1 to the length of that list
      distance_i=distance_formula_with_origin(point[i]) #Calulate the distance for each index on the list
      if distance_i>furthest_distance: #If statement will be used to check if the distance i is greater than the furthest distance then furthest_idx will be i.
          furthest_distance=distance_i
          furthest_idx=i
    return furthest_idx