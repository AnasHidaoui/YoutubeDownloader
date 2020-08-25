""" import the important modul for the programme"""
from stringcolor import *
import pafy
from welcome_by import Welcom_by

""" creat the main programme here"""

class Download :

    """
    simple download from youtube 
    based on: youtube-dl and payf
    """

    tag="================================================================================"

    def __init__(self) :
        Welcom_by.welcom(self)  # hello, in TopTube
        self.get_URL() # get the url from the user
        self.choces()  # chos between video or audio
        self.start() # start download"
        Welcom_by.goodby(self) # goody 


    def get_URL(self) :
        while True :
            url_id = input(cs("Entrer the video ID or URL : ","#40ff00").bold())
            try :
                print(cs("Please wait....","#40ff00").bold())
                self.request = pafy.new(url_id)
            except TypeError :
                print(cs("TypeError: new() missing 1 required positional argument: 'url'", "DeepPink3"))
            except ValueError :
                print(cs("ValueError: Need 11 character video id or the URL of the video !!!!", "DeepPink3"))
            except :
                print(cs("Ooops !! Somthing is not working....try againe", "DeepPink3"))
            else :
                author = self.request.author
                title  = self.request._title
                print(f"Title     :{cs(title, '#ff00ff').bold()}")
                print(f"Author    :{cs(author, '#ff00ff').bold()}")
            
                break


    def path(self) :
        while True :
            path = input(cs("Saved as : ","#40ff00").bold())
            try :
                self.path = str(path)
            except ValueError :
                print(cs("ValueError !!! Please try againe....", "DeepPink3"))
            except :
                print(cs("Ooops !! Somthing is not working....try againe", "DeepPink3"))
            else :
                break


    def choces(self) :  # chose between video or audio
        while True :
            chose = input(cs("Do you want to download video or audio: ","#40ff00").bold())
            try :
                self.chose = str(chose)
            except :
                print(cs("Ooops !! Somthing is not working....try againe", "DeepPink3"))
            else :
                break
    def start(self) :
        if self.chose == "video" :
            self.download_video(self.request)
        else :
            self.download_audio(self.request)

#=========================================================================================================================
    
    def download_video(self,request) :
        streams = request.streams
        cte = 1
        print(cs(self.tag, "purple4").bold())
        print(cs("The quilities are:", "DeepPink3").bold())
        for stream in streams :
            print(f"Quility {cte}: {stream}")
            cte += 1
        print(cs(self.tag, "purple4").bold())
        # part 2: chose the quility number
        while True :
            chose = input(cs("Chose the quility number: ","#40ff00"))
            try :
                chose = int(chose) - 1
                assert chose in range(0,len(streams))
            except ValueError :
                print(cs("ValueError !!! Please try againe....", "DeepPink3"))
            except AssertionError :
                print(cs("Please wait somthing is wrong !!! the chose is not corecte ", "DeepPink3"))
            except :
                print(cs("Ooops !! Somthing is not working....try againe", "DeepPink3"))
            else :
                break
        # get the path
        self.path()

        # part 3:start download
        print(cs("Start download....(Message:if somthing is wrong check the path)", "orchid"))
        ved = streams[chose]
        ved.download(self.path)

#============================================================================================================================================
    
    def download_audio(self,request) :
        streams = request.audiostreams
        cte = 1
        print(cs(self.tag, "purple4").bold())
        print(cs("The quilities are:", "DeepPink3").bold())
        for stream in streams :
            print(f"Quility {cte}: {stream}")
            cte += 1
        print(cs(self.tag, "purple4").bold())
        # part 2: chose the quility number
        while True :
            chose = input(cs("Chose the quility number: ","#40ff00"))
            try :
                chose = int(chose) - 1
                assert chose in range(0,len(streams))
            except ValueError :
                print(cs("ValueError !!! Please try againe....", "DeepPink3"))
            except AssertionError :
                print(cs("Please wait somthing is wrong !!! the chose is not corecte ", "DeepPink3"))
            except :
                print(cs("Ooops !! Somthing is not working....try againe", "DeepPink3"))
            else :
                break
        # get the path
        self.path()
        # part 3:start download
        print(cs("Start download....(Message:if somthing is wrong check the path)", "orchid").bold())
        aud = streams[chose]
        aud.download(self.path)

hidaoui = Download()



