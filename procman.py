import psutil, os, time
import ctypes as ct
from handel.fileacc import *


name_flags = {
        
        'malware_flag': [
                'Trojan', 'Virus', 'logger', 'rat',
                'key', 'AdWare', 'Your', 'Dark'
                'My', 'The', 'User', 'ez', 'haha', 'fake', 'Locky', 'hacked',
                'grabber', 'rabbit'
                ]
        }

def checkUserAccType():
    'Returns boolean value of if account is admin ( true or false )'
    
    return ct.windll.shell32.IsUserAnAdmin() != 0
    
    

def checkProcByNameAndID():
    'Searching proc names for keywords'
    
    struct = {
            
           # 'flagged_prc_opf'  :  [],
           # 'flagged_prc_basic':  [],
            'flagged_prc_loc'  :  []
            
            }
    
    struct['flagged_prc_loc'].clear()
    
    
    try:
        
        #with open( 'virspc.txt', 'r' ) as containment_file:
        
        for proc in psutil.process_iter():
            for keyword in name_flags['malware_flag']:
                #for line in containment_file.readlines():
                #if len(line) < 1: continue
                
                    #for keyword in name_flags['malware_flag']:
                    #for keyword in line:
                                
                name = proc.name()
                Id   = proc.pid
                                
                if keyword.casefold() in name.casefold():
                                    #struct['flagged_prc_opf'].append( '\t\t\t<!>Process name={} | id={} Is Suspected To Be Malware!'.format( name, Id ))
                                    #struct['flagged_prc_basic'].append( '{} | {}'.format( name, Id ))
                                    
                    proc.kill()
                                    
                    if checkUserAccType is True:
                        struct['flagged_prc_loc'].append( proc.exe() )
                    else:
                        print ( '\t\t\t<!>\tUser Is Admin: {} -> Can Not Catch Process location.'.format( checkUserAccType() )); continue
                                
                else : continue
                
            print ( '[*]\tProcess ---> {} (ID={})'.format(proc.name(), proc.pid) );time.sleep(.003)
        
        #containment_file.close()
        
        if len(struct['flagged_prc_loc']) >= 1:
            print ( '\n[*]\t{} Possible Threats Found. ( These Will Be Delt With Later. ) ( ENTER TO CONTINUE )'.format(len(struct['flagged_prc_loc'])) ); input()
            
        else:
            print ('\n[*]\tAppears No Threats Were Detected In Processes. ( ENTER TO CONTINUE ) ' ); input()
            
        
                    
    except ( psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess ):
        #containment_file.close()
        print( '\n\t\t\t<!>\tUser Is Admin: {}'.format( checkUserAccType() ))
        
        
    
    if len(struct['flagged_prc_loc']) >= 1:
        
        try:
            convertFilesIntoTxt( 'this', *struct['flagged_prc_loc'] )
        except:
            print ('\t\t\t<!>\tWas Not Able To Search Process Directory. ( HINT: Try Running As Administrator ) ')
            
    else: pass
            
    



