def test(age,height,weight,duration,hr,bt,g):
    import pandas as pd
    import joblib as joblib
    
    height=height/100
    bmi=weight/(height**2)
    
    if g=='M' or 'm' :
        g=1
    else:
        g=0
    
    feature=pd.DataFrame([[age,bmi,duration,hr,bt,g]])
    model=joblib.load("model.pkl")
    prediction = model.predict(feature)
    prediction = round(prediction[0],2)
    return prediction

# age=eval(input("Enter your age: "))
# weight= eval(input("Enter your weight(in kgs): "))
# height= eval(input("Enter your height(in cm): "))
# duration=eval(input("Enter the duration(in minutes) for you want to predict the calories burned: "))
# hr=eval(input("Enter your heart rate: "))
# bt=eval(input("Enter your body temperature(in C): "))
# g=(input("Enter your gender (m/f): "))

# if g=='M' or 'm' :
#     g=1
# else:
#     g=0
# predicted_value = test(age,bmi,duration,hr,bt,g)
# print("The predicted value of the calories burned:", round(predicted_value[0],2))