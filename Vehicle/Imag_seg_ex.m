pkg load image
%% Image segmentation and extraction
%% Read Image
imagen=imread('image1.jpg');
%% Show image
%figure(1)
%imshow(imagen);
%title('INPUT IMAGE WITH NOISE')
%% Convert to gray scale
if size(imagen,3)==3 % RGB image
    imagen=rgb2gray(imagen);
end
%% Convert to binary image
threshold = graythresh(imagen);
imagen =~im2bw(imagen,threshold);
%% Remove all object containing fewer than 30 pixels
imagen = bwareaopen(imagen,30);
pause(1)
%% Show image binary image
%figure(2)
%imshow(~imagen);
%title('INPUT IMAGE WITHOUT NOISE')
imwrite(~imagen,'sdfsdf.jpg');