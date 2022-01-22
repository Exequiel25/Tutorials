% Here is a sum up of the basics
disp('My first script!')
%Input ('message', 'tag')
a = input('Please, enter a number for a ', 's')
%We must convert it to a number because it is a string
disp("Note that we have a char: (using whos function)")
whos
a = str2num(a);
disp("Note that we now have a double: (using whos function)")
whos
b = input('Pleas enter a number for b ', 's')
b = str2num(b);

disp("We'll sum a and b")
%We should convert the result to string
%Note we need to display as a vector
disp(['The result is ', num2str(a+b)])