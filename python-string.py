msg1 = "Fred scored {} out of {} points."
print(msg1.format(3, 10))

# => 'Fred scored 3 out of 10 points.'

msg2 = 'Fred {verb} a {adjective} {noun}.'
print(msg2.format(adjective='fluffy', verb='tickled', noun='hamster'))

# => 'Fred tickled a fluffy hamster.'

greeting = "Welcome To Chili's"

print(greeting.lower())
# Prints: welcome to chili's

dinosaur = "T-Rex"

print(dinosaur.upper()) 
# Prints: T-REX