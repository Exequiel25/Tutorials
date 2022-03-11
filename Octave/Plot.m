%Plot
%x values for x_axis
x = -5:.5:5;
%y values for each x_axis
y = x.^2;

%basic plot the graphic
%plot(x,y)

%Adding  parameters
title('My first plot')
xlabel('X label in plot')
ylabel('Y label in plot')
grid on;

#linestyles - -- : -.
#markers + o * . x s ^ v  < > p h
#colors k r g b y m c w
plot(x,y,':hb')

%if we want to modify the axis
%axis([-10,10,-5,10])

%to add a text
text(-2,20,'Greetings')