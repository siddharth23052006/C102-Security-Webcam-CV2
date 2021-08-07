import time
import cv2
import random
import dropbox

start_time = time.time()

def take_snapshot():
  number = random.randint(0, 100)
  vid = cv2.VideoCapture(0)
  result = True

  while result:
    ret, frame = vid.read()
    img_name = "img" + str(number) + ".jpg"
    cv2.imwrite(img_name, frame)
    result = False

  vid.release()
  cv2.destroyAllWindows()  
  print("Snapshot taken")
  return img_name

def upload_file(img_name):
  access_token = 'MCkARkfOUaMAAAAAAAAAAfJFax80hVeYO2Wleuak9yi-dfuBYnfMrzX82QN8YXA_'
  file = img_name
  file_from = file
  file_to = "/SecurityPictures/" + (img_name)
  dbx = dropbox.Dropbox(access_token)

  with open(file_from, 'rb') as f:
    dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)

    print("File uploaded.")

def main():
  while True:
    if time.time() - start_time > 5:
      name = take_snapshot()
      upload_file(name)

main()