from random import random
from factory import Factory
import pandas as pd
import factory


class WorkerFactory(Factory):

    class Meta:
        model = dict

    first_name = factory.Faker("first_name")
    last_name = factory.Faker('last_name')
    age = factory.Faker('random_int', min=20, max=50)
    rank = factory.Faker('random_element', elements=('seaman', 'motorman', 'Deck Officer', 'Engine Officer', 'Cook'))
    salary = factory.Faker('random_int', min=2000, max=8000)
    experience = factory.Faker('random_int', min=0, max=100)


num_rows = 100

workers = WorkerFactory.create_batch(num_rows)

for worker in workers:
    if random() < 0.1:
        worker['first_name'] = None
    if random() < 0.1:
        worker['salary'] = -1 * worker['salary']
    if random() < 0.1:
        worker['experience'] = None

df = pd.DataFrame(workers)

df.to_csv('workers_records.csv')

print(df)