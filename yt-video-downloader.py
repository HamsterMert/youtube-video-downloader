from pytubefix import YouTube
from pytubefix.cli import on_progress
import os 
from os import system
import time 



def mp3video():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    output_directory = os.path.join(desktop_path, "İndirilen Şarkılar")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    link = input('İndirmek istediğiniz videonun linkini giriniz. \n > ')
    
    system('cls')
    print(text)

    yt = YouTube(link, on_progress_callback=on_progress)
    print('{} isimli video MP3 olarak indiriliyor...'.format(yt.title))
    
    ys = yt.streams.get_audio_only()
    
    ys.download(output_path=output_directory, filename=f"{yt.title}.mp3")
    print('Video Başarıyla İndirildi.')

    time.sleep(3)
    system('cls')

def mp4video():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    output_directory = os.path.join(desktop_path, "İndirilen Şarkılar")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    link = input('İndirmek istediğiniz videonun linkini giriniz. \n > ')

    system('cls')
    print(text)

    yt = YouTube(link, on_progress_callback = on_progress)
    print('{} isimli video MP4 olarak indiriliyor.'.format(yt.title))
 
    ys = yt.streams.get_highest_resolution()
    ys.download(output_path=output_directory, filename=f"{yt.title}.mp4")

    print('Video Başarıyla İndirildi.')

    time.sleep(3)
    system('cls')

text = '''
██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗  
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
'''



while True:
    print(text)
    print('''
[1] MP3 VIDEO INDIRICI
[2] MP4 VIDEO INDIRICI''')
    select = input('Lütfen bir seçim yapınız. \n > ')

    if select == '1':
        mp3video()

    elif select == '2':
        mp4video()

