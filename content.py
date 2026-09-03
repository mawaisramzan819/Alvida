"""
=============================================================================
A FAREWELL THAT STAYS — Content Configuration
All chapter text, loader messages, and UI strings.
Authentic Pakistani Roman Urdu — Mature, Respectful, Sincere & Emotional
=============================================================================
"""

RECIPIENT_NAME = "Almas"
SENDER_NAME = "Awais"

# -----------------------------------------------------------------------------
# CHAPTER LOADING MESSAGES (Natural Roman Urdu)
# -----------------------------------------------------------------------------
CHAPTER_LOADERS = {
    "home":       {"title": "Home",               "message": "Kuch yaadein dil ke bohat qareeb hoti hain..."},
    "welcome":    {"title": "Welcome",            "message": "Jaane se pehle, dil ki ek aakhri baat..."},
    "memories":   {"title": "Memories",           "message": "Purani yaadon ko sameta ja raha hai..."},
    "words":      {"title": "Words From My Heart","message": "Dil ke woh alfaaz jo sirf ap k liye the..."},
    "respect":    {"title": "Why I Respect You",  "message": "Woh baat jo ap ko aur khoobsurat banati hai..."},
    "learned":    {"title": "What I Learned",     "message": "Har ghalti ne kuch naya sikhaya..."},
    "intentions": {"title": "Intentions",         "message": "Woh iradey jo dil ne hamesha sachche rakhe..."},
    "dua":        {"title": "Dua",                "message": "Tumhari khushi aur sukoon ke liye dil se dua..."},
    "thankyou":   {"title": "Thank You",          "message": "Dil ki gehraiyon se shukriya..."},
    "goodbye":    {"title": "Final Note",         "message": "Aakhri alfaaz... dil ki gehraiyon se..."},
}

# -----------------------------------------------------------------------------
# HOME PAGE
# -----------------------------------------------------------------------------
HOME_SECTION = {
    "hero_headline": "A Farewell\nThat Stays\nin the Heart",
    "hero_subtitle": (
        "Kuch alvida asal mein khatam nahi hotay,\n"
        "wo bas khoobsurat yaadon ki shuruat ban jatay hain."
    ),
    "primary_button": "Start the Journey",
    "secondary_button": "Watch Intro",
    "quote_bar": "Faaslay chahe kitne bhi barh jayein, tum meri duaon aur dil mein hamesha raho gi.",
    "bottom_quote": "Zindagi ap ko jahan bhi le jaye, meri duaein hamesha ap k saath rahein gi.",
}

# Chapter card descriptions for Home grid (Exact Reference UI)
HOME_CARDS = [
    {"id": "home",       "title": "Story Overview",       "desc": "Hamari kahani ke woh lamhe jo hamesha dil mein rahein ge.", "thumb": "thumb_welcome"},
    {"id": "welcome",    "title": "Welcome",              "desc": "Jaane se pehle, ek baar ye khat zaroor parh lena.", "thumb": "thumb_welcome"},
    {"id": "memories",   "title": "Memories",             "desc": "Woh khoobsurat lamhe jo waqt ke saath kabhi dhundhle nahi honge.", "thumb": "thumb_memories"},
    {"id": "words",      "title": "Words From My Heart",  "desc": "Woh sachchi baatein jo main ap k saamne keh na saka.", "thumb": "thumb_words"},
    {"id": "respect",    "title": "Why I Respect You",    "desc": "Woh khoobian jin ki wajah se ap ki izzat hamesha dil mein rahe gi.", "thumb": "thumb_respect"},
    {"id": "intentions", "title": "Intentions",           "desc": "Meri sachchi duaein aur iradey jo sirf ap ki khushi ke liye hain.", "thumb": "thumb_intentions"},
    {"id": "dua",        "title": "Dua",                  "desc": "Tumhari khushi, sukoon aur kamyabi ke liye dil se dua.", "thumb": "thumb_dua"},
    {"id": "goodbye",    "title": "Final Note",           "desc": "Ek aakhri baat... mohabbat, izzat aur duaon ke saath.", "thumb": "thumb_goodbye"},
]

# -----------------------------------------------------------------------------
# STORY OVERVIEW SECTION (Kept untouched)
# -----------------------------------------------------------------------------
STORY_OVERVIEW_SECTION = {
    "eyebrow": "✦ HAMARI KAHANI KA SAFAR",
    "title": "A Farewell That Stays in the Heart",
    "subtitle": "Kuch alvida asal mein khatam nahi hotay — wo bas khoobsurat yaadon ki shuruat ban jatay hain.",
    "paragraphs": [
        (
            "Kuch log sirf zindagi ka hissa nahi bante… wo aadat ban jaate hain.\n"
            "Unki baatein, unki hansi, unka hona — sab kuch itna apna lagne lagta hai\n"
            "ke faasla aane ke baad bhi dil unhein chhor nahi pata."
        ),
        (
            "Shayad waqt ke saath sab kuch badal jaye, lekin kuch yaadein aisi hoti hain\n"
            "jo dil khud sambhal kar rakhta hai. Unhein na waqt mita pata hai,\n"
            "na faaslay kam kar pate hain."
        ),
        (
            "Is safar mein jo kuch bhi hai, wo bas un jazbaat ka ek chhota sa hissa hai\n"
            "jo shayad alfaaz mein poore kabhi aa hi nahi sakte."
        ),
    ],
    "closing_note": "Bas itna hai ke tumhari kami shayad waqt ke saath aadat ban jaye…\nlekin tumhari jagah kabhi koi nahi le sakega.",
}

# -----------------------------------------------------------------------------
# CHAPTER 1 — WELCOME (Unique Welcome Content)
# -----------------------------------------------------------------------------
WELCOME_SECTION = {
    "eyebrow": "✦ JAANE SE PEHLE",
    "title": "Jaane Se Pehle, Ek Baar Parh Lena",
    "subtitle": "Ye safha kisi gile ya shikway ke liye nahi, sirf dil ki sachai ke liye hai.",
    "paragraphs": [
        (
            "Kabhi kabhi kisi insan ka humari zindagi mein aana itna aam sa lagta hai…\n"
            "lekin aahista aahista wahi insan humari roz ki soch, muskurahat aur yaadon\n"
            "ka hissa ban jata hai."
        ),
        (
            "Pata hi nahi chalta ke kab uski ek choti si baat bhi dil ko sukoon dene\n"
            "lagti hai, aur kab uski khamoshi bhi mehsoos hone lagti hai."
        ),
        (
            "Shayad hum har baat keh nahi pate, har ehsaas samjha nahi pate…\n"
            "lekin iska matlab ye nahi hota ke wo ehsaas kam thay.\n"
            "Kuch jazbaat bas dil ke andar reh jaate hain, bina kisi shor ke."
        ),
        (
            "Aur shayad isi liye ye safar bana hai…\n"
            "taake jo baatein kabhi alfaaz tak nahi aa sakin,\n"
            "wo kam az kam yaadon mein apni jagah bana saken."
        ),
    ],
    "closing_note": "Agar kabhi meri baaton ki kami mehsoos ho…\nto bas itna samajh lena ke kuch log door ja kar bhi\ndil se kabhi door nahi hote.",
}

# -----------------------------------------------------------------------------
# CHAPTER 2 — MEMORIES
# -----------------------------------------------------------------------------
MEMORIES_SECTION = {
    "eyebrow": "SAFAR-E-YAADEIN",
    "title": "Woh Yaadein Jo Hamesha Saath Rahein Gi",
    "subtitle": "Hamari kahani ke woh lamhe jo mere dil par hamesha ke liye naqsh ho gaye.",
    "cards": [
        {
            "id": "mem_1",
            "category": "Pehli Salam",
            "title": "Pehli Salam",
            "icon": "🌱",
            "accent_color": "#6ee7b7",
            "preview": "Ek choti si salam… jo baad mein meri zindagi ki sab se gehri yaadon mein se ek ban gayi.",
            "full_text": (
                "School ka woh din shayad ap ke liye bas ek aam sa din tha… lekin mujhe kya pata tha "
                "ke ap ki ek choti si salam meri zindagi ki itni badi yaad ban jayegi. Us waqt bas "
                "muskura kar jawab de diya tha… kaash pata hota ke ek din isi choti si mulaqat ko "
                "yaad karke dil itna bhar aayega. Kuch lamhe us waqt bilkul mamooli lagte hain, aur phir "
                "waqt guzarne ke baad pata chalta hai ke wahi lamhe kitne anmol thay."
            ),
            "placeholder": (
                "School ka woh din shayad ap ke liye bas ek aam sa din tha… lekin mujhe kya pata tha "
                "ke ap ki ek choti si salam meri zindagi ki itni badi yaad ban jayegi. Us waqt bas "
                "muskura kar jawab de diya tha… kaash pata hota ke ek din isi choti si mulaqat ko "
                "yaad karke dil itna bhar aayega. Kuch lamhe us waqt bilkul mamooli lagte hain, aur phir "
                "waqt guzarne ke baad pata chalta hai ke wahi lamhe kitne anmol thay."
            ),
        },
        {
            "id": "mem_2",
            "category": "Volleyball Ground",
            "title": "Volleyball Ground",
            "icon": "🏐",
            "accent_color": "#fbbf24",
            "preview": "Match apni jagah tha… meri nazar hamesha ap ko dhoondti thi.",
            "full_text": (
                "Main volleyball khelta zaroor tha, lekin sach kahun to meri tawajju aksar game se "
                "zyada ap ko dhoondne mein hoti thi. Pata nahi kyun, lekin jab ap nazar aa jati theen "
                "to ek aam sa match bhi dil ke liye khaas ban jata tha. Aur jab ap na hoti theen, "
                "to jeet bhi kuch adhoori si lagti thi… shayad is liye ke meri nazar score se pehle "
                "hamesha ap ko talash karti thi."
            ),
            "placeholder": (
                "Main volleyball khelta zaroor tha, lekin sach kahun to meri tawajju aksar game se "
                "zyada ap ko dhoondne mein hoti thi. Pata nahi kyun, lekin jab ap nazar aa jati theen "
                "to ek aam sa match bhi dil ke liye khaas ban jata tha. Aur jab ap na hoti theen, "
                "to jeet bhi kuch adhoori si lagti thi… shayad is liye ke meri nazar score se pehle "
                "hamesha ap ko talash karti thi."
            ),
        },
        {
            "id": "mem_3",
            "category": "Jab Ap Khaas Ban Gayin",
            "title": "Jab Ap Khaas Ban Gayin",
            "icon": "✨",
            "accent_color": "#f472b6",
            "preview": "Pata hi nahi chala ke ek aam sa rishta dil ke itna qareeb kab aa gaya.",
            "full_text": (
                "Mujhe khud nahi pata ke woh kaunsa lamha tha jab sab kuch badal gaya. Bas ap ki "
                "rehnumai, hamari choti choti baatein aur ek doosre ko samajhte samajhte pata hi nahi "
                "chala ke ap mere liye itni khaas kab ban gayin. Shayad kuch rishte ek pal mein nahi "
                "bante… woh aahista aahista dil mein utarte hain, aur phir ek din ehsaas hota hai "
                "ke ab unke baghair sab kuch adhoora sa lagta hai."
            ),
            "placeholder": (
                "Mujhe khud nahi pata ke woh kaunsa lamha tha jab sab kuch badal gaya. Bas ap ki "
                "rehnumai, hamari choti choti baatein aur ek doosre ko samajhte samajhte pata hi nahi "
                "chala ke ap mere liye itni khaas kab ban gayin. Shayad kuch rishte ek pal mein nahi "
                "bante… woh aahista aahista dil mein utarte hain, aur phir ek din ehsaas hota hai "
                "ke ab unke baghair sab kuch adhoora sa lagta hai."
            ),
        },
        {
            "id": "mem_4",
            "category": "Meri Sab Se Bari Ghalti",
            "title": "Meri Sab Se Bari Ghalti",
            "icon": "🥀",
            "accent_color": "#f87171",
            "preview": "Kuch ghaltiyan waqt ke saath purani ho jati hain… lekin dil ka bojh kam nahi hota.",
            "full_text": (
                "Maine hamari baatein un logon tak pohancha dein jahan unhein kabhi nahi jana "
                "chahiye tha. Baad mein jab bharosa toota to dukh un se zyada apne aap se hua… "
                "kyun ke pehli zimmedari meri thi. Mujhe ap ke bharose, ap ki izzat aur hamari baaton "
                "ki hifazat karni chahiye thi. Shayad kuch ghaltiyan maafi ke baad bhi dil par bojh "
                "ban kar reh jaati hain… aur meri ye ghalti unhi mein se ek hai."
            ),
            "placeholder": (
                "Maine hamari baatein un logon tak pohancha dein jahan unhein kabhi nahi jana "
                "chahiye tha. Baad mein jab bharosa toota to dukh un se zyada apne aap se hua… "
                "kyun ke pehli zimmedari meri thi. Mujhe ap ke bharose, ap ki izzat aur hamari baaton "
                "ki hifazat karni chahiye thi. Shayad kuch ghaltiyan maafi ke baad bhi dil par bojh "
                "ban kar reh jaati hain… aur meri ye ghalti unhi mein se ek hai."
            ),
        },
        {
            "id": "mem_5",
            "category": "Do Saal Ki Khamoshi",
            "title": "Do Saal Ki Khamoshi",
            "icon": "⏳",
            "accent_color": "#a78bfa",
            "preview": "Do saal ki khamoshi thi… lekin dil ke andar sab kuch ab bhi zinda tha.",
            "full_text": (
                "Do saal tak hamare darmiyan koi baat nahi hui… lekin khamoshi ka matlab ye kabhi "
                "nahi tha ke sab kuch khatam ho gaya tha. Ap ki yaadein, apni ghaltiyon ka afsos aur "
                "wo khaali pan jo ap ke baghair mehsoos hota tha, har din mere saath raha. Waqt guzarta "
                "raha, zindagi chalti rahi… lekin dil ke andar ek jagah aisi thi jo bilkul waisi hi "
                "rahi. Shayad isi liye ke kuch log door ho jaate hain, magar unki kami dil se kabhi door nahi hoti."
            ),
            "placeholder": (
                "Do saal tak hamare darmiyan koi baat nahi hui… lekin khamoshi ka matlab ye kabhi "
                "nahi tha ke sab kuch khatam ho gaya tha. Ap ki yaadein, apni ghaltiyon ka afsos aur "
                "wo khaali pan jo ap ke baghair mehsoos hota tha, har din mere saath raha. Waqt guzarta "
                "raha, zindagi chalti rahi… lekin dil ke andar ek jagah aisi thi jo bilkul waisi hi "
                "rahi. Shayad isi liye ke kuch log door ho jaate hain, magar unki kami dil se kabhi door nahi hoti."
            ),
        },
        {
            "id": "mem_6",
            "category": "Accident Aur Ap Ki Dua",
            "title": "Accident Aur Ap Ki Dua",
            "icon": "🤲",
            "accent_color": "#fcd34d",
            "preview": "Jab hosh kam tha… dil phir bhi ap ko yaad kar raha tha.",
            "full_text": (
                "Jab main zindagi aur behoshi ke darmiyan tha, mujhe khud kuch yaad nahi… lekin "
                "ye jaan kar ke ap ki duaein mere liye uth rahi theen, dil ko ajeeb sa sukoon milta hai. "
                "Aur jab hosh wapas aaya, sab se pehle jo naam dil ne mehsoos kiya, wo ap ka tha. "
                "Shayad isi liye kuch log sirf yaadon mein nahi rehte… wo insan ki saanson aur duaon ka hissa ban jaate hain."
            ),
            "placeholder": (
                "Jab main zindagi aur behoshi ke darmiyan tha, mujhe khud kuch yaad nahi… lekin "
                "ye jaan kar ke ap ki duaein mere liye uth rahi theen, dil ko ajeeb sa sukoon milta hai. "
                "Aur jab hosh wapas aaya, sab se pehle jo naam dil ne mehsoos kiya, wo ap ka tha. "
                "Shayad isi liye kuch log sirf yaadon mein nahi rehte… wo insan ki saanson aur duaon ka hissa ban jaate hain."
            ),
        },
        {
            "id": "mem_7",
            "category": "Ap Ka Dobara Lautna",
            "title": "Ap Ka Dobara Lautna",
            "icon": "🕊️",
            "accent_color": "#38bdf8",
            "preview": "Kuch cheezen wapas mil kar bhi nayi nahi lagtin… wo bas apni lagti hain.",
            "full_text": (
                "Itne arsay ke baad ap ka ehsaas dobara meri zindagi mein lautna aisa tha jaise "
                "dil ne apni koi bohat purani, bohat apni cheez dobara paa li ho. Us pal laga ke "
                "zindagi ne meri khoi hui duniya ka ek hissa mujhe wapas kar diya."
            ),
            "placeholder": (
                "Itne arsay ke baad ap ka ehsaas dobara meri zindagi mein lautna aisa tha jaise "
                "dil ne apni koi bohat purani, bohat apni cheez dobara paa li ho. Us pal laga ke "
                "zindagi ne meri khoi hui duniya ka ek hissa mujhe wapas kar diya."
            ),
        },
        {
            "id": "mem_8",
            "category": "Aaj — Ye Lamha",
            "title": "Aaj — Ye Lamha",
            "icon": "🌙",
            "accent_color": "#f1f5f9",
            "preview": "Sab kuch seh liya tha… bas ap ka yun door jana kabhi socha nahi tha.",
            "full_text": (
                "Itna sab kuch sehne ke baad bhi dil ne kabhi ye tasavvur nahi kiya tha ke ek din "
                "ap ko apne se door jaate hue dekhna parega. Shayad is liye ke kahin na kahin dil ko "
                "hamesha ye umeed thi ke ap yunhi paas rahengi. Lekin aaj jab ye faasla haqeeqat ban "
                "kar saamne khara hai, to samajh aa raha hai ke kuch alvida sirf lafzon se nahi hote… "
                "wo andar bohat gehri khamoshi chhor jaate hain."
            ),
            "placeholder": (
                "Itna sab kuch sehne ke baad bhi dil ne kabhi ye tasavvur nahi kiya tha ke ek din "
                "ap ko apne se door jaate hue dekhna parega. Shayad is liye ke kahin na kahin dil ko "
                "hamesha ye umeed thi ke ap yunhi paas rahengi. Lekin aaj jab ye faasla haqeeqat ban "
                "kar saamne khara hai, to samajh aa raha hai ke kuch alvida sirf lafzon se nahi hote… "
                "wo andar bohat gehri khamoshi chhor jaate hain."
            ),
        },
    ],
}

# -----------------------------------------------------------------------------
# CHAPTER 3 — WORDS FROM MY HEART
# -----------------------------------------------------------------------------
WORDS_SECTION = {
    "eyebrow": "DIL KI BAAT",
    "title": "Woh Alfaaz Jo Main Keh Nahi Saka",
    "subtitle": "Kaash ye sachchi baatein main waqt par keh pata...",
    "paragraphs": [
        (
            "Main jaanta hoon ke hamare darmiyan jo sab se gehra zakhm bana, uski wajah "
            "meri ghalti thi. Maine woh baatein doosron ko bata dein jo sirf hamare darmiyan "
            "rehni chahiye theen. Us waqt main samajh nahi saka ke mohabbat ka matlab "
            "sirf jazbaat nahi—bharosa, izzat aur privacy ki hifazat bhi hota hai."
        ),
        (
            "Main guzra hua waqt badal nahi sakta. Ap ko meri wajah se jo takleef mili, "
            "main usay mita nahi sakta. Lekin agar mera afsos waqt ko peechhe le ja sakta, "
            "to main apni kahani ko poori duniya se chhupa kar sirf apne dil mein rakhta."
        ),
        (
            "Do saal ki khamoshi mein bhi koi din aisa nahi tha jab ap meri yaadon se door rahi ho. "
            "Main ye is liye nahi likh raha ke ap ko guilty feel ho. Main ye is liye likh raha hoon "
            "ke ap jaanein ke meri mohabbat sirf alfaaz nahi thi."
        ),
    ],
    "closing_thought": (
        "Main ye sab is liye nahi keh raha ke ap ko rokun. Main ye is liye keh raha hoon "
        "ke ap jaanein ke ek insaan tha jiske liye ap duniya thi."
    ),
}

# -----------------------------------------------------------------------------
# CHAPTER 4 — WHY I RESPECT YOU (Crown-Jewel Hero Feature)
# -----------------------------------------------------------------------------
RESPECT_SECTION = {
    "eyebrow": "✧ MERI NAZAR MEIN AAP KA MAQAM ✧",
    "title": "Why I Respect You",
    "subtitle": "Ye koi behas ya shikwa nahi, balke dil ki gehraiyon se nikli sachi tareef aur be-inteha izzat hai.",
    "plates": [
        {
            "tag": "✦ HONORED TRAIT #01",
            "title": "Rab Ki Mohabbat & Khauf-e-Khuda",
            "icon": "🕊️",
            "summary": "Jab bhi maine rabtay ki koshish ki, aap ne mujhe yaad dilaya ke hum na-mehram hain aur aap Allah ko naraz nahi karna chahtin.",
            "detail": (
                "Aap ne ye baat logon ke darr ya dikhawe se nahi kahi thi. Ye baat aap ke dil mein apne Rab ki sachi mohabbat, haya aur khauf se nikli thi. "
                "Is baat ne mujhe ruk kar sochne par majboor kiya ke ek pakiza aur ba-waqar shakhsiyat kaisi hoti hai."
            ),
            "quote": "“Aap ki is baat ne meri nazar mein aap ki izzat ko hamesha ke liye aasmaan par pohancha diya.”",
        },
        {
            "tag": "✦ SACRED VIRTUE #02",
            "title": "Haya, Pakeezgi & Khud-Daari",
            "icon": "👑",
            "summary": "Aap ne hamesha apne kirdaar, sharafat aur hudood ki aisi hifazat ki jis ki misaal bohot kam milti hai.",
            "detail": (
                "Is se meri izzat aap ke liye kabhi kam nahi hui, balke har guzarte din ke sath barhti gayi. "
                "Aap ki pakeezgi ne mujhe sikhaya ke kisi ki sachhi qadar karna us ki hudood ka ehtaram karne se shuru hota hai."
            ),
            "quote": "“Ek ba-waqar shakhsiyat ka sab se bada gehna us ki haya aur us ka khud-aitemadi se bhara kirdaar hota hai.”",
        },
        {
            "tag": "✦ GUIDING PRINCIPLE #03",
            "title": "Sahih Raastay Ka Sabaq",
            "icon": "✨",
            "summary": "Aap ne mujhe samjhaya ke agar iraada sachcha ho to chhup kar baat karna nahi, balke izzat se saamne aana hota hai.",
            "detail": (
                "Aap ke is rawaiye ne mujhe ye samajh diya ke mera pehla maqsad chhupa kar raastay dhoondna nahi hona chahiye, "
                "balke mujhe itna ba-kirdaar aur qabil banna chahiye ke main sahih tareeqay se, poori izzat ke sath aap ke liye khara ho sakun."
            ),
            "quote": "“Iraada sachcha ho to raastay bhi saaf aur pur-waqar hone chahiyein.”",
        },
        {
            "tag": "✦ TIMELESS PLEDGE #04",
            "title": "Aap Ke Imaan Aur Sukoon Ki Hifazat",
            "icon": "🤍",
            "summary": "Main aap ko kabhi aisi kashmakash mein nahi dekhna chahta jahan aap ko apne Rab aur jazbaat mein se kisi ko chunna paray.",
            "detail": (
                "Agar kabhi Allah ne hamari qismat mein bhalayi likhi, to meri hamesha ye dua rahegi ke woh aise ho jahan Allah raazi ho, "
                "aap ka ghar aur dil sukoon mein ho, aap ki izzat mehfooz ho, aur koi chhupa hua raasta ya dabao na ho."
            ),
            "quote": "“Aap ki izzat aur sukoon meri har khwahish se pehle hai aur hamesha rahegi.”",
        },
    ],
    "main_content": [
        "Jab bhi maine ap se contact karne ki koshish ki, ap ne ek baat kahi jo mujhe ruk kar sochne par majboor kar deti thi.",
        "Ap ne mujhe yaad dilaya ke hum na-mehram hain, aur ke ap Allah ko naraz nahi karna chahtin. Ye baat ap ne logon ke darr se nahi kahi thi. Ye baat ap ne apne Rab ki mohabbat aur khauf se kahi thi.",
        "Isse meri izzat ap k liye kam nahi hui—balke aur barh gayi.",
        "Isse mujhe ye samajh aaya ke agar mera iraada sachcha hai, to mera pehla maqsad chhup kar baat karne ke tareeqe dhoondna nahi hona chahiye. Mera pehla maqsad ye hona chahiye ke main itna qabil banun ke ap k saamne sahih tareeqe se, izzat ke saath aa sakun.",
        "Main ap ko kabhi us position mein nahi rakhna chahta jahan ap ko apne jazbaat aur apne Rab ke rishte mein se kisi ek ko chunna pade."
    ],
    "golden_line": (
        "Meri sab se bari koshish ye nahi honi chahiye ke main chhupe raastay dhoondun... "
        "meri koshish ye honi chahiye ke main itna qabil banun ke sahih raastay aur poori izzat ke sath aa sakun."
    ),
    "signature_seal": "Izzat jo alfaaz se nahi, dil ki gehraiyon se di jaati hai.",
    "closing": (
        "Agar kabhi Allah ne hamari qismat mein bhalayi likhi, to main chahta hoon ke woh aise ho "
        "jahan Allah raazi ho, aap ka ghar sukoon mein ho, aap ki izzat salamat ho, "
        "aur koi chhupa hua raasta ya dabao na ho."
    ),
}

# -----------------------------------------------------------------------------
# CHAPTER 5 — WHAT I LEARNED (Self-Accountability)
# -----------------------------------------------------------------------------
LEARNED_SECTION = {
    "eyebrow": "SEEKH AUR AFSOOS",
    "title": "Ap Se Mohabbat Ne Mujhe Kya Sikhaya",
    "subtitle": "Har rishte mein insaan kuch seekhta hai. Maine bhi seekha.",
    "lessons": [
        {
            "title": "Bharosa Ek Amanat Hai",
            "content": (
                "Kisi ki personal baat doosron ko batana — chahe naadaani mein hi sahi — "
                "ek amanat mein khayanat hai. Ye sabaq mujhe sab se mehnga pada."
            ),
        },
        {
            "title": "Sachche Jazbaat Ghalat Harkatein Justify Nahi Karte",
            "content": (
                "Sirf is liye ke mere dil mein mohabbat thi, iska matlab ye nahi ke mera har qadam sahih tha. "
                "Achi niyyat ke baawajood kuch cheezein main aur behtar handle kar sakta tha."
            ),
        },
        {
            "title": "Sabr Ka Matlab Sirf Intezaar Nahi",
            "content": (
                "Sabr ka matlab hai apne aap ko behtar banana us waqt ke liye jab Allah mauqa de. "
                "Main ne seekha ke bechain hona mohabbat nahi, balke apne aap par qabu na hona hai."
            ),
        },
        {
            "title": "Izzat Dene Ka Matlab",
            "content": (
                "Kisi ki izzat karna sirf unke saamne ache alfaaz bolna nahi. "
                "Izzat ka matlab hai unki na-maujoodgi mein bhi unka naam mehfooz rakhna."
            ),
        },
    ],
    "honest_note": (
        "Main perfect insaan nahi hoon. Main ne ghaltiyan ki hain. Emotions ne mujhe besabra bhi banaya. "
        "Lekin har ghalti ne mujhe ye dikha diya ke agar main sachchi mohabbat ka haqdar banna chahta hoon, "
        "to mujhe pehle khud ko badalna hoga."
    ),
}

# -----------------------------------------------------------------------------
# CHAPTER 6 — INTENTIONS
# -----------------------------------------------------------------------------
INTENTIONS_SECTION = {
    "eyebrow": "SACHCHE IRADEY",
    "title": "Mera Dil Asal Mein Kya Chahta Hai",
    "subtitle": "Ye koi dawa nahi. Ye iradey hain — sachche aur khalis.",
    "intentions": [
        {
            "title": "Ap Ki Khushi",
            "content": (
                "Chahe hamare raaste milein ya na milein — mera sabse pehla iraada ye hai "
                "ke ap khush rahein. Ap ki khushi mere liye kisi bhi cheez se zyada ahem hai."
            ),
        },
        {
            "title": "Ap K Ghar Walon Ka Sukoon",
            "content": (
                "Main kabhi nahi chahunga ke ap apne ghar walon ko mere liye khoyen. "
                "Jin logon ne ap ko pala, ap ki hifazat ki — unka sukoon mere liye bhi zaroori hai. "
                "Agar kabhi main ap ki zindagi mein aaunga, to main chahunga ke ap k apnon ko bhi "
                "is faislay par sukoon ho."
            ),
        },
        {
            "title": "Sahih Raasta",
            "content": (
                "Agar Allah ne hamare liye koi bhalayi likhi hai, to main chahta hoon ke woh "
                "sahih tareeqe se aaye — izzat ke saath, khul kar, bina kisi chhupao ke. "
                "Main chhup kar baat karne mein yakeen nahi rakhta."
            ),
        },
        {
            "title": "Khud Ko Behtar Banana",
            "content": (
                "Chahe kuch bhi ho, main apne aap ko behtar insaan banata rahunga. "
                "Ye kisi ke liye nahi — ye mera apna farz hai. Lekin agar kabhi mauqa mila, "
                "to main chahta hoon ke us waqt main us laayiq hoon."
            ),
        },
    ],
    "family_note": (
        "Main samajhta hoon ke ap k apne ap k liye protective hain. Ye unki mohabbat hai. "
        "Main un logon ko challenge nahi karna chahta — main unka aitbaar jeetna chahta hoon."
    ),
}

# -----------------------------------------------------------------------------
# CHAPTER 7 — DUA
# -----------------------------------------------------------------------------
DUA_SECTION = {
    "eyebrow": "EK KHALIS DUA",
    "title": "Dil Ki Gehraiyon Se Nikli Dua",
    "subtitle": "Jab kuch na kar saka, to Rab ke aage haath utha diye.",
    "paragraphs": [
        (
            "Ya Allah, Tu hamare dilon ka haal jaanta hai. Tu hamari mohabbat, hamari ghaltiyan, "
            "hamari takleef aur woh har baat jaanta hai jo hum kabhi ek doosre se keh nahi sake."
        ),
        (
            "Agar hamara saath hum dono ke haq mein behtar hai, to hamare darmiyan khari har deewar "
            "hata de. Hamari ghaltiyan maaf kar de, hamare dil narm kar de, aur izzat ke saath "
            "hamare raste dobara mila de."
        ),
        (
            "Aur agar hamara saath muqaddar mein nahi, to woh jahan bhi rahe usay hamesha "
            "khush, mehfooz aur pur-sukoon rakhna — chahe uske saath khara hone wala shakhs main na rahun."
        ),
        (
            "Lekin Ya Allah... agar abhi bhi koi rasta baqi hai, to isay hamara aakhri alvida "
            "mat banne dena."
        ),
    ],
    "closing_ayah": "Hasbunallahu wa ni'mal wakeel.",
    "closing_meaning": "Allah hamara kaafi hai, aur woh sab se behtar karsaaz hai.",
}

# -----------------------------------------------------------------------------
# CHAPTER 8 — THANK YOU
# -----------------------------------------------------------------------------
THANKYOU_SECTION = {
    "eyebrow": "DIL SE SHUKRIYA",
    "title": "Har Us Lamhe Ka Shukriya",
    "subtitle": "Har us lamhe ke liye jo ap ne meri zindagi ko diya...",
    "gratitudes": [
        "Mujhe samjhane aur guide karne ka shukriya.",
        "Volleyball khelte hue dekhne wale un chote lekin khoobsurat lamhon ka shukriya.",
        "Us waqt mere liye dua karne ka shukriya jab main khud apne liye dua karne ke qabil nahi tha.",
        "Do saal ki khamoshi ke baad meri zindagi mein dobara lautne ka shukriya.",
        "Meri ghaltiyon ke bawajood hamari kahani ko ek aur mauqa dene ka shukriya.",
        "Mujhe ye sikhane ka shukriya ke mohabbat mein izzat sab se pehle aati hai.",
    ],
    "closing": (
        "Main ap ka shukriya is liye nahi kar raha ke main ap ko khone ke liye tayyar hoon. "
        "Main shukriya is liye kar raha hoon kyun ke ap se mohabbat ne mujhe hamesha ke liye badal diya."
    ),
    "wishes": [
        "Ap ki zindagi mein hamesha khushi ho.",
        "Ap ki har dua qubool ho.",
        "Ap ko woh sab kuch mile jo ap deserve karti hain.",
        "Ap ki aankhon mein kabhi aansu na aayein.",
        "Ap jahan bhi jaayein, ap ki raahein aasan hon.",
    ],
}

# -----------------------------------------------------------------------------
# CHAPTER 9 — FINAL NOTE (Goodbye)
# -----------------------------------------------------------------------------
GOODBYE_SECTION = {
    "eyebrow": "AAKHRI BAAT",
    "title": "Ek Alvida... Jo Dil Se Juda Nahi Karta",
    "subtitle": "Kuch rishte duaon mein zinda rehte hain aur faisla Rab par chor dete hain.",
    "paragraphs": [
        (
            "Agar zindagi ap ko mujhse door le jaaye, to main hamari yaadon ko "
            "talkhi mein nahi badlunga. Main ap ko izzat ke saath yaad rakhunga."
        ),
        (
            "Aur agar hamare raaste kabhi ek hone ke liye nahi likhe gaye, to bhi main dua karunga "
            "ke Allah ap k liye jo shakhs aur jo zindagi chunein, woh ap ko sukoon dein."
        ),
        (
            "Lekin agar zindagi ne kabhi mujhe ek sachcha, izzat bhara mauqa diya ke main ap k saamne "
            "dobara aa sakun — to main umeed karta hoon ke us waqt tak main ek behtar, "
            "zyada zimmadar insaan ban chuka hounga."
        ),
    ],
    "highlighted_line": (
        "Kuch mohabbatein thamne ko kehti hain. "
        "Kuch mohabbatein dua karna seekh leti hain... aur faisla Allah par chor deti hain."
    ),
    "final_visual_text": "Tumhari jagah mere dil mein hamesha khaas rahe gi.",
    "button_label": "Meri Aakhri Baat Parhein",
    "revealed_text": (
        "Main ap se ye nahi keh raha ke ap apni takleef bhool jao. Main sirf ek sachhi aur aakhri baat ka "
        "mauqa maang raha hoon, is se pehle ke hamare itne saalon ki yaadein hamesha ki khamoshi ban jayein. "
        "Agar hamare liye abhi bhi koi chota sa rasta baqi hai, to please bina dil ki baat sune mat jaana."
    ),
    "absolute_last_line": (
        "Alvida nahi kehta... bas itna kehta hoon: "
        "Allah hafiz. Dua mein yaad rakhna."
    ),
}
