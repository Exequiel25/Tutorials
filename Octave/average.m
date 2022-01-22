function[av] = average(array)
    sum = 0;
    for n=1:numel(array)
        sum = sum + array(n);
    endfor
    
    av = sum/numel(array);
    return
endfunction