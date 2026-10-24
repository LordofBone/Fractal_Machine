### Install dependencies
Requires python3

Install the dependencies with pip:

```pip install -r requirements.txt```

If you are running on Windows you will need to follow the instructions [here](https://ghostscript.com/releases/gsdnld.html) to install Ghostscript.

### Setting up the API
1. Go to [OpenAI](https://openai.com/api/) and create an account, generate and grab the API key from Account > API Keys.
2. Copy the `.env.template` file in the project root and rename the copy to `.env`
3. Replace `your_api_key_here` with your actual API key in the `.env` file

### Running the code
```python3 main.py```

### How it works
You can click the different types of shapes, and they will be drawn on screen, the background colour can be changed
they can be drawn in real time, or they can be drawn in the background faster.

There are also options for random positions of the shapes and whether to queue them up or not.

Once the image has been made, the ML Generation button can be pressed which will then send the image off to DALL-E
which will generate a different interpretation of the image based on the input image.