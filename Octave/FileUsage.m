%Open file
%Read or write into
%Close file

arr = [1 2;3 4]
data = 4
value = 10.5

%First we'll open to write (if the file doesn't exist, it'll be created)
%note the folder must be created before
my_file = fopen ('src/my_first_file.csv', 'w');
fprintf(my_file, '%i,%i\n', arr')
fclose(my_file)
fprintf('File saved\n')

my_file = fopen('src/my_second_file.txt', 'w');
fprintf(my_file, 'This is data %d and this is a value %2.1f', data, value)
fclose(my_file)
fprintf('File saved\n')

%Reading
my_file = fopen ('src/my_second_file.txt');
new_data = fscanf(my_file, '%s')
fclose(my_file)
disp(data)
disp(value)

new_arr = csvread('src/my_first_file.csv')
disp(arr)