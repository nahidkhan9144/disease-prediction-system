import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix ,classification_report
from sklearn.ensemble import RandomForestClassifier

from tkinter import *
import numpy as np
import pandas as pd

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']
#List of Diseases is listed in list disease.
disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']
l2=[]
for i in range(0,len(l1)):
    l2.append(0)

df=pd.read_csv("C:\\Users\\Nahid khan\\OneDrive\\Desktop\\login\\Prototype.csv")

#Replace the values in the imported file by pandas by the inbuilt function replace in pandas.

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

#check the df 
#print(df.head())

X= df[l1]

#print(X)

y = df[["prognosis"]]
np.ravel(y)

#print(y)

#Read a csv named Testing.csv

tr=pd.read_csv("C:\\Users\\Nahid khan\\OneDrive\\Desktop\\login\\Prototype-1.csv")

#Use replace method in pandas.

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]

#print(y_test)

np.ravel(y_test)

def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier() 
    clf3 = clf3.fit(X,y)

    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy 
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

class inter:
    def __init__(self,root):

        self.root = root
        self.root.geometry('1350x1875+0+0')
        self.root.configure(bg="lightblue")
#frame=Frame(root,width=1250,height=600,bg="lightgrey")
#frame.place(x=50,y=50)       
        tit=Label(text='DISEASE PREDICTION SYSTEM',bg="lightblue",font=("times new roman",20,"bold"))
        tit.place(x=450,y=50)

        Symptom1 = StringVar()
        Symptom1.set("Select Here")

        Symptom2 = StringVar()
        Symptom2.set("Select Here")

        Symptom3 = StringVar()
        Symptom3.set("Select Here")

        Symptom4 = StringVar()
        Symptom4.set("Select Here")

        Symptom5 = StringVar()
        Symptom5.set("Select Here")

        OPTIONS = sorted(l1)
        Name= Label(text="symptom 1 :",bg="lightblue",font=("Times",18,"bold"))
        Name.place(x=150,y=150)
        S1 = OptionMenu(root, Symptom1,*OPTIONS)
        S1.place(x=300,y=150)
        Name= Label(text="symptom 2 :",bg="lightblue",font=("Times",18,"bold"))
        Name.place(x=550,y=150)
        S2 = OptionMenu(root, Symptom2,*OPTIONS)
        S2.place(x=700,y=150)
        Name= Label(text="symptom 3 :",bg="lightblue",font=("Times",18,"bold"))
        Name.place(x=950,y=150)
        S3 = OptionMenu(root, Symptom3,*OPTIONS)
        S3.place(x=1100,y=150)
        Name= Label(text="symptom 5 :",bg="lightblue",font=("Times",18,"bold"))
        Name.place(x=550,y=230)
        S4 = OptionMenu(root, Symptom5,*OPTIONS)
        S4.place(x=700,y=230)
        Name= Label(text="symptom 4 :",bg="lightblue",font=("Times",18,"bold"))
        Name.place(x=150,y=230)
        S5 = OptionMenu(root, Symptom4,*OPTIONS)
        S5.place(x=300,y=230)
        #buttons
        pred= Label(text="Prediction result:",fg="red",bg="lightblue",font=("Times",20,"bold"))
        pred.place(x=500,y=300)
        btn1=Button(text="decision tree",cursor="hand2",command=DecisionTree, font=("times new roman", 15),bg="white",fg="black")
        btn1.place(x=450,y=370)
        btn2=Button(text="random forest",cursor="hand2" ,command=randomforest,font=("times new roman", 15),bg="white",fg="black")
        btn2.place(x=450,y=430)
        btn3=Button(text="naive bayes",cursor="hand2", command=NaiveBayes,font=("times new roman", 15),bg="white",fg="black")
        btn3.place(x=450,y=500)

        #Name.grid(row=6, column=0, pady=15, sticky=W)
        #l1=Label(text="decision tree algorithm",font=("times new roman", 15),bg="lightblue",fg="black")
        #l1.place(x=150,y=370)
        t1 = Text(root, height=1.5, width=40,bg="white",fg="black")
        t1.place(x=600,y=370)
        #l2=Label(text="random forest algorithm",font=("times new roman", 15),bg="lightblue",fg="black")
        #l2.place(x=150,y=420)
        t2 = Text(root, height=1.5, width=40,bg="white",fg="black")
        t2.place(x=600,y=430)
        #l3=Label(text="naive bayes algorithm",font=("times new roman", 15),bg="lightblue",fg="black")
        #l3.place(x=150,y=470)
        t3 = Text(root, height=1.5, width=40,bg="white",fg="black")
        t3.place(x=600,y=500)
root=Tk()
obj=inter(root)
root.mainloop()