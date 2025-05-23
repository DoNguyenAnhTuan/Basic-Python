#Chèn modun thời gian
import time
import random
import os
import myNumbers
import winsound
# Hàm splash:

def splash_screen(seconds):
  print("\n")
  print(" **************************")
  print(" *                        *")
  print(" * CHIẾC NÓN KỲ DIỆU v1.0 *")
  print(" *                        *")
  print(" *                        *")
  print(" **************************")
  winsound.PlaySound('Home_Run.wav', winsound.SND_FILENAME)
  time.sleep(seconds)
  #os.system('cls')  
  
#Main Program Starts Here....
splash_screen(3)
print("------------------------------------------------------------------------")
print("\n")
name = input("What is your name?: ..... ")
print("\n")
print ("XIN CHÀO BẠN " + name.upper() + ", CHÀO MỪNG BẠN ĐẾN VỚI TRÒ CHƠI CHIẾC NÓN KỲ DIỆU")

print (" ")
#wait for 1 second
time.sleep(1)
print("\n")
print(".............................CÂU HỎi....................................")
print("\n")
print("                 TÊN CỦA HỌC VIỆN TRẺ ĐANG HỌC LÀ GÌ?                   ")
print("\n")
print(".........................................................................")


# ô chữ cần tìm:
word = "teky"
#Biến chứa ký tự người chơi đoán:
guesses = ''
# số lần được phép đoán:
turns = 10
diem =0

#kiểm tra xem biến turn có >0 không?
while turns > 0:         
    # biến đếm số lần trả lời sai
    failed = 0             
    # xét duyệt  ký tự trong ô chữ:   
    for char in word:      
    # kiểm tra:
        if char in guesses:    
        # nếu người chơi đoán đúng thì in ra ký tự đó
            print (" ________")
            print ("|        |")
            print ("    " + char.upper()+ "    ")
            print ("|        |")
            print (" ________")
            
        else:
    
            print (" ________")
            print ("|        |")
            print ("|        |" )
            print ("|        |")
            print (" ________")
            # tắng giá trị biến false
            failed+= 1  
    print("\n")   
    

    # nếu biến false =0 thì ghi ra là:
   
    if failed == 0:        
        print (" You là người chiến thắng!!!!"  )
        print (" Điểm của bạn là: ", diem)
        winsound.PlaySound('Home_Run.wav', winsound.SND_FILENAME)
        # thoát
        break              

    print
    print("NHẤN PHÍM 1 ĐỂ QUAY NÓN: ")
    t=int(input("Yes/No (1|0):..."))
    if(t==1):
                    
      print("Chiêc nón kỳ diệu đang quay ô chữ:")
      for i in range (1,17):
          time.sleep(0.2)
          winsound.PlaySound('beep.wav', winsound.SND_FILENAME)
          print("==",end=' ')
      print()
      for i in range (1,5):
          time.sleep(0.2)
          print("=.............................................=")
                
      for i in range (1,17):
                  time.sleep(0.2)
                  print("==",end=' ')      
      counter = random.randint(1,10)
      print("\n")
      print("Điểm bạn quay được là: ")
      winsound.PlaySound('Bom.wav', winsound.SND_FILENAME)
      if counter==10:
            myNumbers.ten()
      elif counter==9:
            myNumbers.nine()
      elif counter==8:
            myNumbers.eight()
      elif counter==7:
            myNumbers.seven()
      elif counter==6:
            myNumbers.six()
      elif counter==5:
            myNumbers.five()
      elif counter==4:
            myNumbers.four()
      elif counter==3:
            myNumbers.three()
      elif counter==2:
            myNumbers.two()
      elif counter==1:
            myNumbers.one()
      time.sleep(1)      
      diem+=int(counter)
      # Ký tự người chơi đoán
      guess = input("Bạn đoán ký tự gì?:") 
      guesses += guess                    
  
      # Kiểm tra:
      if guess not in word:  
   
       # giảm đi một lượt chơi
          turns -= 1        
   
      # print wrong
          print("\n")
          print ("Ô chữ không có ký tự này... ")
          winsound.PlaySound('sai.wav', winsound.SND_FILENAME)
       # how many turns are left
          print("Bạn còn:  " + str(turns) + " lượt đoán")
   
      # bạn thua cuộc nếu hết lượt
      else:
        print("......................................")
        print("XIN CHÚC MỪNG BẠN TRẢ LỜI ĐÚNG")
        winsound.PlaySound('yes.wav', winsound.SND_FILENAME)
      if (turns == 0):
          print("Bạn đã thua cuộc ")      # print "You Loose"
    else:
      print("xin cảm ơn bạn đã chơi!")
      winsound.PlaySound('Bye.wav', winsound.SND_FILENAME)
      break
    
      
       