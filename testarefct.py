import pandas as pd 
# define a list of column names (as strings)
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# define the URL from which to retrieve the data (as a string)
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# retrieve the CSV file and add the column names
iris = pd.read_csv(url, header=None, names=col_names)
iris['species_num'] = iris.species.map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
def classify_iris(row):

    # calculate the petal_area
    petal_area = row[2] * row[3]
    
    # predict the species based on the rules above    
    if petal_area < 2:
        prediction = 'setosa'
    elif petal_area < 7.4:
        prediction = 'versicolor'
    else:
        prediction = 'virginica'
    
    # map the species name to a numeric value
    species_to_num = {'setosa':0, 'versicolor':1, 'virginica':2}
    
    # return that value
    return species_to_num[prediction]
iris['prediction'] = [classify_iris(row) for index, row in iris.iterrows()]


# calculate the percentage of correct predictions
print(sum(iris.species_num == iris.prediction) / 150)

