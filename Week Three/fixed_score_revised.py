score = float(input("Enter score: "))
def determieScore(score):
    if score < 0:
        theScore = "Invalid score"
    elif score > 100:
        theScore = "Invalid score"
    elif score >= 50 and score < 90:
        theScore = "Passable"
    elif score >= 90:
        theScore = "Excellent"
    elif score < 50:
        theScore = "Bad"
    return theScore
print(determieScore(score))