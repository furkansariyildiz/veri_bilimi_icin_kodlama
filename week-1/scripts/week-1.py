#!/usr/bin/env python3


class Week1:
    def __init__(self):
        pass

    def questionOne(self, name: str = "furkan"):
        """
        @brief Check alphabets of name is upper or lower via for loop.
        @param name (str) Name which will be controlled.
        @returns void
        """
        for alphabet in name:
            if alphabet.isupper():
                print("{} is upper.".format(alphabet))
            else:
                print("{} is lower.".format(alphabet))



    def questionTwo(self, age: int = 18):
        """
        @brief Function that checks whether you are old enough to get a driver's license.
        @param age (int) Age that be controlled for driver license.
        @returns bool
        """
        if age >= 18:
            return True
        
        return False



    def questionFour(self, string: str = "İstanbul Medeniyet Üniversitesi BVB E.A.B.D."):
        """
        @brief Split and print string variable.
        @param string (str) String variable for split and print process.
        @returns void
        """
        print(string.split())

    

if __name__ == '__main__':
    week1 = Week1()

    # Question-1
    name = input("Enter your name: ")
    week1.questionOne(name=name)

    # Question-2
    age = input("Enter your age: ")
    print(week1.questionTwo(age=int(age)))

    # Question-3
    # 3-Python ile uygulama yapılabilecek alanlardan biri değildir 
    #    A.İstatistik (scipy)
    #    B. hepsi yanlış 
    #    C. web kazıma ve bot programı yazma (scrapy,spyder...)
    #    D. Veri analizi (numpy,pandas,sci-kit learn
    #    E. Görüntü işleme (opencv kütüphanesi)
    # Answer(B)

    # Question-4
    week1.questionFour()
    # ['İstanbul', 'Medeniyet', 'Üniversitesi', 'BVB', 'E.A.B.D.']