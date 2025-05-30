# A script that calculates students' results

exam_score = float(input("Input your exam score: "))
test_score = float(input("Input your test score: "))
practical_score = float(input("Input your practical score: "))

# converts the exam score to the representative overall percentage
percentage_exam_score = float((exam_score / 100) * 60)

# converts the test score to the representative overall percentage
percentage_test_score = float((test_score / 100) * 40)

# Ensuring the exam, test and practical scores are not greater than 100, 40, and 20 respectively


def score_authenticator():
    exam_err_msg = "Invalid exam score" if 0 > exam_score > 100 else None
    test_err_msg = "Invalid exam score" if 0 > test_score > 40 else None
    practical_err_msg = "Invalid exam score" if 0 > practical_score > 20 else None

    if (exam_err_msg == True or test_err_msg == True or practical_err_msg == True):
        score_authenticator(True) and print(exam_err_msg, test_err_msg, practical_err_msg)
    



    # return if exam_err_msg == True or test_err_msg or practical_err_msg == True  else result_calculator()

    


def result_calculator():
    # Calculating the general score
    total_score = percentage_exam_score + percentage_test_score + practical_score

    #  Returning an "F" grade if practical score is 0
    if practical_score == float(0):
        grade = "F"

    # Grading the total score
    if total_score >= 70:
        grade = "A"
    elif total_score >= 60:
        grade = "B"
    elif total_score >= 50:
        grade = "C"
    elif total_score >= 45:
        grade = "D"
    elif total_score >= 40:
        grade = "E"
    else:
        grade = "F"

    print("Your grade is ", grade)

def err_message():
    if score_authenticator(True):
        return
    else:
        result_calculator()

# score_authenticator()
err_message()
# result_calculator()