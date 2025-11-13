Driver Drowsiness Detection — Installation & Run Guide
1. Libraries / Tools Used
- numpy
- opencv-python
- dlib
- imutils
- cmake
- scipy (optional)
- Visual C++ Build Tools (if compiling dlib)
  
2. Create Virtual Environment
Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1

3. Install Required Packages (Run One-by-One)
pip install --upgrade pip
pip install numpy
pip install opencv-python
pip install imutils
pip install cmake
Install dlib (prebuilt wheel for Python 3.13 x64):
pip install "https://github.com/omwaman1/dlib/releases/download/dlib/dlib-19.24.99-cp313-cp313-win_a
md64.whl"
Optional:
pip install scipy
pip install face_recognition_models

4. Download Landmark Model
Download: shape_predictor_68_face_landmarks.dat.bz2
Extract it to get: shape_predictor_68_face_landmarks.dat
Place the .dat file in the same folder as Driver_Drowsiness.py or update the full path in the script.

5. Configure Script (if needed)
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
OR
predictor = dlib.shape_predictor(r"D:\path\to\shape_predictor_68_face_landmarks.dat")

6. Run the Program
python Driver_Drowsiness.py

7. Calibration Tips
Open eyes ratio ~0.35–0.45
Closed eyes ratio ~0.22–0.30
Adjust thresholds in script if needed.

8. Troubleshooting
- Ensure .dat file exists
- Verify dlib installation
- Close other webcam apps if camera not detected
- Use prebuilt wheel if dlib fails to compile
