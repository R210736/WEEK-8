import scipy.io.wavfile as au
[fs,x]=au.read("Jazz.wav")
x_revese=x[::-1]
au.write("rev_file.wav",fs,x)
print("Audio file sucessfully reversed and saved")
