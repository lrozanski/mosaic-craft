import base64

import cv2
import numpy as np


def read_image(file_path):
    image = cv2.imread(file_path)
    return image


def posterize_image(image, levels):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    luma_ramp = np.linspace(0, 255, levels + 1)
    quantiz = np.int64(np.linspace(0, 255, levels))

    indices = np.digitize(gray_image, luma_ramp) - 1
    indices = np.clip(indices, 0, levels - 1)
    palette = quantiz[indices]
    img_array = np.array([palette, palette, palette]).transpose(1, 2, 0)

    posterized_image = np.array(img_array, dtype=np.uint8)
    return posterized_image


def cluster_colors(image, num_clusters):
    h, w, _ = image.shape
    reshaped_image = np.float32(image.reshape(-1, 3))

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(reshaped_image, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    clustered_image = centers[labels.flatten()]
    clustered_image = np.uint8(clustered_image.reshape(h, w, 3))

    return clustered_image


def generate_contours(image, min_area_threshold=100):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    unique_colors = np.unique(gray_image)

    contour_image = np.ones_like(gray_image) * 255
    all_filtered_contours = []

    for color in unique_colors:
        mask = (gray_image == color)
        mask = mask.astype(np.uint8) * 255
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > min_area_threshold]
        all_filtered_contours.extend(filtered_contours)
        cv2.drawContours(contour_image, filtered_contours, -1, 0, 2)

    return contour_image, all_filtered_contours


def put_labels(image, posterized_image, filtered_contours, font_scale, font_thickness):
    contour_labels = {}
    for i, contour in enumerate(filtered_contours):
        color = cv2.mean(posterized_image, mask=cv2.drawContours(np.zeros_like(image), [contour], -1, 255, -1))[0:3]
        color_tuple = tuple(np.round(color).astype(int))

        if color_tuple not in contour_labels:
            contour_labels[color_tuple] = i + 1

        label = contour_labels[color_tuple]
        x, y, w, h = cv2.boundingRect(contour)
        text_position = (x + 5, y + h // 2)
        cv2.putText(image, str(label), text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), font_thickness)

    return image


def process_image(base64_image: str, output_path: str, posterize_levels: int, num_clusters: int, blur_ksize: int,
                  min_area_threshold: int, font_scale: float, font_thickness: float,
                  contour_color: (int, int, int, int) = (0, 0, 0, 255),
                  contour_thickness: int = 1):
    # image = cv2.imread(input_path)
    image_data = base64.b64decode(base64_image.split(',')[1])
    image_np = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    posterized_image = posterize_image(image, posterize_levels)
    blurred_image = cv2.medianBlur(posterized_image, blur_ksize)
    clustered_image = cluster_colors(blurred_image, num_clusters)
    contours_image, filtered_contours = generate_contours(clustered_image, min_area_threshold)

    # Create a new blank image with the same dimensions as the input image and an alpha channel
    height, width, _ = image.shape
    result = np.zeros((height, width, 4), dtype=np.uint8)

    # Draw the contours on the result image
    cv2.drawContours(result, filtered_contours, -1, contour_color, contour_thickness)

    # # Draw the index numbers on the result image
    # for i, c in enumerate(filtered_contours):
    #     # Calculate the centroid of the contour
    #     M = cv2.moments(c)
    #     cx = int(M["m10"] / M["m00"])
    #     cy = int(M["m01"] / M["m00"])
    #
    #     # Draw the index number at the centroid
    #     cv2.putText(result, str(i), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0, 255), font_thickness)

    # Save the result image in a format that supports transparency, like PNG
    cv2.imwrite(output_path, result)

    return image_to_base64(result)


# process_image("input_image.png", "output_image.png", posterize_levels=6, num_clusters=5, blur_ksize=3,
#               min_area_threshold=3000, font_scale=0.7, font_thickness=2)


def image_to_base64(image, image_format=".png"):
    # Determine the appropriate MIME type based on the format
    mime_type = "image/png" if image_format == ".png" else "image/jpeg"

    # Save the image to a buffer
    success, buffer = cv2.imencode(image_format, image)

    if not success:
        raise ValueError("Failed to encode image")

    # Convert the buffer to bytes
    image_bytes = buffer.tobytes()

    # Encode the bytes using base64
    base64_str = base64.b64encode(image_bytes).decode("utf-8")

    # Create the data URL by combining the MIME type and the base64 string
    data_url = f"data:{mime_type};base64,{base64_str}"

    return data_url
