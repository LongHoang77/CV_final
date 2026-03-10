import argparse
import cv2
from ultralytics import YOLO

from angle_utils import detect_squat, detect_bicep_curl, update_bicep_counter
from debug_utils import draw_squat_debug, draw_curl_debug


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        default="squat",
        choices=["squat", "curl"],
        help="exercise mode"
    )

    parser.add_argument(
        "--source",
        default="0",
        help="webcam or video"
    )

    return parser.parse_args()


def main():

    args = parse_args()

    model = YOLO("yolov8n-pose.pt")

    source = int(args.source) if args.source.isdigit() else args.source
    cap = cv2.VideoCapture(source)

    squat_count = 0
    squat_frames = 0
    is_squatting = False

    curl_count = 0
    curl_state = "down"

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)

        annotated = results[0].plot() if results else frame.copy()

        if results and results[0].keypoints is not None:

            kpts = results[0].keypoints.xy.cpu().numpy()
            conf = results[0].keypoints.conf.cpu().numpy()

            if len(kpts) > 0:

                k = kpts[0]
                c = conf[0]

                if args.mode == "squat":

                    squat, angle = detect_squat(k, c)

                    if squat:
                        squat_frames += 1
                        is_squatting = True
                    else:
                        if is_squatting and squat_frames > 5:
                            squat_count += 1
                        squat_frames = 0
                        is_squatting = False

                    draw_squat_debug(annotated, angle, squat_count, "down" if squat else "up")

                elif args.mode == "curl":

                    is_up, is_down, angle = detect_bicep_curl(k, c)

                    curl_state, curl_count = update_bicep_counter(
                        is_up,
                        is_down,
                        curl_state,
                        curl_count
                    )

                    draw_curl_debug(annotated, angle, curl_count, curl_state)

        cv2.imshow("Fitness AI", annotated)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()