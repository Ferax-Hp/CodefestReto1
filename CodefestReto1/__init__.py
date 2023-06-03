from keras.models import load_model
import cv2
import numpy as np
from csv import writer

keras_model_h5 = "CodefestReto1/keras_model.h5"
labels_txt = "CodefestReto1/labels.txt"

def detect_objects_in_video(video_path, output_path):
    columns = ["ID", "Objetc Type", "Time", "Coordinates"]
    datos = ["", "", "", "", ""]

    anterior = 0
    print("Cargando archivos...", end="")
    with open(output_path, 'a', newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(columns)


    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(keras_model_h5, compile=False)

    # Load the labels
    class_names = open(labels_txt, "r").readlines()

    print("\rLeyendo el video.......")
    # CAMERA can be 0 or 1 based on default camera of your computer
    data = cv2.VideoCapture(video_path)
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = int(data.get(cv2.CAP_PROP_FPS))
    second = frames / fps

    count = 0
    video_time = second

    while True:
        ret, image = data.read()
        # original = image.copy()

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        if index != 1:
            Horas = int(video_time / 3600)
            Minutos = int(video_time / 60)
            datos = [str(index), class_name[2:].replace("\n", ""), str(Horas) + ":" + str(Minutos) + ":" + str(second),
                     "xxxxx"]
            if anterior != index:
                with open(output_path, 'a', newline='') as csv_file:
                    csv_writer = writer(csv_file)
                    csv_writer.writerow(datos)

        anterior = index

        keyboard_input = cv2.waitKey(1)
        count += 1
        video_time += second
        if keyboard_input == 27:
            break

    data.release()
    cv2.destroyAllWindows()