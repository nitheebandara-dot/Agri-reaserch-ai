 :>
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
