import socket
import threading
import daemon
import sys
import json
from base64 import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
import MySQLdb
from conf import *


def handle_client(s):
    data = s.recv(2048)
#    print data
    if data:
        action , form = data.split(":")
        if (action == "REGISTER") :
            print "trying to register"
            reg_credentials = decrypt_RSA("server_private.pem",form)
            print "******************************************************************\n\n"
            reg_credentials = reg_credentials.split("|")
            #print tuple(reg_credentials)
            try :

                db = MySQLdb.connect(db_address,db_user,db_password,db_name )
                cursor = db.cursor()
                query = "INSERT INTO users(user_fname,user_lname,user_email,user_name,user_password,user_birthdate,user_gendre,user_public_key) VALUES('%s','%s','%s','%s','%s','%s','%s','%s');" % tuple(reg_credentials)
                cursor.execute(query)
                db.commit()
                db.close()
                s.send("Registration Successful \n")
                db = MySQLdb.connect(db_address,db_user,db_password,db_name )
                cursor = db.cursor()
                query = "insert into messages(sender_message,reciever_message,text_message) values ('Support','%s','welcome %s and thanks for using this application <br> feel free to let us know what you think about it , any feedback is welcome ') ;" %(reg_credentials[3],reg_credentials[3])
                cursor.execute(query)
                db.commit()
                db.close()
            except MySQLdb.Error ,e :
                print("Something went wrong ! {} ".format(e.args))
                if "user_name" in e.args[1]:
                    s.send("Username already in use !\n")
                if "user_email" in e.args[1]:
                    s.send("Email address already in use !\n")


        if (action == "LOGIN") :
            print "Trying to login"
            #login_credentials = xor_decrypt(form)
            login_credentials = decrypt_RSA("server_private.pem",form)
            login_credentials = login_credentials.split('|')
            try :
                db = MySQLdb.connect(db_address,db_user,db_password,db_name )
                cursor = db.cursor()
                query = "select * from users where user_name = '%s' and user_password='%s' ; " % tuple(login_credentials)
                print query
                cursor.execute(query)
                data = cursor.fetchall()
                db.close()
                print "data=  " + repr(data)
                if data :
                    reply = "Welcome %s %s " % (data[0][1] , data[0][2])
                    print reply
                    db = MySQLdb.connect(db_address,db_user,db_password,db_name )
                    cursor = db.cursor()
                    query = "update users set user_status ='online' where user_name ='%s' ; " % (login_credentials)[0]
                    print query
                    cursor.execute(query)
                    db.commit()
                else :
                    reply = "no such user/pass "
                print reply
                s.send(reply + '\n')
            except MySQLdb.Error ,e :
                print("Something went wrong ! {} ".format(e.args))

            #s.send("we are still testing some shit here , sorry for the inconvenience\n")
        if (action == "RESET"):
            #reset_mail = xor_decrypt(form)
            reset_mail = decrypt_RSA("server_private.pem",form)
            print "password reset request for %s" %(reset_mail)

        if (action == "ADDCONTACT"):
            print "Trying to add new contact"
            c  = decrypt_RSA("server_private.pem",form).split("|")
            print c
            try :
                reply =""
                db = MySQLdb.connect(db_address,db_user,db_password,db_name )
                cursor = db.cursor()
                query1 = "select user_name from users where user_name = '%s' ;" %(c[1])
                cursor.execute(query1)
                data1 = cursor.fetchall()
                #print "looking for user " +  repr(data1)
                db.close()
                if ( (not data1 ) or (c[0] == c[1]) ) :
                    reply = "not a valid contact  %s !" %(c[1])
                else :
                    db = MySQLdb.connect(db_address,db_user,db_password,db_name )
                    cursor = db.cursor()
                    query =  "select user_contacts from users where user_name ='%s' ;" %(c[0])
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print "current contact list " +  repr (data[0][0].split(","))  # "".join(data)
                    if (c[1] in data[0][0].split(",") ):
                        reply = "user already in contact list "
                    else : # everything is fine , let's add the contact to the db
                        "let's add the new user ! "
                        db = MySQLdb.connect(db_address,db_user,db_password,db_name )
                        cursor = db.cursor()
                        query = "update users set user_contacts='%s' where user_name ='%s' ; " %("".join(data[0])+","+c[1],c[0])
                        #print query
                        cursor.execute(query)
                        db.commit()
                        reply = "user added successfully !"
                print reply
                s.send(reply + '\n')
            except MySQLdb.Error ,e :
                print("Something went wrong ! {} ".format(e.args))
        if (action == "GETCONTACT"):
            username  = decrypt_RSA("server_private.pem",form)
            print username
            print "trying to get %s 's contacts " % username
            db = MySQLdb.connect(db_address,db_user,db_password,db_name )
            cursor = db.cursor()
            query = "select user_contacts from users where user_name='%s' ; " %username
            cursor.execute(query)
            contacts = cursor.fetchall()
            db.close()
            print query
            print contacts
            if contacts :
                info = []
                contacts = contacts[0][0].split(",")
                for x in contacts :
                    db = MySQLdb.connect(db_address,db_user,db_password,db_name )
                    cursor = db.cursor()
                    query = "select user_status,user_fname,user_lname,user_name from users where user_name='%s' ; " %x
                    cursor.execute(query)
                    temp = cursor.fetchall()
                    print "retrieving %s info  : %s " %(x,temp[0][0])
                    print list(temp[0])
                    info.append(list(temp[0]))
                print "the complete list is " + repr(info)
                s.send(json.dumps(info) + '\n')

        if (action == "NEWMSG"):
            print "Someone is trying to send something to somebody "
            c  = decrypt_RSA("server_private.pem",form).split("|")
            print c
            db = MySQLdb.connect(db_address,db_user,db_password,db_name )
            cursor = db.cursor()
            query = " insert into messages(sender_message,reciever_message,text_message) values ('%s','%s','%s') ;" %(c[0],c[1],c[2])
            cursor.execute(query)
            db.commit()
            db.close()
            s.send("message sent  Successfuly \n")

        if (action == "GETMSGS") :
            print "Someone is requesting chat history "
            c  = decrypt_RSA("server_private.pem",form).split("|")
            db = MySQLdb.connect(db_address,db_user,db_password,db_name )
            cursor = db.cursor()
            query = "select sender_message,reciever_message,text_message from messages where (sender_message='%s' and reciever_message='%s') or (sender_message='%s' and reciever_message='%s') order by id_message  ;" % (c[0],c[1],c[1],c[0])
            print query
            cursor.execute(query)
            messages = cursor.fetchall()
            db.close()
            s.send(json.dumps(messages) + '\n')








def serve_forever():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('localhost', 1337)
#    server_address = ('192.168.1.3', 1337)
    print >>sys.stderr, 'starting up on %s port %s' % server_address
    server.bind(server_address)
    server.listen(1)
    while True:
        conn, address = server.accept()
        print >>sys.stderr, 'connection from', address
        thread = threading.Thread(target=handle_client, args=[conn])
        thread.daemon = True
        thread.start()


def encrypt_RSA(public_key_loc, message):
    key = open(public_key_loc, "r").read()
    nb_chunks = len(message) / 200
    chunks = []
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    for i in range(nb_chunks+1):
        encrypted = rsakey.encrypt(message[i*200:(i+1)*200])
        chunks.append(encrypted.encode('base64').rstrip())
    encrypted = rsakey.encrypt(message[(nb_chunks+1)*200:])
    chunks.append(encrypted.encode('base64').rstrip())
    return "-".join(chunks)

def decrypt_RSA(private_key_loc, message):

    open("/tmp/a","w").write(message)
    m = open("/tmp/a","r").read()
    chunks = []
    chunks = m.split('-')
    plain = []
    key = open(private_key_loc, "r").read()
    #print "key found!"
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    for i in range(len(chunks)):
        decrypted = rsakey.decrypt(b64decode(chunks[i].rstrip()))
        plain.append(decrypted)
 	print "".join(plain)
    return  "".join(plain)

serve_forever()