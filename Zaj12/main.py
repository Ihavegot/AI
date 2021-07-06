import numpy as np
import pandas as pd

np.random.seed(7)
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, LSTM
from tensorflow.keras.layers import Embedding
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing import sequence
import gensim
from sklearn import metrics


# from pickle import dump


def wynik(y_test, predictions):
    print(metrics.classification_report(y_test, predictions))
    print(metrics.accuracy_score(y_test, predictions))
    print(metrics.confusion_matrix(y_test, predictions))


df = pd.read_csv('train-amazon.tsv', sep='\t')
X = df['review']
z = df['label']
y = []
for i in z:
    if i == 'neg':
        k = 0
    else:
        k = 1
    y.append(k)

y = to_categorical(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('enwiki_20180420_100d.txt', binary=False)

embedding_matrix = word2vec_model.wv.syn0

top_words = embedding_matrix.shape[0]
mxlen = 20

tokenizer = Tokenizer(num_words=top_words)
tokenizer.fit_on_texts(X_train)
sequences_train = tokenizer.texts_to_sequences(X_train)
sequences_test = tokenizer.texts_to_sequences(X_test)
sequences_val = tokenizer.texts_to_sequences(X_val)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

X_train = sequence.pad_sequences(sequences_train, maxlen=mxlen)
X_test = sequence.pad_sequences(sequences_test, maxlen=mxlen)
X_val = sequence.pad_sequences(sequences_val, maxlen=mxlen)

batch_size = 32
nb_epoch = 100

embedding_layer = Embedding(embedding_matrix.shape[0],
                            embedding_matrix.shape[1],
                            weights=[embedding_matrix],
                            trainable=False)

model = Sequential()
model.add(embedding_layer)

model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dropout(0.2))
model.add(Dense(20, input_dim=129, activation='relu', use_bias=True))
model.add(Dense(2, use_bias=True))
model.add(Activation('softmax'))
model.summary()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
rnn = model.fit(X_train, y_train, epochs=nb_epoch, batch_size=batch_size, shuffle=True, validation_data=(X_val, y_val))

# model.save('model-eng-embed-nn.h5')
# dump(tokenizer, open('tokeny-embedd-en', 'wb'))

# testy
print('testowe')
predykcje = model.predict(X_test)

predictions = predykcje.round()

igrek = len(predictions) * [0]
zet = len(y_test) * [0]
print(metrics.classification_report(y_test, predictions))
print(metrics.accuracy_score(y_test, predictions))
for i in range(len(y_test)):

    a = (predykcje[i][1] - predykcje[i][0])

    if (a > 0):
        igrek[i] = 1
    if (y_test[i][1] == 1):
        zet[i] = 1

print(metrics.confusion_matrix(zet, igrek))
