import sqlite3

connect = sqlite3.connect('database.sqlite')
cursor = connect.cursor()




def insert_db(phrase, answer):
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM phrases")
    new_id = str(cursor.fetchall()[-1][0] +1)
    cursor.execute("insert into phrases values ("+new_id+", '"+phrase+"','"+answer+"')")
    connect.commit()
    connect.close()

def get_db():
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM phrases")
    result = cursor.fetchall()
    print(result)
    connect.close()
    return result

##cursor.execute("""
##CREATE table groups (
#    id integer primary key autoincrement, 
#    group_name text
#);        
#""")

# cursor.execute("""
# CREATE table user (
#     id integer primary key, 
#     chat_id integer,
#     id_group integer,
#     FOREIGN KEY (id_group) REFERENCES groups(id)   
# );        
# """)

# cursor.execute(
#     "insert into groups values (1, 'friends')"
# )

# cursor.execute(
#     "insert into groups values (2, 'classmates')"
# )

# cursor.execute(
#     "insert into groups values (3, 'programmers')"
# )

def add_member(group,chat_id):
    if group == '{"command":"friends"}':
        group_id = 1
    elif group == '{"command":"classmates"}':
        group_id = 2
    elif group == '{"command":"programmers"}':
        group_id = 3
    connect = sqlite3.connect('database.sqlite')
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM user")
    new_id = str(cursor.fetchall()[-1][0] + 1)
    print(chat_id)
    print(group)
    cursor.execute("insert into user values ("+new_id+", "+str(chat_id)+","+str(group_id)+")")
    connect.commit()
    connect.close()
 
def get_member(group):
    if group == 'Friends':
        group_id = 1
    elif group == 'Classmates':
        group_id = 2
    elif group == 'Programmers':
        group_id = 3
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT chat_id FROM user WHERE id_group="+str(group_id))
    result = cursor.fetchall()
    conn.close()
    for i in range(0,len(result)):
        result[i] = result[i][0]
    #print(result)
    return result