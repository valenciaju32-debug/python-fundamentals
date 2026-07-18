# Day2: Conditionals
ticket_priority = int(input ("what is the ticket priority number? "))
if ticket_priority == 5:
    print ("Category: Critical")
elif ticket_priority == 4:
    print ("Category: High")
elif ticket_priority == 3:
    print ("Category: Medium")
elif ticket_priority == 2:
    print ("Category: Low")
else:
    print("Invaild priority")
