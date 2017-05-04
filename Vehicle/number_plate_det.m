pkg load image
clc
close all;
clear;
load imgfildata;
graphics_toolkit gnuplot

for i = 1:2
	picture=imread(strcat("image",int2str(i),".jpg"));
	[~,cc]=size(picture);
	picture=imresize(picture,[720 720]);

	if size(picture,3)==3
		picture=rgb2gray(picture);
	end

	threshold = graythresh(picture);
	picture =~im2bw(picture,threshold);
	picture = bwareaopen(picture,30);

	imwrite(picture,strcat("output1",int2str(i),".jpg"));
	imwrite(~picture,strcat("output1",int2str(i),"b.jpg"));

	if cc>2000
    		picture1=bwareaopen(picture,3500);
	else
		picture1=bwareaopen(picture,3000);
	end

	picture2=picture-picture1;
	picture2=bwareaopen(picture2,200);

	imwrite(picture2,strcat("output2",int2str(i),".jpg"));
	imwrite(~picture2,strcat("output2",int2str(i),"b.jpg"));

end