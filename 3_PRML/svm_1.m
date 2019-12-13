clear
clc
data = load ('bloodTransfusion_noduplicated.txt');
raw_X = data(:,1:end-1);
label = data(:,end);
[num,d] = size(raw_X);
X = raw_X;
%{
X = normalize(raw_X,'norm',1);
%}
alpha = zeros(num,1);
n = randperm(size(X,1));
%≤‚ ‘ºØ
test_X = X(n(351:end),:);
test_label = label(n(351:end),:);
test_alpha = alpha(n(351:end),:);
%—µ¡∑ºØ
X = X(n(1:350),:);
label = label(n(1:350),:);
alpha = alpha(n(1:350),:);
num = size(X,1);
b = 0;
C = 6;
sigma = 0.6;
iteration = 0;
max_iteration = 1000;



while iteration < max_iteration
    alpha_change = 0;
        for i = 1:num
            gi = sum((alpha.*label)'*Kernel(X(i,:),X,sigma)) + b;       
            Ei = gi - label(i);
        
            if ((gi*label(i) <= 1 && (alpha(i) == 0 || alpha(i) <= C))...
                || (gi*label(i) >= 1 && alpha(i) > 0))        
      
                j = randi(num);  
                while i == j
                    j = randi(num);
                end
                
                gj = sum((alpha.*label)'*Kernel(X(j,:),X,sigma)) + b;       
                Ej = gj - label(j);
                            
                eta = Kernel(X(j,:),X(j,:),sigma)...
                + Kernel(X(i,:),X(i,:),sigma) - ...
                2*Kernel(X(i,:),X(j,:),sigma);
                
                        
                if label(i) ~= label(j) 
                    L = max(0,alpha(j) - alpha(i));
                    H = min(C,C + alpha(j) - alpha(i));
                else
                    L = max(0,alpha(j) + alpha(1) -C);
                    H = min(C,alpha(j) + alpha(i));
                end
                if L==H  
                    continue;
                end
                
                alphai_old = alpha(i);
                alphaj_old = alpha(j);
                
                alphaj = alphaj_old + (label(j)*(Ei - Ej)/eta);
                
                if alphaj>H
                    alpha(j) = H;
                elseif alpha(j)>=L && alpha(j)<=H
                    alpha(j) = alphaj;
                else
                    alpha(j) = L;
                end
                
                alpha(i) = alphai_old + label(i)*label(j)*(alphaj_old - alpha(j));
                
                b1 = b - Ei - ...
                    label(i)*(alpha(i)-alphai_old)*Kernel(X(i,:),X(i,:),sigma) - ...
                    label(j)*(alpha(j)-alphaj_old)*Kernel(X(i,:),X(j,:),sigma);
                b2 = b - Ej - ...
                    alpha(i)*(alpha(i)-alphai_old)*Kernel(X(i,:),X(j,:),sigma) - ...
                    label(j)*(alpha(j)-alphaj_old)*Kernel(X(j,:),X(j,:),sigma);
                
                              
                if alpha(i)>0 && alpha(i)<C
                    b = b1;
                elseif alpha(j)>0 && alpha(j)<C
                    b = b2;
                else
                    b = (b1+b2)/2;
                end
                
                alpha_change = alpha_change + 1;
            end
        end
        if alpha_change == 0          
            teration = iteration + 1;
        else
            iteration = 0;
        end
        
        disp(['iteration = ',num2str(iteration)]);
end

indexw = find(alpha ~= 0);

X = test_X;
label = test_label;
predict = (alpha.*label)'*Kernel(X,X,sigma) + b;
predict = sign(predict);

figure;
index1 = find(predict==-1);
data1 = (X(index1,:))';
plot(data1(1,:),data1(2,:),'or');
hold on
index2 = find(predict==1);
data2 = (X(index2,:))';
plot(data2(1,:),data2(2,:),'*b');
hold on
dataw = (X(indexw,:))';
plot(dataw(1,:),dataw(2,:),'+y','LineWidth',1);


function result = Kernel(data1,data2,sigma)
    [m1,~] = size(data1);
    [m2,~] = size(data2);
    result = zeros(m2,m1);
    for l = 1:m1
        for k = 1 : m2
            result(k,l) = exp(-norm(data1(l,:)-data2(k,:))/(2*sigma^2));
        end
    end
end