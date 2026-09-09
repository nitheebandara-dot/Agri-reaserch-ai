<!DOCTYPE html>
<html lang="si">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>හෙළ ගොවි - කතා ක්‍රීඩාව (Hela Govi Story Game)</title>
  <style>
    :root { --primary: #14532d; --gold: #eab308; --bg: #f0fdf4; }
    body { font-family: "Noto Sans Sinhala", "Iskoola Pota", sans-serif; background: var(--bg); color: #1c1917; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
    .game-container { background: #fff; width: 100%; max-width: 600px; border-radius: 20px; box-shadow: 0 10px 25px rgba(20,83,45,0.15); overflow: hidden; border: 2px solid #bbf7d0; }
    .header { background: linear-gradient(135deg, #052e16, #166534); color: #fff; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
    .header h1 { font-size: 1.2rem; margin: 0; }
    .stats { display: flex; gap: 15px; font-size: 0.9rem; background: rgba(255,255,255,0.1); padding: 5px 12px; border-radius: 20px; }
    .content { padding: 25px; }
    .scene-img { font-size: 50px; text-align: center; margin-bottom: 15px; }
    .story-text { font-size: 1.05rem; line-height: 1.6; margin-bottom: 25px; min-height: 80px; }
    .choices { display: flex; flex-direction: column; gap: 12px; }
    button.choice-btn { background: #f0fdf4; border: 2px solid #166534; color: #14532d; padding: 12px 18px; border-radius: 12px; font-size: 1rem; font-family: inherit; font-weight: 600; cursor: pointer; text-align: left; transition: all 0.2s; }
    button.choice-btn:hover { background: #166534; color: #fff; transform: translateY(-2px); }
  </style>
</head>
<body>

<div class="game-container">
  <div class="header">
    <h1>🌾 හෙළ ගොවි: ගමන</h1>
    <div class="stats">
      <span>💰 මුදල්: <b id="money">1000</b></span>
      <span>⭐ කීර්තිය: <b id="rep">10</b></span>
    </div>
  </div>
  <div class="content">
    <div class="scene-img" id="sceneImg">👨‍🌾</div>
    <div class="story-text" id="storyText">පූජ්‍ය පැරණි කුඹුර බේරා ගැනීමට ඔබ ගමට පැමිණ ඇත. ඔබේ ගමන අරඹන්න සූදානම්ද?</div>
    <div class="choices" id="choicesContainer"></div>
  </div>
</div>

<script>
  let stats = { money: 1000, rep: 10 };

  const scenes = {
    start: {
      img: "🌾",
      text: "මහ කන්නය ආරම්භ වීමට නියමිතය. ඔබේ අතෙහි ඇත්තේ බිත්තර වී මල්ලක් සහ සුළු මුදලකි. ඔබ මුලින්ම කුම מה කරන්නට අදහස් කරන්නේද?",
      choices: [
        { text: "1. සාම්ප්‍රදායික ක්‍රමයට කුඹුරργ සකස් කර වී වැපිරීමට පටන් ගන්න.", next: "paddy_start" },
        { text: "2. නවීන තාක්ෂණය හා ඩ්‍රිප් ජල සම්පාදනය ගැන සොයා බලන්න.", next: "tech_start" }
      ]
    },
    paddy_start: {
      img: "🚜",
      text: "ඔබ සාම්ප්‍රදායික ක්‍රමයට කුඹුරργ සකස් කළා. මඩ වගුරට බස්සන්න හරක්පැටවෙක් හෝ ට්‍රැක්ටරයක් කුලියට ගැනීමට අවශ්‍යයි.",
      choices: [
        { text: "කුලී ට්‍රැක්ටරයක් යොදා ඉක්මනින් වැඩ முடிക്കുക (-රු. 300)", action: () => { stats.money -= 300; stats.rep += 5; }, next: "paddy_growth" },
        { text: "ගමේ වැඩිහිටියන්ගේ උදව්වෙන් සාම්ප්‍රදායික ක්‍රමයට කරමු", action: () => { stats.rep += 10; }, next: "paddy_growth" }
      ]
    },
    tech_start: {
      img: "💡",
      text: "ඔබ පොලිටනල් ක්‍රමයට එළවළු සහ මිරිස් වගාවක් ආරම්භ කිරීමට තීරණය කළා. මෙයට මූලික වියදම් අධිකයි.",
      choices: [
        { text: "බෑنකි ණය මුදලක් සඳහා ඉල්ලුම් කරන්න (-රු. 200)", action: () => { stats.money += 500; }, next: "tech_growth" },
        { text: "අත ඇති මුදලින් කුඩා පරිමාණයෙන් පටන් ගන්න", next: "tech_growth" }
      ]
    },
    paddy_growth: {
      img: "🌱",
      text: "පැළ හොඳින් වැඩුීගෙන එයි. නමුත් හදිසියේම කුඹුරට කීඩෑ උවදුරක් පැමිණ තිබේ! ඔබ කුමක් කරන්නේද?",
      choices: [
        { text: "කාබනික කෘමිනාශකයක් (ස්වභාවික දියරයක්) සකස් කර ඉසින්න", action: () => { stats.rep += 15; }, next: "victory" },
        { text: "රසායනික බෙහෙත් වර්ගයක් ඉසින්න (-රු. 200)", action: () => { stats.money -= 200; stats.rep -= 5; }, next: "victory" }
      ]
    },
    tech_growth: {
      img: "🍅",
      text: "ඔබේ වගාවෙන් පළමු අස්වැන්න නෙළා ගැනීමට කාලය පැමිණ ඇත. වෙළඳපොළට රැගෙන යාමට සූදානම්.",
      choices: [
        { text: "ප්‍රාදේශීය කාබනික වෙළඳපොළට ගොස් අස්වැන්න විකුණන්න (+රු. 1500)", action: () => { stats.money += 1500; stats.rep += 20; }, next: "victory" }
      ]
    },
    victory: {
      img: "🏆",
      text: "සුභ පැතුම්! ඔබ අභියෝග ජයගෙන ගමේ දක්ෂ හා ආදර්ශමත් 'හෙළ ගොವියා' බවට පත්ව ඇත. ඔබේ වගාව සාර්ථකයි!",
      choices: [
        { text: "다시 ක්‍රීඩා කරන්න (Restart Game)", next: "start" }
      ]
    }
  };

  function updateStats() {
    document.getElementById("money").innerText = stats.money;
    document.getElementById("rep").innerText = stats.rep;
  }

  function loadScene(sceneKey) {
    const scene = scenes[sceneKey];
    document.getElementById("sceneImg").innerText = scene.img;
    document.getElementById("storyText").innerText = scene.text;
    
    const container = document.getElementById("choicesContainer");
    container.innerHTML = "";

    scene.choices.forEach(choice => {
      const btn = document.createElement("button");
      btn.className = "choice-btn";
      btn.innerText = choice.text;
      btn.onclick = () => {
        if (choice.action) choice.action();
        updateStats();
        loadScene(choice.next);
      };
      container.appendChild(btn);
    });
  }

  updateStats();
  loadScene("start");
</script>

</body>
</html>



