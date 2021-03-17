# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:06:43 2019

@author: foon4
"""

import pyudev
context = pyudev.Context()
for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
    print(device.get('ID_FS_LABEL', 'unlabeled partition'))