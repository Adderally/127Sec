import winreg as reg
import ctypes as ct, time


            
        
def getDefaultBrowserType(**data):
    
    key = reg.OpenKey( data['CURRENT_USER'],
                       data['TARGET_CURRENT'][1],
                       0, reg.KEY_READ )
    
    dbsr =[]
    
    for i in range( 0, reg.QueryInfoKey(key)[1] ):
        formated = reg.EnumValue( key, i )[1].split( '--' or '-' or '/' ); dbsr.append(formated[0])
        
    print( "[*]\tBrowser:\t{} <HASH--> {}".format( dbsr[1], dbsr[0] )); dbsr.clear()
        



def getLocalStartUps(**data):
    
    key = reg.OpenKey( data['LOCAL'],
                       data['TARGET_LOCAL'][0],
                       0, reg.KEY_READ )
    
    
    locstartup = []
    
    for i in range( 0, reg.QueryInfoKey(key)[1] ):
        formated = reg.EnumValue( key, i )[1].split( '--' or '-' or '/' ); locstartup.append(formated[0])
        
    for item in locstartup:
        print ( '[*]\tLOCAL-STARTUP:\t{}'.format(item) );time.sleep(.3)



def scanRegistry():
    
    HKEYS ={
        'CURRENT_USER': reg.HKEY_CURRENT_USER,
        'LOCAL'       : reg.HKEY_LOCAL_MACHINE,
        'TARGET_CURRENT'      : [
                    r'Software\Microsoft\Windows\CurrentVersion\Run',       #CURRENT_USER
                    r'Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice', #CURRENT_USER
                    r'Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice',  #CURRENT_USER
                ],
                
        'TARGET_LOCAL'        : [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'],
                
        'DEFAULT_BROWSER':    ['IE.HTTPS', 'IE.HTTP' ,'ChromeHTML'],
        'POSSIBLE_BACKDOOR':  []
}
    #r'Software\Microsoft\Windows\CurrentVersion\Run'
    
    
    
    key = reg.OpenKey( HKEYS['CURRENT_USER'], r'Software\Microsoft\Windows\CurrentVersion\Run', 0, reg.KEY_ALL_ACCESS )
    
    usrstartup = []
    
    for i in range( 0, reg.QueryInfoKey(key)[1] ):
         
         formated = reg.EnumValue( key, i )[1].split( '--' or '-' or '/' )
             
         usrstartup.append(formated[0])
         
    for item in usrstartup:
        print ( '[*]\tUSER-STARTUP:\t{}'.format(item) );time.sleep(.3)
        
                     
    getLocalStartUps(**HKEYS)
    #getDefaultBrowserType(**HKEYS)
    
    input( '\n[*]\tIdea Of The Certain Things That Might Have Been Scanned... ( ENTER TO CONTINUE )\n' )
         
    return ct.windll.shell32.IsUserAnAdmin() != 0




def createBlockedProcStructure(*quarantine):
    
    mainkey = reg.CreateKey( reg.HKEY_CURRENT_USER,
                            r'Software\Microsoft\Windows\CurrentVersion\Policies\Explorer'
                        )
    
    reg.SetValueEx( 
            mainkey, 
            'DisallowRun', 
            0, 
            reg.REG_DWORD, 
            1 
        )
    
    disallowkey = reg.CreateKey(
            reg.HKEY_CURRENT_USER,
            r'Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun'
        )
    
    for quar in quarantine:
        
        reg.SetValueEx( 
                disallowkey, 
                quar,
                0, 
                reg.REG_SZ, 
                quar
            )