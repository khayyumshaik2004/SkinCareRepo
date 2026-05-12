from gtts import gTTS
import os

texts = {
    "en": {
        "acne": (
            "For acne-prone skin, consistency and balance are key. Wash your face twice a day "
            "using a mild salicylic acid cleanser to remove excess oil and dirt without over-drying. "
            "Avoid touching your face frequently, and never pop pimples as it may lead to scarring. "
            "Drink plenty of water, and include foods rich in zinc, vitamin A, and antioxidants like spinach and berries. "
            "Avoid oily, fried, and processed foods that can worsen breakouts. "
            "Use oil-free moisturizers and apply sunscreen daily, even when indoors. "
            "Regular sleep, reduced stress, and a consistent skincare routine will help your skin heal naturally over time."
        ),
        "dry": (
            "For dry skin, hydration is your best friend. Start your day with a gentle, hydrating cleanser "
            "that doesn’t strip away your natural oils. After cleansing, apply a rich moisturizer containing hyaluronic acid, "
            "ceramides, or shea butter to lock in moisture. Drink plenty of water throughout the day to hydrate from within. "
            "Include foods like avocados, almonds, and omega-rich seeds in your diet to nourish your skin. "
            "Avoid long, hot showers and harsh soaps that can worsen dryness. "
            "Using a humidifier at home and applying sunscreen daily will protect your skin barrier and keep it soft and smooth."
        ),
        "oily": (
            "For oily skin, balance is important. Use a lightweight foaming cleanser to remove excess oil without stripping your skin. "
            "Incorporate a toner with witch hazel or niacinamide to reduce shine and minimize pores. "
            "Avoid over-washing, as it can trigger your skin to produce even more oil. "
            "Use an oil-free moisturizer to maintain hydration without clogging pores. "
            "Weekly gentle exfoliation with a mild chemical exfoliant helps prevent blackheads and acne. "
            "Eat more fresh fruits, vegetables, and fiber, and avoid fried or sugary foods. "
            "A consistent skincare routine and proper diet will help control oil production naturally."
        )
    },
    "te": {
        "acne": (
            "ముక్కుప్పు చర్మం ఉన్నవారు రోజూ రెండు సార్లు మృదువైన క్లెన్సర్‌తో ముఖం కడగాలి. "
            "సాలిసిలిక్ యాసిడ్ లేదా నియాసినమైడ్ ఉన్న ఉత్పత్తులు వాడడం చర్మంలోని మలినాలను తొలగించడంలో సహాయపడుతుంది. "
            "ముఖాన్ని తరచుగా తాకరాదు, అలాగే పింపుల్స్ పగలగొట్టకండి. "
            "తగినంత నీరు త్రాగండి మరియు పండ్లు, కూరగాయలు ఎక్కువగా తినండి. "
            "నూనె పదార్థాలు, జంక్ ఫుడ్ తగ్గించండి. "
            "నాన్-కోమెడోజెనిక్ మాయిశ్చరైజర్ మరియు సన్‌స్క్రీన్ వాడండి. "
            "తగిన నిద్రపోవడం మరియు ఒత్తిడిని తగ్గించడం ద్వారా మీ చర్మం సహజంగా మెరుగుపడుతుంది."
        ),
        "dry": (
            "ఎండిన చర్మం ఉన్నవారు హైడ్రేషన్‌పై ప్రత్యేక శ్రద్ధ చూపాలి. "
            "సోపులు మరియు వేడి నీటిని తప్పించండి, అవి చర్మంలోని సహజ తేమను తగ్గిస్తాయి. "
            "హయాలూరోనిక్ యాసిడ్, సిరమైడ్స్ ఉన్న మాయిశ్చరైజర్ ఉపయోగించండి. "
            "రోజంతా తగినంత నీరు త్రాగండి మరియు అవకాడో, వేరుశనగలు, మరియు ఓమెగా-3 ఫ్యాటీ ఆమ్లాలు ఉన్న ఆహారం తీసుకోండి. "
            "ఇంటి లోపల హ్యూమిడిఫైయర్ వాడడం కూడా చర్మాన్ని తేమగా ఉంచుతుంది. "
            "సన్‌స్క్రీన్ ఉపయోగించడం మరచిపోవద్దు, అది చర్మాన్ని పొడిబారడం నుండి కాపాడుతుంది."
        ),
        "oily": (
            "ఆయిలీ చర్మం ఉన్నవారు తేలికపాటి ఫోమింగ్ క్లెన్సర్ ఉపయోగించాలి. "
            "రోజుకు రెండు సార్లు ముఖం కడగడం సరిపోతుంది, ఎక్కువ సార్లు కడగడం ఆయిల్ ఉత్పత్తిని పెంచుతుంది. "
            "విచ్ హేజల్ లేదా నియాసినమైడ్ ఉన్న టోనర్ వాడండి. "
            "ఆయిల్ ఫ్రీ మాయిశ్చరైజర్ వాడి చర్మానికి తేమను సమతుల్యం చేయండి. "
            "తిన్న ఆహారంలో పండ్లు, కూరగాయలు మరియు నీరు ఎక్కువగా తీసుకోండి. "
            "తలస్నానం తర్వాత చర్మం తడిగా ఉన్నప్పుడు తేలికపాటి మాయిశ్చరైజర్ రాసుకోవడం మంచిది."
        )
    },
    "hi": {
        "acne": (
            "मुंहासे वाली त्वचा के लिए नियमित देखभाल बहुत ज़रूरी है। "
            "दिन में दो बार हल्के सैलिसिलिक एसिड वाले क्लेंज़र से चेहरा धोएं ताकि तेल और गंदगी निकल जाए। "
            "चेहरे को बार-बार छूने से बचें और पिंपल्स न फोड़ें। "
            "पर्याप्त मात्रा में पानी पिएं और हरी सब्ज़ियां, फल, और विटामिन ए से भरपूर भोजन खाएं। "
            "तेलिय और तले हुए भोजन से बचें। "
            "ऑयल-फ्री मॉइस्चराइज़र और सनस्क्रीन का उपयोग करें। "
            "अच्छी नींद और तनावमुक्त जीवन से आपकी त्वचा स्वाभाविक रूप से साफ़ और स्वस्थ दिखेगी।"
        ),
        "dry": (
            "सूखी त्वचा के लिए हाइड्रेशन सबसे ज़रूरी है। "
            "मॉर्निंग और नाइट रूटीन में हल्के क्लींजर और हाइड्रेटिंग मॉइस्चराइज़र का प्रयोग करें। "
            "हायालुरोनिक एसिड और सेरामाइड्स वाली क्रीम आपकी त्वचा की नमी को बरकरार रखेगी। "
            "पर्याप्त पानी पिएं और एवोकाडो, बादाम, और ओमेगा फैटी एसिड्स से भरपूर भोजन लें। "
            "गर्म पानी से स्नान न करें और बहुत ज़्यादा साबुन से परहेज़ करें। "
            "सनस्क्रीन का उपयोग करना न भूलें ताकि आपकी त्वचा नरम और चमकदार बनी रहे।"
        ),
        "oily": (
            "तैलीय त्वचा के लिए हल्का फोमिंग क्लेंज़र दिन में दो बार इस्तेमाल करें। "
            "विच हेज़ल या नियासिनामाइड वाले टोनर का प्रयोग करें ताकि अतिरिक्त तेल कम हो। "
            "ऑयल-फ्री मॉइस्चराइज़र लगाएं ताकि त्वचा हाइड्रेटेड रहे लेकिन चिपचिपी न लगे। "
            "सप्ताह में एक या दो बार हल्का एक्सफोलिएशन करें ताकि ब्लैकहेड्स और मुंहासे न हों। "
            "फल और सब्ज़ियों का सेवन बढ़ाएं और तले हुए या मीठे भोजन से दूरी रखें। "
            "नियमित स्किनकेयर रूटीन से त्वचा का तेल संतुलित रहेगा और चेहरा ताज़ा दिखेगा।"
        )
    }
}

# 🎧 Generate Audio Files
for lang, skindata in texts.items():
    folder = f"static/audios/{lang}"
    os.makedirs(folder, exist_ok=True)
    for skin, text in skindata.items():
        tts = gTTS(text=text, lang=lang)
        tts.save(f"{folder}/{skin}.mp3")

print("✅ All 1-minute audio files generated successfully!")
