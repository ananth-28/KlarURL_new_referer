<h1 align="center">Tiranozor</h1>

![GitHub stars](https://img.shields.io/github/stars/Turkce-Botlar-Sohbet/Tiranozor?style=social)
![GitHub forks](https://img.shields.io/github/forks/Turkce-Botlar-Sohbet/Tiranozor?style=social)

### Bağlantıları Yüklemek için Telegram Botu.

**Özellikler**:

- [x] [YT-DLP'de Desteklenen Bağlantıları](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) Telegram'a yükler.
- [x] HTTP/HTTPS'yi Dosya/Video olarak Telegram'a yükler.
- [x] Kalıcı Thumbnail desteği.
- [x] Kullanıcılara mesaj yayınlar.
- [x] Şifreli giriş desteği.

## Deploy 🚀

<details><summary>Heroku'ya Dağıt</summary>
<p>
<br>
<a href="https://heroku.com/deploy">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details>
    <summary>Render'a Dağıt</summary>

    1️⃣New / Static Site
    2️⃣https://github.com/andta200/KlarURL_new_referer
    3️⃣Build Command: python3 bot.py
    4️⃣Publish directory: ./
    5️⃣Advanced / Add Environment Variable
      API_HASH
      APP_ID
      AUTH_CHANNEL: -100xxxxxxxx, Zorunlu abonelik kanalı (Botu kanala yönetici yapmayı unutma)
      BOT_TOKEN: @BotFather
      CHUNK_SIZE:128
      DATABASE_URL: MongoDB URL
      DEF_THUMB_NAIL_VID_S: https://i.ytimg.com/vi/NXeTO5QM-Gw/maxresdefault.jpg
      LOG_CHANNEL: -100xxxxxxxx, Kayıtların tutulduğu kanal (Botu kanala yönetici yapmayı unutma)
      OWNER_ID: Kullanıcı Telegram ID
      PASS: maymun
      PROMO: False
      REFERER: dizipal364.com
      REFERER_URL: stream.dizipal364.com
      SESSION_NAME: urlyukleyici

</details>

<details>
    <summary>Vps'ye Dağıt</summary>
    <br>
    <p align="center">

    Yerel Makine'de Dağıtım.

</p>

```console
    git clone https://github.com/Turkce-Botlar-Sohbet/Tiranozor
    cd Tiranozor
    pip3 install -r requirements.txt
```
<br>
  
```     
config.env'yi kendi değerlerinizle yapılandırın.
Ve son olarak başlatın.
```  
```console
    python bot.py
```  
</details>    

#### Komutlar
```
start - start
broadcast - Toplu mesaj gönder
help - Yardım    
genthumb - Kapak resmi ekle
delthumb - Kapak resmi sil
ban - Kullanıcı yasakla
unban - Kullanıcının yasağını kaldır
```

## Kredi ve Teşekkürler.

* [X-URL-Uploader](https://github.com/X-Gorn/X-URL-Uploader/tree/database) için [@X-Gorn](https://t.me/xgorn)
* [TG-URL-Uploader](https://github.com/TGExplore/TG-URL-Uploader) için [@TGExplore](https://t.me/ViruZs)
* [AnyDLBot](https://telegram.dog/AnyDLBot) için [@SpEcHlDe](https://t.me/ThankTelegram)
* [Pyrogram Library](https://github.com/pyrogram/pyrogram) için [Dan Tès](https://t.me/haskell)
* [UploaditBot](https://telegram.dog/UploaditBot) için [Yoily](https://t.me/YoilyL)
* [database.py](https://github.com/AbirHasan2005/VideoCompress/blob/main/bot/database/database.py) için [@AbirHasan2005](https://t.me/AbirHasan2005)

#### LİSANS
- GPLv3


[![telegram badge](https://img.shields.io/badge/Telegram-Grup-30302f?style=flat&logo=telegram)](https://telegram.dog/botsohbet)
[![telegram badge](https://img.shields.io/badge/Telegram-Kanal-30302f?style=flat&logo=telegram)](https://telegram.dog/botarsivi)
