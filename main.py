# Copyright 2018 Stanly Moses (stanlimoses@gmail.com)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===================================================================================
# -*- coding: utf-8 -*-


import cv2
import tensorflow as tf
import cv2 as cv
import config as cfg
import argparse


def main(arg):
    args = vars(arg.parse_args())

    cam = cv2.VideoCapture(0)

    detection_graph = tf.GraphDef()

    with tf.Session() as persisted_sess:
        print("Loading Graph")
        with tf.gfile.FastGFile(args["model"], 'rb') as f:
            detection_graph.ParseFromString(f.read())
            persisted_sess.graph.as_default()
            tf.import_graph_def(detection_graph, name='')
    print("Graph has been loaded")
    with tf.Session() as sess:

        while True:
            ret_val, frame = cam.read()
            points = []
            image = sess.graph.get_tensor_by_name("image:0")
            predict_op = sess.graph.get_tensor_by_name('Convolutional_Pose_Machine/stage_5_out:0')
            img = frame
            frame = cv.resize(frame, (192, 192))
            prep_img = frame.reshape([1, 192, 192, 3])
            output_img = sess.run(predict_op, feed_dict={
                image: prep_img
            })

            frameWidth = img.shape[1]
            frameHeight = img.shape[0]

            for i in range(0, output_img.shape[3]):
                heatMap = output_img[0, :, :, i]
                _, conf, _, point = cv.minMaxLoc(heatMap)

                x = (frameWidth * point[0]) / 96
                y = (frameHeight * point[1]) / 96
                points.append((int(x), int(y)) if conf > args["threshold"] else None)

            for i in range(len(cfg.POSE_PAIRS)):
                pair = cfg.POSE_PAIRS[i]
                partFrom = pair[0]
                partTo = pair[1]

                idFrom = cfg.BODY_PARTS[partFrom]
                idTo = cfg.BODY_PARTS[partTo]
                if points[idFrom] and points[idTo]:
                    cv.line(img, points[idFrom], points[idTo], cfg.COLORS[i], 3)
                    cv.ellipse(img, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
                    cv.ellipse(img, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

            cv2.imshow('Pose', img)
            if cv2.waitKey(1) == 27:
                break
        cv2.destroyAllWindows()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-m", "--model", required=False, default="model/mod.pb",
                    help="Name of the model")
    ap.add_argument("-t", "--threshold", type=int, required=False, default=0.2,
                    help="Confidence rate")
    main(ap)
