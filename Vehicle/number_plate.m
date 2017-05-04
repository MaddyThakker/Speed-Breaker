function np=number_plate(img)
%image correlation method
%matches 2 matrix
load('imgfildata.mat');
[~,cc]=size(img);
picture=imresize(img,[300 500]);

if size(picture,3)==3
  picture=rgb2gray(picture);  %grey values are btwn 0 to 1 or 0 to 255
end



threshold = graythresh(picture);  %greythresh gives the threshold value of greyscale image
picture =~im2bw(picture,threshold);   %black nd white values are 0 or 1 and values greater thn threshold=1,rest=0 and invert white and black ie 1 to 0 and 0 to 1
picture = bwareaopen(picture,30);  % those things that have less than 30 pixels are removed


if cc>2000
    picture1=bwareaopen(picture,3500);  %those things that have less than 3500 pixels are removed ie excluding nmbr plate
else
picture1=bwareaopen(picture,3000);  %those things that have less than 3000 pixels are removed ie excluding nmbr plate
end

picture2=picture-picture1;  %only number plate is left


picture2=bwareaopen(picture2,200);   %only text is there in the nmbr plate



[L,Ne]=bwlabel(picture2);  %l gives matrix which has info of nmbr plate and Ne gives number of digits or characters


final_output=[];
t=[];
for n=1:Ne
  [r,c] = find(L==n);   
  n1=picture(min(r):max(r),min(c):max(c));   %picture command crops nth object from L
  n1=imresize(n1,[42,24]);     %in database size is 42,24 so it is resized so that we can match it with the database
 
  
  x=[ ];

totalLetters=size(imgfile,2);

 for k=1:totalLetters
    
    y=corr2(imgfile{1,k},n1);
    x=[x y];
    
 end
%  t=[t max(x)];
 if max(x)>.35
 z=find(x==max(x));
 out=cell2mat(imgfile(2,z));

final_output=[final_output out];
end
end

np=final_output;


end