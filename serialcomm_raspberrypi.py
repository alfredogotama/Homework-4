import serial
ser = serial.Serial('/dev/ttyAMA0', 9600)
ser.write(chr(68))
print ser.readline()
#chr
