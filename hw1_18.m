function correctRate  = hw1_18()
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here

data = textread('Data/hw1_18_train.dat');
idx = Shuffle(1:size(data,1));
data = data(idx,:);
best_mistakes =size(data,1)+1;
w = zeros(5,1);
w_hat = w;
count  = 0;
for count=1:100
    i = find_mistake(data, w);
    %old_mistakes
    if length(i) < best_mistakes
        best_mistakes = length(i);
        w_hat = w;
    end
    toCorrect = RandSample(i,[1,1]);
    w = correct_mistake(data, w, toCorrect);
end

data_test = textread('Data/hw1_18_test.dat');

mis= find_mistake(data_test, w_hat);
correctRate = length(mis)/size(data_test,1);
end

function i =  find_mistake(data, w)
x = [ones(size(data,1),1) data(:,1:4)]';
i = find(sign(w'*x)' ~= data(:,5));
end


function w_new = correct_mistake(data, w, i)
global count
    count = count+1;
    w_new = w + 0.5*data(i,5)*([1 data(i,1:4)])';
end
