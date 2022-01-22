function [sum, rest, mult, div] = operators (x, y)
    sum = x+y;
    rest = x-y;
    mult = multiply(x,y);
    div = x/y;
    return
endfunction