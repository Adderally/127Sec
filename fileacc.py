import os, time, ctypes as ct
from intoxicate import *


basic_api_calls = {
    "python_import": 'import',
    "pyton_from": 'from',
    "clang_#include": '#include',
    "clang_macros": '#define'
    }



def resigFile(file):
    
    os.rename(file, file[:-4])



def convertFilesIntoTxt(dir_, *files):
    'search txt for key words, like imports and other calls'
    
    txt_files_to_scan = []; txt_files_to_scan.clear()
    original_filetype = []; original_filetype.clear()
    trojan_files = []; trojan_files.clear()

    
    for file in files:
        
        if file.endswith('.url'): continue
        if file.endswith('.lnk'): continue
    
        original_filetype.append(file)
        
        try:
            
            new_ext_file = '{}.txt'.format(file)
            os.rename(file, new_ext_file)
            txt_files_to_scan.append(new_ext_file)
            
        except:print('\t<#>\t {}'.format(file))
    
        
    
    
    if len(txt_files_to_scan) >= 1:
        
        searched = 0; threats = 0
        
        for moc_file in txt_files_to_scan:
            
            #if moc_file == None:print('\t<#>\tAppears there are no files to scan here?')
            with open(str(moc_file), 'r') as target_file:
                
                try:
                    
                    print('\n[*]\tScanning File:\t{}\n'.format(moc_file[:-4]))
                    
                    for line in target_file.readlines():
                        for item in basic_api_calls.values():
                            if item in line: 
                                
                                #print('\t\t\t<!>\tFile -> {} appears to have hidden data! -> {}'.format(moc_file[:-4], line))
                                print('\t\t\t<!>\tFile -> {} appears to have hidden data!'.format(moc_file[:-4]))
                                trojan_files.append(moc_file[:-4])
                                threats += 1
                                break
                                
                            else : 
                                searched += 1
                                continue
                            
                        break
                            
                    target_file.close()
                    time.sleep(.003)
                    resigFile(moc_file)
                    
                except UnicodeDecodeError:
                    target_file.close()
                    time.sleep(.003)
                    resigFile(moc_file)
                    continue
            
            
            
                
                ct.windll.kernel32.SetConsoleTitleW("127Sec - v1.0.0 - Files {} | Threats {}".format(searched, threats))
            
            
            
        if len(trojan_files) >= 1:
            
            valied_input = False
            
            print ( '\n\n\n[*]\tYou Have 4 Options.' )
            print ( '\n1.\tDelete All Threats... ( Forever delete these files off your machine )' )
            print ( '2.\tQuarantine All Threats... ( Doing this you will never have access to these files again )' )
            print ( '3.\tDelete Quarantined Files...' )
            print ( '4.\tList All Quarantined Files...' )
            
            while valied_input is False:
            
                opt = input( '\nEnter An Option ( 1, 2, 3, 4 )>\t' )
                
                if len(opt) < 1: continue
                if len(opt) > 1: continue
                if opt == 'done': raise SystemExit
            
                if opt == '1': 
                    
                    valied_input = True
                    deleteTagedFiles(*trojan_files)
                    
                elif opt == '2': 
                    
                    valied_input = True
                    quarantineFilesBase(*trojan_files)
                    
                elif opt == '3':
                    
                    valied_input = True
                    deleteQuar()
                        
                elif opt == '4':
                    
                    valied_input = True
                    lstQuarItems()