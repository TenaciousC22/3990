from __future__ import absolute_import, division, print_function

import pathlib
import pandas as pd
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt


#dataset_path = keras.utils.get_file("auto-mpg.data","https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
#print(dataset_path)

column_names=['JanTem1','JanPre1','FebTem1','FebPre1','MarTem1','MarPre1','AprTem1','AprPre1','MayTem1','MayPre1','JunTem1','JunPre1','JulTem1','JulPre1','AugTem1','AugPre1','SepTem1','SepPre1','OctTem1','OctPre1','NovTem1','NovPre1','DecTem1','DecPre1',
	'JanTem2','JanPre2','FebTem2','FebPre2','MarTem2','MarPre2','AprTem2','AprPre2','MayTem2','MayPre2','JunTem2','JunPre2','JulTem2','JulPre2','AugTem2','AugPre2','SepTem2','SepPre2','OctTem2','OctPre2','NovTem2','NovPre2','DecTem2','DecPre2',
	'JanTem3','JanPre3','FebTem3','FebPre3','MarTem3','MarPre3','AprTem3','AprPre3','MayTem3','MayPre3','JunTem3','JunPre3','JulTem3','JulPre3','AugTem3','AugPre3','SepTem3','SepPre3','OctTem3','OctPre3','NovTem3','NovPre3','DecTem3','DecPre3',
	'JanTem4','JanPre4','FebTem4','FebPre4','MarTem4','MarPre4','AprTem4','AprPre4','MayTem4','MayPre4','JunTem4','JunPre4','JulTem4','JulPre4','AugTem4','AugPre4','SepTem4','SepPre4','OctTem4','OctPre4','NovTem4','NovPre4','DecTem4','DecPre4',
	'JanTem5','JanPre5','FebTem5','FebPre5','MarTem5','MarPre5','AprTem5','AprPre5','MayTem5','MayPre5','JunTem5','JunPre5','JulTem5','JulPre5','AugTem5','AugPre5','SepTem5','SepPre5','OctTem5','OctPre5','NovTem5','NovPre5','DecTem5','DecPre5',
	'JanTemOut','JanPreOut','FebTemOut','FebPreOut','MarTemOut','MarPreOut','AprTemOut','AprPreOut','MayTemOut','MayPreOut','JunTemOut','JunPreOut','JulTemOut','JulPreOut','AugTemOut','AugPreOut','SepTemOut','SepPreOut','OctTemOut','OctPreOut','NovTemOut','NovPreOut','DecTemOut','DecPreOut',
	]
raw_dataset=pd.read_csv('..\data\Canada5.csv',names=column_names,na_values="?",comment='\t',sep=",",skipinitialspace=True)
dataset=raw_dataset.copy()
dataset.pop('JanTemOut')
dataset.pop('FebTemOut')
dataset.pop('FebPreOut')
dataset.pop('MarTemOut')
dataset.pop('MarPreOut')
dataset.pop('AprTemOut')
dataset.pop('AprPreOut')
dataset.pop('MayTemOut')
dataset.pop('MayPreOut')
dataset.pop('JunTemOut')
dataset.pop('JunPreOut')
dataset.pop('JulTemOut')
dataset.pop('JulPreOut')
dataset.pop('AugTemOut')
dataset.pop('AugPreOut')
dataset.pop('SepTemOut')
dataset.pop('SepPreOut')
dataset.pop('OctTemOut')
dataset.pop('OctPreOut')
dataset.pop('NovTemOut')
dataset.pop('NovPreOut')
dataset.pop('DecTemOut')
dataset.pop('DecPreOut')
#print(dataset.tail())
#print(dataset.isna().sum())
#dataset=dataset.dropna()

#print(dataset.tail())

train_dataset=dataset.sample(frac=0.8,random_state=0)
test_dataset=dataset.drop(train_dataset.index)

#print(train_dataset.tail())
#print(test_dataset.tail())

#sns.pairplot(train_dataset[['JanTem1','JanPre1','FebTem1','FebPre1',]],diag_kind="kde")
#plt.show()

train_stats=train_dataset.describe()
train_stats.pop('JanPreOut')
train_stats=train_stats.transpose()
#print(train_stats)

train_labels=train_dataset.pop('JanPreOut')
test_labels=test_dataset.pop('JanPreOut')

def norm(x):
	return(x-train_stats['mean'])/train_stats['std']

normed_train_data=norm(train_dataset)
normed_test_data=norm(test_dataset)

def build_model():
	model=keras.Sequential([
		layers.Dense(120,activation=tf.nn.relu,input_shape=[len(train_dataset.keys())]),
		layers.Dense(60,activation=tf.nn.relu),
		layers.Dense(30,activation=tf.nn.relu),
		layers.Dense(1)
		])

	optimizer=tf.keras.optimizers.RMSprop(0.001)
	model.compile(loss='mse',optimizer=optimizer,metrics=['mae','mse'])
	return model

model=build_model()
#model.summary()

example_batch=normed_train_data[:10]
example_result=model.predict(example_batch)
#print(example_result)

class PrintDot(keras.callbacks.Callback):
	def on_epoch_end(self,epoch,logs):
		if epoch % 100 == 0: print('.',end='')

EPOCHS=1000

history=model.fit(normed_train_data,train_labels,epochs=EPOCHS,validation_split=0.2,verbose=0,callbacks=[PrintDot()])
hist=pd.DataFrame(history.history)
hist['epoch']=history.epoch
#print(hist.tail())



def plot_history(history):
	hist = pd.DataFrame(history.history)
	hist['epoch'] = history.epoch
	plt.figure()
	plt.xlabel('Epoch')
	plt.ylabel('Mean Abs Error January Tempurature')
	plt.plot(hist['epoch'], hist['mean_absolute_error'],label='Train Error')
	plt.plot(hist['epoch'], hist['val_mean_absolute_error'],label = 'Val Error')
	plt.legend()
	plt.ylim([0,5])
	plt.figure()
	plt.xlabel('Epoch')
	plt.ylabel('Mean Square Error January Tempurature')
	plt.plot(hist['epoch'], hist['mean_squared_error'],label='Train Error')
	plt.plot(hist['epoch'], hist['val_mean_squared_error'],label = 'Val Error')
	plt.legend()
	plt.ylim([0,20])

plot_history(history)
#plt.show()

#model=build_model()

#early_stop=keras.callbacks.EarlyStopping(monitor='val_loss',patience=20)
#history=model.fit(normed_train_data,train_labels,epochs=EPOCHS,validation_split=0.2,verbose=0,callbacks=[early_stop,PrintDot()])

#plot_history(history)

#plt.show()
#print('\n')

loss,mae,mse=model.evaluate(normed_test_data,test_labels,verbose=0)

print(' ',end='')
print("Testing set Mean Abs Error for Canada, 5 inputs: {:5.2f} mm" .format(mae))

test_predictions=model.predict(normed_test_data).flatten()

#plt.scatter(test_labels, test_predictions)
#plt.xlabel('True Values MPG')
#plt.ylabel('Predictions MPG')
#plt.axis('equal')
#plt.axis('square')
#plt.xlim([0,plt.xlim()[1]])
#plt.ylim([0,plt.ylim()[1]])
#_=plt.plot([-100,100],[-100,100])
#plt.show()

error = test_predictions - test_labels
plt.hist(error, bins = 25)
plt.xlabel("Prediction Error Temp")
_ = plt.ylabel("Count")
#plt.show()