import os
import ctypes as ct, shutil
from reg.basicdicscan import *

def getpriv(perm):
    def execute(taged):
        def methodology(*ology):
             
            if perm is False:
                print ( '\n\t\t\t<!>\tUser Is Admin: {}\n'.format( perm ))
 
            taged(*ology)
        return methodology
    return execute


@getpriv( ct.windll.shell32.IsUserAnAdmin() != 0 )
def deleteTagedFiles(*badfiles):
    
    flags = {
            
            'COULD_not_REMOVE': [],
            'COULD_successfully_REMOVE': []
        }
    
    flags['COULD_successfully_REMOVE'].clear()
    flags['COULD_not_REMOVE'].clear()
    rmv_ctr = 0
    
    for file in badfiles:
        
        try:
            os.remove( file )
        except OSError:
            
            flags['COULD_not_REMOVE'].append( file )
            #print( '\t\t\t<!>\tCould Not Delete File: {}'.format( file ))
            
            continue
        
        flags['COULD_successfully_REMOVE'].append( file )
        rmv_ctr += 1
        
        
    if rmv_ctr >= 1:
        print( '\n\n[*]\tRemoved {} Files!'.format(rmv_ctr) )
        
    if len(flags['COULD_not_REMOVE']) >=  1:
        
        for item in flags['COULD_not_REMOVE']:
            print( '\n\t\t\t<!>\tCould Not Delete File: {}'.format( item ))
        
        
@getpriv( ct.windll.shell32.IsUserAnAdmin() != 0 )
def quarantineFilesBase(*badfiles):
    
    proctoblk = []
    
    for file in badfiles:
        if file == '__init__.py': continue
        try:
            #shutil.move( file, __file__[:-13]+'{}'.format( 'qtine' ) )
            shutil.move( file, __file__[:-13]+'{}'.format( 'qtine' ) )
            print( '[*]\tQuarantined File {}'.format( file ) )
            proctoblk.append(file)
        except OSError as e:
            print( '\t\t\t<!>\tCould Not Move {} To Quarantine! --> {}'.format( file, e ) )
            continue
        #except:
            #print( '\n\t\t\t<!>\tCould NOT Quarantine File: {}'.format( file ))
            
            #continue
        
    if len(proctoblk) >= 1:
        createBlockedProcStructure(*proctoblk)
        


def deleteQuar():
    
    try:
        for file in os.listdir(__file__[:-13]+'{}'.format( 'qtine' ) ):
            if file == '__init__.py': continue
            #if file.isDir(): continue
            try:
                os.remove(__file__[:-13]+'qtine\\{}'.format( file ) )
                print( '\t[*]\tRemoved File {} from Quarantine'.format( file ) )
            except OSError as e: 
                print ( e )
                print( '\t\t\t<!>\tCould Not Delete {} From Quarantine!'.format( file ) )
    except:
        print( '\n\t[*]\tQuarantine Could Be Empty? Or Unable To Delete File(s)' )
        
        
        
def lstQuarItems():
    
    #print ( __file__[:-13]+'{}')
    
    try:
        for file in os.listdir(__file__[:-13]+'{}'.format( 'qtine' ) ):
            if file == '__init__.py': continue
            #if file.isDir(): continue
            try:
                print( '[*]\t{}'.format( file ) )
            except OSError: break
    except:
        print( '\n\t[*]\tQuarantine Could Be Empty?' )