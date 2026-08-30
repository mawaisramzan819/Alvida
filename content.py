"""
=============================================================================
STREAMLIT FAREWELL WEB APP — CENTRALIZED CONTENT CONFIGURATION
Roman Urdu Authentic Heartfelt Farewell Story
=============================================================================
"""

# Personalization placeholders
RECIPIENT_NAME = "Almas"
SENDER_NAME = "Awais"

# -----------------------------------------------------------------------------
# CHAPTER LOADING MESSAGES (Roman Urdu)
# -----------------------------------------------------------------------------
CHAPTER_LOADERS = {
    "home": {
        "title": "Home",
        "message": "Dil ki baat dobara khul rahi hai...",
    },
    "message": {
        "title": "Message",
        "message": "Woh alfaaz jo kabhi keh nahi saka...",
    },
    "memories": {
        "title": "Memories",
        "message": "Purani yaadon ko sameta ja raha hai...",
    },
    "wishes": {
        "title": "Wishes",
        "message": "Adhoori khwahishon ko parha ja raha hai...",
    },
    "dua": {
        "title": "Dua",
        "message": "Dil se nikli dua khul rahi hai...",
    },
    "future": {
        "title": "Future",
        "message": "Woh mustaqbil jo ap k saath socha tha...",
    },
    "thankyou": {
        "title": "Thank You",
        "message": "ap ka shukriya ada kiya ja raha hai...",
    },
    "goodbye": {
        "title": "Goodbye",
        "message": "Woh alvida jo main kehna nahi chahta...",
    },
}

# -----------------------------------------------------------------------------
# CHAPTER 1 — HOME
# -----------------------------------------------------------------------------
OPENING_SECTION = {
    "eyebrow": "AP K JAANE SE PEHLE",
    "main_title": "Maine kabhi nahi socha tha ke hamari kahani ka aakhri lafz “Alvida” hoga.",
    "subtitle": (
        "Mere dil ka ek hissa abhi bhi ap k ruk jaane ka intezar kar raha hai. "
        "Main nahi jaanta ke ap k baghair zindagi ko kaise sochun. In safhon mein woh sab kuch hai "
        "jo main ap k saamne kabhi keh nahi saka—meri mohabbat, hamari yaadein, meri ghaltiyon ka afsos "
        "aur woh har dua jo aaj bhi ap k liye nikalti hai."
    ),
    "primary_button": "Woh Parho Jo Mera Dil Keh Na Saka →",
    "music_play_btn": "▶ Start background music",
    "music_pause_btn": "⏸ Stop background music",
    "bottom_quote": "“Agar main is kahani ka anjaam badal sakta, to main ek baar phir sirf ap ko hi chunta.”",
}

# -----------------------------------------------------------------------------
# CHAPTER 2 — MESSAGE
# -----------------------------------------------------------------------------
MESSAGE_SECTION = {
    "eyebrow": "EK AAKHRI PAIKAAR",
    "title": "WOH ALFAAZ JO MAIN KEH NAHI SAKA",
    "subtitle": "Kash main waqt ko peeche le ja sakta aur sab kuch theek kar pata...",
    "paragraphs": [
        (
            "Main maanta hoon ke hamare darmiyan jo sab se gehra zakhm bana, uski wajah meri ghalti thi. "
            "Maine woh baatein doosron ko bata dein jo sirf ap k aur mere darmiyan rehni chahiye theen."
        ),
        (
            "Us waqt main samajh nahi saka ke kisi se mohabbat karne ka matlab uske bharose, "
            "uski izzat aur uski privacy ki hifazat karna bhi hota hai."
        ),
        (
            "Main guzra hua waqt badal nahi sakta. ap ko meri wajah se jo baatein sunni pareen aur jo takleef mili, "
            "main usay mita nahi sakta. Lekin agar mera afsos waqt ko peechhe le ja sakta, to main apni kahani ko "
            "poori duniya se chhupa kar sirf apne dil mein rakhta."
        ),
        (
            "Do saal ki khamoshi mein bhi koi din aisa nahi tha jab ap  meri yaadon se door rahi ho."
        ),
        (
            "Main ye sab is liye nahi likh raha ke main ap ko khushi se alvida keh raha hoon. "
            "Main ye is liye likh raha hoon kyun ke mera dil aaj bhi ap ko khone ke liye tayyar nahi."
        ),
    ],
}

# -----------------------------------------------------------------------------
# CHAPTER 3 — MEMORIES (8 Authentic Timeline Cards)
# -----------------------------------------------------------------------------
MEMORIES_SECTION = {
    "eyebrow": "SAFAR-E-YADEIN",
    "title": "WOH YADEIN JO AAJ BHI MERE SAATH HAIN",
    "subtitle": "Hamari kahani ke woh lamhe jo mere dil par hamesha ke liye naqsh ho gaye.",
    "cards": [
        {
            "category": "Pehli Salam",
            "icon": "🌱",
            "accent_color": "#14b8a6",
            "placeholder": (
                "School ke ek aam se din mein hamari kahani ek choti si salam se shuru hui. "
                "Humein kya pata tha ke woh chota sa lamha meri zindagi ki sab se gehri yaad ban jayega."
            ),
        },
        {
            "category": "Volleyball Ground",
            "icon": "🏐",
            "accent_color": "#f59e0b",
            "placeholder": (
                "Main volleyball khelta tha, lekin meri nazrein aksar ap ko dhoondti rehti theen. "
                "Ap ka mujhe dekhna ek aam se match ko mere liye khaas bana deta tha."
            ),
        },
        {
            "category": "Jab ap  Achi Lagne Lageen",
            "icon": "✨",
            "accent_color": "#38bdf8",
            "placeholder": (
                "Mujhe yaad nahi ke woh kaunsa ek lamha tha. Bas ap ki rehnumai, hamari baaton "
                "aur ek doosre ko samajhte samajhte ap  mere liye sab kuch ban gayi."
            ),
        },
        {
            "category": "Meri Sab Se Bari Ghalti",
            "icon": "🥀",
            "accent_color": "#f43f5e",
            "placeholder": (
                "Maine hamari baatein ghalat logon ko bata dein. Unhon ne mera bharosa toda, "
                "lekin pehli ghalti meri thi—main ap k bharose aur izzat ki hifazat nahi kar saka."
            ),
        },
        {
            "category": "Do Saal Ki Khamoshi",
            "icon": "⏳",
            "accent_color": "#a855f7",
            "placeholder": (
                "Do saal tak hamare darmiyan koi baat nahi hui. Sirf yaadein, afsos aur "
                "ap k baghair reh jaane wali khamoshi mere saath rahi."
            ),
        },
        {
            "category": "Accident Aur ap ki Dua",
            "icon": "🤲",
            "accent_color": "#fbbf24",
            "placeholder": (
                "Jab main zindagi aur behoshi ke darmiyan tha, ap ki duaein mere saath theen. "
                "Jab mujhe hosh aaya, mere dil ne sab se pehle sirf ap ko yaad kiya."
            ),
        },
        {
            "category": "ap ka Dobara Lautna",
            "icon": "🕊️",
            "accent_color": "#14b8a6",
            "placeholder": (
                "Itne arsay ke baad ap ki awaaz dobara sunna aisa tha jaise zindagi ne mujhe "
                "meri khoi hui duniya wapas kar di ho."
            ),
        },
        {
            "category": "Aaj",
            "icon": "🌙",
            "accent_color": "#ea580c",
            "placeholder": (
                "Itna sab kuch sehne ke baad bhi maine kabhi nahi socha tha ke ek din main ap ko "
                "apne se door jaate hue dekhunga."
            ),
        },
    ],
}

# -----------------------------------------------------------------------------
# CHAPTER 4 — WISHES (5 Heartfelt Roman Urdu Wishes)
# -----------------------------------------------------------------------------
WISHES_SECTION = {
    "eyebrow": "DIL KI KHWAHISHEIN",
    "title": "MERI ADHOORI KHWAHISHEIN",
    "subtitle": "Kash ye sab badal sakta...",
    "cards": [
        {
            "title": "Pehla Kaash",
            "icon": "🤍",
            "accent_type": "teal",
            "description": "Kaash main waqt par ap k bharose ki hifazat kar pata.",
        },
        {
            "title": "Doosra Kaash",
            "icon": "✨",
            "accent_type": "amber",
            "description": "Kaash hamare darmiyan jo toot gaya, usay jorne ka ek aur mauqa mil jata.",
        },
        {
            "title": "Teesra Kaash",
            "icon": "🌱",
            "accent_type": "blue",
            "description": "Kaash ap  dekh pateen ke main hamare liye kaisa insaan banne ki koshish kar raha tha.",
        },
        {
            "title": "Chautha Kaash",
            "icon": "🕊️",
            "accent_type": "violet",
            "description": "Kaash hamari aakhri yaad ek alvida na hoti.",
        },
        {
            "title": "Aakhri Kaash",
            "icon": "🪷",
            "accent_type": "rose",
            "description": "Aur sab se zyada… kaash ap  ruk jao.",
        },
    ],
}

# -----------------------------------------------------------------------------
# CHAPTER 5 — DUA
# -----------------------------------------------------------------------------
DUA_SECTION = {
    "eyebrow": "EK KHALIS DUA",
    "title": "JAB KUCH NA KAR SAKA TO ap k LIYE DUA KI",
    "subtitle": "Rab ke huzoor dil ka har haal rakh diya...",
    "paragraphs": [
        (
            "Ya Allah, Ap hamare dilon ka haal jaanty hain. Ap hamari mohabbat, hamari ghaltiyan, "
            "hamari takleef aur woh har baat jaanty hain jo hum kabhi ek doosre se keh nahi sake."
        ),
        (
            "Agar hamara saath hum dono ke haq mein behtar hai, to hamare darmiyan khari har deewar hata de. "
            "Hamari ghaltiyan maaf kar de, hamare dil narm kar de aur izzat ke saath hamare raste dobara mila de."
        ),
        (
            "Aur agar hamara saath muqaddar mein nahi, to woh jahan bhi rahe usay hamesha khush, mehfooz "
            "aur pur-sukoon rakhna—chahe uske saath khara hone wala shakhs main na rahun."
        ),
        (
            "Lekin Ya Allah… agar abhi bhi koi rasta baqi hai, to isay hamara aakhri alvida mat banne dena."
        ),
    ],
}

# -----------------------------------------------------------------------------
# CHAPTER 6 — FUTURE
# -----------------------------------------------------------------------------
FUTURE_SECTION = {
    "eyebrow": "SOCHA HUA KAL",
    "title": "WOH MUSTAQBIL JO MAINE ap k SAATH SOCHA THA",
    "subtitle": "Woh khwab jo sirf ap k naam se shuru aur ap  par khatam hotay thay.",
    "quote_art": "ap  sirf meri khwahish nahi, mera mustaqbil theen...",
    "content": [
        "Jab bhi maine apne career, kamyabi aur ek behtar zindagi ka socha, us tasveer mein ap  hamesha mere saath theen.",
        "Main ap ko sirf apne aasaan dino mein nahi chahta tha. Main ap k liye ek aisa insaan banna chahta tha jo izzat ke saath ap ka haath maang sake aur zindagi bhar ap k saath khara reh sake.",
        "Shayad mujhe bohat waqt lag gaya. Shayad zindagi mujhse zyada tez chalti rahi. Lekin jis mustaqbil ke liye main mehnat kar raha tha, woh ap k baghair kabhi mukammal nahi tha.",
    ],
}

# -----------------------------------------------------------------------------
# CHAPTER 7 — THANK YOU
# -----------------------------------------------------------------------------
THANK_YOU_SECTION = {
    "eyebrow": "DIL KI GEHRAIYON SE",
    "title": "MERI ZINDAGI MEIN AANE KA SHUKRIYA",
    "main_quote": "Har us lamhe ke liye jo ap ne meri zindagi ko diya...",
    "lines": [
        "Mujhe samjhane aur guide karne ka shukriya.",
        "Mujhe volleyball khelte hue dekhne wale un chote lekin khoobsurat lamhon ka shukriya.",
        "Us waqt mere liye dua karne ka shukriya jab main khud apne liye dua karne ke qabil nahi tha.",
        "Do saal ki khamoshi ke baad meri zindagi mein dobara lautne ka shukriya.",
        "Meri ghaltiyon ke bawajood hamari kahani ko ek aur mauqa dene ka shukriya.",
    ],
    "final_line": (
        "Main ap ka shukriya is liye nahi kar raha ke main ap ko khone ke liye tayyar hoon. "
        "Main shukriya is liye kar raha hoon kyun ke ap se mohabbat ne mujhe hamesha ke liye badal diya."
    ),
}

# -----------------------------------------------------------------------------
# CHAPTER 8 — GOODBYE
# -----------------------------------------------------------------------------
GOODBYE_SECTION = {
    "eyebrow": "WOH LAFZ JO MAIN KEH NAHI PA RAHA",
    "heading": "Main ap ko alvida kaise kahun?",
    "paragraphs": [
        "Main us shakhs ko alvida kaise kahun jo meri itni saari yaadon mein basa hua hai?",
        "Main kaise maan loon ke jisne kabhi meri zindagi ke liye dua ki, woh ab meri zindagi ka hissa nahi rahegi?",
        "Main jaanta hoon ke maine ap ko takleef di. Main ye bhi jaanta hoon ke sirf mohabbat guzra hua sab kuch nahi mita sakti. Lekin ap ko kho dena aaj bhi mere dil ko qabool nahi.",
        "Main ap  par koi zabardasti nahi karna chahta. Main ap ki takleef ko chota bhi nahi kehna chahta. Main sirf itna chahta hoon ke agar ap k dil ke kisi kone mein hamari kahani abhi bhi zinda hai, to please isay yahin khatam mat hone dena.",
    ],
    "highlighted_line": "Main ap k baghair zindagi nahi chahta tha… aur aaj bhi nahi chahta.",
    "button_label": "Meri Aakhri Baat Parho",
    "revealed_text": (
        "Main ap se ye nahi keh raha ke ap  apni takleef bhool jao. Main sirf ek sachhi aur aakhri baat ka "
        "mauqa maang raha hoon, is se pehle ke hamare itne saalon ki yaadein hamesha ki khamoshi ban jayein. "
        "Agar hamare liye abhi bhi koi chota sa rasta baqi hai, to please bina dil ki baat sune mat jaana."
    ),
    "final_quote": "“ap  door ja rahi ho, lekin mera dil aaj bhi ap ko jaane ki ijazat nahi de pa raha.”",
}
