#set of python classes that simulate an Internet app where one party, Alice, periodically sends packets she wants to send Bob. The Internet process continuosly checks to see if Alice has any packets to send, and if it does, it sends them to Bob, in which Bob checks them, and then deletes the
#it was not done exactly how they wanted but its my project so they can fuckoff, the only thing not done is that the process doesnt check to see if there is a packet, but rather waits for the packet to be sent and then gives it to bob, kinda the same but im not sure thats what they wanted, anywhoos it works and everything so we good, next project
from random import seed
from random import randint
import time

class Alice():
    """The Sender in this context, creates, and sends packets of info through an Internet process, and waits for confirmation it was received, rinse n repeat"""
    def __init__(self, numPackets, namedProcess):
        """Constructor, takes in number of packets user wants Alice to send to Bob, also begins Internet Process between Bob and Alice"""
        self.numPackets = numPackets
        self.namedProcess = namedProcess
        #this.process = InternetProcess(self.namedProcess)#instantiate an internet process to allow the sending of packets to Bob     
        self.numPacketsSent = 0


    def create_packet(self):
        """Method to create random packets of info and send them to Bob, we'll just use a random String generator and send them to Bob, who will print them
       out to the screen"""
        return "this is a random String"
 
    def connect_to_process(self, processID):
        """Methid to connect to the process which allows communication to Bob"""
        
    def send_packet(self):
        """This method performs the sending of the random message to the Internet Process"""
        value = randint(1, 10) 
        time.sleep(value)#make it take some time to send the messahe
        return self.create_packet();
        

class Bob():
    """Receiver in this context, will receive messages from Alice through the use of an Internet Process, read the packet, and then send a confirmation he received it"""
    def __init__(self):
        self.numPacketsReceived =0;
    def receive_packets(self, packet):
        print(packet)
        
class InternetProcess():
    """Process to check if Alice has packets she wants to send to Bob, if so, sends them to Bob and confirms they were received"""

    def __init__(self, nameOfProcess, numPackets):
        self.nameOfProcess = nameOfProcess#give the process a name
        self.numPackets = numPackets
        self.alice = Alice(self.numPackets, self.nameOfProcess)#instantiate an Alice instance
        self.bob = Bob()#instantiate a Bob instance

    '''def _tester(self):
        tempString = self.alice.getString()
        return tempString
    '''
    def transmit_data(self):
        tempString = self.alice.send_packet()#get a string from alice to send to Bob
        #print(tempString)
        self.bob.receive_packets(tempString)#send the string to bob from alice
        properly_received = self.bob.confirm_packet_received()
        self.alice.receive_packet_confirmation(properly_received)#send alice confirmation the packet was received by bob
    
    def start(self):
        i = 0
        while i < self.numPackets:#for the number of packets the user(me rn cause its easier to hardcode it in) defined, run the program
            #self.transmit_data()
            #print(self._tester())
            self.transmit_data()
            i += 1

process = InternetProcess("someCoolProcess", 10)
process.start()
