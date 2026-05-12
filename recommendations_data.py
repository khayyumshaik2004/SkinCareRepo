# recommendations_data.py

RECOMMENDATIONS = {
    'acne': [
        # CLEANSERS
        {'Product_English': 'Minimalist Salicylic Acid Cleanser', 
         'Product_Telugu': 'మినిమలిస్ట్ సాలిసిలిక్ యాసిడ్ క్లెన్సర్',
         'Product_Hindi': 'मिनिमलिस्ट सैलिसिलिक एसिड क्लींजर',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40233784_3-minimalist-salicylic-acid-lha-2-face-cleanser-reduces-sebum-prevents-breakouts.jpg', 
         'Website': 'https://beminimalist.co/products/salicylic-lha-2-cleanser'
        },
        {'Product_English': 'The Derma Co AHA-BHA Foaming Cleanser', 
         'Product_Telugu': 'డెర్మా కో AHA-BHA ఫోమింగ్ క్లెన్సర్',
         'Product_Hindi': 'द डर्मा को AHA-BHA फोमिंग क्लींजर',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40255176_1-the-derma-co-3-aha-bha-foaming-face-wash-oil-free-controls-acne-for-all-skin-types.jpg', 
         'Website': 'https://www.amazon.in/Derma-Co-AHA-BHA-Foaming-Cleanser/dp/B08TRCJZLP'
        },
        {'Product_English': 'Neutrogena Oil-Free Acne Wash', 
         'Product_Telugu': 'న్యూట్రోజినా ఆయిల్-ఫ్రీ యాక్నే వాష్',
         'Product_Hindi': 'न्यूट्रोजीना ऑयल-फ्री एक्ने वॉश',
         'Recommendation': 'https://images.ctfassets.net/f3tkdizvrgki/5w8ARcl9isSp9se8vBncOP/e5cc35e0fb2057053e75f6707c108f84/oilfreeacnewash-hero-fr-ca?fm=webp&w=3840', 
         'Website': 'https://www.amazon.in/Neutrogena-Oil-Free-Acne-Wash-175ml/dp/B01NCBOZQ5'
        },

        # SUNSCREENS
        {'Product_English': 'Re’equil Oxybenzone Free Sunscreen', 
         'Product_Telugu': 'రీక్విల్ ఆక్సిబెన్జోన్ ఫ్రీ సన్‌స్క్రీన్',
         'Product_Hindi': 'रीक्विल ऑक्सीबेंज़ोन फ्री सनस्क्रीन',   
         'Recommendation': 'https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_600/NI_CATALOG/IMAGES/CIW/2025/6/26/0164c176-c7ee-417c-98b7-ce2070215171_944283_1.png', 'Website': 'https://www.swiggy.com/instamart/p/re-equil-oxybenzone-free-sunscreen-spf-50-for-oily-acne-prone-skin-50-R964S6VS8Z'},
        {'Product_English': 'Minimalist Sunscreen SPF 50', 
         'Product_Telugu': 'మినిమలిస్ట్ సన్‌స్క్రీన్ SPF 50',
         'Product_Hindi': 'मिनिमलिस्ट सनस्क्रीन SPF 50',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40341758_2-minimalist-light-fluid-spf-50-pa-face-sunscreen.jpg', 'Website': 'https://www.bigbasket.com/pd/40341758/minimalist-light-fluid-spf-50-pa-face-sunscreen-50-ml/'},
        {'Product_English': 'The Derma Co Matte Sunscreen Gel', 
         'Product_Telugu': 'డెర్మా కో మ్యాట్ సన్‌స్క్రీన్ జెల్',
            'Product_Hindi': 'द डर्मा को मैट सनस्क्रीन जेल',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40255158_1-the-derma-co-ultra-matte-sunscreen-gel-spf-60-lightweight-oil-free-prevents-sun-damages.jpg', 'Website': 'https://www.bigbasket.com/pd/40255158/the-derma-co-ultra-matte-sunscreen-gel-spf-60-lightweight-oil-free-prevents-sun-damages-50-g/'},

        # MOISTURIZERS
        {'Product_English': 'Neutrogena Hydro Boost Water Gel', 
            'Product_Telugu': 'న్యూట్రోజినా హైడ్రో బూస్ట్ వాటర్ జెల్',
            'Product_Hindi': 'न्यूट्रोजीना हाइड्रो बूस्ट वाटर जेल',
         'Recommendation': 'https://images.ctfassets.net/aub2fvcyp2t8/7KNPvxTsaEUZAdlWhF7h0p/016350854a21ef0ab6595b6d7f07536e/nourishing_cream_50g_front-en-in?fm=webp&w=3840', 'Website': 'https://www.bigbasket.com/pd/40171051/neutrogena-hydro-boost-water-gel-50-g/'},
        {'Product_English': 'Minimalist Vitamin B5 10% Moisturizer',
         'Product_Telugu': 'మినిమలిస్ట్ విటమిన్ B5 10% మాయిశ్చరైజర్',
         'Product_Hindi': 'मिनिमलिस्ट विटामिन B5 10% मॉइस्चराइज़र',
          'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40298813_2-minimalist-vitamin-b5-10-moisturizer-with-zinc-copper-magnesium-ha-for-oily-skin-lightweight-repairs-skin.jpg', 'Website': 'https://global.beminimalist.co/products/vitamin-b5-10-moisturizer'},
        {'Product_English': 'Cetaphil Pro Oil Absorbing Moisturizer', 
            'Product_Telugu': 'సెటాఫిల్ ప్రో ఆయిల్ అబ్సార్బింగ్ మాయిశ్చరైజర్',
            'Product_Hindi': 'सेटाफिल प्रो ऑयल एब्जॉर्बिंग मॉइस्चराइज़र',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/xl/40276209_1-cetaphil-pro-oil-control-moisturising-lotion-matte-finish-for-oily-acne-prone-skin-spf-30.jpg', 'Website': 'https://www.bigbasket.com/pd/40276209/cetaphil-pro-oil-control-moisturising-lotion-matte-finish-for-oily-acne-prone-skin-spf-30-120-ml/'},

        # MASKS
        {'Product_English': 'The Ordinary Salicylic Acid Mask', 
         'Product_Telugu': 'ది ఆర్డినరీ సాలిసిలిక్ యాసిడ్ మాస్క్',
            'Product_Hindi': 'द ऑर्डिनरी सैलिसिलिक एसिड मास्क',
         'Recommendation': 'https://escentual.com/cdn/shop/files/the_ordinary_salicylic_acid_2_masque.png?v=1729190562&width=416', 'Website': 'https://escentual.com/products/the-ordinary-salicylic-acid-2-masque?srsltid=AfmBOooUuHdZFlUntYk6MOd2pvqyNAvTtX-QJznZrcJBPzj1BIwQMpCw'},
        {'Product_English': 'O3+ Sulfur Cooling Mask', 
         'Product_Telugu': 'O3+ సల్ఫర్ కూలింగ్ మాస్క్',
            'Product_Hindi': 'O3+ सल्फर कूलिंग मास्क',
         'Recommendation': 'https://rukminim2.flixcart.com/image/480/640/jxz0brk0/face-treatment/z/2/f/50-purifying-sulfur-cooling-facial-mask-with-organic-willow-bark-original-imafgber9hhz7gny.jpeg?q=90', 'Website': 'https://www.o3plus.com/products/purifying-sulfur-cooling-facial-masque?srsltid=AfmBOoqoHsXKrtNiy1Rzfk9aqgxkzkMTEZBd6QPJsZagwXzOlx_k8l7k'},
        {'Product_English': 'Innisfree Volcanic Pore Clay Mask', 
         'Product_Telugu': 'ఇన్నిస్‌ఫ్రీ వోల్కానిక్ పోర్ క్లే మాస్క్',
            'Product_Hindi': 'इनिसफ्री वोल्केनिक पोर्स क्ले मास्क',
         'Recommendation': 'https://beautybellbd.com/wp-content/uploads/2023/12/f19c9085-1.png', 'Website': 'https://beautybellbd.com/product/innisfree-jeju-volcanic-pore-clay-mask-100-ml/?srsltid=AfmBOooTVzTlotpZ-qN63Rg8ajCzO3ZHt07WODR9usJFofeR822gvieW'},

        # SERUMS
        {'Product_English': 'Minimalist Niacinamide 10% Serum', 
         'Product_Telugu': 'మినిమలిస్ట్ నయాసినమైడ్ 10% సీరమ్',
            'Product_Hindi': 'मिनिमलिस्ट नियासिनमाइड 10% सीरम',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40341764_1-minimalist-niacinamide-10-face-serum.jpg', 'Website': 'https://www.bigbasket.com/pd/40341764/minimalist-niacinamide-10-face-serum-10-ml/'},
        {'Product_English': 'The Ordinary Niacinamide 10% + Zinc 1%', 
         'Product_Telugu': 'ది ఆర్డినరీ నయాసినమైడ్ 10% + జింక్ 1%',
            'Product_Hindi': 'द ऑर्डिनरी नियासिनमाइड 10% + जिंक 1%',
         'Recommendation': 'https://lobeautyuae.com/cdn/shop/products/rdn-niacinamide-10pct-zinc-1pct-30ml.png?v=1632913756', 'Website': 'https://www.myntra.com/serum-and-gel/theordinary/the-ordinary-niacinamide-10--zinc-1---30ml/33135565/buy'},
        {'Product_English': 'The Derma Co 10% Niacinamide Serum', 
         'Product_Telugu': 'డెర్మా కో 10% నయాసినమైడ్ సీరమ్',
            'Product_Hindi': 'द डर्मा को 10% नियासिनमाइड सीरम',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40255159_1-the-derma-co-10-niacinamide-face-serum-with-zinc-fragrance-free-for-acne-marks.jpg', 'Website': 'https://www.bigbasket.com/pd/40255159/the-derma-co-10-niacinamide-face-serum-with-zinc-fragrance-free-for-acne-marks-30-ml/'}
    ],

    'dry': [
        # CLEANSERS
        {'Product_English': 'Minimalist Oat Extract Gentle Cleanser', 
         'Product_Telugu': 'మినిమలిస్ట్ ఓట్ ఎక్స్‌ట్రాక్ట్ జెంటిల్ క్లీన్సర్',
            'Product_Hindi': 'मिनिमलिस्ट ओट एक्सट्रैक्ट जेंटल क्लींजर',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/xl/40276165_2-minimalist-6-oat-extract-gentle-cleanser-with-hyaluronic-acid-for-sensitive-skin.jpg', 
         'Website': 'https://www.bigbasket.com/pd/40276165/minimalist-6-oat-extract-gentle-cleanser-with-hyaluronic-acid-for-sensitive-skin-120-ml/'
        },
        {'Product_English': 'CeraVe Hydrating Cream-to-Foam Cleanser', 
         'Product_Telugu': 'సెరావే హైడ్రేటింగ్ క్రీమ్-టు-ఫోమ్ క్లీన్సర్',
            'Product_Hindi': 'सेरावे हाइड्रेटिंग क्रीम-टू-फोम क्लींजर',
         'Recommendation': 'https://www.cerave.ca/en-ca/-/media/project/loreal/brand-sites/cerave/americas/ca/clp/primary/3606000569072_primary.png', 
         'Website': 'https://www.cerave.ca/en-ca/skincare/cleansers/hydrating-cream-to-foam-cleanser'
        },
        {'Product_English': 'Simple Moisturizing Facial Wash', 
         'Product_Telugu': 'సింపుల్ మాయిశ్చరైజింగ్ ఫేసియల్ వాష్',
            'Product_Hindi': 'सिंपल मॉइस्चराइजिंग फेशियल वॉश',
         'Recommendation': 'https://assets.unileversolutions.com/v1/123498785.png', 
         'Website': 'https://www.bigbasket.com/pd/40185922/simple-kind-to-skin-moisturising-facial-wash-150-ml/'
        },

        # SUNSCREENS
        {'Product_English': 'Neutrogena Ultra Sheer Dry-Touch Sunscreen',
            'Product_Telugu': 'న్యూట్రోజినా అల్ట్రా షీర్ డ్రై-టచ్ సన్‌స్క్రీన్',
                'Product_Hindi': 'न्यूट्रोजीना अल्ट्रा शियर ड्राई-टच सनस्क्रीन',
         'Recommendation': 'https://images.ctfassets.net/bcjr30vxh6td/6g1ShR5mVF1HtfrlnhAAvv/c87546d8ded352cd1ba0581170e31143/6868785_Carousel1.webp',    
         'Website': 'https://www.neutrogena.in/sun/ultra-sheer-sunscreen'
        },
        {'Product_English': 'Minimalist Sunscreen SPF 60',
         'Product_Telugu': 'మినిమలిస్ట్ సన్‌స్క్రీన్ SPF 60',
         'Product_Hindi': 'मिनिमलिस्ट सनस्क्रीन SPF 60',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/xl/40233802_3-minimalist-spf-60-silymarin-face-sunscreen-with-antioxidant-for-complete-sun-protection.jpg',
         'Website': 'https://beminimalist.co/products/spf-60-silymarin?srsltid=AfmBOopkk_0VWzRiLNt4nJN4R-ZonIhvHHgkDvvcOlJXTvgdUHWnVrpH'
        },
        {'Product_English': 'The Derma Co Hyaluronic Sunscreen Aqua Gel',
         'Product_Telugu': 'ది డెర్మా కో హయాలురోనిక్ సన్‌స్క్రీన్ ఆక్వా జెల్',
         'Product_Hindi': 'द डर्मा को हायालूरोनिक सनस्क्रीन एक्वा जेल',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/xl/40255163_1-the-derma-co-1-hyaluronic-sunscreen-aqua-gel-spf-50-for-broad-spectrum-blue-light-protection.jpg',
         'Website': 'https://www.bigbasket.com/pd/40255163/the-derma-co-1-hyaluronic-sunscreen-aqua-gel-spf-50-for-broad-spectrum-blue-light-protection-50-g/'
        },

        # MOISTURIZERS
        {'Product_English': 'Minimalist Ceramide 0.3% Moisturizer',
            'Product_Telugu': 'మినిమలిస్ట్ సిరామైడ్ 0.3% మాయిశ్చరైజర్',
            'Product_Hindi': 'मिनिमलिस्ट सेरामाइड 0.3% मॉइस्चराइज़र',
         'Recommendation': 'https://media6.ppl-media.com/tr:h-550,w-550,c-at_max,dpr-2/static/img/product/399327/minimalist-vitamin-b12-repair-complex-5-5-percentage-face-moisturizer-50-gm_3_display_1747823376_5c1b5b73.jpg',
            'Website': 'https://www.bigbasket.com/product-reviews/40240703/minimalist-face-cream-ceramide-03-bisabolol-repairs-moisturize-dry-skin-30-g/?page=1'
        },
        {'Product_English': 'CeraVe Moisturizing Cream',
         'Product_Telugu': 'సెరావే మాయిశ్చరైజింగ్ క్రీమ్',
         'Product_Hindi': 'सेरावे मॉइस्चराइजिंग क्रीम',
         'Recommendation': 'https://www.ceraveindia.com/-/media/project/loreal/brand-sites/cerave/americas/in/scx/products/pdp/packshots/moisturising-cream/moisturising-cream-454g-lg.jpg?rev=-1',
         'Website': 'https://www.ceraveindia.com/ceramides-skin-care/moisturisers/moisturising-cream'
        },
        {'Product_English': 'Clinique Moisture Surge 100H',
         'Product_Telugu': 'క్లినిక్ మాయిశ్చర సర్జ్ 100H',
         'Product_Hindi': 'क्लिनिक मॉइस्चर सर्ज 100एच',
         'Recommendation': 'https://cdn.fynd.com/v2/falling-surf-7c8bb8/fyprod/wrkr/products/pictures/item/free/original/000000000491941123/BdCa4eHvT-000000000491941123_1.png',
         'Website': 'https://www.clinique.in/product/moisture-surge-100h-auto-replenishing-hydrator'
        },

        # MASKS
        {'Product_English': 'LANEIGE Water Sleeping Mask',
            'Product_Telugu': 'లేనేజ్ వాటర్ స్లీపింగ్ మాస్క్',
            'Product_Hindi': 'लेनज वॉटर स्लीपिंग मास्क',
         'Recommendation': 'https://luxiface.com/cdn/shop/files/Laneige-Water-Sleeping-Mask-70ml.png?v=1734787238',
         'Website': 'https://my.laneige.com/water-sleeping-mask-trial-size.html?srsltid=AfmBOoqNiGX4yXNf46ss9td-it6_Y97VBTci5kJYXsMpjjBJdAI6tWVD'
        },
        {'Product_English': 'The Body Shop British Rose Plumping Mask', 
            'Product_Telugu': 'ది బాడీ షాప్ బ్రిటిష్ రోజ్ ప్లంపింగ్ మాస్క్',
            'Product_Hindi': 'द बॉडी शॉप ब्रिटिश रोज प्लम्पिंग मास्क',
         'Recommendation': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdc-OQDgmOnj9PMiO0p5xPu8BwN5tGbb9saQ&s', 
         'Website': 'https://www.thebodyshop.com.au/products/british-rose-fresh-plumping-mask'
        },
        {'Product_English': 'Innisfree Aloe Revital Sleeping Pack', 
            'Product_Telugu': 'ఇన్నిస్‌ఫ్రీ అలొ రివిటల్ స్లీపింగ్ ప్యాక్',
            'Product_Hindi': 'इनिसफ्री एलो रिवाइटल स्लीपिंग पैक',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40256455_2-innisfree-innisfree-aloe-revital-sleeping-pack.jpg', 
         'Website': 'https://www.bigbasket.com/pd/40256455/innisfree-innisfree-aloe-revital-sleeping-pack-100-ml-bottle/'
        },

        # SERUMS
        {'Product_English': 'Minimalist Hyaluronic Acid 2% Serum', 
            'Product_Telugu': 'మినిమలిస్ట్ హయాలురోనిక్ యాసిడ్ 2% సీరమ్',
                'Product_Hindi': 'मिनिमलिस्ट हायालूरोनिक एसिड 2% सीरम',
         'Recommendation': 'https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_600/NI_CATALOG/IMAGES/CIW/2025/8/1/be4add15-a5fc-49c4-9707-7b3b7eb1a508_CQPDIYL7OA.png', 
            'Website': 'https://www.bigbasket.com/pd/40233785/minimalist-hyaluronic-acid-2-b5-face-serum-for-glowing-skin-intense-hydration-fines-lines-30-ml/'
        },
        {'Product_English': 'The Ordinary Hyaluronic Acid 2% + B5', 
            'Product_Telugu': 'ది ఆర్డినరీ హయాలురోనిక్ యాసిడ్ 2% + B5',
                'Product_Hindi': 'द ऑर्डिनरी हायालूरोनिक एसिड 2% + B5',
         'Recommendation': 'https://images-static.nykaa.com/media/catalog/product/2/4/244c0f5THECI00000093_a1.jpg?tr=w-500', 
         'Website': 'https://www.nykaa.com/the-ordinary-hyaluronic-acid-2percent-b5/p/13806304?skuId=13806302'
        },
        {'Product_English': 'L’Oreal Paris Revitalift 1.5% Hyaluronic Serum', 
            'Product_Telugu': 'లోరియల్ పారిస్ రివిటాలిఫ్ట్ 1.5% హయాలురోనిక్ సీరమ్',
                'Product_Hindi': 'ल\'ओरियल पेरिस रिवाइटालिफ्ट 1.5% हायालूरोनिक सीरम',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40212693_2-loreal-paris-revitalift-15-hyaluronic-acid-serum.jpg', 
         'Website': 'https://www.bigbasket.com/pd/40212693/loreal-paris-revitalift-15-hyaluronic-acid-serum-30-ml/'
        }

    ],

    'oily': [
        # CLEANSERS
        {'Product_English': 'Minimalist Salicylic Acid Cleanser', 
         'Product_Telugu': 'మినిమలిస్ట్ సాలిసిలిక్ యాసిడ్ క్లీన్సర్',
         'Product_Hindi': 'मिनिमलिस्ट सैलिसिलिक एसिड क्लेंजर',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40233784_3-minimalist-salicylic-acid-lha-2-face-cleanser-reduces-sebum-prevents-breakouts.jpg', 
         'Website': 'https://beminimalist.co/products/salicylic-lha-2-cleanser'
        },
        {'Product_English': 'CeraVe Foaming Facial Cleanser', 
            'Product_Telugu': 'సెరావే ఫోమింగ్ ఫేషియల్ క్లీన్సర్',
            'Product_Hindi': 'सेरावे फोमिंग फेशियल क्लेंजर',
         'Recommendation': 'https://media.ulta.com/i/ulta/2254420?w=500&h=500', 
         'Website': 'https://africa.cerave.com/en/sitecore/content/loreal/brandsites/cerave/americas/us/home/skincare/cleansers/foaming-facial-cleanser'
        },
        {'Product_English': 'The Derma Co AHA-BHA Foaming Cleanser', 
         'Product_Telugu': 'ది డెర్మా కో AHA-BHA ఫోమింగ్ క్లీన్సర్',
            'Product_Hindi': 'द डर्मा को AHA-BHA फोमिंग क्लींजर',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40255176_1-the-derma-co-3-aha-bha-foaming-face-wash-oil-free-controls-acne-for-all-skin-types.jpg', 
         'Website': 'https://www.bigbasket.com/pd/40255176/the-derma-co-3-aha-bha-foaming-face-wash-oil-free-controls-acne-for-all-skin-types-100-ml/'
        },

        # SUNSCREENS
        {'Product_English': 'Minimalist Sunscreen SPF 50 Matte', 
         'Product_Telugu': 'మినిమలిస్ట్ సన్‌స్క్రీన్ SPF 50 మాట్',
            'Product_Hindi': 'मिनिमलिस्ट सनस्क्रीन SPF 50 मैट',
         'Recommendation': 'https://www.havin.in/cdn/shop/files/f840aacMINIM00000108_7.png?v=1710251995&width=1024', 
        'Website': 'https://www.newu.in/products/minimalist-spf-50-sunscreen'
        },
        {'Product_English': 'Re’equil Ultra Matte Dry Touch Sunscreen', 
         'Product_Telugu': 'రీ’క్విల్ అల్ట్రా మాట్ డ్రై టచ్ సన్‌స్క్రీన్',
            'Product_Hindi': 'रीक्विल अल्ट्रा मैट ड्राई टच सनस्क्रीन',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40342837_1-reequil-ultra-matte-dry-touch-sunscreen-with-spf-50-pa.jpg', 
         'Website': 'https://www.bigbasket.com/pd/40342837/reequil-ultra-matte-dry-touch-sunscreen-with-spf-50-pa-50-g/'
        },
        {'Product_English': 'The Derma Co Hyaluronic Sunscreen Aqua Gel', 
            'Product_Telugu': 'ది డెర్మా కో హయాలురోనిక్ సన్‌స్క్రీన్ ఆక్వా జెల్',
            'Product_Hindi': 'द डर्मा को हायालूरोनिक सनस्क्रीन एक्वा जेल',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/xl/40255163_1-the-derma-co-1-hyaluronic-sunscreen-aqua-gel-spf-50-for-broad-spectrum-blue-light-protection.jpg', 
         'Website': 'https://www.bigbasket.com/pd/40255163/the-derma-co-1-hyaluronic-sunscreen-aqua-gel-spf-50-for-broad-spectrum-blue-light-protection-50-g/'
        },

        # MOISTURIZERS
        {'Product_English': 'Minimalist Vitamin B5 10% Moisturizer',
            'Product_Telugu': 'మినిమలిస్ట్ విటమిన్ B5 10% మాయిశ్చరైజర్',
            'Product_Hindi': 'मिनिमलिस्ट विटामिन B5 10% मॉइस्चराइज़र', 
         'Recommendation': 'https://www.cureka.com/wp-content/uploads/2023/09/Layer_199-1.jpg', 
         'Website': 'https://global.beminimalist.co/products/vitamin-b5-10-moisturizer'
        },
        {'Product_English': 'Neutrogena Hydro Boost Gel',
         'Product_Telugu': 'న్యూట్రోజెనా హైడ్రో బూస్ట్ జెల్',
         'Product_Hindi': 'न्यूट्रोजेना हाइड्रो बूस्ट जेल',
         'Recommendation': 'https://images.ctfassets.net/aub2fvcyp2t8/7KNPvxTsaEUZAdlWhF7h0p/016350854a21ef0ab6595b6d7f07536e/nourishing_cream_50g_front-en-in?fm=webp&w=3840',
         'Website': 'https://www.neutrogena.in/face/hydro-boost'
        },
        {'Product_English': 'The Derma Co Oil-Free Moisturizer',
         'Product_Telugu': 'ది డెర్మా కో ఆయిల్-ఫ్రీ మాయిశ్చరైజర్',
         'Product_Hindi': 'द डर्मा को ऑयल-फ्री मॉइस्चराइज़र',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/xl/40333328_2-the-derma-co-oil-free-daily-face-moisturizer.jpg',
         'Website': 'https://www.bigbasket.com/pd/40333328/the-derma-co-oil-free-daily-face-moisturizer-100-g/'
        },

        # MASKS
        {'Product_English': 'O3+ Sulfur Cooling Mask', 
         'Product_Telugu': 'O3+ సల్ఫర్ కూలింగ్ మాస్క్',
            'Product_Hindi': 'O3+ सल्फर कूलिंग मास्क',
         'Recommendation': 'https://www.o3plus.com/cdn/shop/products/product.jpg?v=1756727905', 
         'Website': 'https://www.o3plus.com/products/purifying-sulfur-cooling-facial-masque?srsltid=AfmBOoo__Y3knE3ChLOZvcOIk7Z19pCt5WRBIT-CLKRoJgaK1Dx7EJq4'
        },
        {'Product_English': 'Innisfree Volcanic Pore Clay Mask', 
            'Product_Telugu': 'ఇన్నిస్‌ఫ్రీ వోల్కానిక్ పోర్ క్లే మాస్క్',
                'Product_Hindi': 'इनिसफ्री वोल्केनिक पोर्स क्ले मास्क',
         'Recommendation': 'https://in.innisfree.com/cdn/shop/files/131174448_9fba21fe-eeec-41a8-ab01-64d30a3588f4.jpg?v=1754914230', 
        'Website': 'https://in.innisfree.com/products/super-volcanic-pore-clay-mask-100ml?srsltid=AfmBOoqJka_8upuZzC8LBzjhuPxcxJGDQvVN3hIvdWXNwpmP_bP-rs5C'
        },
        {'Product_English': 'The Body Shop Himalayan Charcoal Mask',
            'Product_Telugu': 'ది బాడీ షాప్ హిమాలయన్ చార్కోల్ మాస్క్',
                'Product_Hindi': 'द बॉडी शॉप हिमालयन चारकोल मास्क', 
         'Recommendation': 'https://images-static.nykaa.com/media/catalog/product/5/a/5aace55E000942_01.png', 
         'Website': 'https://www.nykaa.com/the-body-shop-himalayan-charcoal-purifying-glow-mask/p/875901?skuId=120385'
        },

        # SERUMS
        {'Product_English': 'Minimalist Niacinamide 10%', 
            'Product_Telugu': 'మినిమలిస్ట్ నయాసినమైడ్ 10%',
                'Product_Hindi': 'मिनिमलिस्ट नियासिनमाइड 10%',
         'Recommendation': 'https://www.bbassets.com/media/uploads/p/l/40341764_1-minimalist-niacinamide-10-face-serum.jpg', 
         'Website': 'https://www.bigbasket.com/pd/40341764/minimalist-niacinamide-10-face-serum-10-ml/'
        },
        {'Product_English': 'The Ordinary Niacinamide 10% + Zinc 1%', 
            'Product_Telugu': 'ది ఆర్డినరీ నయాసినమైడ్ 10% + జింక్ 1%',
                'Product_Hindi': 'द ऑर्डिनरी नियासिनमाइड 10% + जिंक 1%',
         'Recommendation': 'https://lobeautyuae.com/cdn/shop/products/rdn-niacinamide-10pct-zinc-1pct-30ml.png?v=1632913756', 
         'Website': 'https://www.nykaa.com/the-ordinary-niacinamide-10percent-zinc-1percent/p/15707745?skuId=5003164'
        },
        {'Product_English': 'The Derma Co Niacinamide Serum', 
            'Product_Telugu': 'ది డెర్మా కో నయాసినమైడ్ సీరమ్',
                'Product_Hindi': 'द डर्मा को नियासिनमाइड सीरम',
         'Recommendation': 'https://images.thedermaco.com/catalog/product/n/i/niacinamide-daily-face-serum-1.jpg?auto=format&fit=contain&width=720&auto=compress?format=auto', 
         'Website': 'https://thedermaco.com/product/5-niacinamide-daily-face-serum-with-alpha-arbutin-multivitamin-30ml?srsltid=AfmBOoppymEj5AD759drvnzcCsqDLzfcONYPh31i7FqjIUSFEz1vrFnS'
        }

    ]
}
