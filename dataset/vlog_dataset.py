from faker import Faker
import pandas as pd
import numpy as np
import csv

N = 100000
fake= Faker()

categories = ["Travel", "Skin Care", "Fashion", "Health", "Movies", "Food"]
prev_users= []


class Person:
  def __init__(self, id, gender, age, country):
    self.id = id
    self.gender = gender
    self.age = age
    self.country = country


def get_user():
	if len(prev_users)>0 and np.random.randint(1,11) <= 5:	## 50% probability
		return prev_users[ fake.random_int(0, len(prev_users)-1 ) ]
	else:
		gender= "MF"
		user = Person( fake.random_int(1,N), gender[fake.random_int(0,1)], 
						fake.random_int(15,80) , fake.country() )
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
		data[i]['vlog_id']= fake.random_int(1,N)
		data[i]['tag']= categories[ fake.random_int(0,len(categories)-1 ) ]
		data[i]['time_spent']= fake.random_int(0,30)
		data[i]['like']= fake.random_int(0, 1)
		data[i]['comment']= fake.random_int(0, 1)
		data[i]['save']= fake.random_int(0, 1)


	return data


def create_csv_file(dataset):
    with open('./vlog_dataset.csv', 'w', newline='') as csvfile:

        fieldnames = ['user_id', 'gender', 'age', 'country', 'vlog_id',
                      'tag', 'time_spent', 'like', 'comment', 'save']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1,N):
            writer.writerow( dataset[i] )


if __name__ == '__main__':

	dataset = create_data()
	create_csv_file(dataset)

	## print( dataset )