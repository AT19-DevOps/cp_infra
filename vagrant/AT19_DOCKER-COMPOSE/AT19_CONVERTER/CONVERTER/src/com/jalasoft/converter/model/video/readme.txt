Video Converter Service v.1.0
------------------------------------------------

1. Description

    - Converts video (any format) to sequence of images (any format).
    - Converts video (any format) to video (any format).
    - Extracts audio (any format) from video (any format).

    Converts between video, audio and images formats using the free "ffmpeg" library running command line shell.

    General syntax for ffmpeg (This is an example only):
    ffmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...
    
2. Prerequisites
    
    For testing purpouses it's necessary a video file in the same location as this script.
    Please, review the "requirements.txt" file for additional libraries to be installed that are necessary to work.
    Run the following command for unattended installation.

    (Python 2)
    $ pip install -r requirements.txt

    (Python 3) 
    $ pip3 install -r requirements.txt


    2.1. Requeriments: UI, End Point

        Video to images:
            - Source file selector (options to upload video file, paste URL).
            - Output filename field (text box).
            - Output format selector (combo box).
            - Number of fps to process (combo box with a write option).
            - Zipping function. 

        Video to video:
            - Source file selector (options to upload video file, paste URL).
            - Output filename field (text box).
            - Output format selector (combo box).
            - Encoder/Decoder (combo box).

        General functions:
            - Basic operations with files (CRUD).