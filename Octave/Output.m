% Print function (from C language)
a=2
name= 'Exequiel'
f=3.14
%remember to print an endline \n
fprintf('\n\t---- integer ---- \n') %Printing manual writing text
fprintf('Introducing "a" as the value %i assigned before\n', a) %Printing an integer
fprintf('\nAlso doubles like "f" with full precision %f or just for example precision 1: %.1f\n', f, f)  %Printing a float
fprintf('\nName:%s\t note is spelled with %c, not spelled with z\n', name, name(2))%Printing a string and a char

%Printing an array
%Note we print each element, not the array
%similar to iterating print until end of array is reach
arr = [1 2 3]
fprintf('The array is\n')
fprintf('%i',arr)
fprintf('\n')
fprintf('In array %i \n', arr)
fprintf('---\n')
fprintf('In array %i \t', arr)
fprintf('---\n')
fprintf('In array %i , %i \n', arr) 
fprintf('---\n')

%Printing matrix
matrix = [1 2;3 4]
fprintf('The matrix is not:\n')
fprintf('%i %i \n', matrix)
%Remeber matrixes are read vertically
%we should print transposed
fprintf('The matrix is:\n')
fprintf('%i %i \n', matrix')
fprintf('\n')

%If matrix has three columns:
matrix = [1 2 3; 4 5 6]
fprintf('%i %i %i \n', matrix')