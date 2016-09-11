"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

#for i in STATE_NAMES:
#    print("{}     is    {}".format(STATE_NAMES, STATE_NAMES[i]))

for state in STATE_NAMES:
    print("{:<3s} is {}".format(state, STATE_NAMES[state]))