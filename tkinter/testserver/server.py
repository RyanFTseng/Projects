 import os
 from threading import Thread
 from _thread import*
+import threading
 
 ip='0.0.0.0'
-port=19991
+port=180
 s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 s.bind((ip,port))
 s.listen(5)
             #message=message.encode()
             #if message=='exit':
             #    break
-            print(len(c))
+            print('Multithreaded Python server: Waiting for connections from TCP listens...')
+            #print('broadcast or chat?')
+            #if input()=='broadcast':
+            #    t.send()
+            #print(len(c))
             for a in c:
                 a.send(data)
+                time.sleep(0.01)
             #conn.send(message)
-s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
-
-while 1:
-    s.listen(4)
-    print('Multithreaded Python server: Waiting for connections from TCP listens...')
+    def send(self):
+        message=input('Multithreaded Python server:Enter response from Server/Enter exit:')
+        message=message.encode()
+        print(c)
+        for f in c:
+            f.send(message)
+def t():
     (conn,(ip,port))=s.accept()
-    c.append(conn)
     t=ClientThread('0.0.0.0',2004,conn)
-    t.start()
+    c.append(conn)
+    #t.start()
     #t.run()
-    threads.append(t)
+
+
+s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
+
+while 1:
+    try:
+        s.listen(4)
+        print(len(c))
+        t1=threading.Thread(target=t)
+        t1.start()
+        #t1.run()
+        print('broadcast or chat?')
+        #bc = input()
+        print(len(c))
+        threads.append(t)
+    except:
+        for connection in c:
+            connection.close()
     
 for i in threads:
     i.join()
