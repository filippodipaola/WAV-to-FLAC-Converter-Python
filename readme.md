This script has several requirements listed below:
* Python 2.7.x <- Must be Python 2.7, this script does not work with Python 3.
* FFMPY <- http://ffmpy.readthedocs.io/en/latest/
* Mutagen <- https://mutagen.readthedocs.io/en/latest/

To install this script, install all the requirements listed above and then clone the repo. 
Next COPY the .DB from the Cocktail Audio device hard drive to your PC, place the script "music_orderer_full.py" 
in the same level of the directory as the .DB/ folder and then open your terminal and type >python music_orderer_full.py

The result will be all the .WAV files from the .DB/ folder will be converted into FLAC files with FULL metadata/ID3 tags 
and the folder structure will be order such that the hierachry is ARTIST->ALBUM->FLAC file.
