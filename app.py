  import sqlite3                                                                                                                                                                       
  import subprocess                                                                                                                                                                    
  import os                                                                                                                                                                            
                  
  def get_user(username):                                                                                                                                                              
      conn = sqlite3.connect("db.sqlite3")
      cursor = conn.cursor()                                                                                                                                                           
      query = "SELECT * FROM users WHERE username = '" + username + "'"
      cursor.execute(query)                                                                                                                                                            
      return cursor.fetchall()
                                                                                                                                                                                       
  def run_command(user_input):                                                                                                                                                         
      os.system("ls " + user_input)
                                                                                                                                                                                       
  def ping(host):                                                                                                                                                                      
      subprocess.call("ping -c 1 " + host, shell=True)
                                                                                                                                                                                       
  SECRET_KEY = "hardcoded-secret-key-123"                                                                                                                                              
  EOF

