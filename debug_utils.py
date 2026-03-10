import cv2


def draw_squat_debug(frame, angle, squat_count, state):
    angle_text = f"{angle:.1f}" if angle is not None else "N/A"

    cv2.putText(
        frame,
        f"Squat angle: {angle_text}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Squats: {squat_count}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Squat state: {state}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 100, 100),
        2
    )


def draw_lunge_debug(frame, angle, lunge_count, state):
    angle_text = f"{angle:.1f}" if angle is not None else "N/A"

    cv2.putText(
        frame,
        f"Lunge angle: {angle_text}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 200, 0),
        2
    )

    cv2.putText(
        frame,
        f"Lunges: {lunge_count}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Lunge state: {state}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 100, 100),
        2
    )


    import cv2


def draw_squat_debug(frame, angle, squat_count, state):
    angle_text = f"{angle:.1f}" if angle is not None else "N/A"

    cv2.putText(frame, f"Squat angle: {angle_text}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.putText(frame, f"Squats: {squat_count}", (20,70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)


def draw_curl_debug(frame, angle, curl_count, state):

    angle_text = f"{angle:.1f}" if angle is not None else "N/A"

    cv2.putText(frame, f"Curl angle: {angle_text}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,200,0), 2)

    cv2.putText(frame, f"Curls: {curl_count}", (20,70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)

    cv2.putText(frame, f"Curl state: {state}", (20,100),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,100,100), 2)