import cv2

def main():
    running = True
    while running:
        try:
            image = image_queue.get(block=True, timeout=1)
        except queue.Empty:
            if not running:
                break
            else:
                continue
        image = run(image)
        cv2.imshow('image', image)
        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:  # Press q or esc to exit(按q或者esc退出)
            break

    cv2.destroyAllWindows()
    rclpy.shutdown()

def image_callback(ros_image):
    cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    bgr_image = np.array(cv_image, dtype=np.uint8)
    if image_queue.full():
        # Discard the oldest image if the queue is full(如果队列已满，丢弃最旧的图像)
        image_queue.get()
        # Put the image into the queue(将图像放入队列)
    image_queue.put(bgr_image)