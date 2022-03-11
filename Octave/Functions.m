%We'll use the function that we've created
a = input('Please, enter a number ', 's')
a = str2num(a);

b= input('Please, enter a number ', 's')
b = str2num(b);

r=multiply(a,b);
fprintf('Result is %f\n', r)

%We can also manage multiple outputs
[s r m d] = operators(a,b);
fprintf('sum %f\trerst %f\tmult %f\tdiv %f\t\n', s,r,m,d)

%Arrays
arr = [1 5 8 6 7 2];
p = average(arr);
fprintf('Average of array is %f\n', p)

%Anonimous function

%we don't need to write a new script
%it's just a one line function
sum=@(a,b) a+b;

n=5;
m=2;
r=sum(n,m)
s=sum(25,2)