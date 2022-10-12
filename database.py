import mysql.connector as c
import database as db
con = c.connect(host = "localhost",user = "root",password = "honeychandu",database = 'project')
def date(date,cars,gen):
    cursor = con.cursor()
    cursor.execute("""insert into data(Date,Route,gender)values('{date}','{cars}','{gen}');
    
    
    """.format(date = date,cars = cars,gen =gen))
    con.commit()
    cursor.close()
    return 'date updated'
def show():
    cursor = con.cursor()
    cursor.execute(""" select * from data;""")
    table = cursor.fetchall()
    con.commit()
    cursor.close()
    return table
def signup(name,email,mobile,gender,passw):
    cursor = con.cursor()
    cursor.execute("""insert into signup(fullname,email,mobile,gender,password)values('{name}','{email}',{mobile},'{gender}','{passw}');
    
    
    
    """.format(name=name,email=email,mobile=mobile,gender=gender,passw=passw))
    con.commit()
    cursor.close()
    return 'Sucessfully Registered'

def signup_val():
    cursor = con.cursor()
    cursor.execute(""" 
    select email from signup;
    
    """)
    data = cursor.fetchall()
    con.commit()
    cursor.close()
    return data
def signin(email):
    cursor = con.cursor()
    cursor.execute(""" 
    select password from signup where email ='{email}';
    
    """.format(email = email))
    data = cursor.fetchall()[0]
    con.commit()
    cursor.close()
    return data
def name(email):
    cursor = con.cursor()
    cursor.execute(""" 
    select fullname from signup where email ='{email}'; 
    """.format(email = email))
    data = cursor.fetchall()[0]
    con.commit()
    cursor.close()
    return data
def book(route,type,date):

    cursor = con.cursor()
    cursor.execute(""" 
    select s_no,BusName,BusNum,route,type,DepTime,Date,TotalTime,Price from buses where route ='{route}' and  type = '{type}' and  Date = '{date}';
    
    """.format(route = route,type =type,date = date))
    data = cursor.fetchall()
    con.commit()
    cursor.close()
    return data
def bookbus(ID):
    cursor = con.cursor()
    cursor.execute(""" 
    select Price from buses where s_n o = {ID};
    """.format(ID = ID))
    busid = cursor.fetchall()[0]
    con.commit()
    cursor.close()
    return busid
def custidf(email):
    cursor = con.cursor()
    cursor.execute(""" 
    select s_no from signup where email = '{ID}';
    """.format(ID = email))
    global custid
    custid = cursor.fetchall()[0]
    con.commit()
    cursor.close()
    return custid

def disticket():
    cursor = con.cursor()
    cursor.execute("""
   select signup.s_no,signup.fullname,signup.mobile,signup.gender,buses.BusName,buses.BusNum,buses.route,buses.Date,buses.depTime,buses.type,buses.TotalTime from signup join buses where signup.s_no = {ID} and buses.s_no = {busid};

    """.format(ID = custid[0],busid = busid[0]))
    data =  cursor.fetchall()
    con.commit()
    cursor.close
    return data