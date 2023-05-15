"""
Search for transitions frames between gameplay/non-gameplay
"""
from classify_frame import classify_frame

def get_transition_frames(frames: list[str], min_transition: int = 16) -> list[int]:
    """
    Returns a list of transition frames
    frames: ordered list of file paths to frames
    min_transition: minimum number of frames between transitions
    """
    transition_frames = []
    last_class = classify_frame(frames[0])

    for i in range(min_transition, len(frames), min_transition):
        current_class = classify_frame(frames[i])
        if current_class != last_class:
            # there's a change in classification, binary search the exact transition frame
            left = i - min_transition
            right = i
            while left < right:
                mid = (left + right) // 2
                mid_class = classify_frame(frames[mid])
                if mid_class == last_class:
                    # transition is in the right half
                    left = mid + 1
                else:
                    # transition is in the left half
                    right = mid
            # add the transition frame to the result list
            transition_frames.append(left)
            last_class = current_class

    return transition_frames
