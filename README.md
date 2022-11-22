# cdaDownloader
Simple cli tool from downloading videos/folder content from cda.pl

## Requirements
* At least python 3.0 
* Python version that supports all needed libraries
* Python libraries:
    * urlib
    * randomheader
    * requests
    * bs4
    * json (standard python lib)
    * os   (standard python lib)
    * sys  (standard python lib)


## Usage
### Example usage

```
python3 main.py -q 1080p https://www.cda.pl/video/13617843 -p C:\Users\user\Desktop\coolVideos
```
To download entire content of folder just pass url to that folder  
\
Execute main script with python providing url to video/folder you want to download.

* Use -q (or --quality) _quality_ to specify quality of every video that will be downloaded. By default script will look for best quality available

* use -p (or --path) _full path_ to specify where content will be saved. By default this value is set to current directory in terminal

\
Script should handle every (at least most of) user errors. If video with required quality doesn't exists program should ask user if he wants to continue with best quality available. In case of any network related and downloading fails script will try 2 more times.

## License
Copyright 2022 Jakub Wojciechowski

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.