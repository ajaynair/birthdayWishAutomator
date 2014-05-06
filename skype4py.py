import Skype4Py
import datetime
import time
def terminate(wasRunning):
    print wasRunning	
    if wasRunning == False:
        print 'Shutting down skype client'
        skype.Client.Shutdown()
        print 'Skype client shutdown'

def sendMsg(name):
    skype.SendMessage(name,'Happy Birthday')

def wishIfBirthday(date):
    for user in skype.Friends:
        if user.Birthday == date:
            print 'Today is ' + user.FullName + '\'s birthday. Sending him/her a happy birthday message'
            sendMsg(user.Handle)
            print 'message sent'

'''
Initializes skype client. Return a boolean to denote if the skype was already running
'''
def initialize(wasRunning):
    global skype
    skype = Skype4Py.Skype()
    if skype.Client.IsRunning == False:
        wasRunning = False
        print 'Skype client not running'
        print 'Starting skype client'
        skype.Client.Start()
    	time.sleep(50)
    print 'Skype client found'
    skype.Attach()
    return wasRunning

def main():
    #Constants
    #########################################
    date = (datetime.date.today()) #Today's date
    #date = datetime.date(1990, 8, 31) #Uncomment and  put anyone's birthday to send a message now to the particular person
    wasRunning = True #Set to true if the skype client was already running.
    #########################################

    wasRunning = initialize(wasRunning)
    wishIfBirthday(date)
    terminate(wasRunning)

if __name__ == '__main__':
    main()
