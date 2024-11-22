import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 directorybuster.py')
    run('mkdir /usr/share/directorybuster')
    run('cp directorybuster.py /usr/share/directorybuster/directorybuster.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/directorybuster/directorybuster.py "$@"')
    with open('/usr/bin/directorybuster','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/directorybuster & chmod +x /usr/share/directorybuster/directorybuster.py')
    print('''\n\ncongratulation directorybuster is installed successfully \nfrom now just type \x1b[6;30;42mdirectorybuster\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/directorybuster ')
    run('rm /usr/bin/directorybuster ')
    print('[!] now directorybuster  has been removed successfully')
