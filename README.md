# GeneratingRandomness

The program is written in Python 3.8 version.
The program is divided into 4 stages: 
  Prepocessing of the data: The training data is collected
  Grouping of the data: An dictionary of useful data is created
  Testing of the data: A test data string was given to check its working
  Conversion to a game: All the above data was done and later converted to a game
 
The game consists of the user having $1000 initially,
  1. The user is initial asked to input training data for the model to preprocess. Here a minimum of 100 bits are required.
  2. Then the user gives an input of some random collection of 0s and 1s. 
  3. For the every bit the model predicts correctly the the user loses $1.
  4. For every bit the model is wrong the user gains $1.
  5. The data collected ie the testing value given by the user is added to the training data and the model updates the dictionary.
  6. The game continues until the user gives the input "enough".
  7. After this Game over! is dispayed and the program comes to an end.
