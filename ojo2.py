
import cv2
import mediapipe as mp
import serial

com = serial.Serial('COM5', 9600, timeout=2)

d = 'd'
i = 'i'
p = 'p'
u = 'u'
b = 'b'
marca = 0
xmo = 0
ymo = 0

cap = cv2.VideoCapture(0)

detector = mp.solutions.face_detection
dibujo = mp.solutions.drawing_utils


def mouse(evento, xm, ym, flags, params):
    global xmo, ymo, marca
    if evento == cv2.EVENT_LBUTTONDOWN:
        marca = 1
        xmo = xm
        ymo = ym
        print("Click:", xmo, ymo)

cv2.namedWindow('cam')
cv2.setMouseCallback('cam', mouse)

with detector.FaceDetection(min_detection_confidence=0.75, model_selection=0) as rostros:
    while True:

        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultados = rostros.process(rgb)

        al, an, c = frame.shape
        centrox = an // 2
        centroy = al // 2

        if resultados.detections is not None:
            for id, punto in enumerate(resultados.detections):

                dibujo.draw_detection(frame, punto)

                x = int(punto.location_data.relative_bounding_box.xmin * an)
                y = int(punto.location_data.relative_bounding_box.ymin * al)
                w = int(punto.location_data.relative_bounding_box.width * an)
                h = int(punto.location_data.relative_bounding_box.height * al)

                xf = x + w
                yf = y + h

                cx = x + w // 2
                cy = y + h // 2

                cv2.circle(frame, (cx, cy), 3, (0, 0, 255), -1)
                cv2.line(frame, (cx, 0), (cx, al), (0, 0, 255), 2)

                # si hubo click
                if marca == 1:

                    if x < xmo < xf and y < ymo < yf:

                        cv2.circle(frame, (xmo, ymo), 20, (0,255,0), 2)
                        cv2.rectangle(frame, (x, y), (xf, yf), (255,255,0), 3)
                        cv2.putText(frame, str(id), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

                        xmo, ymo = cx, cy

                        # ---- MOVIMIENTOS ----

                        if xmo < centrox - 50:
                            print("izquierda")
                            com.write(d.encode('ascii'))

                        elif xmo > centrox + 50:
                            print("derecha")
                            com.write(i.encode('ascii'))

                        elif ymo < centroy - 50:
                            print("arriba")
                            com.write(b.encode('ascii'))

                        elif ymo > centroy + 50:
                            print("abajo")
                            com.write(u.encode('ascii'))

                        elif abs(xmo - centrox) < 40 and abs(ymo - centroy) < 40:
                            print("centro")
                            com.write(p.encode('ascii'))

        cv2.imshow('cam', frame)

        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()