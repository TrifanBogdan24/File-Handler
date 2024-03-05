#!/usr/bin/env python3

import sys      # pentru argumentele din linia de comanda, exit code
import os       # OS routines
import shutil   # files and directory trees

import time

import re       # RegExp


from pathlib import Path



def pwd():
    print(os.getcwd())


def echo():

    # ./main.py echo -n 1 2 3 4
    nr_args = len(sys.argv)

    start_pos = (3 if nr_args >= 3 and sys.argv[2] == "-n" else 2)

    for i in range(start_pos, nr_args):
        if start_pos != nr_args - 1:
            print(sys.argv[i], end = ' ')
        else:
            print(sys.argv[i], end = '')

    if nr_args >= 3 and sys.argv[2] == "-n":
        print(end = '')     # echo -n ...
    else:
        print(end = '\n')   # echo ...

    return 0





def cat():

    # ./main cat file1 file2 file3

    nr_args = len(sys.argv)

    if nr_args == 2:
        return 255        # comanda invalida


    for i in range(2, nr_args + 1):

        try:
            fisier_text = open(sys.argv[i])

            # list comprehension
            [print(line, end = '') for line in fisier_text]
        except:
            return 236            # comanda nu s-a executat cu succes

    return 0




def mkdir():

    nr_args = len(sys.argv)     # numarul de argumente in linia de comanda

    if nr_args == 2:
        return 255      # comanda invalida

    ret_val = 0                 # se va incerca crearea tutoror directoarelor
        
    for i in range(2, nr_args):
        try:
            os.makedirs(sys.argv[i])
        except:
            ret_val = 226  # comanda nu s-a executat cu succes

    return ret_val



def mv():

    nr_args = len(sys.argv)     # numarul de argumente in linia de comanda

    if nr_args != 4:
        return 255      # comanda invalida

    src = sys.argv[2]
    dest = sys.argv[3]

    try:
        shutil.move(src, dest)
    except:
        return 216      # comanda nu s-a executat cu succes

    return 0



def ln():

    # ./main.py ln file1 link1
    # ./main.py ln -s file2 link2

    nr_args = len(sys.argv)

    if nr_args < 4 and nr_args > 5:
        return 255      # comanda invalida

    if nr_args == 4:
        # hard link : ./main.py ln file1 link1
        try:
            ok = os.link(sys.argv[2], sys.argv[3])
            return 0
        except:
            return 236

    # soft link : ./main.py ln -s file1 link1
    if sys.argv[2] != "-s" and sys.argv[2] != "--symbolic":
        return 255      # comanda invalida

    try:
        os.symlink(sys.argv[3], sys.argv[4])
        return 0
    except:
        return 236
    
    return 0



def rmdir():

    nr_args = len(sys.argv)

    if nr_args == 2:
        return 255      # comanda invalida
    
    ret_val = 0         # se va incerca stergerea tuturor directoarelor goale

    for i in range(2, nr_args):
        try:
            os.rmdir(sys.argv[i])
        except:
            ret_val = 196

    return ret_val


def rm():

    nr_args = len(sys.argv)

    flag_rec_dir = ['-r', "-R", "--recursive"]
    flag_empty_dir = ["-d", "--dir"]
    
    all_flags = flag_rec_dir + flag_empty_dir

    if nr_args <= 2:
        # invalid number of arguments
        return 255
    
    if nr_args == 3 and sys.argv[2] in all_flags:
        # invalid command: the last arg is a flag
        return 255


    if nr_args == 4 and sys.argv[3] in all_flags:
        # invalid command: the last arg is a flag
        return 255


    if nr_args > 4 and sys.argv[2] in flag_rec_dir and sys.argv[3] in flag_rec_dir:
        # invalid command: two flags are the same
        return 255

    if nr_args > 4 and sys.argv[2] in flag_empty_dir and sys.argv[3] in flag_empty_dir:
        # invalid command: two flags are the same
        return 255


    if nr_args >= 4 and sys.argv[2] not in all_flags and sys.argv[3] in all_flags:
        # invalid command: ./main.py rm [not flag] [flag] ....
        return 255 


    rm_r = False
    rm_d = False

    start = 2

    if nr_args > 3 and sys.argv[2] in flag_rec_dir:
        start = 3
        rm_r = True
    
    if nr_args > 3 and sys.argv[2] in flag_empty_dir:
        start = 3
        rm_d = True
    

    if nr_args > 4 and sys.argv[3] in flag_rec_dir:
        start = 4 
        rm_r = True
    
    if nr_args > 4 and sys.argv[3] in flag_empty_dir:
        start = 4
        rm_d = True

    ret_val = 0


    for i in range(start, nr_args):

        path = sys.argv[i]

        if os.path.isdir(path):
            # rm dir

            if rm_r == True:
                # rm -r dir

                try:
                    # rm -r dir
                    shutil.rmtree(path)
                except:
                    # comanda nu s-a executat cu succes
                    ret_val = 186
                
                continue
            

            if rm_d == True:
                dir = os.listdir(path)  # lists the content of the directory

                if len(dir) != 0:
                    # comanda a esuat
                    # cannot remove non-empty directory
                    ret_val = 186
                    continue
                
                try:
                    # rm -d dir
                    os.rmdir(sys.argv[i])
                except:
                    # comanda a esuat
                    ret_val = 186
                    continue
  


            # s-a incercat stergere unui director, fara vreun flag specificat
            ret_val = 186
            

        
        else:
            # rm file

            try:
                os.remove(path)
            except:
                # comanda nu s-a executat cu succes
                ret_val = 186


    
    return ret_val







def touch():
    
    nr_args = len(sys.argv)

    if nr_args <= 2:
        # invalid command: no aguments provided to `touch`
        return 255


    modify_atime = False
    modify_ctime = False
    modify_mtime = False


    for i in range(2, nr_args - 1):
        flag = sys.argv[i]

        if flag == "-a":
            modify_atime = True
        elif flag in ["-c", "--no-create"]:
            modify_ctime = True        
        elif flag == "-m":
            modify_mtime = True
        else:
            # comanda invalida: flag-ul nu a fost gasit
            return 255


    if modify_atime == True and modify_mtime == True:
        # comanda invalida
        # se poate modifica doar atime / mtime, nu simultan
        return 255


    file_path = sys.argv[nr_args - 1]


    if os.path.isfile(file_path) == False:
        # Fisierul nu exista; trebuie creat
        file = open(file_path, 'w')
        file.close()


    try:
        now = time.time()

        if modify_atime == True:
            os.utime(file_path, (now, now))
            return 0

        if modify_mtime == True:
            os.mtime(file_path, (now, now))
            return 0
    
    except:
        return 156

    return 0


def grep():
    nr_args = len(sys.argv)

    if nr_args <= 2 or nr_args >= 6:
        # comanda este invalida: numar nepotrivit de argumente
        return 255


    ignore_case = False


    if nr_args == 5 and sys.argv[2] != "-i":
        # flag-ul este invalid
        # asteptam: ./main.py -i exp file
        return 255


    if nr_args == 5 and sys.argv[2] == "-i":
        # ./main.py -i exp file
        ignore_case = True


    pattern = sys.argv[nr_args - 2]
    file_path = sys.argv[nr_args - 1]

    

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):

            if ignore_case == False:
                sensitive_grep(pattern, line)
            else:
                insensitive_grep(pattern, line)


    return 0



def sensitive_grep(pattern, line):
    # case sensitive
    if not re.search(pattern, line):
        return

    print(line, end = '')    
    # print(f"{file_path}:{line_number}: {line.strip()}")


def insensitive_grep(pattern, line):
    # case insensitive
    if re.search(pattern, line, flags=re.IGNORECASE):
        return
    print(line, end = '')
    
    # print(f"{file_path}:{line_number}: {line.strip()}")
    






def chmod():

    nr_args = len(sys.argv)

    if nr_args <= 3:
        # invalid command: missing arg for permision / files
        return 255

    permission = sys.argv[2]


    chmod_type = ''

    try:
        oct_permission = int(permission, 8)
        chmod_type = 'numeric'    
    except:
        chmod_type = 'alfa'


    if chmod_type == 'numeric' and permission[0] in "+-":
        chmod_type = 'add_remove_numeric'

    
    if chmod_type == 'numeric':
        return numeric_chmod()
    elif chmod_type == 'add_remove_numeric':
        return add_remove_numeric_chmod()
    else:
        return alfa_chmod()

    return 0



def numeric_chmod():
    # ./main.py chmod 741 file1 file2 ...

    nr_args = len(sys.argv)

    perm = int(sys.argv[2])

    if perm < 0 or perm > 777:
        # invalid permission
        return 255


    # converts the permission in an octal (base 8) integer
    file_oct_perm = int(sys.argv[2], 8)

    ret_val = 0


    for i in range(3, nr_args):
        file_name = sys.argv[i]

        try:
            os.chmod(file_name, file_oct_perm)
        except:
            ret_val = 231


    return ret_val



def add_remove_numeric_chmod():
    """
    ./main.py chmod +740 file
    ./main.py chmod -740 file
    """

    nr_args = len(sys.argv)


    perm_sign = sys.argv[2][0]

    if not perm_sign in "+-":
        # invalid command
        return 255

    perm = int(sys.argv[2][1:], 10)

    if perm < 0 or perm > 777:
        # invalid permission
        return 255


    # converts the permission in an octal (base 8) integer
    oct_perm = int(sys.argv[2][1:], 8)


    # getting permission bytes
    read_owner = (True if oct(0o400 & oct_perm) != oct(0) else False)
    write_owner = (True if oct(0o200 & oct_perm) != oct(0) else False)
    exec_owner = (True if oct(0o100 & oct_perm) != oct(0) else False)

    read_group = (True if oct(0o040 & oct_perm) != oct(0) else False)
    write_group = (True if oct(0o020 & oct_perm) != oct(0) else False)
    exec_group = (True if oct(0o010 & oct_perm) != oct(0) else False)

    read_others = (True if oct(0o004 & oct_perm) != oct(0) else False)
    write_others = (True if oct(0o002 & oct_perm) != oct(0) else False)
    exec_others = (True if oct(0o001 & oct_perm) != oct(0) else False)

    

    ret_val = 0


    for i in range(3, nr_args):
        
        file_name = sys.argv[i]

        try:
            # get file permissions
            file_stats = os.stat(file_name)
            file_perm = file_stats.st_mode



            # modify file permsision            
            if perm_sign == '+':
                # we add permission using logic OR
                if read_owner == True: file_perm |= 0o400
                if write_owner == True: file_perm |= 0o200
                if exec_owner == True: file_perm |= 0o100
                
                if read_group == True: file_perm |= 0o040
                if write_group == True: file_perm |= 0o020
                if exec_group == True: file_perm |= 0o010
                
                if read_others == True: file_perm |= 0o004
                if write_others == True: file_perm |= 0o002
                if exec_others == True: file_perm |= 0o001

            else:
                # we add permission using logic AND
                if read_owner == True: file_perm &= 0o400
                if write_owner == True: file_perm &= 0o200
                if exec_owner == True: file_perm &= 0o100
                
                if read_group == True: file_perm &= 0o040
                if write_group == True: file_perm &= 0o020
                if exec_group == True: file_perm &= 0o010
                
                if read_others == True: file_perm &= 0o004
                if write_others == True: file_perm &= 0o002
                if exec_others == True: file_perm &= 0o001


            # change file permission
            os.chmod(file_name, file_perm)
        
        except:
            ret_val = 231

    return ret_val
    





def alfa_chmod():
    # ./main.py chmod ga+rx file1 file2 ... 
    
    nr_args = len(sys.argv)

    perm_chars = sys.argv[2]

    
    # verificarea permisiunilor valide
    # u/g/o/a +/- r/w/x

    ret_val = 0


    (ugo, sign, rwx, ret_val) = get_chmod_perm_modification()


    if ret_val == 255:
        # invalid command
        return ret_val
    

    for i in range(3, nr_args):

        file_name = sys.argv[i]
        
        if os.path.exists(file_name) == False:
            # the command fails for a file
            ret_val = 231
            continue

        try:
            # get file permissions
            file_stats = os.stat(file_name)
            file_perm = file_stats.st_mode
        except:
            # the command failed at getting the permissions of a file
            ret_val = 231
            continue
        

        new_file_perm = transform_file_permissions(file_perm, ugo, sign, rwx)


        try:
            os.chmod(file_name, new_file_perm)
        except:
            # the command failed at changing the permissions of a file
            ret_val = 231

    return ret_val





def get_chmod_perm_modification():

    perm_chars = sys.argv[2]

    ugo = ''
    sign = ''
    rwx = ''

    for char in perm_chars:
        
        if char == 'u':
            if (sign != '') or (rwx != '') or ('u' in ugo == True):
                # invalid comand: misplaced category
                return (ugo, sign, rwx, 255)
            ugo += 'u'
        
        elif char == 'g':
            if (sign != '') or (rwx != '') or ('g' in ugo == True):
                # invalid comand: misplaced category
                return (ugo, sign, rwx, 255)
            ugo += 'g'
        
        elif char == 'o':
            if (sign != '') or (rwx != '') or ('o' in ugo == True):
                # invalid comand: misplaced category
                return (ugo, sign, rwx, 255)
            ugo += 'o'
        
        elif char == 'a':
            if (sign != '') or (rwx != '') or (ugo != ''):
                # invalid comand: misplaced category
                return (ugo, sign, rwx, 255)
            ugo += 'ugo'
       
        elif (char in "+-") == True:
            if (sign != '') or (rwx != ''):
                # invalid comand: misplaced category
                return (ugo, sign, rwx, 255)
            
            sign = char     # + / -

            if ugo == '':
                # chmod +rwx file or chmod -x file
                ugo += 'ugo'
            

        elif char == 'r':
            if (ugo == '') or (sign == '') or ('r' in rwx == True):
                # invalid comand: misplaced category
                return (ugo, sign, rwx, 255)
            rwx += 'r'
        
        elif char == 'w':
            if (ugo == '') or (sign == '') or ('w' in rwx == True):
                # invalid comand: misplaced category
                return (ugo, sign, rwx, 255)
            rwx += 'w'

        elif char == 'x':
            if (ugo == '') or (sign == '') or ('x' in rwx == True):
                # invalid comand: misplaced category
                return (ugo, sign, rwx, 255)
            rwx += 'x'
        
        else:
            # invalid character for file permission
            return (ugo, sign, rwx, 255)
        
    return (ugo, sign, rwx, 0)






def transform_file_permissions(file_perm, ugo, sign, rwx):
    
    # `|` -> logic OR for adding permissions
    # `&` -> logic AND for eliminating permissions


    # user(owner)

    if ('u' in ugo) and (sign == '+') and ('r' in rwx):
        file_perm |= 0o400

    if ('u' in ugo) and (sign == '-') and ('r' in rwx):
        file_perm &= 0o400
        
    
    if ('u' in ugo) and (sign == '+') and ('w' in rwx):
        file_perm |= 0o200

    if ('u' in ugo) and (sign == '-') and ('w' in rwx):
        file_perm &= 0o200
    
    if ('u' in ugo) and (sign == '+') and ('x' in rwx):
        file_perm |= 0o100
    
    if ('u' in ugo) and (sign == '-') and ('x' in rwx):
        file_perm &= 0o100



    # group

    if ('g' in ugo) and (sign == '+') and ('r' in rwx):
        file_perm |= 0o040

    if ('g' in ugo) and (sign == '-') and ('r' in rwx):
        file_perm &= 0o040
    
    if ('g' in ugo) and (sign == '+') and ('w' in rwx):
        file_perm |= 0o020

    if ('g' in ugo) and (sign == '-') and ('w' in rwx):
        file_perm &= 0o020
    
    if ('g' in ugo) and (sign == '+') and ('x' in rwx):
        file_perm |= 0o010
    
    if ('g' in ugo) and (sign == '-') and ('x' in rwx):
        file_perm &= 0o010




    # others

    if ('o' in ugo) and (sign == '+') and ('r' in rwx):
        file_perm |= 0o004

    if ('o' in ugo) and (sign == '-') and ('r' in rwx):
        file_perm &= 0o004
    
    if ('o' in ugo) and (sign == '+') and ('w' in rwx):
        file_perm |= 0o002

    if ('o' in ugo) and (sign == '-') and ('w' in rwx):
        file_perm &= 0o002
    
    if ('o' in ugo) and (sign == '+') and ('x' in rwx):
        file_perm |= 0o001
    
    if ('o' in ugo) and (sign == '-') and ('x' in rwx):
        file_perm &= 0o001


    return file_perm






# functia `ls` nu este facuta suficient de bine
def ls():
    # ./main.py ls [options] [directories]

    nr_args = len(sys.argv)

    all_flags = ["-a", "--all", "-R", "--recursive", "-l"]
    dir_paths = []

    ls_all = False
    ls_rec = False
    ls_list = False

    nr_all_flags = 0
    nr_rec_flags = 0
    nr_list_flags = 0

    # deciding if the flags are valid
    # and which arguments are the directories

    for i in range(2, nr_args):
        
        if sys.argv[i] in all_flags and len(dir_paths) > 0:
            # invalid command
            return 255

        if sys.argv[i] in ["-a", "--all"]:
            ls_all = True
            nr_all_flags += 1
        elif sys.argv[i] in ["-R", "--recursive"]:
            ls_rec = True
            nr_rec_flags += 1
        elif sys.argv[i] == "-l":
            ls_list = True
            nr_list_flags += 1
        else:
            dir_paths.append(sys.argv[i])
            
    
    if nr_all_flags > 1 or nr_rec_flags > 1 or nr_list_flags > 1:
        # invalid commnand: repeated flags
        return 255


    if len(dir_paths) == 0:
        # ./main.py ls [options] .
        dir_paths = [os.getcwd()]


    ret_val = 0
    
    for path_dir in dir_paths:

        if os.path.isdir(path_dir) == False:
            # the command fails for a given argument
            ret_val = 176
            continue

        

        old_cwd = os.getcwd()    # get current working directory
        new_cwd = os.chdir(path_dir)

        ls_list_dir_content(path_dir, ls_all, ls_rec, ls_list)

        os.chdir(old_cwd)


    return ret_val







def ls_list_dir_content(path_dir, ls_all, ls_rec, ls_list):
    
    if ls_rec:
        print(f"{path_dir}:")

    listed_file_paths = []


    for file_name in os.listdir(path_dir):
        if file_name.startswith(".") and ls_all == False:
            continue
        listed_file_paths.append(os.path.join(path_dir, file_name))

    for file_path in listed_file_paths:
        if ls_list == False:
            if os.path.basename(file_path) not in ['.', '..']:
                print(os.path.basename(file_path))
        else:
            ls_l_file(file_path)

    for file_path in listed_file_paths:
        if os.path.isdir(file_path) and ls_rec:
            print()
            ls_list_dir_content(file_path, ls_all, ls_rec, ls_list)









def ls_l_file(file_name):

    is_cwd = False
    is_parent_cwd = False

        

    # permission
    perm = ''

    # file type
    if os.path.isfile(file_name):
        perm += '-'
    
    elif os.path.isdir(file_name):
        perm += 'd'
    
    elif os.path.islink(file_name):
        perm += 'l'

    else:
        perm += '-'


    file_stats = os.stat(file_name)


    file_perm = file_stats.st_mode


    # owner (user)
    perm += ('r' if oct(0o400 & file_perm) != oct(0) else '-')
    perm += ('w' if oct(0o200 & file_perm) != oct(0) else '-')
    perm += ('x' if oct(0o100 & file_perm) != oct(0) else '-')
    
    # group
    perm += ('r' if oct(0o040 & file_perm) != oct(0) else '-')
    perm += ('w' if oct(0o020 & file_perm) != oct(0) else '-')
    perm += ('x' if oct(0o010 & file_perm) != oct(0) else '-')
    
    # other users
    perm += ('r' if oct(0o004 & file_perm) != oct(0) else '-')
    perm += ('w' if oct(0o002 & file_perm) != oct(0) else '-')
    perm += ('x' if oct(0o001 & file_perm) != oct(0) else '-')

    
    print(perm, end = ' ')

    print(Path(file_name).owner(), end = ' ')
    print(Path(file_name).group(), end = ' ')

    print(file_stats.st_size, end = ' ')


    # the time of the last modification
    ti_m = os.path.getmtime(file_name)

    m_ti = time.ctime(ti_m)

    # Using the timestamp string to create a 
    # time object/structure
    t_obj = time.strptime(m_ti)
    
    # Transforming the time object to a timestamp 
    # of ISO 8601 format
    # time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)

    numeric_month = time.strftime("%m", t_obj)
    day = time.strftime("%d", t_obj)
    hour = time.strftime("%H", t_obj)
    minute = time.strftime("%M", t_obj)


    # Transform the numeric month to its corresponding letter value
    month_mapping = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
        '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
        '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }

    chars_month = month_mapping[numeric_month]


    print(f"{chars_month} {day} {hour}:{minute}", end = ' ')


    print(file_name)



def main():
    # numele interpretorului (pyton3) nu se considera a fi argument
    nr_args = len(sys.argv)

    code = 0

    if nr_args < 2:
        code = 255       # comanda invalida
    elif sys.argv[1] == "pwd":
        code = pwd()
    elif sys.argv[1] == "echo":
        code = echo()
    elif sys.argv[1] == "cat":
        code = cat()
    elif sys.argv[1] == "mkdir":
        code = mkdir()
    elif sys.argv[1] == "mv":
        code = mv()
    elif sys.argv[1] == "ln":
        code = ln()
    elif sys.argv[1] == "rmdir":
        code = rmdir()
    elif sys.argv[1] == "rm":
        code = rm()
    elif sys.argv[1] == "ls":   
        code = ls()
    elif sys.argv[1] == "touch":
        code = touch()
    elif sys.argv[1] == "chmod":
        code = chmod()
    elif sys.argv[1] == "grep":
        code = grep()
    else:
        code = 255


    if code == 255:
        print("Invalid command")
    sys.exit(code)           # se verifica in terminal ruland `echo $?``

if __name__ == "__main__":
    main()
