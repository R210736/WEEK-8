inputFile='/home/sumanth/Jazz.wav'
outputFile='/home/sumanth/sumanth.wav'
[x,fs]=audioread(inputFile);
x_rev=flipud(x);
audiowrite(outputFile,x_rev,fs);
disp('Audio file reversed and saved successfully');
