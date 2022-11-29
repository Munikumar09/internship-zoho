## Prerequisites
elasticsearch
## To install elasticsearch
1. Download elasticsearch from https://www.elastic.co/downloads/enterprise-search
2. extract the downloaded file and move inside it
3. run bin/elasticsearch command  

**Note** To run elasticsearch cluster jvm is required. Install openjdk 
## To run application  
options:  
--regex, -re  
                    regular expression that represents the file path to add files  
    ```
    eg:  
    streamlit run app.py -- -re  "/home/local/user/Desktop(/[\w-]*){3,5}\.(tgz)$"
    ```
--recursive-files-extraction, -r  
                    File path to recursively search and extract audio files  
    ```
    eg:  
    streamlit run app.py -- -r "/home/local/user/zspeech/datasets/asr/evalution/en"
    ```

--audio-path-file, -f  
                        Path to the audio file (tgz format)  
    ```
    eg:  
    streamlit run app.py -- -f "/home/local/user/Desktop/audio/accent.tgz"
    ```

--audio-path-dir , -d   
                        Path to the directory that contain the audio files  
    ```
    eg:  
    streamlit run app.py -- -d "/home/local/user/Desktop/audio_files"
    ```