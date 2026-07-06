import streamlit as st
import random

# වෙබ් පිටුවේ ප්‍රධාන සැකසුම් (Page Configuration)
st.set_page_config(
    page_title="AI Agriculture Research Engine",
    page_icon="🌱",
    layout="centered"
)

# ප්‍රධාන මාතෘකාව සහ බැනරය
st.title("🌱 AI Agriculture Research Engine")
st.subheader("Agro-Tech Research Engine v5.0")
st.markdown("---")

# 📋 PART 1: FIELD DATA COLLECTION (පරිශීලක දත්ත ඇතුළත් කිරීම)
st.header("📋 ක්ෂේත්‍ර දත්ත එකතු කිරීම (Field Data Collection)")

# Input 1: Soil pH (Slider එකක් මඟින් ලස්සනට තෝරන්න)
soil_pH = st.slider("👉 පසෙහි pH අගය ඇතුළත් කරන්න (Soil pH):", min_value=1.0, max_value=14.0, value=6.2, step=0.1)

# Input 2: Land Size
land_size = st.number_input("👉 වගා භූමියේ ප්‍රමාණය පර්චස් වලින් (Land Size in Perches):", min_value=1.0, value=10.0, step=1.0)

# Input 3: Soil Type (Dropdown Menu)
soil_type_mapping = {
    "රතු ලැටරයිට් පස (Red Latosols / තෙත් කලාපීය පස)": 1,
    "වැලි සහිත පස (Sandy Soil / වියළි කලාපීය පස)": 2,
    "මැටි මිශ්‍ර කළු පස (Alluvial / කුඹුරු පස)": 3
}
soil_type_display = st.selectbox("👉 ඔයාගේ වගා බිමේ පවතින පස් වර්ගය (Soil Type) තෝරන්න:", list(soil_type_mapping.keys()))
soil_type = soil_type_mapping[soil_type_display]

# Input 4: Climate Zone (Dropdown Menu)
zone_mapping = {
    "වියළි කලාපය (Dry Zone)": 1,
    "තෙත් කලාපය (Wet Zone)": 2,
    "උඩරට කඳුකර කලාපය (Upcountry)": 3
}
zone_display = st.selectbox("👉 වගා ප්‍රදේශයේ කෘෂි දේශගුණික කලාපය (Climate Zone) තෝරන්න:", list(zone_mapping.keys()))
zone_choice = zone_mapping[zone_display]

# Input 5: Previous Crop (Dropdown Menu)
prev_crop_mapping = {
    "වී (Paddy)": 1,
    "මිරිස් හෝ තක්කාලි (Solanaceous Crops)": 2,
    "අල වර්ග (Root Crops)": 3
}
prev_crop_display = st.selectbox("👉 දැනට එම බිමෙහි වගා කර ඇති/අවසන් වූ බෝගය (Previous Crop):", list(prev_crop_mapping.keys()))
prev_crop = prev_crop_mapping[prev_crop_display]

st.markdown("---")

# 🔄 PROCESSING & REPORT GENERATION (විශ්ලේෂණ බොත්තම)
if st.button("🚀 දත්ත විශ්ලේෂණය කර වාර්තාව ලබාගන්න (Run AI Analysis)"):
    
    with st.spinner("AI Core: දත්ත පද්ධති විශ්ලේෂණය කරමින් පවතී..."):
        # Variables for Predictions
        recommended_crop = ""
        npk_ratio = ""
        fertilizer = ""
        pest_tip = ""
        water_per_perch = 0
        yield_per_perch = 0
        
        # 1. Soil pH Analysis
        if soil_pH < 5.5:
            soil_status = "අධික ආම්ලික පසක් (Strongly Acidic)"
            remedy = "ආම්ලිකතාවය අඩු කිරීමට ඩොලමයිට් (Dolomite) එකතු කරන්න."
        elif 5.5 <= soil_pH <= 6.5:
            soil_status = "මද ආම්ලික පසක් (Slightly Acidic - Ideal for Crops)"
            remedy = "පස ප්‍රශස්ත මට්ටමක පවතී. සාමාන්‍ය කාබනික වසුන් යොදන්න."
        else:
            soil_status = "භාෂ්මික පසක් (Alkaline Soil)"
            remedy = "භාෂ්මිකතාවය පාලනයට සල්ෆර් අඩංගු පොහොර හෝ කාබනික ද්‍රව්‍ය යොදන්න."

        # 2. Crop Prediction
        if zone_choice == 1: # Dry Zone
            if soil_type == 2:
                recommended_crop = "රටකජු (Peanut)"
                water_per_perch = 10.0
                yield_per_perch = 8.5
                npk_ratio = "N:10% | P:10% | K:12%"
                fertilizer = "කාබනික පොහොර (කොහුබත්) සහ පොටෑසියම් බහුල මිශ්‍රණ"
                pest_tip = "පස වේලීම වැළැක්වීමට වසුන් ක්‍රම (Mulching) පාවිච්චි කරන්න."
            else:
                recommended_crop = "මිරිස් (Chilli)"
                water_per_perch = 15.5
                yield_per_perch = 12.0
                npk_ratio = "N:12% | P:14% | K:10%"
                fertilizer = "නයිට්‍රජන් (N) සහ පොස්පරස් (P) වැඩි පොහොර මිශ්‍රණ"
                pest_tip = "කොළ අකුලා යාමේ වෛරස් පාලනයට සුදු මැස්සන් මර්දනය කරන්න."
                
        elif zone_choice == 2: # Wet Zone
            if soil_type == 3:
                recommended_crop = "වී වගාව (Paddy - Wet Cycle)"
                water_per_perch = 4.0
                yield_per_perch = 18.0
                npk_ratio = "N:18% | P:8% | K:10%"
                fertilizer = "යුරියා සහ මඩ පොහොර (TSP)"
                pest_tip = "ගොයම් මැස්සා පාලනයට ස්වාභාවික කොහොඹ නිස්සාරණය යොදන්න."
            else:
                recommended_crop = "කුරුඳු (Cinnamon)"
                water_per_perch = 5.0
                yield_per_perch = 6.0
                npk_ratio = "N:15% | P:7% | K:15%"
                fertilizer = "කොම්පෝස්ට් සමඟ සම්මත කුරුඳු පොහොර මිශ්‍රණය"
                pest_tip = "ජල අපවහනය (Drainage) නිසිලෙස සකස් කර මුල් කුණුවීම වළක්වන්න."
                
        elif zone_choice == 3: # Upcountry
            recommended_crop = "අර්තාපල් (Potato) හෝ කැරට්"
            water_per_perch = 12.0
            yield_per_perch = 25.0
            npk_ratio = "N:20% | P:10% | K:10%"
            fertilizer = "හොඳින් දිරාපත් වූ කුකුළු පොහොර සහ NPK රසායනික මිශ්‍රණ"
            pest_tip = "සීතල නිසා ඇතිවන 'අංගමාරය' ਰෝගයෙන් ආරක්ෂා වීමට පූර්ව දිලීර නාශක යොදන්න."

        # 3. Crop Rotation Logic
        next_rotation_crop = ""
        companion_crop = ""
        ecological_benefit = ""
        
        if prev_crop == 1:
            next_rotation_crop = "මුංඇට (Green Gram) හෝ කව්පි"
            companion_crop = "පලා වර්ග (Intercropping)"
            ecological_benefit = "රනිල කුලයේ බෝග මඟින් පසෙහි නයිට්‍රජන් ස්වභාවිකව තැන්පත් කරයි (Nitrogen Fixation)."
        elif prev_crop == 2:
            next_rotation_crop = "රාබු හෝ බෝංචි"
            companion_crop = "ගෝවා (Cabbage)"
            ecological_benefit = "මිරිස් වගාවෙන් පසු ඇතිවන රෝග චක්‍රය සහ පසෙහි පළිබෝධ වර්ධනය බිඳ දමයි."
        elif prev_crop == 3:
            next_rotation_crop = "බණ්ඩක්කා (Okra) හෝ කරවිල"
            companion_crop = "දස්පෙතියා මල් (Marigold)"
            ecological_benefit = "මරිගෝල්ඩ් මල් මඟින් පසෙහි වෙසෙන හානිකර නෙමටෝඩාවන් (Nematodes) ස්වභාවිකව පාලනය කරයි."

        total_water_needed = land_size * water_per_perch
        estimated_total_yield = land_size * yield_per_perch
        price_trend = random.choice(["ඉහළ යාමේ ප්‍රවණතාවයක් ඇත 📈", "ස්ථාවරව පවතී 📊", "පහළ යා හැක 📉"])

        # 📊 OUTPUT REPORT (ප්‍රතිඵල ලස්සනට වෙබ් පිටුවේ පෙන්වීම)
        st.success("📊 පර්යේෂණ වාර්තාව සකස් කර අවසන්! (AI Analysis Report)")
        
        # 1. Soil Info Box
        st.subheader("🧪 පසෙහි වත්මන් තත්ත්වය")
        st.info(f"**වත්මන් තත්ත්වය:** {soil_status}\n\n**නිවැරදි කිරීමේ උපදෙස්:** {remedy}")
        
        # 2. Crop Recommendations
        st.subheader("🌾 බෝග සහ පෝෂක නිර්දේශයන්")
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="නිර්දේශිත හොඳම බෝගය", value=recommended_crop)
            st.write(f"**💡 ප්‍රශස්ත පෝෂක අනුපාතය (NPK):** {npk_ratio}")
        with col2:
            st.write(f"**🧪 නිර්දේශිත පොහොර:** {fertilizer}")
            st.write(f"**🛡️ පළිබෝධ/රෝග පාලනය:** {pest_tip}")
            
        # 3. Mathematical Predictions
        st.subheader("📊 නිෂ්පාදන සහ වෙළඳපොළ අනාවැකි")
        col3, col4 = st.columns(2)
        with col3:
            st.metric(label="දිනක මුළු ජල අවශ්‍යතාවය", value=f"{total_water_needed:.1f} L")
            st.metric(label="ඇස්තමේන්තුගත මුළු අස්වැන්න", value=f"{estimated_total_yield:.1f} kg")
        with col4:
            st.warning(f"💰 **වෙළඳපොළ මිල අනාවැකිය:** \n\n මිල {price_trend}")

                # 4. Crop Rotation Card
        st.subheader("🔄 විද්‍යාත්මක බෝග මාරු නිර්දේශය (Crop Rotation)")
        
                # 4. Crop Rotation Card
        st.subheader("🔄 විද්‍යාත්මක බෝග මාරු නිර්දේශය (Crop Rotation)")
        
        st.write(f"🟢 **ඉදිරි කන්නයේ වගාව:** {next_rotation_crop}")
        st.write(f"🤝 **සහකාර බෝගය (Companion):** {companion_crop}")
        st.write(f"🔬 **විද්‍යාත්මක පදනම:** {ecological_benefit}")

            
    
            
        




    

    


         

st.markdown("---")
st.caption("🌱 Sustainable Agri-Tech Research Prototype v5.0 | Developed for Research Purposes")
