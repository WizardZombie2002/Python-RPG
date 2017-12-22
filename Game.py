from time import *
camera_1 = False
camera_2 = False
camera_3 = True
camera_4 = True
camera_5 = True
camera_6 = True
camera_7 = True
camera_8 = True
camera_10 = True
battery_level = int(100)
time = int(300)

while battery_level >= 1:
        battery_level = battery_level - 1
        time = time - 1
        sleep(2)
        print('Battery: ')
        print(battery_level)
        print('Time: ')
        print(time)
        print('''
--------
|cam 1 |
|      |________
--------       |
  |           ---------           ---------
  |    -------|cam 2  |-----------|cam 3  |---------
  -----|      |       |   |       |       |        |
       |      ---------   |       ---------        |
       |                  |                        |
    --------              |                        |
    |cam 4 |              |                      --------
    |      |              |                      |cam 5 |
    --------          ---------                  |      |
       |              |cam 8  |                  --------
       |              |       | -------------------|
       |              ---------                    |
       |                |                        --------
     --------           |                        |cam 7 |
     |cam 6 |           |                        |      |
     |      |           |                        --------
     --------           |                          |
       |                |                   ---------
       |----------------|-------------------|cam 9  |
                        |                   |       |
                        |                   ---------
                        |
                    ---------
                    |cam 10 |
                    |  You  |
                    ---------
''')

if battery_level <= 0:
        print('''
        ________
               |
  |                               
  |    -------         -----------         ---------
  -----|                  |                        |
       |                  |                        |
       |                  |                        |
                          |                        |
                          |                      
                          |                    
                                         
       |                                         
       |                        -------------------|
       |                                           |
       |                |                        
                        |                        
                        |                       
                        |                     
                        |                          |
       |                |                   
       |----------------|-------------------
                        |                   
                        |                   
                        |
                     



''')
