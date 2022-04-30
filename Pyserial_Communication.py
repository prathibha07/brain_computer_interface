import serial   #Serial communication module
import sys
import json     #json format module
import time     #time module
from telnetlib import Telnet  #Telnet communication
ser=serial.Serial('COM5',57600,timeout=0.25)

tn=Telnet('localhost',13854);
start=time.clock();

i=0;

tn.write('{"enableRawOutput": true, "format": "Json"}');


outfile="null";
if len(sys.argv)>1:
                outfile=sys.argv[len(sys.argv)-1];
                outfptr=open(outfile,'w');

eSenseDict={'attention':0, 'meditation':0};
#waveDict={'lowGamma':0, 'highGamma':0, 'highAlpha':0, 'delta':0, 'highBeta':0, 'lowAlpha':0, 'lowBeta':0, 'theta':0};
signalLevel=0;

while i<100:
                blinkStrength=0;
        
                line=tn.read_until('\r');
                if len(line) > 20:              
                                timediff=time.clock()-start;
                                dict=json.loads(str(line));  #returns an object from a string representing a json object.
                                if "poorSignalLevel" in dict:
                                                signalLevel=dict['poorSignalLevel'];
                                if "blinkStrength" in dict:
                                                blinkStrength=dict['blinkStrength'];
                                if "eegPower" in dict:
                                                waveDict=dict['eegPower'];
                                                eSenseDict=dict['eSense'];
                                                bb=json.dumps(blinkStrength);
                                                print bb
                                                ser.write(bb)
                                                time.sleep(1)

                                               

                                              
                                                
                                
                                




                                

        
tn.close();
outfptr.close();




        





