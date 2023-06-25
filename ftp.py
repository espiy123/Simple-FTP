from ftplib import FTP
class ftpConnect:
    def __init__(self,host,user,password, *args):
        self.host = host
        self.user = user
        self.password = password
        self.port =  args[0]
        self.mode = args[1]
        
        conn = FTP(host)
        conn.login(user=self.user,passwd=self.password)
        
        try:
            conn = FTP(host)
            conn.login(user=self.user,passwd=self.password)
            print(conn.getwelcome())
            print("You location on drive is: "+str(conn.pwd()))

        except:
            print("Can't connect to server")