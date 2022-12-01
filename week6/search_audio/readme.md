## Prerequisites
elasticsearch software
## To install elasticsearch
1. Download elasticsearch from https://www.elastic.co/downloads/enterprise-search
2. extract the downloaded file and move inside it
3. run bin/elasticsearch command  

**Note** To run elasticsearch cluster jvm is required. Install openjdk 
## To run application  
options to add source file path in text input field:  
regular expression that represents the file path to add files  
```
    eg:  
    /home/local/user/Desktop(/[\w-]*){3,5}\.(tgz)$ re
```  
Normal source file path to add audio files:
```
    eg:
    /home/local/user/Desktop/zspeech/datasets/asr/en
```
