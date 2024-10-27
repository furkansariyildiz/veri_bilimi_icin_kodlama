#!/usr/bin/env python3



def number_condition(number: float):
    """
    Function to check number condition.

    **Args**:
        number (float): Number to check.

    **Returns**:
        str: Result of number condition.
    """
    if number > 0:
        return "Number is positive"
    elif number < 0:
        return "Number is negative"
    else:
        return "Number is zero"



def number_subtraction(number1: int, number2: int):
    """
    Number subtraction function.

    **Args**:
        number1 (int): First number.
        number2 (int): Second number.

    **Returns**:
        int: Subtraction of two numbers
    """
    return number1 - number2



def number_addition(number1: int, number2: int):
    """
    Number addition function.

    **Args**:
        number1 (int): First number.
        number2 (int): Second number.

    **Returns**:
        int: Addition of two numbers
    """
    return number1 + number2



def number_square(number: int):
    """
    Number square function.

    **Args**:
        number (int): Number to square.

    **Returns**:
        int: Square of number
    """
    return number ** 2



class Student:
    def __init__(self, identification_number: int, name: str, surname: str):
        """
        Constructor of Student class.

        **Args**:
            identification_number (int): Identification number of student.
            name (str): Name of student.
            surname (str): Surname of student.
        """
        self.identification_number = identification_number
        self.name = name
        self.surname = surname



class RegisterCourse:
    def __init__(self):
        """
        Constructor of RegisterCourse class.

        **Args**
            None
        """
        self.name = "Ahmet" # Public attribute, name of student
        self.surname = "Kaleli" # Public attribute, surname of student
        self.__exam1 = 74 # Private attribute, first exam grade
        self.__exam2 = 80 # Private attribute, second exam grade



class Week5:
    def __init__(self):
        pass

    

    def question1(self):
        """
        Get a number from user and check if it is positive, negative or zero.

        **Args**:
            None
        """
        # There is type casting to float because input function returns string.
        input_number = float(input("Enter a number: "))

        # Call number_condition function. This function gets a number and returns a string.
        result = number_condition(input_number)
        print(result)
        


    def question2(self):
        """
        class Animal():
            def __init__(self): 
                pass

            def sesVer(self): # sesVer isimli deger dondurmeyen fonksiyon
                print("ses cikar")

        class kedi(Animal): # Kedi sinifi, Animal sinifindan miras aliyor
            def __init__(self):
                pass

            def sesVer(self): # sesVer isimli deger dondurmeyen fonksiyon. Bu fonksiyonu override ediyoruz.
                print("miyav")

            a = Animal() # Animal sinifindan bir nesne olusturduk
            a.sesVer() # Animal sinifindaki sesVer fonksiyonunu cagirdik. Ekrana "ses cikar" yazisi yazilacak

            k = kedi() # kedi sinifindan bir nesne olusturduk
            k.sesVer() # kedi sinifindaki sesVer fonksiyonunu cagirdik. Ekrana "miyav" yazisi yazilacak
        """



    def question3(self):
        """
        Get two numbers from user and subtract them.

        **Args**:
            None
        """
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        result = number_subtraction(number1, number2)
        print(f"Result: {result}")



    def question4(self):
        """
        Create a class named Student with attributes: identification_number, name, surname.

        **Args**:
            None
        """
        student = Student(3445212014, "Ali", "Sari")
        print(f"Student: {student.identification_number} {student.name} {student.surname}")



    def question5(self):
        """
        Create a class named RegisterCourse with attributes: name, surname, __exam1, __exam2.

        **Args**:
            None
        """
        register = RegisterCourse() # Create an object of RegisterCourse class
        print("İsim: ", register.name) # Access to public attribute
        print("Soyisim: ", register.surname) # Access to public attribute
        print("Exam 1: ", register.__exam1) # Access to private attribute with error. 
        print("Exam 2: ", register.__exam2) # Access to private attribute with error.



    def question6(self):
        """
        Print the result of the following equation: a + b + c where a = 2, b = 5, c = b ** a.
        """
        a = 2
        b = 5
        c = b ** a
        d = a + b + c
        print(d)



    def question7(self):
        """
        With def keyword, we can create a function.
        """



    def question8(self):
        """
        To convert an input to integer, we can use int() function. 
        """ 
        a = int(input("Enter your exam grade: "))

        print(f"{a * 5}")
        print(f"{a + 5}")



    def question9(self):
        """
        while, continue, if, elif, else and break keywords are used in decision making.
        def keyword is used to define a function.
        So answer is def keyword.
        """
    


    def question10(self):
        """
        Split function is used to split a string into a list.

        **Args**:
            None
        """
        sentence = "Doğuş Üniversitesi Bilgisayar Programcılığı"
        print(sentence.split())



    def question11(self):
        """
        Adding two numbers and square result via functions.

        **Args**:
            None
        """
        number1 = 1
        number2 = 2
        result = number_square(number_addition(number1, number2))
        print(f"Result: {result}")



    def question12(self):
        """
        Difference between list and tuple.

        **Args**:
            None
        """
        # List example
        print("\nList example")
        # List is mutable.
        self.list_ = [0, 1, 2]
        self.list_.append(3)
        self.list_.remove(1)
        
        # List can be indexed.
        self.list_[0] = 5
        print(self.list_[0])
        
        # List can be iterated and data proccessed.
        for i in self.list_:
            print(i)

        print(f"Total: {sum(self.list_)}" )

        # Dynamic arrays
        self.list_ = []
        for i in range(5):
            self.list_.append(i)

        # Stroring different data types
        self.list_ = [1, "Hello", 3.4]
        print(self.list_)

        #Processing data
        sentence = "Hello world from Python"
        self.list_ = sentence.split()
        for word in self.list_:
            print(word)

        print("----------------------------------")

        # Tuple example
        print("\nTuple example")
        # Tuple is immutable. 
        self.tuple_ = (10, 20)
        # self.tuple_[0] = 30 # Error
        print(self.tuple_)



    def question13(self):
        """
        While loop example.

        **Args**:
            None
        """
        # This loop gives error because int type does not have len() function.
        while True:
            s = int(input("Enter a number: "))
            if s == 0:
                break
            if len(s) < 3:
                continue
            else:
                print("Number is greater than 100")



if __name__ == "__main__":
    week5 = Week5()
    
    # Question 1
    week5.question1()

    # Question 2
    week5.question2()

    # Question 3
    week5.question3()

    # Question 4
    week5.question4()

    # Question 5
    week5.question5()

    # Question 6
    week5.question6()

    # Question 7
    week5.question7()

    # Question 8
    week5.question8()

    # Question 9
    week5.question9()

    # Question 10
    week5.question10()

    # Question 11
    week5.question11()

    # Question 12
    week5.question12()

    # Question 13
    week5.question13()