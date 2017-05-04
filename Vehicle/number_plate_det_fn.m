clc
close all;
clear;
load imgfildata;
[file,path]=uigetfile({'*.jpg;*.bmp;*.png;*.tif'},'Choose an image');
s=[path,file];
img=imread(s);
np=number_plate(img);
disp(np);