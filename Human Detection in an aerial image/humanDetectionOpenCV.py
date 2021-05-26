import cv2 

filename = 'TopDownHumanDetection_4032x3024.jpg'
 
def main():
 
  hog = cv2.HOGDescriptor()
     
  hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
     

  image = cv2.imread(filename)

  (bounding_boxes, weights) = hog.detectMultiScale(image, 
                                                   winStride=(4, 4),
                                                   padding=(8, 8), 
                                                   scale=1)
 
  for (x, y, w, h) in bounding_boxes: 
    cv2.rectangle(image, 
                  (x, y),  
                  (x + w, y + h),  
                  (0, 0, 255), 
                   4)
                     
  size = len(filename)
  new_filename = filename[:size - 4]
  new_filename = new_filename + '_detect.jpg'
     
  cv2.imwrite(new_filename, image)
     
  #cv2.imshow("Image", image) 
     
  cv2.waitKey(0) 
     
  cv2.destroyAllWindows() 
 
main()
