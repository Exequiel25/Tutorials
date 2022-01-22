%Create 2 vectors
x = 1:5
y=6:10

%We create a new vector
vector = [x y]

%We create a new matrix
%Note that x and y must be same size
matrix = [x;y]

%Not only numbers, but strings
name= ['Marta']
surname=['Lopez']

sentence = [name,' ',surname, ' must go to work']

%To create a matrix
sentences = char(name,surname,'must','go')