# Automatic Download/Modify Images Python Script
This script is made to automatically download from 1 to 10 images and modify them as you wish.
- [Requirements](#requirements)
- [Installation](#installation)
- [Use](#use)
- [License](#license)

### Requirements
This is a list of the libraries used in this code:
- certifi==2024.2.2
- charset-normalizer==3.3.2
- idna==3.7
- pillow==10.3.0
- requests==2.32.2
- urllib3==2.2.1

### Installation
Below is the process installation for each package and the Python script, for this you must have already installed git [Click here to install git](https://git-scm.com/downloads) and Python [Click here to install Python](https://www.python.org/downloads/).
|Steps|Description|
|-|-|
Step 1|Open your code editor and open up a new terminal
Step 2|Install image editor library (Pillow), therefore, copy and paste the below command:<br>```pip install pillow```
Step 3|Install API handler (Requests), therefore, copy and paste the below command:<br>```pip install pillow```
Step 4|Pull the Python Script into your folder, please copy and paste this command:<br>```git clone https://github.com/luisca12/Python-2-UCR---Second-Project.git```

NOTE: If step 4 fails, please check that you have Git installed.

### Use
Once the Python script is loaded into your code editor program you will notice the following Python files:
- functions.py
- httpRequests.py
- imageModifications.py
- log.py
- main.py
- strings.py

To run the program you will need to go to main.py and run it from there.
#### Instructions to use it
1. You will be prompted to the following menu where you have to first choose option #1 to choose the number of images to download.
```
        --------------------------------------------------
          Welcome to the automatic modify images program
        --------------------------------------------------
  --------------------------------------------------------------
                Menu - Please choose an option
                  Only numbers are accepted
  --------------------------------------------------------------
  >             Paso #1. Escoger la cantidad de imagenes       <
  >             Paso #2. Modificar las imagenes                <
  >             Paso #3. Ingresar el correo destinatario       <
  >             Paso #4. Salir                                 <
  --------------------------------------------------------------

Please choose a number from 1 to 4:
```
2. Once you have chosen the number of images to download, choose option number 2 to modify each individual image.
```
  -------------------------------------------------------------- 
                Menu - Please choose an option
                  Only numbers are accepted
  -------------------------------------------------------------- 
  >             Paso #1. Escoger la cantidad de imagenes       <
  >             Paso #2. Modificar las imagenes                <
  >             Paso #3. Ingresar el correo destinatario       <
  >             Paso #4. Salir                                 <
  --------------------------------------------------------------

Please choose a number from 1 to 4: 2
Do you want to modify the image number 1? (y/n):y
Do you want to make the image black and white? (y/n):y
Do you want to transpose the image? (y/n):y
Do you want to blur the image? (y/n):y
Do you want to rotate 90 degress the image? (y/n):y
```
3. Once you have modified all the images, please choose option number 3 to input the destination email to send the final images.
```
  --------------------------------------------------------------
                Menu - Please choose an option
                  Only numbers are accepted
  --------------------------------------------------------------
  >             Paso #1. Escoger la cantidad de imagenes       <
  >             Paso #2. Modificar las imagenes                <
  >             Paso #3. Ingresar el correo destinatario       <
  >             Paso #4. Salir                                 <
  --------------------------------------------------------------

Please choose a number from 1 to 4: 3
Please enter your email:example@gmail.com
```
4. Please repeat this process to download/modify more images, otherwise, please choose option 4 to exit the program.

### License
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
