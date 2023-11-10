#!/usr/bin/env python3

import sys      # pentru argumentele din linia de comanda, exit code
import os

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

    for i in range(2, nr_args):
        try:
            fisier_text = open(sys.argv[i])

            try:
                print(fisier_text.read())
            except:
                return 236        # comanda nu s-a executat cu succes
        except:
            return 236            # comanda nu s-a executat cu succes

    return 0


def cat():


    nr_args = len(sys.argv)     # numarul de argumente din linia de comanda
    # daca rulam pyhon3 main.py arg arg ... in loc de ./main.py arg args ...
    # python3 nu se contorizeaza ca argument in linia de comanda

    if nr_args == 2:
        return 255        # comanda invalida

    for i in range(2, nr_args):
        try:
            fisier_text = open(sys.argv[i])

            try:
                print(fisier_text.read(), end = '')
            except:
                return 236        # comanda nu s-a executat cu succes
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

    flag_director_recursiv = ['-r', "-R", "--recursive"]
    flag_director_gol = ["-d", "--dir"]

    rm_r = false
    rm_d = false
    start_pos = 2

    if nr_args >= 3:
        if sys.atgv[2] in flag_director_recursiv == true:
            rm_r = true

        if sys.argv[2] in flag_director_gol == true:
            rm_d = true

        start_pos = 3

    if nr_args >= 4 and (sys.argv[3] in flag_director_gol == true or sys.argv[3] in flag_director_recursiv == true):
        # avem doua flaguir : ne astam sa gasim un flag diferit pe poztia precedenta
        
        if sys.argv[2] in flag_director_gol == false and sys.argv[2] in flag_director_recursiv == false:
            return 255  # comanda invalida

        if sys.argv[2] in flag_director_gol == true and rm_d == true:
            return 255  # comanda invalida

        if sys.argv[2] in flag_director_recursiv == true and rm_r == true:
            return 255  # comanda invalida

        if sys.argv[3] in flag_director_gol == true:
            rm_d = true
        
        if sys.argv[3] in flag_director_recursiv == true:
            rm_r = true

        start_pos = 4

    if nr_args == start_pos:
        # avem doar numele utilitarului si flag-uri
        return 255  # comanda invalida


    # se va incerca stergerea tutror argumentelor
    ret_val = 0

    for i in range(start_pos, nr_args):

        if os.path.exists(sys.argv[i]) == false:
            ret_val = 186
            continue
        
        if os.path.isfile(sys.argv[i]) == true:
            
            try:
                os.remove(sys.argv[i])
            except:
                ret_val = 186

            continue
        
        if os.path.isdir(sys.argv[i]) == true:
            
            if rm_r == false:

                if len(os.list(sys.argv[i])) != 0:
                    # rm non-empty-dir
                    ret_val = 186
                    continue
                else: 
                    
                    if rm_d == true:
                        # rm -d empty-dir
                        try:
                            os.remove(sys.argv[i])      # <=> rmdir
                        except:
                            ret_val = 186
                            continue
                    
                    if rm_d == false:
                        # rm empty-dir
                        ret_val = 186
                        continue
            else:

                # rm -r dir
                try:
                    os.rmtree(sys.argv[i])
                except:
                    ret_val = 186
                    continue

        
        ret_val = 186

    return ret_val

def main():
    # numele interpretorului (pyton3) nu se considera a fi argument
    nr_args = len(sys.argv)

    ret_val = 0

    if nr_args < 2:
        ret_val = 255       # comanda invalida
    elif sys.argv[1] == "pwd":
        ret_val = pwd()
    elif sys.argv[1] == "echo":
        ret_val = echo()
    elif sys.argv[1] == "cat":
        ret_val = cat()
    elif sys.argv[1] == "mkdir":
        ret_val = mkdir()
    elif sys.argv[1] == "mv":
        ret_val = mv()
    elif sys.argv[1] == "ln":
        ret_val = ln()
    elif sys.argv[1] == "rmdir":
        ret_val = rmdir()
    elif sys.argv[1] == "rm":
        ret_val = rm()


    if ret_val == 255:
        print("Invalid command")
    sys.exit(ret_val)           # se verifica in terminal ruland echo $?

if __name__ == "__main__":
    main()
