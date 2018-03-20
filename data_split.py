import pandas as pd
import numpy as np 
import numpy as np
from sklearn.model_selection import train_test_split

data_path = 'shuffled-full-set-hashed.csv'

raw_data = pd.read_csv(data_path, engine='python', header=None)
numpy_array = raw_data.as_matrix()
y = numpy_array[:,0]
X = numpy_array[:,1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

y_test_reshape = np.reshape(y_test ,(-1,1))
y_train_reshape = np.reshape(y_train ,(-1,1))

train = np.concatenate((y_train_reshape,X_train), axis = 1)
test = np.concatenate((y_test_reshape,X_test), axis = 1)



df = pd.DataFrame(data = train)
df.to_csv("training_data.csv", header=None, index = False)

df = pd.DataFrame(data = test)
df.to_csv("test_data.csv", header=None, index = False)
