import time, serial, sys

ser = serial.Serial(
  port=sys.argv[1],
  baudrate=115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS
)
ser.isOpen()



def printOutputIfAvailable():
  time.sleep(1) # wait one second before attempting to read response
  out = ""
  while ser.inWaiting() > 0:
    out += ser.read(ser.inWaiting())
  if out != '':
    print out

### STATUS INFORMATION THAT XYZware polls periodically
ser.write("XYZ_@3D:" + '\n')
printOutputIfAvailable()
ser.write("XYZ_@3D:6" + '\n')
printOutputIfAvailable()
ser.write("XYZ_@3D:5" + '\n')
printOutputIfAvailable()
ser.write("XYZ_@3D:8" + '\n')
printOutputIfAvailable()

### Check printer is ready to offline print from SD card?
ser.write("XYZ_@3D:4" + '\n')
printOutputIfAvailable()


### Send gcode to printer
with open(sys.argv[2], 'rb') as fin:
    gcode = fin.read()
    gcode = str.replace(gcode, '\n', '\r\n') # XYZware includes carriage feed
    gcode = bytearray(gcode)
    gcode.append(0x00);
    gcode.append(0x00);
    gcode.append(0xB9); # some sort of checksum? how to calculate this?
    gcode.append('.');
    # print ' '.join(x.encode('hex') for x in str(gcode))
    ser.write("M1:MyTest,711,0.3.16,EE1_OK,EE2_OK\n" + gcode)
printOutputIfAvailable()
