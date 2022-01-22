%Vector
disp('My first vector:')

v=[1 2 3 4]
%get an element
%note first index is 1 and not 0
disp(['Here we got second element',num2str(v(2))])
disp(v(2:4))

%Matrix
disp('My first matrix')

A=[1 2; 3 4]

%sum each element
A.+2

%sum A+B
B=[2 1;4 3]

C=A+B

%ones function
O=ones(2,3)
%zeros function
Z=zeros(3,4)
%rand function (random numers)
R=rand(3,2)
%randn function (random normalized numers)
Rn=randn(5,1)
%randp function (random numbers with an avarage parameter)
Rp=randp(1,3,4)

%Identity matrix
I=eye(2)

%Iteration
disp('Using iteration')

i=0:.5:10

%or with default step (1)

it=0:10