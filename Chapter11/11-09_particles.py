# 11-09_particles.py
# パーティクルがランダムに動くアニメーション

import cv2
import numpy as np
import random

width, height = 640, 480
num_particles = 100

# パーティクルの位置をランダムに初期化
particles = [(random.randint(0, width), random.randint(0, height)) for _ in range(num_particles)]

image = np.ones((height, width, 3), dtype=np.uint8) * 255

while True:
    image[:] = 255

    for i, (x, y) in enumerate(particles):
        cv2.circle(image, (x, y), 3, (0, 0, 0), -1)
        # 各パーティクルをランダムな方向に少し移動させる
        particles[i] = (x + random.randint(-5, 5), y + random.randint(-5, 5))

    cv2.imshow("Particle System", image)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
