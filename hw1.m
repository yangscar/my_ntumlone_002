function hw_1

global count
data = textread('Data/hw1_15_train.dat');
idx = Shuffle(1:size(data,1));
data = data(idx,:);
count = 0;
i = 1;
w = zeros(5,1);
while i < size(data,1)
    w = correct_mistake(data, w, i);
    i = find_mistake(data, w);
end

%disp(count);
end

function i =  find_mistake(data, w)
    for i = 1:size(data,1)
        x= [1 data(i,1:4)]';
        tmp = sign(w'*x);
        if  tmp ~= data(i,5)
            return;
        end
    end
    
end

function w_new = correct_mistake(data, w, i)
global count
    count = count+1;
    w_new = w + 0.5*data(i,5)*([1 data(i,1:4)])';
end