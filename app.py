import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="AI Agriculture Research Engine",
    page_icon="🌱",
    layout="centered"
)

# Header
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
}# # Input 4: දිස්ත්‍රික්කය තෝරාගැනීම (District Selection)
district_mapping = {
    "කොළඹ (Colombo)": "Wet Zone",
    "ගම්පහ (Gampaha)": "Wet Zone",
    "කළුතර (Kalutara)": "Wet Zone",
    "ගාල්ල (Galle)": "Wet Zone",
    "මාතර (Matara)": "Wet Zone",
    "රත්නපුරය (Ratnapura)": "Wet Zone",
    "කෑගල්ල (Kegalle)": "Wet Zone",
    "මහනුවර (Kandy)": "Upcountry",
    "නුවරඑළිය (Nuwara Eliya)": "Upcountry",
    "බදුල්ල (Badulla)": "Upcountry",
    "මාතලේ (Matale)": "Upcountry",
    "අනුරාධපුරය (Anuradhapura)": "Dry Zone",
    "පොළොන්නරුව (Polonnaruwa)": "Dry Zone",
    "කුරුණෑගල (Kurunegala)": "Dry Zone",
    "පුත්තලම (Puttalam)": "Dry Zone",
    "හම්බන්තොට (Hambantota)": "Dry Zone",
    "මොනරාගල (Monaragala)": "Dry Zone",
    "අම්පාර (Ampara)": "Dry Zone",
    "මඩකලපුව (Batticaloa)": "Dry Zone",
    "ත්‍රිකුණාමලය (Trincomalee)": "Dry Zone",
    "යාපනය (Jaffna)": "Dry Zone",
    "කිලිනොච්චිය (Kilinochchi)": "Dry Zone",
    "මන්නාරම (Mannar)": "Dry Zone",
    "වවුනියාව (Vavuniya)": "Dry Zone",
    "මුලතීවු (Mullaitivu)": "Dry Zone"
}

district_display = st.selectbox("👉 වගා බිම පිහිටි දිස්ත්‍රික්කය තෝරන්න:", list(district_mapping.keys()))
selected_zone = district_mapping[district_display]

# කලාපය අනුව අගයන් (1, 2, 3) mapping එකට දීම (ඔයාගේ පරණ ලොජික් එක බිඳෙන්නේ නැති වෙන්න)
zone_mapping = {"Dry Zone": 1, "Wet Zone": 2, "Upcountry": 3}
zone_choice = zone_mapping[selected_zone]

# පරිශීලකයාට තේරුණු කලාපය visual එකක් විදිහට පෙන්වන්න
st.info(f"📍 තෝරාගත් දිස්ත්‍රික්කය අනුව දේශගුණික කලාපය: **{selected_zone}**")

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
        
        st.write(f"🟢 **ඉදිරි කන්නයේ වගාව:** {next_rotation_crop}")
        st.write(f"🤝 **සහකාර බෝගය (Companion):** {companion_crop}")
        st.write(f"🔬 **විද්‍යාත්මක පදනම:** {ecological_benefit}")

            
    
            
        




    

    


         

st.markdown("---")
st.caption("🌱 Sustainable Agri-Tech Research Prototype v5.0 | Developed for Research Purposes")
# AI Chatbot සෙක්ෂන් එක
st.markdown("---")
st.subheader("🤖 AI කෘෂිකාර්මික උපදේශක")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("වගාව ගැන අහන්න..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    user_input = prompt.lower()
    if "මිරිස්" in user_input:
        response = "🌶️ මිරිස් වගාව සඳහා උපදෙස්: 1. හොඳින් හිරු එළිය ලැබෙන ස්ථානයක් තෝරාගන්න. 2. පසෙහි ජලය බැස යන ගතිය හොඳ විය යුතුයි."
    else:
        response = "මම තවමත් ඉගෙන ගන්නවා. මට 'මිරිස් වගාව' ගැන අහන්න, මම උදව් කරන්නම්!"
    
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    user_input = prompt.lower()
    if "මිරිස්" in user_input:
        response = "🌶️ මිරිස් වගාව: හොඳින් හිරු එළිය ලැබෙන පසක් තෝරාගෙන සතියකට වරක් දියර පොහොර යොදන්න."
    elif "බටු" in user_input or "වම්බටු" in user_input:
        response = "🍆 වම්බටු වගාව: පස හොඳින් කාබනික පොහොර මිශ්‍ර කර, පැළ සිටුවා දින 10කට වරක් වටපිටාව වල් පැලෑටි වලින් තොරව තබා ගන්න."
    elif "ගෝවා" in user_input:
        response = "🥬 ගෝවා වගාව: සිසිල් දේශගුණයක් ප්‍රිය කරන නිසා උඩරට කලාපයට වඩාත් සුදුසුයි. පස තෙතමනය සහිතව තබා ගන්න."
    elif "බෝංචි" in user_input:
        response = "🫛 බෝංචි වගාව: වැල් වර්ගයක් නම් ආධාරක යොදන්න. නයිට්‍රජන් අඩංගු පොහොර මඳක් යෙදීම සාර්ථක අස්වැන්නකට උදව් වේ."
    else:
        response = "මම තවමත් ඉගෙන ගන්නවා. මට 'මිරිස්', 'බටු', 'ගෝවා' හෝ 'බෝංචි' ගැන අහන්න, මම උදව් කරන්නම්!"
import google.generativeai as genai
import streamlit as st

# 1. Page Config & Title
st.set_page_config(
    page_title="AI ගොවි උපදේශක", page_icon="🌱", layout="centered"
)

st.title("🌱 AI ගොවිපළ වගා උපදේශක")
st.write(
    "ඔබේ ඕනෑම වගාවක් (බෝංචි, මිරිස්, තක්කාලි, බටු ආදී) පිළිබඳ ගැටලුව පහතින් යොමු කරන්න."
)

# 2. Gemini API Configuration (ඔයාගේ Key එක ඇතුළත් කර ඇත)
API_KEY = "AQ.Ab8RN6I_VvAGyUAIVR0v163q1f4sGyAQLy8RUpLhvO-zC4-VWQ"
genai.configure(api_key=API_KEY)

# Gemini Model එක සක්‍රිය කිරීම
model = genai.GenerativeModel("gemini-1.5-flash")

# 3. User Input Form
with st.form("agri_form"):
  crop_name = st.text_input(
      "🌾 වගාවේ නම:", placeholder="උදා: බෝංචි, මිරිස්, තක්කාලි"
  )
  user_query = st.text_area(
      "❓ ගැටලුව / ප්‍රශ්නය:",
      placeholder="උදා: කොළ කහ පාට වෙනවා, පාලනය කරන්නේ කෙසේද?",
  )
  submit_button = st.form_submit_button("උපදෙස් ලබාගන්න 🚀")

# 4. AI Response Generation
if submit_button:
  if crop_name and user_query:
    with st.spinner("AI උපදේශක පිළිතුර සකසමින් පවතී..."):
      prompt = f"""
            ඔබ ශ්‍රී ලංකාවේ පළපුරුදු කෘෂිකාර්මික උපදේශකයෙකි. 
            ගොවියාගේ වගාව: {crop_name}
            ගොවියාගේ ප්‍රශ්නය: {user_query}
            
            කරුණාකර පහත අංශ කෙරෙහි අවධානය යොමු කරමින් පැහැදිලි, සරල සිංහලෙන් පිළිතුරු සපයන්න:
            1. රෝගය හෝ ගැටලුව හඳුනාගැනීම සහ ඊට හේතුව
            2. කාබනික සහ රසායනික විසඳුම් / පොහොර භාවිතය
            3. වගාව ආරක්ෂා කර ගැනීමට අනාගතයේදී ගත යුතු පියවර
            """

      try:
        response = model.generate_content(prompt)
        st.success("✅ AI උපදේශකගේ පිළිතුර:")
        st.markdown(response.text)
      except Exception as e:
        st.error(
  else:
    st.warning("කරුණාකර වගාවේ නම සහ ප්‍රශ්නය යන දෙකම ඇතුළත් කරන්න.")<!DOCTYPE html>
<html lang="si">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
  <title>HORDI ගොවීන් ප්‍රශ්නාවලිය | 8 ශ්‍රේණිය</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@400;600;700&family=Poppins:wght@500;700&display=swap" rel="stylesheet" />
  <style>
    :root {
      --g: #1b5e3b;
      --g2: #2e7d4f;
      --g3: #e8f5e9;
      --ink: #1a2b22;
      --muted: #5b6b62;
      --line: #d7e4da;
      --card: #ffffff;
      --warn: #c62828;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: "Noto Sans Sinhala", "Poppins", sans-serif;
      color: var(--ink);
      background: #eef5f0;
    }
    .hero {
      background: linear-gradient(180deg, rgba(12,40,24,.55), rgba(12,40,24,.82)),
                  url("header_farm.jpg") center/cover no-repeat;
      color: #fff;
      padding: 28px 18px 22px;
    }
    .hero small { opacity: .9; letter-spacing: .4px; }
    .hero h1 { margin: 8px 0 6px; font-size: 1.25rem; line-height: 1.45; }
    .hero p { margin: 0; font-size: .92rem; line-height: 1.55; opacity: .95; }
    .wrap { max-width: 720px; margin: 0 auto; padding: 14px; }
    .card {
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 16px;
      margin: 12px 0;
      box-shadow: 0 6px 18px rgba(27,94,59,.06);
    }
    h2 {
      margin: 0 0 10px;
      font-size: 1.05rem;
      color: var(--g);
    }
    label, .q { display: block; font-weight: 600; margin: 14px 0 8px; }
    .help { font-weight: 400; color: var(--muted); font-size: .86rem; margin-top: 4px; }
    input[type=text], input[type=number], textarea, select {
      width: 100%;
      padding: 12px;
      border: 1px solid var(--line);
      border-radius: 12px;
      font: inherit;
      background: #fbfefc;
    }
    textarea { min-height: 90px; resize: vertical; }
    .opts { display: grid; gap: 8px; }
    .opt {
      display: flex; align-items: flex-start; gap: 10px;
      padding: 11px 12px; border: 1px solid var(--line); border-radius: 12px;
      background: #fff; cursor: pointer;
    }
    .opt:has(input:checked) { border-color: var(--g2); background: var(--g3); }
    .scale { display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; }
    .scale label {
      margin: 0; text-align: center; padding: 10px 0;
      border: 1px solid var(--line); border-radius: 10px; background: #fff;
      font-weight: 700; cursor: pointer;
    }
    .scale label:has(input:checked) { background: var(--g2); color: #fff; border-color: var(--g2); }
    .scale input { display: none; }
    .scale-cap { display: flex; justify-content: space-between; color: var(--muted); font-size: .78rem; margin-top: 6px; }
    .row2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
    @media (max-width: 560px) { .row2 { grid-template-columns: 1fr; } }
    .actions { display: flex; gap: 8px; flex-wrap: wrap; margin: 16px 0 28px; }
    button {
      border: 0; border-radius: 12px; padding: 12px 16px;
      font: 700 15px "Noto Sans Sinhala", sans-serif; cursor: pointer;
    }
    .go { background: var(--g); color: #fff; flex: 1; }
    .ghost { background: #fff; color: var(--g); border: 1px solid var(--g2); }
    .ok { background: #1565c0; color: #fff; }
    .note { background: #fff8e1; border: 1px solid #ffe082; border-radius: 12px; padding: 12px; font-size: .9rem; }
    .okbox { display: none; background: #e8f5e9; border: 1px solid #a5d6a7; border-radius: 16px; padding: 18px; margin: 12px 0; }
    .err { color: var(--warn); font-size: .88rem; display: none; margin-top: 6px; }
    footer { text-align: center; color: var(--muted); font-size: .8rem; padding: 8px 12px 28px; }
    .count { font-size: .85rem; color: var(--g); font-weight: 700; }
  </style>
</head>
<body>
  <header class="hero">
    <small>HORDI ගන්නෝරුව · 8 ශ්‍රේණ
... 
