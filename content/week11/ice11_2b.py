from ice11_2a import display_all_gpas

gpa_dict = {'George Leung': 3.4, 'Eric Wong': 3.9, 'Michelle Lee': 3.1}
print("Current GPA information")
print()
display_all_gpas(gpa_dict)

name = input("Whose GPA do you want to change? ")
while name not in gpa_dict:
    print("Sorry! This student doesn't exist.")
    print()
    name = input("Whose GPA do you want to change? ")
gpa_dict[name] = float(input("What's the new GPA?"))
print("Thanks! GPA has changed.")
print()
print("The new GPA information:")
print()
display_all_gpas(gpa_dict)
