# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:39:54 2017

@author: Filippo
"""

import os
import sys
from ffmpy import FFmpeg
from mutagen.flac import FLAC as fl
from mutagen.flac import Picture as pic
from mutagen.id3 import ID3 as id3




for file_header in os.listdir(".DB/"):
    output_file_type = ".flac"
    dir1 = output_file_type 
    dir2 = ""
    dir3 = ""
    file_header = os.path.join(".DB",file_header)
    ### GET THE ALBUM ART IF EXISTS
    album_art_dir = None
    if (os.path.isdir(file_header+"folder.jpg")):
        album_art_dir = file_header+"folder.jpg"
    else:
        album_art_dir = None
        
        

    for file_name in os.listdir(file_header):
        wav_full_dir = ""
        name_full_dir = ""
        ### FILE NAME DISCOVERY
        if file_name.endswith(".wav"):
            if '?' in file_name:
                new_file_dir = os.path.join(file_header,file_name.replace("?",""))
                old_file_dir = os.path.join(file_header,file_name)
                print("Old File Name: %s\nNew File Name: %s" %(old_file_dir,new_file_dir))
                os.rename(old_file_dir,new_file_dir)
                file_name = file_name.replace("?","")
                print "AHHHHHHHHHHHHHHHH!"
#            if True in [ord(i) < 128 for i in file_name]:
#                new_file_name = "".join([i if ord(i) < 128 else '' for i in file_name])
#                print("Old File Name: %s\nNew File Name: %s" %(file_header+file_name,file_header+new_file_name))
#                os.rename(file_header+file_name,file_header+new_file_name)
#                file_name = new_file_name

            print("New WAV file found: %s, proceeding with conversion, saving and naming." %(file_header+file_name))
            wav_full_dir = os.path.join(file_header,file_name)
            f_name = file_name.replace(".wav","")
            name_full_dir = wav_full_dir.replace(".wav","")
            
            ### ID3 Tags reading
            id3_tags = {}
            id3_dir = name_full_dir+".id3"
            if os.path.isfile(id3_dir):
                aud = id3(id3_dir)
                try:
                    id3_tags['Year'] = str(aud['TDRC'])
                except KeyError:
                    id3_tags['Year'] = "1900"
                # Cleanse the title
                try:
                    id3_tags['Title'] = ''.join([i if ord(i) < 128 else '' for i in str(aud['TIT2'])])
                except KeyError:
                    id3_tags['Title'] = f_name
                output_name = id3_tags['Title']
                try:
                    id3_tags['Artist'] = str(aud['TPE1'])
                except KeyError:
                    id3_tags['Artist'] = "Various"
                dir2 = id3_tags['Artist'] + "/"
                try:
                    id3_tags['Album'] = str(aud['TALB'])
                except KeyError:
                    id3_tags['Album'] = "Various"
                dir3 = id3_tags['Album'] + "/"
                try:
                    id3_tags['Genre'] = str(aud['TCON'])
                except KeyError:
                    id3_tags['Genre'] = "Unknown"
            else:
                print("Could NOT find ID3 tag for %s" %id3_dir)
                sys.exit([1])
                
            ### FOLDER SET UP, DIRECTORIES FOR FLAC OUTPUT.
            if not (os.path.exists(dir1)):
                os.makedirs(dir1)
            if not (os.path.exists(os.path.join(dir1,dir2))):
                os.makedirs(os.path.join(dir1,dir2))
            if not (os.path.exists(os.path.join(dir1,dir2,dir3))):
                os.makedirs(os.path.join(dir1,dir2,dir3))
            output_dir = os.path.join(dir1,dir2,dir3)
            output_file = os.path.join(output_dir,output_name+output_file_type)
            full_out_path = os.path.join(output_dir,output_file)
                
            ### CONVERSION 
            if not (os.path.exists(output_file)):
                ff = FFmpeg( executable="C:/Users/Filippo/Documents/ffmpeg-20170520-64ea4d1-win64-static/bin/ffmpeg.exe",global_options="-y",inputs={wav_full_dir: None}, outputs={output_file:None})
                ff.cmd
                ff.run()
        
                ## FLAC TAG WRITTING
                flac = fl(output_file)
                flac["year"] = id3_tags['Year']
                flac["title"] = id3_tags['Title']
                flac["artist"] = id3_tags['Artist']
                flac["album"] = id3_tags['Album']
                flac["genre"] = id3_tags['Genre']
                if album_art_dir:
                    art = pic()
                    art.type = 3
                    with open(album_art_dir, 'rb') as f:
                        art.data = f.read()
                    flac.add_picture(art)
                flac.save()
        
def generate_tags()
    
    

    
                           