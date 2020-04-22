import requests
import threading
import datetime
import time


# Variable Settings
#####################
global STATUS_200   #
global STATUS_ERROR #
                    #
USER_ID = "1352408" #
STATUS_200 = 0      #
STATUS_ERROR = 0    #
#####################


# Main Process in sending a single requests
##################################################################################################################################
def start_botting():                                                                                                             #
  global STATUS_200                                                                                                              #
  global STATUS_ERROR                                                                                                            #
                                                                                                                                 #
  while True:                                                                                                                    #
    with requests.Session() as s:                                                                                                #
      try:                                                                                                                       #
        r = s.get("https://miningph.com/application/views/user/getHashes.php?xVal=1&id={id}&yVal=10000".format(id=USER_ID))      #
        response = r.content.decode('utf-8')                                                                                     #
                                                                                                                                 #
        if response == '{"hash":null,"total":0,"xVal":"1"}':                                                                     #
          STATUS_200 += 1                                                                                                        #
        else:                                                                                                                    #               
          STATUS_ERROR += 1                                                                                                      #
      except Exception as e:                                                                                                     #
        STATUS_ERROR += 1                                                                                                        #
##################################################################################################################################



# THREADING starts when all requirements are met
###################################################################
class ThreadMultipleRequests(threading.Thread):                   #
  def run(self):                                                  #
    while True:                                                   #
      start_botting()                                             #
###################################################################



# Single thread that prints out information.
##############################################################################################################
class Informer(threading.Thread):                                                                            #
  def run(self):                                                                                             #
    started_time = datetime.datetime.now()                                                                   #
                                                                                                             #
    while True:                                                                                              #
      alive_threads = threading.active_count() - 3                                                           #
      previous_ok200 = STATUS_200                                                                            #
      time.sleep(1)                                                                                          #
      current_ok200 = STATUS_200 - previous_ok200                                                            #
      current_time = datetime.datetime.now() - started_time                                                  #
      pd = "Alive Threads: {a}  Time Elapsed: {t}  STATUS_200: {s}  STATUS_200/s: {sp}  Errors: {e}".format( #
        t=current_time,s=STATUS_200,sp=current_ok200,e=STATUS_ERROR,a=alive_threads)                         #
      print(pd, end='\r')                                                                                    #      
##############################################################################################################



# Performs the amount of THREADING supplied by the user
###################################################################
def CallMultiThreader(uid, reqs):                                 #
  global USER_ID                                                  #
  USER_ID = uid                                                   #
                                                                  #
  for _ in range(reqs):                                           #                            
    multireq = ThreadMultipleRequests()                           # 
    multireq.start()                                              #
  print("Started THREADING with {} threads.".format(reqs))        #
###################################################################






def main():
  CallMultiThreader(1352408, 123)
  messprint = Informer()
  messprint.start()




  
if __name__ == "__main__":
  main()
