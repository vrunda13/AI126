import random

def SimpleReflexVacuumAgent(locationCondition):
        print(locationCondition)
        Score = 0
        if(locationCondition['A']==1 and locationCondition['B']==1):
            vacuumLocation = random.randint(0, 1)
        elif(locationCondition['A']==1):
            vacuumLocation =0
        elif(locationCondition['B']==1):
            vacuumLocation =1
        else:
            vacuumLocation = random.randint(0, 1)
        if vacuumLocation == 0:
            print("Vacuum is randomly placed at Location A")
            if locationCondition['A'] == 1:
                print("Location A is Dirty. ")
                locationCondition['A'] = 0;
                Score += 1
                print("Location A has been Cleaned. :D")
                if locationCondition['B'] == 1:
                    print("Location B is Dirty.")
                    print ("Moving to Location B...")
                    Score -= 1
                    locationCondition['B'] = 0;
                    Score += 1
                    print ("Location B has been Cleaned :D.")
            else:
                if locationCondition['B'] == 1:
                    print ("Location B is Dirty.")
                    Score -= 1
                    print ("Moving to Location B...")
                    locationCondition['B'] = 0;
                    Score += 1
                    print ("Location B has been Cleaned. :D")

        elif vacuumLocation == 1:
            print ("Vacuum is randomly placed at Location B. ")
            if locationCondition['B'] == 1:
                print ("Location B is Dirty")
                locationCondition['B'] = 0;
                Score += 1
                print ("Location B has been Cleaned")
                if locationCondition['A'] == 1:
                    print ("Location A is Dirty")
                    Score -= 1
                    print ("Moving to Location A")
                    locationCondition['A'] = 0;
                    Score += 1
                    print ("Location A has been Cleaned")
            else:
                if locationCondition['A'] == 1:
                    print ("Location A is Dirty")
                    print ("Moving to Location A")
                    Score -= 1
                    locationCondition['A'] = 0;
                    Score += 1
                    print ("Location A has been Cleaned")
        print (locationCondition)
        print ("Performance Measurement: " + str(Score))

locationCondition = {'A': '0', 'B': '0'}
locationCondition['A'] = int(input("Enter State of A:(0/1)"))
locationCondition['B'] = int(input("Enter State of B:(0/1)"))
SimpleReflexVacuumAgent(locationCondition)
