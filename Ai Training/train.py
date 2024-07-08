# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:32:30 2021

@author: Furkan

pip install pandas
pip install numpy
pip install matplotlip
pip install keras
pip install tensorflow

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, Dropout, LSTM, Dense, Bidirectional 
from keras.preprocessing.text import Tokenizer
from keras.callbacks import EarlyStopping,ModelCheckpoint
from keras.models import Sequential


#reads csv file
df = pd.read_csv('lyrics-data.csv')

#drops unuseful columns
df.drop(['ALink','SName','SLink'],axis=1,inplace=True)
print(df.shape)

#filters dataframe 
df = df[df['Idiom']=='ENGLISH']

#choosing random 1400 samples in data
#that code will same result with same random_state number
df=df.sample(n = 1000, random_state=20)

#counts number of words in each lyric and adds as a column
df['Number_of_words'] = df['Lyric'].apply(lambda x:len(str(x).split()))
print(df.head())
#shows dataframe's statistical info
print(df.describe())
print("--------------------------")
#drops lyrics that longer than 500 words
indexNames = df[(df['Number_of_words'] > 500)].index 
df.drop(indexNames , inplace=True)
df.drop(["Idiom"], axis=1,inplace=True)
print(df.describe())
#Tokenization
#That part converting words to numbers
#So computer can make sense between words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(df['Lyric'].astype(str).str.lower())

total_words = len(tokenizer.word_index)+1
tokenized_sentences = tokenizer.texts_to_sequences(df['Lyric'].astype(str))

#Slash sequences into n gram sequence
input_sequences = list()
for i in tokenized_sentences:
    for t in range(1, len(i)):
        n_gram_sequence = i[:t+1]
        input_sequences.append(n_gram_sequence)
        
#Pre-padding
#Filling sequences for make them all same length
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

#Create predictors and label
X, labels = input_sequences[:,:-1],input_sequences[:,-1]
#One hot encoding
y = tf.keras.utils.to_categorical(labels, num_classes=total_words)


#Configure the checkpoint and callbacks
#That checkpoint saves the best model with model statistic
checkpoint_name = 'Weights-LSTM-improvement-epoch{epoch:02d}--acc{accuracy:.3f}--loss{loss:.4f}-bigger.hdf5'
checkpoint = ModelCheckpoint(checkpoint_name, monitor='loss', verbose = 1, save_best_only = True, mode ='min')
callbacks_list = [checkpoint]
earlystop = EarlyStopping(monitor='loss', min_delta=0, patience=5, verbose=0, mode='auto')



# create model
model = Sequential()
model.add(Embedding(total_words, 48, input_length=max_sequence_len-1))
model.add(Bidirectional(LSTM(256)))
model.add(Dropout(0.1))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history=model.fit(X, y, epochs=25, batch_size=32, verbose=1, callbacks=[checkpoint,earlystop])

# plot the accuracy
plt.plot(history.history['accuracy'], label='train acc')
plt.legend()
plt.show()
plt.savefig('AccVal_acc')