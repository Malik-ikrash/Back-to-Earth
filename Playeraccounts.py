 
import mysql.connector



class register_player():
    def __init__(self,Email,password,username):
        self.conn = None
        self.Email = Email
        self.password = password
        self.username = username
        self.cursor = None


    def createdbconn(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "Backtoearth",
            password = "130624146",
            database = "backtoearth")
        self.cursor = self.conn.cursor()
            

               

    def checkdetails(self):
        sql = f"SELECT * FROM Players WHERE Email = '{self.Email}' or username = '{self.username}';"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if len(result) == 0:
            details = True
            return details
        else:
            print("Email or username is already registerd")
            details = False
            return details
        



    def insertdetails(self):

        sql = "SELECT * FROM Players"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if len(result) == 0:
            foregin_key = 1
        else:
            foregin_key = len(result) + 1
        

        if (self.conn.is_connected()):
            players = "INSERT INTO players (Email,password,username) Values (%s,%s,%s)"
            player_table = (self.Email,self.password,self.username)
            scores = "INSERT INTO scores (Totalscore,PlayerID) VALUES (%s,%s)"
            score_table = (0,foregin_key)
            scores_track = "INSERT INTO store_scores (level_1,level_2,level_3,level_4,level_5,level_6,level_7,level_8,PlayerID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            scores_track_table = (0,0,0,0,0,0,0,0,foregin_key)


            self.cursor.execute(players,player_table)
            self.conn.commit()
            self.cursor.execute(scores,score_table)
            self.conn.commit()
            self.cursor.execute(scores_track,scores_track_table)
            self.conn.commit() 

        return foregin_key


    


class sign_in_players:
    def __init__(self,Email,password):
        self.Email = Email
        self.password = password
        self.conn = None
        self.cursor = None
        self.key = None 


    def createdbconn(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "Backtoearth",
            password = "130624146",
            database = "backtoearth")
        self.cursor = self.conn.cursor()



    def checkdetails(self):
        sql = f"SELECT * FROM Players WHERE Email = '{self.Email}' and password = '{self.password}';"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if len(result) > 0:
            details = True
            return details
        else:
            details = False
            return details

    def getkey(self):

        findkey = f"SELECT playerID FROM Players WHERE Email = '{self.Email}' and password = '{self.password}';"
        self.cursor.execute(findkey)
        get = self.cursor.fetchone()
        list_to_int = int(''.join(map(str,get)))# Turning the foregin key from a list of string into an integer 
        self.key = list_to_int
        

    def insertscore1(self,score):
        value = score
        sql = f"UPDATE store_scores SET level_1 = '{value}' WHERE playerID = '{self.key}';"
        self.cursor.execute(sql)
        self.conn.commit()
        

    def insertscore2(self,score):
        value = score
        sql = f"UPDATE store_scores SET level_2 = '{value}' WHERE playerID = '{self.key}';"
        self.cursor.execute(sql)
        self.conn.commit()

    def insertscore3(self,score):
        value = score
        sql = f"UPDATE store_scores SET level_3 = '{value}' WHERE playerID = '{self.key}';"
        self.cursor.execute(sql)
        self.conn.commit()


    def insertscore4(self,score):
        value = score
        sql = f"UPDATE store_scores SET level_4 = '{value}' WHERE playerID = '{self.key}';"
        self.cursor.execute(sql)
        self.conn.commit()


    def insertscore5(self,score):
        value = score
        sql = f"UPDATE store_scores SET level_5 = '{value}' WHERE playerID = '{self.key}';"
        self.cursor.execute(sql)
        self.conn.commit()


    def insertscore6(self,score):
        value = score
        sql = f"UPDATE store_scores SET level_6 = '{value}' WHERE playerID = '{self.key}';"
        self.cursor.execute(sql)
        self.conn.commit()


    def insertscore7(self,score):
        value = score
        sql = f"UPDATE store_scores SET level_7 = '{value}' WHERE playerID = '{self.key}';"
        self.cursor.execute(sql)
        self.conn.commit()


    def insertscore8(self,score):
        value = score
        sql = f"UPDATE store_scores SET level_8 = '{value}' WHERE playerID = '{self.key}';"
        self.cursor.execute(sql)
        self.conn.commit()


    def addtohighscore(self):
        allscore = 0
        get = f"SELECT level_1,level_2,level_3,level_4,level_5,level_6,level_7,level_8 FROM store_scores WHERE playerID = '{self.key}';"
        self.cursor.execute(get)
        results = self.cursor.fetchone()
        for counter in range(0,8):
            allscore += float(results[counter])
            addingall = round(allscore)
        score = f"UPDATE scores SET Totalscore = '{addingall}' WHERE playerID = '{self.key}';"
        self.cursor.execute(score)
        self.conn.commit()

    
        


class making_leaderboard():
    def __init__(self):
        self.conn = None
        self.cursor = None


    def createdbconn(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "Backtoearth",
            password = "130624146",
            database = "backtoearth")
        self.cursor = self.conn.cursor()


    def sort_scores(self):
        

        scores = "SELECT Totalscore FROM scores"
        self.cursor.execute(scores)
        strings = self.cursor.fetchall()
        # Fetches the highscores and makes them into a list of strings
        highscores = [int(i[0]) for i in strings]
        #converts the list of strings into a list of integers so it can compare properly


        ids = "SELECT PlayerID FROM scores"
        self.cursor.execute(ids)
        stringids = self.cursor.fetchall()
        # Fetches the highscores and makes them into a list of strings
        allids = [int(i[0]) for i in stringids]
        #converts the list of strings into a list of integers so it can compare properly



        maximum = len(highscores)
        for counter in range(1,maximum):
            print(highscores)
            inside = counter
            while inside > 0 and highscores[inside-1] <= highscores[inside]:
                highscores[inside-1],highscores[inside] = self.change_scores(highscores[inside-1],highscores[inside])
                allids[inside-1],allids[inside] = self.change_scores(allids[inside-1],allids[inside])
                inside = inside - 1
            print(highscores)
        seperate = highscores[0:10]
        tenids = allids[0:10]
        

        topscores = []
        for counter in range(0,len(seperate)):
            topscores.append(highscores[counter])


        topids = []
        for counter in range(0,len(tenids)):
            topids.append(tenids[counter])


        
        name = []
        for counter in  range(0, len(topids)):
            users = f"SELECT Username from players WHERE playerID = '{topids[counter]}';"
            self.cursor.execute(users)
            name_list = self.cursor.fetchall() # gets the usernames

            name.append(name_list) # appends them for every loop 
        name = [remove[0][0] for remove in name] # removes the unwanted square brackets and commans
 


        with open("highscore.txt","w") as writefile:
            for counter in range(0,len(name)):
                writefile.write(name[counter]+","+str(topscores[counter])+"\n")


    def change_scores(self,swap1,swap2):
        return swap2,swap1
    
    




