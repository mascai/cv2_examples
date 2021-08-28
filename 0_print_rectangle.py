import cv2


def print_rectangle(
    image_path,
    start_point = (110, 110),
    end_point = (220, 220),
    color = (255, 0, 0),
    thickness = 25):

    image = cv2.imread(image_path) 
    image = cv2.rectangle(image, start_point, end_point, color, thickness) 
    if cv2.imwrite(image_path, image):
        print("Successfully printed rectangle")
    else:
        print("Error")

print_rectangle("image.png")
