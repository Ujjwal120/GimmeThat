from faker import Faker
import pandas as pd
import numpy as np
import csv

N= 100
fake= Faker()

categories = ["Beard", "Skin Care", "Fashion"]
prev_users= []


class Person:
  def __init__(self, id, gender, age, country):
    self.id = id
    self.gender = gender
    self.age = age
    self.country = country


def get_user():
	if len(prev_users)>0 and np.random.randint(1,11) <= 3:	## 30% probability
		return prev_users[ fake.random_int(0, len(prev_users)-1 ) ]
	else:
		gen= "MF"
		user = Person( fake.random_int(1,N), gen[fake.random_int(0,1)] , fake.random_int(15,80) , fake.country() )
		prev_users.append(user)
		return user

def create_data():
	data = {}

	for i in range(N):

		user= get_user()

		data[i]={}
		data[i]['user_id']= user.id
		data[i]['gender']= user.gender
		data[i]['age']= user.age
		data[i]['country']= user.country
		data[i]['product_id']= fake.random_int(1,N)
		data[i]['prod_category']= categories[ fake.random_int(0,len(categories)-1 ) ]
		data[i]['rating']= fake.random_int(1,6)

	return data


def create_csv_file(dataset):
    with open('./product_dataset.csv', 'w', newline='') as csvfile:

        fieldnames = ['user_id', 'gender', 'age', 'country', 'product_id',
                      'prod_category', 'rating']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1,N):
            writer.writerow( dataset[i] )


if __name__ == '__main__':

	dataset = create_data()
	create_csv_file(dataset)

	## print( dataset )