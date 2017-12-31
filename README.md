# MNIST


## Prerequisites
To run the files, you must have TensorFlow installed on your system, look at [tensorflow.org/install](https://www.tensorflow.org/install/) for more info. Additionally, you must have Python 3.0 or later, go to [python.org/downloads](https://www.python.org/downloads/) for more info. 


## Running the Program
After installing TensorFlow, enable  it in terminal. On MacOS, type ``` source activate tensorflow``` into the terminal, and on Windows type ```activate tensorflow``` into CMD. Afterwards, move into the directory where the MNIST downloaded file is located. To run the prediction, type in ```python prediction.py "FILENAME.FILETYPE"``` where ```FILENAME.FILETYPE``` is the name of the file followed by its extension (ie ```numberOne.jpg```). The resulting value will be the predicted value that was displayed in the image. The prediction program *mostly* provides the correct values for the images in the ```test-images``` folder.


## Creating the Model
If you want to recreate the model, run the ```MNIST.py``` file, changing the value on ```line 82``` to however many trials you would like. On a system with a GTX 1080, running this trial with 20,000 iterations takes about 3 minutes, while it takes around 8 hours on a system with only a dual core processor, so don't run this if you don't have a decent GPU. 
