import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
"sun",
(20,250),
cv2.FONT_HERSHEY_COMPLEX,
0.9,
(255,255,255)
)

cv2.putText(img,
"mercury",
(120,250),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255)
)

cv2.putText(img,
"venus",
(200,250),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255)
)

cv2.putText(img,
"earth",
(295,260),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255)
)

cv2.putText(img,
"mars",
(390,250),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255)
)

cv2.putText(img,
"jupiter",
(500,350),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255)
)

cv2.putText(img,
"saturn",
(780,290),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255)
)

cv2.putText(img,
"uranus",
(985,290),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255)
)

cv2.putText(img,
"neptune",
(1130,290),
cv2.FONT_HERSHEY_COMPLEX,
0.3,
(255,255,255)
)

cv2.imshow("output",img)
cv2.waitKey(0)
