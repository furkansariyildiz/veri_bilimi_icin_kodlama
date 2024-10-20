#!/usr/bin/env python3

import json
import numpy as np
import pandas as pd


class Week4:
    """
    Week 4 class which has questions of week 4.
    """
    def __init__(self):
        """
        Constructor of Week4 class.
        """
        pass


    
    def question1(self):
        """
        Function to get differences between list, tuple and dictionary.

        **Source**:
            https://www.geeksforgeeks.org/differences-and-applications-of-list-tuple-set-and-dictionary-in-python/

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

        # Dictionary keys via tuple. Tuplles are immutable, so they can be used as keys in dictionaries.
        self.locations_ = {
            ("40.7128", "74.0060"): "New York",
            ("34.0522", "118.2437"): "Los Angeles"
        }
        print(self.locations_)

        # Tuples can hold elements of different data types. (Heterogeneous)
        self.person_ = ("Furkan Sariyildiz", 28, "Turkey", "furkan@example.com")
        print(self.person_)

        print("----------------------------------")

        # Dictionary example
        print("\nDictionary example")

        # Database Record Example
        self.record_ = {
            "name": "Furkan Sariyildiz",
            "age": 28,
            "country": "Turkey",
            "email": "furkan@example.com"
        }
        print(self.record_)

        # Counting frequency of elements in list
        self.list_ = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
        print(self.list_)
        self.frequency_ = {}
        for item in self.list_:
            self.frequency_[item] = self.frequency_.get(item, 0) + 1
        print(self.frequency_)

        # Fast lookups
        self.lookup_ = {
            "TL": "Turkish Lira",
            "USD": "United States Dollar",
            "EUR": "Euro",
            "JPY": "Japanese Yen"
        }
        print(self.lookup_["USD"])

        # Storing and accessing JSON data
        self.json_data_ = '{"name": "Furkan", "age": 28, "city": "Istanbul"}'
        self.data_ = json.loads(self.json_data_)
        print(self.data_["name"]) 

        # Grouping data by keys
        self.data_  = [
            {"name": "Furkan", "age": 28, "city": "Istanbul"},
            {"name": "Ahmet", "age": 30, "city": "Ankara"},
            {"name": "Mehmet", "age": 25, "city": "Izmir"},
            {"name": "Ayse", "age": 22, "city": "Istanbul"},
            {"name": "Fatma", "age": 35, "city": "Ankara"}
        ]

        self.grouped_data_ = {}
        for item in self.data_:
            city = item["city"]
            if city not in self.grouped_data_:
                self.grouped_data_[city] = []
            self.grouped_data_[city].append(item["name"])
        
        print(self.grouped_data_)

        print("----------------------------------")


    
    def question2(self):
        """
        Function to show examples of numpy array and pandas dataframe.

        **Args**:
            None
        """
        # Numpy array example
        print("\nNumpy array example")
        self.numpy_array_ = np.random.randint(0, 100, size=10)

        print("Numpy array: " + str(self.numpy_array_))
        print("Maximum value: " + str(np.max(self.numpy_array_)))
        print("Minimum value: " + str(np.min(self.numpy_array_)))
        print("Mean value: " + str(np.mean(self.numpy_array_)))
        print("Median value: " + str(np.median(self.numpy_array_)))
        
        self.muxed_array_ = self.numpy_array_ * 2
        print("Numpy array after multiplication: " + str(self.muxed_array_))

        print("--------------------------------------------\n")

        self.numpy_array_2d_ = np.random.randint(0, 100, size=(3, 3))
        print("2D Numpy array: " + str(self.numpy_array_2d_))
        print("Transpose of 2D Numpy array: " + str(self.numpy_array_2d_.T))

        self.muxed_array_2d_ = self.numpy_array_2d_ * 10
        print("2D Numpy array after multiplication: " + str(self.muxed_array_2d_))

        self.sum_rows_ = np.sum(self.numpy_array_2d_, axis=1)
        print("Sum of rows: " + str(self.sum_rows_))

        self.sum_columns_ = np.sum(self.numpy_array_2d_, axis=0)
        print("Sum of columns: " + str(self.sum_columns_))

        print("--------------------------------------------\n")

        # Pandas dataframe example
        print("\nPandas dataframe example")

        self.data_ = {
            'İsim': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Zeynep'],
            'Yaş': [30, 22, 28, 26, 35],
            'Maaş': [5000, 3500, 4800, 3900, 5200] 
        }

        self.df_ = pd.DataFrame(self.data_) 
        print("Dataframe: " + str(self.df_))

        age_filter_ = self.df_[self.df_['Yaş'] > 25]
        print("Dataframe after filtering: " + str(age_filter_))

        salary_filter_ = self.df_[self.df_['Maaş'] > 4000][['İsim', 'Maaş']]
        print("Dataframe after filtering: " + str(salary_filter_))

        cities_ = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Adana']
        self.df_['Şehir'] = cities_

        print("Dataframe after adding new column\n " + str(self.df_))




if __name__ == "__main__":
    week4 = Week4()

    # Question 1
    week4.question1()

    # Question 2
    week4.question2()