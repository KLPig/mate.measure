# Measuring length of the *shipwreck*

## Requirements
- `Measure.exe` window executable file
- A photo of shipwreck
  + The **camera**(i.e. ROV) should be distant from the *shipwreck* underwater
  + The photo can be taken by the ROV camera
  + Save as common image format (e.g. JPEG, PNG)

## Steps
1. Open `Measure.exe`
2. Select the photo of shipwreck
3. Click points on the window according to the instructions (e.g.give the coordinates of the measured pipe, 30cm and the unknown pipe with variable length)
4. The results will be displayed on window

## Alternative solution
> If `measure.exe` cannot be executed, use these steps

- Download `python3.x`
- Install `python` with `Add python to PATH` enabled
- Open `command prompt`
- Get the source code `main.py`
- Install the required packages by
```commandline
pip install pygame
```
- Run the code by
```commandline
python main.py
```
Where main.py is substituted with the name and the absolute path of the source code file.