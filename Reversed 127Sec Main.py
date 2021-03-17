def findShortcutTarget(root_p, *tagedFile):
    """Returns the path that shortcut is pointing too"""
    print('\n\n')
    for taged in tagedFile:
        shell = win32com.client.Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut('{}\\{}'.format(root_p, taged))
        print('<?>\t(SHORTCUT?)\tTarget path for <{}> = <{}>'.format(taged, shortcut.TargetPath))


def getFilesInDirectory(dir_):
    """simply catch all files and a directory"""
    directory_content = []
    directory_content.clear()
    subdirectory = []
    subdirectory.clear()
    subdirectory.append(dir_)
    for _dir in subdirectory:
        for filetype in os.listdir(_dir):
            subdir = '{}\\{}'.format(_dir, filetype)
            if os.path.isdir(subdir):
                subdirectory.append(subdir)
                continue
                if filetype.endswith(common_file_sigs_exts[8]):
                    findShortcutTarget(_dir, '{}'.format(filetype))
                if filetype.endswith(common_file_sigs_exts[9]):
                    findShortcutTarget(_dir, '{}'.format(filetype))
                if filetype.endswith(common_file_sigs_exts[1]):
                    continue
                elif filetype.endswith(common_file_sigs_exts[10]):
                    continue
                elif filetype.endswith(common_file_sigs_exts[11]):
                    continue
                elif filetype.endswith(common_file_sigs_exts[12]):
                    continue
                elif filetype.endswith(common_file_sigs_exts[5]):
                    continue
                elif filetype.endswith(common_file_sigs_exts[4]):
                    continue
                else:
                    directory_content.append('{}\\{}'.format(_dir, filetype))

    print('\n\n')
    if len(directory_content) is not None:
        convertFilesIntoTxt(dir_, *directory_content)


if __name__ == '__main__':
    ct.windll.kernel32.SetConsoleTitleW('127Sec -Offline')
    valid_input = False
    main_loop = True
    first_run = False
try:
    while main_loop is True:
        while valid_input is False:
            print('\n\n\n======================================================================================')
            _dir = input('Enter A Directory To Search In >\t')
            print('\n\n')
            if len(_dir) <= 3:
                raise SystemExit
            if ',' in _dir:
                show_hdw = _dir.split(',')
                if show_hdw[1] == 'hdw'.casefold():
                    renderTypes()
                elif show_hdw[1] == 'ls_q'.casefold():
                    lstQuarItems()
                elif show_hdw[1] == 'dl_q'.casefold():
                    deleteQuar()
                else:
                    print('\t\t\t<!>\t{} Not Reconnized Paramater!'.format(show_hdw[1]))
                    continue
            if 'done'.casefold() in _dir:
                if len(_dir) is 4:
                    main_loop = False
                    break
                try:
                    if not os.listdir(_dir):
                        print('\t\t\t<!>\t{} Is Empty!'.format(_dir))
                except:
                    continue

                if first_run is False:
                    print('[*]\tScanning Certain Items...( some not listed )\n\n')
                    time.sleep(2)
                    scanRegistry()
                    print('[*]\tScanning For Possible Threats...\n')
                    time.sleep(2)
                    checkProcByNameAndID()
                getFilesInDirectory(_dir)
                first_run = True

    print('\n\n[*]\tApplication Done!...')
except OSError as e:
    try:
        print('\n\t\t\t<!>\tUmmm, not sure what went wrong? -> {}'.format(e))
        time.sleep(7)
    finally:
        e = None
        del e
