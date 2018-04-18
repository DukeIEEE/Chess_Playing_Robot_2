import serial

ser = serial.Serial("COM6", 9600)   # open serial port that Arduino is using
print(ser)

while True:
    if ser.readline() == "b'Player Made Move'":
        ser.write(b"blah")
        #Figure out new board state
        #write to serial what move to make
        #Probably have math to convert chess move (i.e. Bc3xNd4) into numerical start/end positions in the Python rather than Arduino code