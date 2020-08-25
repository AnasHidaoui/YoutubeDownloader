# import thre string color modulr
from stringcolor import *
from os import system
from sys import exit
from platform import system as getos

# creat class Welcom goodby
class Welcom_by :
    """
    class  called welcom_by using in the first part of this project
    """
    def welcom(self) :

        if getos().lower()[0] is not "w" :
            system("clear")

        else:
            system("cls")

        wel = """

                     ,------.   ,-----. ,--.   ,--.,--.  ,--. 
                     |  .-.  \ '  .-.  '|  |   |  ||  ,'.|  | 
                     |  |  \  :|  | |  ||  |.'.|  ||  |' '  | 
                     |  '--'  /'  '-'  '|   ,'.   ||  | `   | 
                     `-------'  `-----' '--'   '--'`--'  `--' 
                        By : HIDAOUI ANAS / Augaust 5 2020 /
                         https://github.com/rootAnashidaoui
                                versio: 3.0.4
        """
        print(cs(wel,"purple4").bold())


    def goodby(self) :

        gb = """
                        ==================================
                        |  Tanks you for using TopTube   |
                        +--------------------------------+
                        |      By : HIDAOUI ANAS         |
                        |        versio: 3.0.4           |        
                        +--------------------------------+
                        | www.rootAnashidaoui@githab.com |
                        |       July 29 2020             |
                        ==================================
        """
        print(cs(gb,"purple4").bold())


b = Welcom_by()
b.goodby()
