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
    {"id": "intentions", "title": "Intentions",         "desc": "Meri sachchi duaein aur iradey jo sirf ap ki khushi ke liye hain.", "thumb": "thumb_intentions"},
    {"id": "goodbye",    "title": "Final Note",         "desc": "Ek aakhri baat... mohabbat, izzat aur duaon ke saath.", "thumb": "thumb_goodbye"},
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
            "category": "Jab Ap Achi Lagne Lageen",
            "icon": "✨",
            "accent_color": "#38bdf8",
            "placeholder": (
                "Mujhe yaad nahi ke woh kaunsa ek lamha tha. Bas ap ki rehnumai, hamari baaton "
                "aur ek doosre ko samajhte samajhte ap mere liye sab kuch ban gayi."
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
            "category": "Accident Aur Ap Ki Dua",
            "icon": "🤲",
            "accent_color": "#fbbf24",
            "placeholder": (
                "Jab main zindagi aur behoshi ke darmiyan tha, ap ki duaein mere saath theen. "
                "Jab mujhe hosh aaya, mere dil ne sab se pehle sirf ap ko yaad kiya."
            ),
        },
        {
            "category": "Ap Ka Dobara Lautna",
            "icon": "🕊️",
            "accent_color": "#14b8a6",
            "placeholder": (
                "Itne arsay ke baad ap ki awaaz dobara sunna aisa tha jaise zindagi ne mujhe "
                "meri khoi hui duniya wapas kar di ho."
            ),
        },
        {
            "category": "Aaj — Ye Lamha",
            "icon": "🌙",
            "accent_color": "#d4796a",
            "placeholder": (
                "Itna sab kuch sehne ke baad bhi maine kabhi nahi socha tha ke ek din main "
                "ap ko apne se door jaate hue dekhunga. Lekin aaj yehi sach hai."
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
# CHAPTER 4 — WHY I RESPECT YOU (Special Visual Treatment)
# -----------------------------------------------------------------------------
RESPECT_SECTION = {
    "eyebrow": "WOH BAAT JO AP KO AUR KHOOBSURAT BANATI HAI",
    "title": "Woh Baat Jis Ki Main Hamesha Izzat Karunga",
    "subtitle": "Ye koi behas nahi, dil se nikli sachi tareef aur izzat hai.",
    "main_content": [
        (
            "Jab bhi maine ap se contact karne ki koshish ki, ap ne ek baat kahi jo mujhe "
            "ruk kar sochne par majboor kar deti thi."
        ),
        (
            "Ap ne mujhe yaad dilaya ke hum na-mehram hain, aur ke ap Allah ko naraz nahi karna chahtin. "
            "Ye baat ap ne logon ke darr se nahi kahi thi. Ye baat ap ne apne Rab ki mohabbat aur khauf se kahi thi."
        ),
        (
            "Isse meri izzat ap k liye kam nahi hui—balke aur barh gayi."
        ),
        (
            "Isse mujhe ye samajh aaya ke agar mera iraada sachcha hai, to mera pehla maqsad "
            "chhup kar baat karne ke tareeqe dhoondna nahi hona chahiye. Mera pehla maqsad ye hona chahiye "
            "ke main itna qabil banun ke ap k saamne sahih tareeqe se, izzat ke saath aa sakun."
        ),
        (
            "Main ap ko kabhi us position mein nahi rakhna chahta jahan ap ko apne jazbaat "
            "aur apne Rab ke rishte mein se kisi ek ko chunna pade."
        ),
    ],
    "golden_line": (
        "Meri sab se bari koshish ye nahi honi chahiye ke ap ko ek aur message bhejun. "
        "Meri sab se bari koshish ye honi chahiye ke main is qabil banun ke sahih raaste se ap k liye aa sakun."
    ),
    "closing": (
        "Agar kabhi Allah ne hamari kismet mein bhalayi likhi, to main chahta hoon ke woh aise ho "
        "jahan Allah raazi ho, ap ka ghar sukoon mein ho, ap ki izzat salamat ho, "
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
