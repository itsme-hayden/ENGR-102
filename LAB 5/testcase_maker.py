from math import*
import random


def calculate_total(sex, tol):
    if(sex == "M"):
        if(tol < 0):
            return "<1"
        elif(tol == 0):
            return 1
        elif(tol == 1):
            return 1
        elif(tol == 2):
            return 1
        elif(tol == 3):
            return 1
        elif(tol == 4):
            return 1
        elif(tol == 5):
            return 2
        elif(tol == 6):
            return 2
        elif(tol == 7):
            return 3
        elif(tol == 8):
            return 4
        elif(tol == 9):
            return 5
        elif(tol == 10):
            return 6
        elif(tol == 11):
            return 8
        elif(tol == 12):
            return 10
        elif(tol == 13):
            return 12
        elif(tol == 14):
            return 16
        elif(tol == 15):
            return 20
        elif(tol == 16):
            return 25
        elif(tol >= 17):
            return ">30"
    if(sex == "F"):
        if(tol < 9):
            return "<1"
        elif(tol == 9):
            return 1
        elif(tol == 9):
            return 1
        elif(tol == 10):
            return 1
        elif(tol == 11):
            return 1
        elif(tol == 12):
            return 1
        elif(tol == 13):
            return 2
        elif(tol == 14):
            return 2
        elif(tol == 15):
            return 3
        elif(tol == 16):
            return 4
        elif(tol == 17):
            return 5
        elif(tol == 18):
            return 6
        elif(tol == 19):
            return 8
        elif(tol == 20):
            return 11
        elif(tol == 21):
            return 14
        elif(tol == 22):
            return 17
        elif(tol == 23):
            return 22
        elif(tol == 24):
            return 27
        elif(tol >= 25):
            return ">30"
    
    

def create_output(sex, age, cho, smo, hdl, sbp, med):
    tol = 0
    if(sex == "M"):
        if(age <=34):
            tol -= 9
        elif(age >= 35 and age <=39):
            tol -= 4
        elif(age >= 40 and age <=44):
            tol += 0
        elif(age >= 45 and age <=49):
            tol += 3
        elif(age >= 50 and age <=54):
            tol += 6
        elif(age >= 55 and age <=59):
            tol += 8
        elif(age >= 60 and age <=64):
            tol += 10
        elif(age >= 65 and age <=69):
            tol += 11
        elif(age >= 70 and age <=74):
            tol += 12
        elif(age >= 75):
            tol += 13
        
        if(cho < 160):
            tol += 0
        elif(cho >= 160 and cho <= 199):
            if(age <= 39):
                tol += 4
            elif(age >= 40 and age <= 49):
                tol += 3
            elif(age >= 50 and age <= 59):
                tol += 2
            elif(age >= 60 and age <= 69):
                tol += 1
            elif(age >= 70):
                tol += 0
        elif(cho >= 200 and cho <= 239):
            if(age <= 39):
                tol += 7
            elif(age >= 40 and age <= 49):
                tol += 5
            elif(age >= 50 and age <= 59):
                tol += 3
            elif(age >= 60 and age <= 69):
                tol += 1
            elif(age >= 70):
                tol += 0
        elif(cho >= 240 and cho <= 279):
            if(age <= 39):
                tol += 9
            elif(age >= 40 and age <= 49):
                tol += 6
            elif(age >= 50 and age <= 59):
                tol += 4
            elif(age >= 60 and age <= 69):
                tol += 2
            elif(age >= 70):
                tol += 1
        elif(cho >= 280):
            if(age <= 39):
                tol += 11
            elif(age >= 40 and age <= 49):
                tol += 8
            elif(age >= 50 and age <= 59):
                tol += 5
            elif(age >= 60 and age <= 69):
                tol += 3
            elif(age >= 70):
                tol += 1

        if(smo == "Y"):
            if(age <= 39):
                tol += 8
            elif(age >= 40 and age <= 49):
                tol += 5
            elif(age >= 50 and age <= 59):
                tol += 3
            elif(age >= 60 and age <= 69):
                tol += 1
            elif(age >= 70):
                tol += 1
        
        if(hdl >= 60):
            tol -= 1
        elif(hdl >= 50 and hdl <= 59):
            tol += 0
        elif(hdl >= 40 and hdl <= 49):
            tol += 1
        elif(hdl <= 40):
            tol += 2

        if(med == "N"):
            if(sbp >= 130 and sbp <= 139):
                tol += 1
            elif(sbp >= 140 and sbp <= 159):
                tol += 1
            elif(sbp >= 160):
                tol += 2
        elif(med == "Y"):
            if(sbp >= 120 and sbp <= 129):
                tol += 1
            elif(sbp >= 130 and sbp <= 139):
                tol += 2
            elif(sbp >= 140 and sbp <= 159):
                tol += 2
            elif(sbp >= 160):
                tol += 3

        

    elif(sex == "F"):
        if(age <= 34):
            tol -= 7
        elif(age >= 35 and age <=39):
            tol -= 3
        elif(age >= 40 and age <=44):
            tol += 0
        elif(age >= 45 and age <=49):
            tol += 3
        elif(age >= 50 and age <=54):
            tol += 6
        elif(age >= 55 and age <=59):
            tol += 8
        elif(age >= 60 and age <=64):
            tol += 10
        elif(age >= 65 and age <=69):
            tol += 12
        elif(age >= 70 and age <=74):
            tol += 14
        elif(age >= 75):
            tol += 16

        
        if(cho < 160):
            tol += 0
        elif(cho >= 160 and cho <= 199):
            if(age <= 39):
                tol += 4
            elif(age >= 40 and age <= 49):
                tol += 3
            elif(age >= 50 and age <= 59):
                tol += 2
            elif(age >= 60 and age <= 69):
                tol += 1
            elif(age >= 70):
                tol += 1
        elif(cho >= 200 and cho <= 239):
            if(age <= 39):
                tol += 8
            elif(age >= 40 and age <= 49):
                tol += 6
            elif(age >= 50 and age <= 59):
                tol += 4
            elif(age >= 60 and age <= 69):
                tol += 2
            elif(age >= 70):
                tol += 1
        elif(cho >= 240 and cho <= 279):
            if(age <= 39):
                tol += 11
            elif(age >= 40 and age <= 49):
                tol += 8
            elif(age >= 50 and age <= 59):
                tol += 5
            elif(age >= 60 and age <= 69):
                tol += 3
            elif(age >= 70):
                tol += 2
        elif(cho >= 280):
            if(age <= 39):
                tol += 13
            elif(age >= 40 and age <= 49):
                tol += 10
            elif(age >= 50 and age <= 59):
                tol += 7
            elif(age >= 60 and age <= 69):
                tol += 4
            elif(age >= 70):
                tol += 2


        if(smo == "Y"):
            if(age <= 39):
                tol += 9
            elif(age >= 40 and age <= 49):
                tol += 7
            elif(age >= 50 and age <= 59):
                tol += 4
            elif(age >= 60 and age <= 69):
                tol += 2
            elif(age >= 70):
                tol += 1

        if(hdl >= 60):
            tol -= 1
        elif(hdl >= 50 and hdl <= 59):
            tol += 0
        elif(hdl >= 40 and hdl <= 49):
            tol += 1
        elif(hdl <= 40):
            tol += 2

        if(med == "N"):
            if(sbp >= 120 and sbp <= 129):
                tol += 1
            if(sbp >= 130 and sbp <= 139):
                tol += 2
            elif(sbp >= 140 and sbp <= 159):
                tol += 3
            elif(sbp >= 160):
                tol += 4
        elif(med == "Y"):
            if(sbp >= 120 and sbp <= 129):
                tol += 3
            elif(sbp >= 130 and sbp <= 139):
                tol += 4
            elif(sbp >= 140 and sbp <= 159):
                tol += 5
            elif(sbp >= 160):
                tol += 6
 
    return calculate_total(sex, tol)

f = open("testcases.txt", "a")

for i in range(200):
    sex = "F"
    smo = "Y"
    med = "Y"

    MorF = random.random()
    if(MorF < .5):
        sex = "M"
    age = random.randint(15,85)
    cho = random.randint(150,290)
    smoke = random.random()
    if(smoke < .5):
        smo = "N"
    hdl = random.randint(30,70)
    sbp = random.randint(110, 170)
    meds = random.random()
    if(meds < .5):
        med = "N"

    out = create_output(sex, age, cho, smo, hdl, sbp, med)
    txt = f"sex:{sex} age:{age} cho:{cho} smo:{smo} hdl:{hdl} sbp:{sbp} med:{med} out:{out}\n"
    print(txt)
    f.write(txt)
f.close()
