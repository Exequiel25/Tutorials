%if (condition)
%     statement
%else
%     statement
%endif

a = input('Please, enter a number ', 's')
a = str2num(a);

if(a > 10)
    disp('Your number is greater than 10')
else
    disp('Your number is lower than 10')
endif

%if (condition)
%     statement
%elseif (condition2)
%     statement2
%else
%     statement3
%endif

%if (condition)
%     if...else statement
%     endif
%else
%     statement
%endif

%Switch
var = 'div'
b=2

switch var
    case {'sum'}
        r=a+b;
    case {'subs'}
        r=a-b;
    case {'mult'}
        r=a*b;
    case {'div'}
        r=a/b;
    otherwise
        disp('Out of switch options :(')
endswitch

disp(['The result is ', num2str(r)])