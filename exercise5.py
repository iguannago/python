my_name = 'David Crespo'
my_age = 37 # not a lie
my_height = 84 # inches
my_weight = 180 # lbs
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall and %f cms" % (my_height, my_height * 2.54)
print "He's %d pounds heavy and %d kgrs" % (my_weight, my_weight * 0.453592)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)