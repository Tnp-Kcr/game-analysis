from faker import Faker
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

faker = Faker()
data = {
    'Player_ID': [faker.uuid4() for _ in range(100)],
    'Player_Name': [faker.user_name() for _ in range(100)],
    'Age': [faker.random_int(min=10, max=40) for _ in range(100)],
    'Country': [faker.country() for _ in range(100)],
    'Play_Time': [random.randint(10, 500) for _ in range(100)],
    'Game_Score': [random.randint(0, 10000) for _ in range(100)],
    'Items_Bought': [random.randint(0, 20) for _ in range(100)],
    'In_Game_Spend': [round(random.uniform(0, 100), 2) for _ in range(100)]
}


df = pd.DataFrame(data)


plt.figure(figsize=(8, 6))
sns.scatterplot(x='Play_Time', y='Game_Score', data=df)
plt.title('Play Time vs Game Score')
plt.xlabel('Play Time (Minutes)')
plt.ylabel('Game Score')
plt.show()


plt.figure(figsize=(10, 6))
df['Country'].value_counts().plot(kind='bar')
plt.title('Number of Players by Country')
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.show()
