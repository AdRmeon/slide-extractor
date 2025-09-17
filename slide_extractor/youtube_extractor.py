import pafy
import cv2

url = "https://www.youtube.com/watch?v=ypeRrYF087g"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

capture = cv2.VideoCapture(best.url)
i =0
while True:
    grabbed, frame = capture.read()
    i+=1
    if i==1000:
        print("\nPlease check the preview image for the area you want to be compared")
        cv2.imshow('image', frame)
        cv2.waitKey(0)
        break