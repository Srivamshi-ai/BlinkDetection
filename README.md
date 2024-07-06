# Drowsiness Detection System

This project is a Drowsiness Detection System that uses computer vision techniques to detect and monitor drowsiness based on eye blinking patterns. The system captures video from a webcam, detects faces, and analyzes eye landmarks to calculate the blinking ratio. Based on the blinking ratio, the system determines whether the user is drowsy, sleeping, or active and displays appropriate alerts on the screen.

## Features

- **Real-time Face Detection**: Detects faces in the video feed using the dlib library.
- **Eye Landmark Detection**: Identifies key landmarks around the eyes to calculate the blinking ratio.
- **Blinking Ratio Calculation**: Calculates the ratio of horizontal to vertical eye dimensions to determine blinking patterns.
- **Drowsiness Detection**: Categorizes the user state as "BLINKING", "SLEEPING", or "ACTIVE" based on the blinking ratio.
- **Visual Alerts**: Displays text alerts on the screen to indicate the user's state.

## Installation

### Prerequisites

- Python 3.x
- Webcam

### Required Libraries

use requirements.txt 
`pip install -r requirements.txt`

You can install the required libraries using pip:

```bash
pip install opencv-python
pip install numpy
pip install dlib
pip install imutils

