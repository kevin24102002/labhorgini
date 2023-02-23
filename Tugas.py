import speech_recognition as srec
import pyttsx3 as pyt
from gtts import gTTS                       
import os            
import pywhatkit 
import wikipedia 
import playsound 
import datetime 

# suara = gTTS(text='halo, nama saya gerald', lang = 'id', slow = False)
# # suara.save('contoh.mp3')
# os.system('contoh.mp3')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('volume',20)
# suara = gTTS(text='halo, nama saya gerald', lang = 'id', slow = False)
# suara.save('contoh.mp3')
# os.system('contoh.mp3')

def perintah():
    mendengar = srec.Recognizer()
    with srec.Microphone() as source:
        # print('你好， 我是郑少勤，你有什么事儿吗?')
        # pyt.speak('Halo apa kabar? ada yang bisa saya bantu ?')
        print('Mendengar....')
        suara = mendengar.listen(source,phrase_time_limit=3)
        try: 
            print('Diterima...')
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        
        except Exception as e:
            print(e)
            # print("对不起， 我不懂，你能不能再说一遍 ？")
            return "None"
        # except Exception : 
        #     pyt.speak('对不起， 我不懂，你能不能再说一遍 ？')
        return dengar

# def speak(text):
#     suara = gTTS(text=text, lang = 'id', slow = False)
#     suara.save('contoh.mp3')
#     os.system('contoh.mp3')

def speak(text):
    tts = gTTS(text=text, lang='id')

    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)



def tell_day():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'senin', 2: 'selesa',
				3: 'rabu', 4: 'kamis',
				5: 'jumat', 6: 'sabtu',
				7: 'Minggu'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("hari ini adalah hari" + day_of_the_week)

def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like
	# this "2020-06-05 17:50:14.582630"
	#nd then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak('sekarang jam' + hour +'dan' +  min + "Menit")
   

def hello():
    speak('halo')

def belajar():
    speak('belajar python')

def hobi():
    speak('renang, membaca')

def pertanyaan ():
    speak('apa kabar')

def shaoqin():
    speak('apa ?')















































# def perintah():
#     mendengar = srec.Recognizer()
#     with srec.Microphone() as source:
#         pyt.speak('Hi my name is michelle, can I help you ?')
#         print('Listening.....')
#         mendengar.pause_threshold= 0.9
#         suara =mendengar.listen(source, phrase_time_limit=5)
#         try:
#             print('processing...')
#             layanan = mendengar.recognize_google(suara)
#             print(layanan)
#         except:
#             pass
#         return layanan

# perintah()


# def ngomong(self):
#     teks = (self)
#     bahasa = 'id'
#     namafile = 'ngomong.mp3'
#     def reading():
#         suara = gTTS(text=teks, lang=bahasa, slow=False)
#         suara.save(namafile)
#         os.system(f'start {namafile}')
#     reading()

def run_michelle():
    hello()
    while(True):
        Layanan = perintah().lower()
        # ngomong(Layanan)
        if 'buka' in Layanan:
            video = Layanan.replace('temukan', '')
            speak('temukan' + video)
            print(video + ' temukan..')
            pywhatkit.playonyt(video)

        elif 'temukan' in Layanan :
            wiki = Layanan.replace('find out', '')
            wikipedia.set_lang("id")
            hasil = wikipedia.summary(wiki, sentences = 4)
            print(hasil)
            speak(hasil)
            

        # elif '累' in Layanan :
        #     Layanan.replace('lagu...', '')
        #     pyt.speak('saya akan memutarkan lagu semangat untuk anda ')
        #     os.startfile('C:\\Users\\kevin\\Music\\music1.mp3')
        
        elif 'sampai jumpa' in Layanan :
            speak('sampai jumpa')
            exit()
        
        elif 'hari ini ' in Layanan:
            tell_day()
            continue
        
        elif 'jam' in Layanan:
            tellTime()
        
        elif 'nama'in Layanan :
            speak('gerald')
        
        # elif '聪明' in Layanan:
        #     belajar()
        # elif '爱好' in Layanan :
        #     hobi()
        
        # elif '男朋友' in Layanan:
        #     pertanyaan()

        # elif '你好' in Layanan:
        #     shaoqin()


            
    
        
if __name__ == '__main__':
	
	# main method for executing
	# the functions
	run_michelle()