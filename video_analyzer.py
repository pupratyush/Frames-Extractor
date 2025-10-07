import cv2
import os

def extract_video_frames(video_path, output_folder):
    """
    Counts the total number of frames in a video and saves each frame as an image.

    Args:
        video_path (str): The full path to the input video file.
        output_folder (str): The path to the directory where frames will be saved.
    """
    # --- 1. Input and Output Setup ---

    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at '{video_path}'")
        return

    # Create the output directory if it doesn't exist [1]
    os.makedirs(output_folder, exist_ok=True)
    print(f"Frames will be saved to: '{output_folder}'")

    # --- 2. Video Processing ---

    # Open the video file for reading [2]
    video_capture = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully [3]
    if not video_capture.isOpened():
        print(f"Error: Could not open video file '{video_path}'.")
        return

    frame_count = 0
    print("Starting frame extraction...")

    # Loop through the video frame by frame
    while True:
        # Read one frame from the video. 'success' is a boolean that is
        # False when the end of the video is reached. [4]
        success, frame = video_capture.read()

        # If a frame was not read successfully, we've reached the end of the video
        if not success:
            break

        # Construct the output filename with zero-padding for proper sorting
        # e.g., "frame_00001.jpg"
        filename = f"frame_{frame_count:05d}.jpg"
        output_path = os.path.join(output_folder, filename)

        # Save the current frame as a JPG image [1]
        cv2.imwrite(output_path, frame)

        # Increment the frame counter
        frame_count += 1

    # --- 3. Cleanup and Final Report ---

    # Release the video capture object to free up resources [3, 1]
    video_capture.release()

    print("\n--- Process Complete ---")
    print(f"Successfully extracted and saved {frame_count} frames.")

# --- Main execution block ---
if __name__ == "__main__":
    # The path to your video file
    input_video_path = r""

    # The folder where you want to save the extracted frames
    output_frames_folder = r""

    # Run the extraction function
    extract_video_frames(input_video_path, output_frames_folder)
