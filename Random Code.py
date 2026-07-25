import cv2

def image_callback(ros_image):
    cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    bgr_image = np.array(cv_image, dtype=np.uint8)
    if image_queue.full():
        # Discard the oldest image if the queue is full(如果队列已满，丢弃最旧的图像)
        image_queue.get()
        # Put the image into the queue(将图像放入队列)
    image_queue.put(bgr_image)

def image_callback(ros_image):
    cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    bgr_image = np.array(cv_image, dtype=np.uint8)
    if image_queue.full():
        # Discard the oldest image if the queue is full(如果队列已满，丢弃最旧的图像)
        image_queue.get()
        # Put the image into the queue(将图像放入队列)
    image_queue.put(bgr_image)