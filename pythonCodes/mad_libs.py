# A script to output stories to users based on their inputs using conditionals

name = str(input("State your name: "))
gender = str(input("Male or Female: "))
occupation = str(input("Select beetween Programming, Medicine, Engineering or Teaching: "))

female_doctor = "Dear doctor " + name + " here's a brief female doctor's story"
male_doctor = "Dear doctor " + name + " here's a brief male dotor's story"

female_programmer = "Dear developer "+ name +" here's a brief female developer story"
male_programmer = "Dear developer " + name + " here's a brief male developer story"

female_engineer = "Dear engineer " + name + " here's a brief female engineer's story"
male_engineer = "Dear engineer " + name + " here's a brief male engineer's story"

female_teacher = "Dear teacher " + name + " here's a brief female teacher's story"
male_teacher = "Dear teacher " + name + " here's a brief male teacher's story"


if gender == "male" and occupation == "medicine":
    print(male_doctor)
elif gender == "female" and occupation == "medicine":
    print(str(female_doctor))
elif gender == "male" and occupation == "programming":
    print(male_programmer)
elif gender == "female" and occupation == "programming":
    print(female_programmer)
elif gender == "male" and occupation == "engineering":
    print(male_engineer)
elif gender == "female" and occupation == "engineerring":
    print(female_engineer)
elif gender == "male" and occupation == "teaching":
    print(male_teacher)
elif gender == "male" and occupation == "teaching":
    print(male_teacher)
elif gender == "female" and occupation == "teaching":
    print(female_teacher)
else:
    print("opps no story for you", name, "choose a gender and occupation that is listed")
