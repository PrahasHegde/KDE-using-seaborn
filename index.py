import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#simple example
sample = np.array([3, 4, 5, 1, 2, 3, 4, 5, 6, 3, 3, 3, 5, 6, 7, 1, 1, 1, 3, 3, 3, 5])
sns.histplot(sample)
plt.show()

#example KDE plot
sample = np.array([3, 4, 5, 1, 2, 3, 4, 5, 6, 3, 3, 3, 5, 6, 7, 1, 1, 1, 3, 3, 3, 5])
sns.kdeplot(sample, bw=0.1)
plt.show()

#Loading dataset -> mileage per gallon
car = sns.load_dataset('mpg')
print(car.head())
print(car.info())


#in cylinder column
print(car.cylinders.nunique())
print(car.cylinders.unique())
sns.histplot(car.cylinders)
plt.show()
#KDE plot
sns.kdeplot(car.cylinders, fill=True)
plt.title('KDE of Car Cylinders')
plt.show()


#Dealing with null values
print(car.isnull().sum())

#in horsepower column
sns.kdeplot(car.horsepower)
plt.show()


#graph tells us the density of data present in both columns mpg and horsepower
sns.kdeplot(data=car, x=car.mpg, y=car.horsepower)
plt.show()


#The density of cars with more mpg and horsepower based on cylinders (hue = ))
sns.kdeplot(data=car, x=car.mpg, y=car.horsepower, hue=car.cylinders)
plt.show()


"""If we set the shade and the cbar parameters to true we will have some good colors indicating our density in 2D, 
the dark color places mean high density, and the light color places indicate low density"""

plt.figure(figsize=(20, 15))
sns.kdeplot(data=car, x=car.mpg, y=car.horsepower, hue=car.cylinders, fill=True, cbar=True)
plt.show()