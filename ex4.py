cars = 100              #We have 100 cars
space_in_a_car = 4.0        #how much passengers car be in car
drivers = 30        #We have 30 drrivers
passengers = 90         #We need to drive 90 passenger
cars_not_driven = cars - drivers        #Cars without drivers
cars_driven = drivers       #Cars with drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put", average_passengers_per_car, "in each car."
 
