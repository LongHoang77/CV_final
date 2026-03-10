import numpy as np


def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    angle = np.degrees(np.arccos(np.clip(cosine, -1.0, 1.0)))
    return angle


def detect_squat(kpts, conf, threshold=140, conf_thres=0.3):
    left_ok = conf[11] >= conf_thres and conf[13] >= conf_thres and conf[15] >= conf_thres
    right_ok = conf[12] >= conf_thres and conf[14] >= conf_thres and conf[16] >= conf_thres

    if not left_ok and not right_ok:
        return False, None

    angles = []

    if left_ok:
        angles.append(calculate_angle(kpts[11], kpts[13], kpts[15]))
    if right_ok:
        angles.append(calculate_angle(kpts[12], kpts[14], kpts[16]))

    angle = min(angles)
    return angle < threshold, angle


def detect_bicep_curl(kpts, conf, up_threshold=60, down_threshold=150, conf_thres=0.3):
    """
    Bicep curl detection using elbow angle.

    COCO keypoints:
    5  left shoulder
    6  right shoulder
    7  left elbow
    8  right elbow
    9  left wrist
    10 right wrist
    """

    left_ok = conf[5] >= conf_thres and conf[7] >= conf_thres and conf[9] >= conf_thres
    right_ok = conf[6] >= conf_thres and conf[8] >= conf_thres and conf[10] >= conf_thres

    if not left_ok and not right_ok:
        return False, False, None

    angles = []

    if left_ok:
        angles.append(calculate_angle(kpts[5], kpts[7], kpts[9]))

    if right_ok:
        angles.append(calculate_angle(kpts[6], kpts[8], kpts[10]))

    elbow_angle = min(angles)

    is_up = elbow_angle <= up_threshold
    is_down = elbow_angle >= down_threshold

    return is_up, is_down, elbow_angle


def update_bicep_counter(is_up, is_down, state, rep_count):
    """
    down -> up -> down = 1 rep
    """

    if state == "down":
        if is_up:
            state = "up"

    elif state == "up":
        if is_down:
            rep_count += 1
            state = "down"

    return state, rep_count