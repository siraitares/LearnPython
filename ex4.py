cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "cars not driven"
print "We can transport", carpool_capacity, "persons"
print "We have", passengers, "to carpool"
print "We need to put about", average_passengers, "in each car"
