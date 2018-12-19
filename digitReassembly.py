# Works in Python 2.7
def digit_reassembly(number,places):

    origString = str(number);
    total = 0;
    newString = ""
    oldString = str(number)

    while (len(oldString) >= places):
        newString = oldString[:places]
        total = total + int(newString)
        oldString = oldString[1:]
    print ("Input: " + origString + "\n" + "Output: " + str(total))
      
'''
Test Cases
digit_reassembly(1325678905,2)
digit_reassembly(54981230845791,5)
digit_reassembly(4837261529387456,3)
digit_reassembly(385018427388713440,4)
digit_reassembly(623387770165388734,11)
'''
