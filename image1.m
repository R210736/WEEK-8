inputFile = '/home/sumanth/image1.jpg';
imageData = imread(inputFile);
redChannel = imageData(:,:,1);
greenChannel = imageData(:,:,2);
blueChannel = imageData(:,:,3);
redOutputFile = 'r.csv';
greenOutputFile = 'g.csv';
blueOutputFile = 'b.csv';
csvwrite(redOutputFile, redChannel);
csvwrite(greenOutputFile, greenChannel);
csvwrite(blueOutputFile, blueChannel);

disp('Red, green, and blue channels saved to separate CSV files successfully!');