pkg load image
%This function converts an image file with filename,"input_image" into a text
%file with filename,"output_text".
%
%for example,
%image2text('mess1.jpg','cont.txt')
%converts a image file with filename,"mess.jpg' into a text file with
%filename,"cont.txt".

%function image2text(input_image,output_text);

%y=input_image;
img=imread('image2.jpg');
img=double(img);

[m n r]=size(img);
%-------------------------------------------------
char2=[];
for(k=1:r)
for(i=1:m)
char1=[];
for(j=1:n)
    char1=[char1 imgnum2str(img(i,j,k))];
end
char2=[char2;char1];
end
end
%-------------------------------------------------
char_temp=[];
if(r==1)
    char_sign='.';
end
if(r==3)
    char_sign='/';
end
for(i=1:2*n-2)
    char_temp=[char_temp char_sign];
end
char_temp=[imagenum2strall(m) char_temp];
%-------------------------------------------------
char2=[char_temp;char2];
%-------------------------------------------------
stringing=char2;
%-------------------------------------------------
for(i=1:length(y)-4)
    name_file(i)=y(i);
end
%-------------------------------------------------
filename=output_text;
f = fopen(filename,'wt');
if(f==-1)
    disp('error writing to the text file')
end
if(f~=-1)
   for dion=1:3*m+1
        fprintf(f,'%s\n',stringing(dion,:)); %\n is similar as in C i-e 'enter' at the end of one row(see help fprintf)
   end
  fclose(f);          % closing the file as in C++
end
%-------------------------------------------------