#!/usr/bin/env python
# coding: utf-8

# Name : Ashutosh Singh Kushwaha
# Admission No : 22MT0084
# ADBMS LAB 4
# Date : 06-02-2023

# ### Establishing MySql Connection 

# In[23]:


import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Kushashu123",
    database = "adbms"
)
print(mydb)


# In[25]:


cursor = mydb.cursor(buffered = True)
cursor.execute('show tables')
for x in cursor:
    print(x)


# In[35]:


## Question 1
cursor.execute('SELECT * FROM instructor')
myresult = cursor.fetchall()
for x in myresult:
  print(x)


# In[32]:


## Question 2
cursor.execute("insert into  instructor value('10211', 'Smith', 'Biology', 66000)")


# In[34]:


## Question 3
cursor.execute("delete from instructor where id =10211")


# In[37]:


## Question 4
cursor.execute("select * from instructor where dept_name = 'History'")
myresult = cursor.fetchall()
for x in myresult:
  print(x)


# In[48]:


## Question 5
cursor.execute("select * from instructor , teaches")
myresult = cursor.fetchall()
print("Row Count ",cursor.rowcount)
for x in myresult:
  print(x)


# In[47]:


## Question 6
cursor.execute("select name from instructor a where a.id not in (select b.id from teaches b)")
myresult = cursor.fetchall()
print("Row Count ",cursor.rowcount)
for x in myresult:
  print(x)


# In[45]:


## Question 7
cursor.execute("select name from instructor where name like '%dar%'")
myresult = cursor.fetchall()
print("Row Count ",cursor.rowcount)
for x in myresult:
  print(x)


# In[46]:


## Question 8
cursor.execute("select name from instructor where salary between 90000 and 100000")
myresult = cursor.fetchall()
print("Row Count ",cursor.rowcount)
for x in myresult:
  print(x)


# In[ ]:




