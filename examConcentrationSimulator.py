'''
Create a function named exam_concentration_simulator that receives questions and difficulty_levels as its parameters.
This function simulates a student's thought process during an intense exam, focusing on advanced string and array manipulation. It processes a list of exam questions based on their difficulty levels and specific conditions.

Parameters:
questions (list of str): A list of strings representing exam questions.
difficulty_levels (list of int): A list of integers representing the difficulty level of each question (1-10, where 10 is the most difficult).

The function should process the questions as follows:
If a question's difficulty level is greater than 7, reverse the entire question string.
If a question contains the word "explain" (case-insensitive), skip processing that question and move to the next one.
If a question's length is a prime number, reverse the order of words in the question.
If a question's difficulty level is a multiple of 3, convert every third character to uppercase.
If a question starts with "What" or "How", continue to the next question without processing it.

The function returns a list of processed questions, maintaining the original order but with the above modifications applied.
Remember to handle edge cases, such as empty input lists or mismatched lengths between questions and difficulty levels.
'''

def isNumberPrime(num):
    if num<0:
        return False
    if num==1:
        return False
    if num==2:
        return True
    if num==3:
        return True
    halfNum = int(num/2)
    primeStatus = True
    for i in range(2,halfNum+1,1):
        if num%i==0:
            primeStatus = False
            break
    return primeStatus

def exam_concentration_simulator(questions, difficulty_levels):
    # Write code here 
    for i in range( len(questions) ):
        if len(questions[i]) == 0:
            questions[i] = ''
            continue
        if difficulty_levels[i]>7:
            questions[i] = questions[i][::-1] 
        if questions[i].lower().startswith("what") or questions[i].lower().startswith("how"):
            continue
        if 'explain'.casefold() in questions[i]:
            break
        if isNumberPrime( len(questions[i]) ):
            questionAsList = questions[i].split()
            questionAsList.reverse()
            questions[i]= " ".join(questionAsList)     
        if difficulty_levels[i]%3==0 and difficulty_levels[i]>2:
            for j in range( len(questions[i]) ):
                if(j+1)%3==0:
                     new_string = questions[i][:j] + questions[i][j].upper()  + questions[i][j+1:]
                     questions[i] = new_string
    return questions
