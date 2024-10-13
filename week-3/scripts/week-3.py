#!/usr/bin/env python3



import numpy as np
import pandas as pd



class Car:
    """
    Car class which has brand, model and year attributes.
    """
    def __init__(self, brand: str, model: str, year: int):
        """
        Constructor of Car class.

        **Args**:
            brand (str): Brand of car.
            model (str): Model of car.
            year (int): Year of car.
        """
        self.brand_ = brand
        self.model_ = model
        self.year_ = year



    def print_information(self):
        """
        Print information of car.

        **Args**:
            None
        """
        print("Brand: " + self.brand_)
        print("Model: " + self.model_)
        print("Year: " + str(self.year_))



class Week3:
    def __init__(self):
        pass



    def question1(self):
        """
        Checking data structures and their methods.

        **Args**:
            None
        """
        self.numbers_ = [0, 1, 2, 3, 4, 5]
        self.names_ = ['Oğuz', 'Ahmet', 'Necati', 'Ali', 'Mehmet', 'Ziya']

        for i, j in zip(self.numbers_, self.names_):
            print("Number: " + str(i) + ", Name: " + j)

        print("\n")

        # Instead of zip method, we can use enumerate method.
        for i, j in enumerate(self.names_):
            print("Number: " + str(self.numbers_[i]) + ", Name: " + j)



    def question2(self):
        """
        Take a number which will be used as age. If age is greater than 18, print "You can drive.".

        **Args**:
            None
        """
        age = int(input("Enter your age: "))

        if age >= 18:
            print("You can drive.")
        else:
            print("You can't drive.")



    def question3(self):
        np_array = np.array([1, 2, 3, 4, 5])
        print("Numpy array: " + str(np_array))

        # Multiply all elements of numpy array with 2.
        np_array = np_array * 2
        print("Numpy array after multiplication: " + str(np_array))
        
        print("--------------------------------------------\n") 

        data = {
            'Name': ['Ahmet', 'Ayşe', 'Fatma', 'Mehmet'],
            'Age': [25, 30, 22, 35],
            'City': ['Istanbul', 'Ankara', 'Izmir', 'Bursa']
        }

        df = pd.DataFrame(data)
        print("Dataframe: " + str(df))

        print("--------------------------------------------\n")

        # Print only ages which are greater than 30.
        print(str(df[df['Age'] > 30]))



    def question4(self):
        """
        Create a car object and print its information.
        """
        car = Car(brand="Mazda", model="RX8", year=2010)
        car.print_information()
    
        

    def question5(self):
        """
        Search numbers which are divisible 3, 5 and 3 and 5.

        **Args**:
            None
        """
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print("Number: " + str(i) + " is divisible by 3 and 5.")
            elif i % 3 == 0:
                print("Number: " + str(i) + " is divisible by 3.")
            elif i % 5 == 0:
                print("Number: " + str(i) + " is divisible by 5.")
        



if __name__ == "__main__":
    week3 = Week3()

    # Question 1
    week3.question1() 

    # Question 2
    week3.question2()

    # Question 3
    week3.question3()

    # Question 4
    week3.question4()

    # Question 5
    week3.question5()
