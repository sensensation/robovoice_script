#This script transforms txt files into mp3. Use it to make sounds from you writtens!
#Данный скрипт превращает txt файлы в mp3. Используйте его, чтобы превратить текст в голос!

#by cybersen

from gtts import gTTS
from tqdm import tqdm
from time import sleep

file_path = input( 'Enter file path / Введите путь к файлу: ' )
file = open( file_path, 'r' )
messagetext = file.read()

file.close()

for i in tqdm( range( 100 ) ):
   sleep( 0.01 )

tts = gTTS ( text = messagetext, lang = 'en' ) #You can switch language, put 'ru' instead 'en'. Если хотите
                                               #изменить текст чтения, измените 'en' на 'ru'.          
tts.save( 'robovoice.mp3' )

print( 'File saved / Файл сохранен' )
