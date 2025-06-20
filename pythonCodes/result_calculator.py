# A script that calculates students' results

class InvalidScoreError(Exception):
    def __init__(self, score_type):
        self.score_type = score_type

    def __str__(self):
        return f"Error: Invalid {self.score_type} score"


def main():

    try:
        exam_score = float(input("Input your exam score: "))        
        if exam_score < 0 or exam_score > 100:
            raise InvalidScoreError("exam")
        test_score = float(input("Input your test score: "))
        if test_score < 0 or test_score > 20:
            raise InvalidScoreError("test")
        
        practical_score = float(input("Input your practical score: "))
        if practical_score < 0 or practical_score > 20:
            raise InvalidScoreError("practical")
    except InvalidScoreError as err:
        print(err)
    except ValueError as err:
        print("Error: Only numbers are allowed", err)

    else:
        percentage_exam_score = float((exam_score / 100) * 60) # converts the exam score to percentage

        total_score = percentage_exam_score + test_score + practical_score

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

        if practical_score == 0:
            grade = "F"
        
        print(f"Your Result \n{"-" * 10} \nExam score: {exam_score} \nTest Score: {test_score} \nPractical Score: {practical_score} \n{"-"*10} \nTotal Score: {total_score} \nGrade: {grade}")
    

if __name__ == "__main__":
    main()