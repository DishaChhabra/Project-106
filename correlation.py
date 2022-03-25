import pandas

data=pandas.read_csv('https://raw.githubusercontent.com/whitehatjr/finding-correlation/master/cups%20of%20coffee%20vs%20hours%20of%20sleep.csv')
print(data.corr())

data2 = pandas.read_csv('https://raw.githubusercontent.com/whitehatjr/finding-correlation/master/Student%20Marks%20vs%20Days%20Present.csv')
print(data2.corr())