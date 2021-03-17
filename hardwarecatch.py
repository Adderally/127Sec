import wmi

#print('Graphics Card: {0}'.format(gpu_info.Name))


computer = wmi.WMI()

def captureGpuType(gpu):
    def execute(taged):
        def methodology(*ology):
             
            print('[*]\tProcessor:\t{}'.format(gpu))
 
            taged(*ology)
        return methodology
    return execute
 
     
         
@captureGpuType(computer.Win32_Processor()[0].Name)
def DisplayGpuTypesInUsage(*taged):
    
    print('[*]\tGPU:\t\t{}\t|\t{}\n\n'.format(taged[0], taged[1]))
    print('[*]\tRAM:\t\t{} GB'.format(taged[2]))
    
    
    

def renderTypes():
    
    types = []; types.clear()
    types.append(computer.Win32_VideoController()[0].Name)
    types.append(computer.Win32_VideoController()[0].VideoProcessor)
    types.append(float(computer.Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576)
    
    DisplayGpuTypesInUsage(*types)