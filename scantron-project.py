### CMPT 120 
### author Diana Cukierman
###
### Project - Scantron Data processing 
###
###  CODE PROVIDED
import turtle as t


def read_string_list_from_file(the_file):
    '''
    GENERIC READING OF TEXT FILE
    USE AS TEMPLATE, INCORPORATE IN YOUR FILE
    GENERATES A LIST OF STRINGS, ONE STRING PER ELEMENT
    AUTHOR: Diana Cukierman

    Assumptions:
    1) the_file is in the same directory (folder) as this program 
    2) the_file contains one student per "line"  
    3) lines are separated by "\n", that is, after each "line" (student)
       in the file  there is a return ("\n") . Also there is (one single)
       return ("\n") after the last line  in the_file
    4) Thhis function returns a list of strings
    '''
    
    fileRef = open(the_file,"r")      # opening file to be read
    localList=[]                      # new list being constructed
    for line in fileRef:
        string = line[0:len(line)-1]  # -1: eliminates trailing '\n'
                                      # of each line 
                                    
        localList.append(string)      # appends a new element
                                      # of type string to the list
        
    fileRef.close()  
        
    #........
    '''
    print ("\n JUST TO TRACE, the local list of strings is:\n")
    for element in localList:
        print (element)  # element is a string for one student'''
    #........
        
    return localList

    
    
def write_result_to_file(lres,the_file):
    '''
    Creates a text output file from a list of strings
    AUTHOR: Diana Cukierman
    
    Assumptions:
    1) lres is a list of strings, where each string
       will be one line in the output file
    2) the_file will contain the name fo the output file.
       for this porgram it shoudl be a name with .csv extension
    3) it is assumed that each string in lres already includes
       the character "\n" at the end
    4) the resulting file will be in the same directory (folder) as this program 
    5) the resulting file will  contain one student data per line 
    '''
    
    fileRef = open(the_file,"w") # opening file to be written
    for line in lres:
        fileRef.write(line)
                                    
    fileRef.close()
    return
                
                
def listofPoints(): #This returns a list of the POINTS for each question
        answerKey = read_string_list_from_file("IN_key+pts.txt")
        line = answerKey[1] #Retrieves a string of the second line in the text file
        x = line.split() #Takes the string and splits the numbers with spaces and places it in a list
        #print (x)
        return (x)

def listofAnswerKey(): #This returns a list of the ANSWER KEY
        answerKey = read_string_list_from_file("IN_key+pts.txt")
        line = answerKey [0]
        x = []
        for i in range(len(line)):
                x.append(line[i])
        #print (x)
        return (x)

def numbersToLetters(): #This functions receives a list of the answer key and changes the numbers to letters
        answerKey = listofAnswerKey()
        x = []
        for i in range(len(answerKey)):
                if (answerKey[i] == '1'):
                        x.append('A')
                elif (answerKey[i] == '2'):
                        x.append('B')
                elif (answerKey[i] == '3'):
                        x.append('C')
                elif (answerKey[i] == '4'):
                        x.append('D')
        #print (x)
        return (x)
        

def listofAllAnswers(): #This function retrieves a list of ALL the ANSWERS from the STUDENTS
        studentsAnswers = read_string_list_from_file("IN_data_studs.txt")
        x = []
        
        line = 0
        while (line < len(studentsAnswers)):
                l = []
                answer = studentsAnswers[line]
                for i in range(8, len(answer)):
                        l.append(answer[i])
                line += 1
                x.append(l)
        #print (x)
        return (x)
        


def totalPoints(): #This function calculates the TOTAL possible POINTS
        listPoints = listofPoints()
        points = 0
        for i in range(len(listPoints)):
                points += float(listPoints[i])
        #print (points)
        return (points)
        
def countStudents(): #Returns the AMOUNT of STUDENTS
        count = 0
        listofStudents = listofAllAnswers()
        for i in range(len(listofStudents)):
                count += 1
        #print (count)
        return (count)
        
def countQuestions(): #Returns the AMOUNT of QUESTIONS
        count = 0
        listofQuestions = listofAnswerKey()
        for i in range(len(listofQuestions)):
                count += 1
        #print (count)
        return (count)
        
name = "BBB" #TEST NAME 
        
def listofSelectedAnswers(name): #This function retrieves a list of a SELECTED STUDENT
        studentsAnswers = read_string_list_from_file("IN_data_studs.txt")
        x = []
        line = 0
        for line in range(len(studentsAnswers)):
                check = studentsAnswers[line]
                space = check.find(' ')
                if (check[0:space] == name[0:len(name)]):
                        start = 8
                        while (start < len(check)):
                                x.append(check[start])
                                start += 1
        #print (x)
        return (x)


def classList():        #this function creates a list of the studetns names
        studentinfo = read_string_list_from_file("IN_data_studs.txt")
        x = []
        i = 0
        for i in range(len(studentinfo)):
                    check = studentinfo[i]
                    space = check.find(' ')
                    x.append(check[0:space])
        #print(x)
        return(x)
          

def checkAllAnswers(): #This function calculates the points of ALL STUDENTS COMBINED
        listPoints = listofPoints()
        answerKey = listofAnswerKey()   
        allAnswers = listofAllAnswers()
        
        points = 0
        for x in range(len(allAnswers)):
                for i in range(x):
                        if (answerKey[i] == allAnswers[x][i]):
                                points += float(listPoints[i])
        #print (points)
        return (points)


def checkSelected(name): #This function calculates the points of a SELECTED STUDENT
        listPoints = listofPoints()
        answerKey = listofAnswerKey()
        studentsAnswers = listofSelectedAnswers(name)
        points = 0
        for i in range(len(listPoints)):
                if (answerKey[i] == studentsAnswers[i]):
                        points += float(listPoints[i])   

        #print (points)
        return (points)

def percentage(name): #Calculates the percentage of a students score
        x = float(checkSelected(name))/(totalPoints())*100
        return (x)

                             
        
def Maximum(): #Retrieves the highest score in the class
        checkselected = checkSelected(name)
        classlist = classList()
        maximum = 0
        for i in range(len(classlist)):
                if checkSelected(classlist[i]) > maximum:
                        maximum = checkSelected(classlist[i])
        #print(maximum)
        return (maximum)         
        
def average():          #Returns the average score of the whole class
        checkselected = checkSelected(name)
        classlist = classList()
        total = 0
        for i in range(len(classlist)):
                total = total + checkSelected(classlist[i])
        ave = total/countStudents()
        #print(ave)
        return (ave)
        

def optionALL():   #functions prints (Student, Score, Percentage) for all students
        classlist = classList()
        checkselected = checkSelected(name)
        for i in range(len(classlist)):
                   print(classlist[i] + "," + str(checkSelected(classlist[i])) + "," + str(percentage(classlist[i])))



def countCorrect():
        answerKey = listofAnswerKey()
        allAnswers = listofAllAnswers()
        numberofQuestions = countQuestions()
        
        points = 0
        l = []

        for i in range(len(answerKey)):
                x = 0
                points = 0
                while (x < len(allAnswers)):
                        if (answerKey[i] == allAnswers[x][i]):
                                points += 1                     
                        x += 1
                l.append(points)
                
        return (l)


def hardestQuestions():
        count = countCorrect()
        numberofQuestions = countQuestions()
        amountofStudents = listofAllAnswers()
        final = 15
        x = []
        pos = 0
        
        for i in range(len(count)):
                if int(count[i]) < final:
                        pos = i
                        final = count[i]
                elif (count[i] == final):
                        position = i
                        x.append(position+1)
                else:
                        final = final
        x.append(pos+1)        
        return(x)             

def distribution():
        x = []
        for i in range(10):
            x.append(0)
        classlist = classList()
        for i in range(len(classlist)):
                if (percentage(classlist[i]) > 90):
                        x[9] += 1
                elif (percentage(classlist[i]) > 80 and percentage(classlist[i]) <= 90):
                        x[8] += 1
                elif (percentage(classlist[i]) > 70 and percentage(classlist[i]) <= 80):
                        x[7] += 1
                elif (percentage(classlist[i]) > 60 and percentage(classlist[i]) <= 70):
                        x[6] += 1
                elif (percentage(classlist[i]) > 50 and percentage(classlist[i]) <= 60):
                        x[5] += 1
                elif (percentage(classlist[i]) > 40 and percentage(classlist[i]) <= 50):
                        x[4] += 1
                elif (percentage(classlist[i]) > 30 and percentage(classlist[i]) <= 40):
                        x[3] += 1
                elif (percentage(classlist[i]) > 20 and percentage(classlist[i]) <= 30):
                        x[2] += 1
                elif (percentage(classlist[i]) > 10 and percentage(classlist[i]) <= 20):
                        x[1] += 1
                else:
                        x[0] += 1  
                      
        return(x)
        
def distance(input1, input2):
        dis = 0
        answerKey = listofAnswerKey()
        allAnswers = listofAllAnswers()
        i = 0

        while (i < len(allAnswers)):
                if (allAnswers[i][input1-1] == answerKey[input1-1] and allAnswers[i][input2-1] == answerKey[input2-1] or not(allAnswers[i][input1-1]) == answerKey[input1-1] and not(allAnswers[i][input2-1]) == answerKey[input2-1]):
                        dis = dis
                else:
                        dis += 1
                i += 1
        return (dis)

def tracedistance(input1, input2):
        dis = 0
        answerKey = listofAnswerKey()
        allAnswers = listofAllAnswers()
        classNames = classList()
        i = 0

        while (i < len(allAnswers)):
                if (allAnswers[i][input1-1] == answerKey[input1-1] and allAnswers[i][input2-1] == answerKey[input2-1] or not(allAnswers[i][input1-1]) == answerKey[input1-1] and not(allAnswers[i][input2-1]) == answerKey[input2-1]):
                        dis = 0
                        print("TRACE: Distance for student " + classNames[i] + " is " + str(dis))
                else:
                        dis = 1
                        print("TRACE: Distance for student " + classNames[i] + " is " + str(dis))
                i += 1
        
def Graph():
        t.speed(25)
        x = input("Would you like to graph the distribution? (Y/N)")
        if x == "Y":
                distribute = distribution()
                t.forward(280)
                t.left(180)
                t.forward(560)
                t.left(180)
                for i in range(len(distribute)):
                        t.left(90)
                        t.forward(distribute[i]*25)
                        t.right(90)
                        t.forward(20)
                        t.right(90)
                        t.forward(distribute[i]*25)
                        t.left(90)
                        t.forward(20)
                                     

        else:
                print("No graph will be presented.")

                
def questionDistance():
        x = input("Would you like to calulate the distance? (Y/N), Case sensitive: ")
        if x == "Y":
                input1 = 1
                input2 = 1
                zero = '0'
                while (not(int(input1)) == 0 or not(int(input2)) == 0):
                        input1 = int(input("Input the first question you would like to compare. Enter 0 if you would like to end:  \n"))
                        input2 = int(input("Input the second question you would like to compare. Enter 0 if you would like to end:  \n"))
                        if (input1 == 0 or input2 == 0):
                                print ("Done!")
                                return 
                        else:
                                ##print("TRACE" + str(tracedistance(input1, input2)))
                                print ("The distance is: " + str(distance(input1,input2)))
                                tracedistance(input1,input2)
                
        else:
                print("Distance will not be calculated")



def main():
        print("JUST TO TRACE, the local list of strings is: " + str(read_string_list_from_file("IN_data_studs.txt")))
        print()
        print()
        totalPoints()
        countStudents()
        countQuestions()
        numbersToLetters()

        listofPoints()
        listofAnswerKey()
        listofAllAnswers()
        listofSelectedAnswers(name)
        
        checkAllAnswers()
        checkSelected(name)


        
        print("CMPT 120,\n" +
                "Fall 2017, SFU Burnaby (Afternoon)\n" +
                "Final Project babyyy\n" +
                "Instructor : Diana Cukierman\n" + 
                "| Brian Panjaitan | Christien John | Clarence Lam |  \n")

        print("This program will process files containing all the names of the students and their answers \n" +
                  "The scantron contains " + str(countQuestions()) + " questions \n" + 
                "There are " + str(countStudents()) + " students who answered a scantron \n" + 
                "The total points a student can recieve is " + str(totalPoints()) + "\n" + 
                "The answer key is " + str(numbersToLetters()))
          
        keyPress = input("Type ALL if you would like to process all the answers of every student \n" + 
                                         "Type SEL if you would like to process a selected student's answers (Cap sensitive) \n")
        all = "ALL"
        sel = "SEL"
        inputName = 1
        Ls = []
        if (keyPress == sel):
            listofStudents = classList()
            while (not(inputName) == "END"):
                    for i in range(len(listofStudents)):
                            inputName = input("Please input a name of the student you would like to process, type END to process students: ")
                            if (inputName == "END"):
                                print ("All your selected students have been processed!")
                                print()
                                print("Your output will be: ")
                                for i in range(len(Ls)):
                                        print(Ls[i] + "," + str(checkSelected(Ls[i])) + "," + str(percentage(Ls[i])))
                                checkselected = checkSelected(name)

                                maximum = 0
                                for i in range(len(Ls)):
                                        if checkSelected(Ls[i]) > maximum:
                                                maximum = checkSelected(Ls[i])

                                checkselected = checkSelected(name)
                                total = 0
                                for i in range(len(Ls)):
                                        total = total + checkSelected(Ls[i])
                                ave = total/len(Ls)


                                
                                studentsAnswers = read_string_list_from_file("IN_data_studs.txt")
                                x = []
                                line = 0
                                for i in range(len(Ls)):
                                        listss = []
                                        for line in range(len(studentsAnswers)):
                                                check = studentsAnswers[line]
                                                space = check.find(' ')
                                                if (check[0:space] == Ls[i][0:len(Ls[i])]):
                                                        start = 8
                                                        while (start < len(check)):
                                                                listss.append(check[start])
                                                                start += 1
                                        x.append(listss)       
                    
                                answerKey = listofAnswerKey()
                                numberofQuestions = countQuestions()
                    
                                points = 0
                                l = []

                                for i in range(len(answerKey)):
                                        y = 0
                                        points = 0
                                        while (y < len(x)):
                                                if (answerKey[i] == x[y][i]):
                                                        points += 1                     
                                                y += 1
                                        l.append(points)

                                hardest = 15
                                LIST = []
                                pos = 0
                                for i in range(len(l)):
                                        if int(l[i]) < hardest:
                                                pos = i
                                                hardest = l[i]
                                        elif (l[i] == hardest):
                                                position = i
                                                x.append(position+1)
                                        else:
                                                hardest = hardest
                                LIST.append(pos+1)

                                x = []
                                for i in range(10):
                                    x.append(0)
                                for i in range(len(Ls)):
                                        if (percentage(Ls[i]) > 90):
                                                x[9] += 1
                                        elif (percentage(Ls[i]) > 80 and percentage(Ls[i]) <= 90):
                                                x[8] += 1
                                        elif (percentage(Ls[i]) > 70 and percentage(Ls[i]) <= 80):
                                                x[7] += 1
                                        elif (percentage(Ls[i]) > 60 and percentage(Ls[i]) <= 70):
                                                x[6] += 1
                                        elif (percentage(Ls[i]) > 50 and percentage(Ls[i]) <= 60):
                                                x[5] += 1
                                        elif (percentage(Ls[i]) > 40 and percentage(Ls[i]) <= 50):
                                                x[4] += 1
                                        elif (percentage(Ls[i]) > 30 and percentage(Ls[i]) <= 40):
                                                x[3] += 1
                                        elif (percentage(Ls[i]) > 20 and percentage(Ls[i]) <= 30):
                                                x[2] += 1
                                        elif (percentage(Ls[i]) > 10 and percentage(Ls[i]) <= 20):
                                                x[1] += 1
                                        else:
                                                x[0] += 1  
                                  

                      
                                print()
                                print("HERE ARE THE STATS!")
                                print("===================")
                                print()
                                print("Maximum points:" + " " + str(maximum))
                                print()
                                print("Average points:" + " " + str(ave))
                                print()
                                print("Number of students processed " + str(len(Ls)))
                                print("Number of times each question was answered correctly\n" + str(l))
                                print()
                                print("Most difficult question(s) " + str(LIST))
                                print()
                                print("Distribution points " + str(x))
                                print("(Considering ranges: [10,20,30,40,50,60,70,80,90,100]")
                                print()
                                Dist = input("Would you like to calculate the distance? (Y/N) Case sensitive.")
                                if Dist == "Y":
                                        input1 = 1
                                        input2 = 1
                                        zero = '0'
                                        while (not(int(input1)) == 0 or not(int(input2)) == 0):
                                                input1 = int(input("Input the first question you would like to compare. Enter 0 if you would like to end:  \n"))
                                                input2 = int(input("Input the second question you would like to compare. Enter 0 if you would like to end:  \n"))
                                                if (input1 == 0 or input2 == 0):
                                                        print ("Done!")
                                                        print("All stats are done! BYE!")
                                                        return 
                                                else:
                                                        print ("The distance is: " + str(distance(input1,input2)))
                                else:
                                    print("All stats are done! BYE!")
                                      
                                
                            elif (not(inputName) in listofStudents):
                                print ("Sorry what you have inputted is not in the file")

                            else:
                                    print (inputName + "," + str(checkSelected(inputName)) + "," + str(percentage(inputName)))
                                    Ls.append(inputName)

        
               
        elif (keyPress == all):
                optionALL()
                print()
                print("HERE ARE THE STATS!")
                print("===================")
                print()
                print("Maximum points:" + " " + str(Maximum()))
                print()
                print("Average points:" + " " + str(average()))
                print()
                print("Number of students processed:" + " " + str(countStudents()))
                print()
                print("Number of times each answer was correct \n" + str(countCorrect()))
                print()
                print("Most difficult questions" + str(hardestQuestions()))
                print()
                print("Distribution points" + " " + str(distribution()))
                print("(Considering ranges: [10,20,30,40,50,60,70,80,90,100]")
                Graph()
                questionDistance()
                print("All the stats are done! BYE!")
                      
                

        else:
                print ("What you have inputed is not a proper answer")

        

main()


