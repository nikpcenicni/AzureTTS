import tkinter as tk
from tkinter import *
import os
import dotenv
import AzureTTS.texttospeech as texttospeech

def play():
    text = input.get("1.0", "end-1c")
    speed = speedslider.get()
    pitch = pitchSlider.get()
    texttospeech.texttospeechOptions(text, speed, pitch)
    return  
    
def openConfig():
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    keytext.insert("1.0", os.environ["SPEECH_KEY"])
    regionText.insert("1.0", os.environ["SPEECH_REGION"])
        
    variable.set(os.environ["SPEECH_SYNTHESIS_VOICE_NAME"][6:])
    
    textFrame.pack_forget()
    controlFrame.pack_forget()
    configFrame.pack()
    return
    
def main():
    keytext.delete("1.0", "end")
    regionText.delete("1.0", "end")
    configFrame.pack_forget()
    textFrame.pack()
    controlFrame.pack()
    return

def saveConfig():
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    key = keytext.get("1.0", "end-1c")
    os.environ["SPEECH_KEY"] = key
    dotenv.set_key(dotenv_file, "SPEECH_KEY", os.environ["SPEECH_KEY"])
    
    region = regionText.get("1.0", "end-1c")
    dotenv.set_key(dotenv_file, "SPEECH_REGION", region)
    
    voice = "en-us-" + variable.get()
    dotenv.set_key(dotenv_file, "SPEECH_SYNTHESIS_VOICE_NAME", voice)

def voiceChanged(*args):
    print(voicemenu.get())
    

root = tk.Tk()
root.title("GUI")
root.geometry("400x500")
root.resizable(True, True)

textFrame = tk.Frame(root)
input = tk.Text(textFrame)
input.pack()

controlFrame = tk.Frame(root)
controlFrame.columnconfigure(0, weight=1)
controlFrame.rowconfigure(0, weight=1)
startbtn = tk.Button(controlFrame, text="Start", command=play)
startbtn.grid(row=0, column=0, sticky="nsew")
stopbtn = tk.Button(controlFrame, text="Stop")
stopbtn.grid(row=0, column=2, sticky="nsew")
pausebtn = tk.Button(controlFrame, text="Pause")
pausebtn.grid(row=0, column=1, sticky="nsew")

speedLbl = tk.Label(controlFrame, text="Speed")
speedLbl.grid(row=1, column=0, sticky="nsew")

speedslider = tk.Scale(controlFrame, from_=-100, to=200, digits=3, resolution=1, orient=tk.HORIZONTAL, length=200)
speedslider.grid(row=2, column=0, columnspan=3, sticky="nsew")
speedslider.set(0)

pitchLbl = tk.Label(controlFrame, text="Pitch")
pitchLbl.grid(row=3, column=0, sticky="nsew")

pitchSlider = tk.Scale(controlFrame, from_=-50, to=50, digits=2, resolution=1, orient=tk.HORIZONTAL, length=200)
pitchSlider.grid(row=4, column=0, columnspan=3, sticky="nsew")
pitchSlider.set(0)

configbtn = tk.Button(controlFrame, text="Config", command=openConfig)
configbtn.grid(row=5, column=0, sticky="nsew")


configFrame = tk.Frame(root)
configFrame.columnconfigure(0, weight=1)
configFrame.rowconfigure(0, weight=1)

backbtn = tk.Button(configFrame, text="Back", command=main)
backbtn.grid(row=0, column=0, sticky="w")

configlbl = tk.Label(configFrame, text="Config")
configlbl.grid(row=1, column=1, sticky="nsew", columnspan=1)

keylbl = tk.Label(configFrame, text="API Key")
keylbl.grid(row=2, column=0, sticky="nsew")
keytext = tk.Text(configFrame, height=1, width=20)
keytext.grid(row=2, column=1, sticky="nsew", columnspan=3)

regionLbl = tk.Label(configFrame, text="Region")
regionLbl.grid(row=3, column=0, sticky="nsew")
regionText = tk.Text(configFrame, height=1, width=20)
regionText.grid(row=3, column=1, sticky="nsew", columnspan=3)



voicelbl = tk.Label(configFrame, text="Voice")
voicelbl.grid(row=4, column=0, sticky="nsew")

voice_list = ['JennyNeural',
              'GuyNeural',
              'AmberNeural',
              'AnaNeural',
              'AriaNeural',
              'AshleyNeural',
              'BrandonNeural',
              'ChristopherNeural',
              'CoraNeural',
              'ElizabethNeural',
              'EricNeural',
              'JacobNeural',
              'MichelleNeural',
              'MonicaNeural',
              'SaraNeural'
              ]

variable = StringVar(configFrame)

voicemenu = tk.OptionMenu(configFrame, variable, *voice_list)
voicemenu.grid(row=4, column=1, sticky="nsew", columnspan=5)

savebtn = tk.Button(configFrame, text="Save", command=saveConfig)
savebtn.grid(row=5, column=0, sticky="nsew", columnspan=4)

textFrame.pack()
controlFrame.pack()

root.mainloop()


