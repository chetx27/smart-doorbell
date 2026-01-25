import cv2
import time
from cvzone.FaceDetectionModule import FaceDetector

def main():
    cap = cv2.VideoCapture(0)
    detector = FaceDetector(minDetectionCon=0.6)
    
    start_time = None
    alert_limit = 5 

    while True:
        success, img = cap.read()
        if not success:
            break

        img, bboxs = detector.findFaces(img, draw=False)

        if bboxs:
            if start_time is None:
                start_time = time.time()
            
            dwell_time = int(time.time() - start_time)

            for bbox in bboxs:
                x, y, w, h = bbox['bbox']
                
                # Boundary safety check
                x, y = max(0, x), max(0, y)
                
                face_roi = img[y:y+h, x:x+w]
                if face_roi.size > 0:
                    blur = cv2.GaussianBlur(face_roi, (99, 99), 30)
                    img[y:y+h, x:x+w] = blur

                color = (0, 255, 0)
                label = f"Visitor: {dwell_time}s"

                if dwell_time > alert_limit:
                    color = (0, 0, 255)
                    label = f"LOITERING ALERT: {dwell_time}s"
                
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        else:
            start_time = None

        cv2.imshow("Doorbell Feed", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()