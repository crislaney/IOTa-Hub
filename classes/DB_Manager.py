import sqlite3
import json
import hashlib

class DB_Manager():

    def __init__(self):
        # build db
        # check for existing database
        self.conn = sqlite3.connect('iota.db')
        curs = self.conn.cursor()

        check_user = "SELECT name FROM sqlite_master\
        WHERE type='table' AND name='Users';"
        
        check_scripts = "SELECT name FROM sqlite_master\
        WHERE type='table' AND name='Scripts';"

        curs.execute(check_user)
        self.conn.commit()
        user_exist = curs.fetchone()

        curs.execute(check_scripts)
        self.conn.commit()
        script_exist = curs.fetchone()

        if user_exist is None or script_exist is None:
            print("did not find users or scripts")
            drop_users = "DROP TABLE IF EXISTS Users;"
            drop_scripts = "DROP TABLE IF EXISTS Scripts;"

            curs = self.conn.cursor()
            curs.execute(drop_users)
            self.conn.commit()

            curs = self.conn.cursor()
            curs.execute(drop_scripts)
            self.conn.commit()

            create_users = "CREATE TABLE Users (\
            user_id INTEGER PRIMARY KEY UNIQUE,\
            user_name text UNIQUE,\
            hash_pass TEXT);"
            create_scripts = "CREATE TABLE Scripts(\
            script_id INTEGER Primary KEY UNIQUE,\
            script_name TEXT,\
            script_json TEXT, \
            user_id INTEGER NOT NULL,\
            FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE);"

            curs = self.conn.cursor()
            curs.execute(create_users)
            self.conn.commit()

            curs = self.conn.cursor()
            curs.execute(create_scripts)
            self.conn.commit()

        else:
            print("Found table")

    # make sure to try except this
    def Insert_User(self, user_name, password):
        insert_stmt = "INSERT INTO 'Users' (user_name, hash_pass) \
        VALUES(?, ?);"
        curs = self.conn.cursor()
        print("Inserting User")
        curs.execute(insert_stmt, (user_name, hashlib.sha3_512(password.encode('utf-8')).hexdigest()))
        self.conn.commit()
        print("Committed User")
        # print(self.conn.Error)


    #TODO
    def Delete_User(self, user_name):
        delete_stmt = "DELETE FROM 'Users' WHERE user_name = ?;"
        # (user_name)
        return
    
    def Get_User(self, user_name, id=None):
        get_stmt = "SELECT * FROM 'Users' WHERE user_name = ?;"
        if id is not None:
            get_stmt = "SELECT * FROM 'Users' WHERE id = ?;"
         
        curs = self.conn.cursor()
        curs.execute(get_stmt, (user_name,))
        self.conn.commit()
        return curs.fetchone()


    def Insert_Script(self, user_name, script):
        user_id = self.Get_User(user_name)[0]
        #get username
        insert_stmt = "INSERT INTO 'Scripts' \
        (script_name, script_json, user_id) VALUES(?, ?, ?);"
        curs = self.conn.cursor()
        curs.execute(insert_stmt, (script.name, json.dumps(script.steps), user_id))
        self.conn.commit()


    #TODO
    def Delete_Script(self, script, id=None):
        delete_stmt = "DELETE FROM 'Scripts' WHERE script_name = ?;"
        return


    def Get_All_Scripts(self, user_name):
        user_id = self.Get_User(user_name)[0]

        query_string = "SELECT * FROM 'Scripts' WHERE Scripts.user_id=?;"
        curs = self.conn.cursor()
        curs.execute(query_string, (user_id,))
        self.conn.commit()

        return curs.fetchall()
    
    def Authorize_User(self, user_name, password):
        hashed_pass = ""
        user_id = -1

        try:
            user = self.Get_User(user_name)
            user_id = user[0]
            hashed_pass = user[2]
        except Exception as e:
            return None

        hashed_attempt = hashlib.sha3_512(password.encode('utf-8')).hexdigest()

        if hashed_pass != hashed_attempt:
            return None

        return user_id

    #TODO
    def Get_Script(self, script_name, id=None):
        return

    
    #TODO
    def Get_Auth_Rooms(self, user_name):
        return
    
    