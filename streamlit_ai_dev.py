import streamlit as st

st.set_page_config(page_title="AI 發展與應用", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: 800; background: linear-gradient(135deg, #f97316, #ef4444); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.3rem; }
    .sub-header { font-size: 1.1rem; color: #94a3b8; }
    .meta-text { font-size: 0.85rem; color: #64748b; }
    .section-title { font-size: 1.4rem; font-weight: 700; color: #fb923c; margin: 1rem 0; padding-bottom: 0.5rem; border-bottom: 2px solid #334155; }
    .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 1.2rem; margin-bottom: 1rem; }
    .card h3 { color: #fb923c; font-size: 1.1rem; margin-bottom: 0.5rem; }
    .card p, .card li { color: #cbd5e1; font-size: 0.9rem; }
    .highlight-box { background: #1e293b; border-left: 4px solid #fb923c; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .code-box { background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 1rem; margin: 0.5rem 0; font-family: 'Courier New', monospace; font-size: 0.8rem; color: #a5b4fc; white-space: pre-wrap; }
    .flow-step { display: inline-block; background: #334155; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.8rem; margin: 0.2rem; }
    .flow-step .num { background: #fb923c; color: #0f172a; width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.7rem; margin-right: 0.3rem; }
    .tool-card { background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 1rem; margin-bottom: 0.5rem; }
    .tool-card .name { font-weight: 700; color: #fb923c; }
    .tool-card .desc { font-size: 0.8rem; color: #94a3b8; }
    hr { border-color: #334155; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div style='font-size:1.2rem; font-weight:700; color:#fb923c; margin-bottom:1rem;'>🤖 目錄</div>", unsafe_allow_html=True)

nav = [
    ("intro", "📖 課程概述"),
    ("m1", "🧠 Section 1: AI進化與設計革命"),
    ("m2", "🖨️ Section 2: AI與3D列印"),
    ("m3", "🛠️ Section 3: 主流AI工具圖譜"),
    ("m4", "⚖️ Section 4: 版權與倫理"),
    ("afternoon_a", "🎨 下午實作A: Prompt工程"),
    ("afternoon_b", "🖼️ 下午實作B: 圖片優化"),
    ("afternoon_c", "🧊 下午實作C: 2D轉3D"),
]

selected = None
for key, label in nav:
    if st.sidebar.button(label, key=f"nav_{key}", use_container_width=True, type="secondary"):
        selected = key
if not selected:
    selected = "intro"

st.sidebar.markdown("---")
st.sidebar.markdown("<div style='font-size:0.75rem; color:#64748b;'>講師：嚴稑榛<br>艾瑩科技 ・ 勞動部桃竹苗分署<br>115.04.20</div>", unsafe_allow_html=True)

st.markdown('<div class="main-header">🤖 AI 發展與應用</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">從零開始，掌握 AI 時代的設計力</div>', unsafe_allow_html=True)
st.markdown('<div class="meta-text">AI產品設計與全彩3D列印產品實作班 第⼀期｜班級代碼：162052｜115.04.20｜講師：嚴稑榛</div>', unsafe_allow_html=True)
st.markdown("---")

# ════════ Intro ════════
if selected == "intro":
    st.markdown('<div class="section-title">📖 課程概述</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 今日課程總覽
    | 時間 | 主題 | 內容 |
    |:----|:----|:----|
    | 09:00-10:30 | 🧠 **AI的進化與設計革命** | 什麼是AI？AI如何改變設計產業？一人公司的崛起 |
    | 10:30-11:30 | 🖨️ **AI與3D列印的完美共生** | 全彩3D列印技術現況、生成式設計概念 |
    | 11:30-12:00 | 🛠️ **當前主流AI工具圖譜** | Midjourney、DALL-E 3、Tripo AI、Meshy |
    | 貫穿全天 | ⚖️ **智慧財產權與商業倫理** | AI生成物版權、建立個人品牌力 |
    | 13:00-18:00 | 🎨 **下午術科實作** | Prompt工程、圖片優化、2D轉3D |
    """)

    cols = st.columns(3)
    with cols[0]:
        st.metric("🗓️ 日期", "115.04.20", "上午+下午")
    with cols[1]:
        st.metric("📄 總頁數", "86頁", "學科+術科")
    with cols[2]:
        st.metric("🎯 課程主線", "DALL-E 3 → Meshy AI → 3D列印", "")

    st.markdown("""
    <div class="highlight-box">
    <strong>🎯 課程主線流程：</strong>
    DALL-E 3（生成設計圖）→ Meshy AI（轉3D模型）→ 全彩3D列印（成品輸出）
    </div>
    """, unsafe_allow_html=True)

# ════════ Section 1 ════════
elif selected == "m1":
    st.markdown('<div class="section-title">🧠 Section 1: AI的進化與設計革命</div>', unsafe_allow_html=True)
    st.markdown("""
    ### AI 是什麼？
    ```
    ┌─────────────────────────────────────────┐
    │  人工智慧 (AI)                           │
    │  讓電腦模仿人類思考與學習                  │
    │  ┌──────────────────────────────────┐   │
    │  │  機器學習 (ML)                    │   │
    │  │  從大量資料自行學習規律             │   │
    │  │  ┌──────────────────────────┐   │   │
    │  │  │  深度學習 (DL)            │   │   │
    │  │  │  模擬人腦神經網路          │   │   │
    │  │  │  ┌──────────────────┐   │   │   │
    │  │  │  │ 生成式AI (GenAI) │   │   │   │
    │  │  │  │ 創造全新內容     │   │   │   │
    │  │  │  └──────────────────┘   │   │   │
    │  │  └──────────────────────────┘   │   │
    │  └──────────────────────────────────┘   │
    └─────────────────────────────────────────┘
    ```
    
    ### AI 發展里程碑
    | 年代 | 里程碑 |
    |:----|:-------|
    | 1950 | 圖靈測試提出 |
    | 2012 | AlexNet 開啟深度學習時代 |
    | 2017 | Transformer 架構誕生 |
    | 2022 | ChatGPT 引爆生成式AI |
    | 2026 | AI 生成 3D 模型成熟 |
    
    ### 傳統 vs AI 輔助設計
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.error("**傳統設計**\n\n❌ 需學 AutoCAD / ZBrush\n❌ 設計到樣品需 2-4 週\n❌ 每次修改耗費大量時間\n❌ 前期投入成本高")
    with col2:
        st.success("**AI 輔助設計**\n\n✅ 文字描述即可生成草圖\n✅ 設計到 3D 預覽只需數分鐘\n✅ 即時調整，快速迭代\n✅ 幾乎零學習成本起步")

    st.markdown("### AI 賦能「一人公司」")
    st.markdown("""
    - 過去：一人公司受限於技能（不會畫圖、不會3D）
    - 現在：AI 補足所有技能短板
    - 案例：設計師用 AI 在 1 天內完成過去 2 週的工作
    """)

# ════════ Section 2 ════════
elif selected == "m2":
    st.markdown('<div class="section-title">🖨️ Section 2: AI 與 3D 列印的完美共生</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 3D 列印技術演進
    | 時期 | 技術 | 特性 |
    |:----|:----|:----|
    | 1980s | SLA / FDM | 單色、粗糙 |
    | 2000s | SLS / PolyJet | 多材質、高精度 |
    | 2010s | CJP 全彩 | **百萬色彩** |
    | 2020s | AI + 全彩 | 自動生成、即時列印 |
    
    ### 全彩 3D 列印技術
    - **CJP（彩色噴射成型）**：多個噴頭同時噴射 UV 固化樹脂
    - **PolyJet**：像彩色噴墨印表機，層層堆疊
    - **Bambu Lab AMS**：最多 16 色換料系統
    
    ### AI 生成式設計的優勢
    - **結構減重**：AI 自動計算最佳結構（如飛機零件減重 30%）
    - **美感提升**：AI 生成有機形態（人類想不到的曲線）
    - **快速迭代**：10 分鐘生成 100 種設計方案
    """)
    st.image("https://via.placeholder.com/600x200/1e293b/fb923c?text=AI+Generative+Design+Example", caption="AI 生成式設計示意圖")

    st.markdown("### 全彩 3D 列印的技術限制")
    st.warning("⚠️ 需了解的限制：最小壁厚 ≥ 1.5mm、懸垂結構需支撐、全彩成本較高")

# ════════ Section 3 ════════
elif selected == "m3":
    st.markdown('<div class="section-title">🛠️ Section 3: 當前主流 AI 工具圖譜</div>', unsafe_allow_html=True)

    st.markdown("### 語言 AI")
    c1, c2, c3 = st.columns(3)
    for col, name, desc, price in zip([c1, c2, c3], ["ChatGPT", "Claude", "Gemini"], ["文案、問答、Prompt", "長文章、邏輯分析", "Google 整合"], ["✅ 免費", "✅ 免費", "✅ 免費"]):
        with col:
            st.markdown(f'<div class="tool-card"><div class="name">{name}</div><div class="desc">{desc}</div><div class="price">{price}</div></div>', unsafe_allow_html=True)

    st.markdown("### 圖像 AI")
    c1, c2, c3 = st.columns(3)
    for col, name, desc, price in zip([c1, c2, c3], ["Midjourney", "DALL-E 3 ⭐", "Bing Image Creator"], ["美感最強、設計首選", "最易上手、初學者首選", "免費、中文OK"], ["💲 付費 $10/月", "✅ ChatGPT 內免費", "✅ 完全免費"]):
        with col:
            st.markdown(f'<div class="tool-card"><div class="name">{name}</div><div class="desc">{desc}</div><div class="price">{price}</div></div>', unsafe_allow_html=True)

    st.markdown("### 3D 生成 AI")
    c1, c2, c3 = st.columns(3)
    for col, name, desc, price in zip([c1, c2, c3], ["Meshy.ai ⭐", "Tripo AI", "Rodin AI"], ["紋理最佳、全彩列印首選", "速度最快（10-30秒）", "最高品質、商業用途"], ["✅ 200點/月", "✅ 免費點數", "💲 預覽免費"]):
        with col:
            st.markdown(f'<div class="tool-card"><div class="name">{name}</div><div class="desc">{desc}</div><div class="price">{price}</div></div>', unsafe_allow_html=True)

    st.markdown("### 課程主線流程")
    st.markdown('<div class="highlight-box"><strong>DALL-E 3</strong>（生成設計圖）→ <strong>Meshy AI</strong>（轉3D模型）→ <strong>3D列印</strong>（成品輸出）</div>', unsafe_allow_html=True)

    st.info("💡 學習期間：免費工具組合完全夠用，月費 NT$0 也能完成完整作品！")

# ════════ Section 4 ════════
elif selected == "m4":
    st.markdown('<div class="section-title">⚖️ Section 4: 智慧財產權與商業倫理</div>', unsafe_allow_html=True)
    st.markdown("""
    ### AI 生成物的版權現況
    | 國家/地區 | AI 生成物版權 | 說明 |
    |:---------|:-------------|:----|
    | 🇺🇸 美國 | ❌ 不保護 | 無人類創作要素不受版權保護 |
    | 🇪🇺 歐盟 | ❌ 不保護 | 需人類「原創性」貢獻 |
    | 🇯🇵 日本 | ⚠️ 灰色地帶 | 討論中，傾向開放 |
    | 🇹🇼 台灣 | ⚠️ 灰色地帶 | 尚無明確判例 |
    
    ### 台灣設計師安全指南
    1. ✅ 加入「足夠的人類創作」— 修改、組合、挑選
    2. ✅ 記錄創作過程（Prompt + 修改記錄）
    3. ✅ 商業使用前確認各工具的使用條款
    4. ⚠️ 避免直接複製他人風格
    
    ### AI 時代建立個人品牌
    - 不要只當「AI 操作員」— 要當「AI 創意總監」
    - 你的價值在於：品味 × 判斷力 × 市場洞察
    - 案例：台灣設計師用 AI 接國外訂單，月收 $3,000+
    
    ### AI 創作倫理原則
    1. 透明揭露：標示 AI 輔助創作
    2. 尊重原創：不抄襲、不侵權
    3. 品質把關：AI 輸出需人工審核
    4. 社會責任：不製作有害內容
    """)

# ════════ 下午實作A ════════
elif selected == "afternoon_a":
    st.markdown('<div class="section-title">🎨 下午實作 A: Prompt 工程</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 實作目標
    學會用 AI 生成「具有 3D 結構感」的產品設計圖
    
    ### Prompt Engineering 黃金公式
    ```
    主體 + 場景 + 風格 + 光線 + 顏色
    ```
    
    ### 產品設計 Prompt 關鍵詞彙庫
    | 類別 | 關鍵詞 |
    |:----|:-------|
    | 形狀 | 圓潤、幾何、有機、流線型 |
    | 材質 | 光滑、霧面、金屬、木紋 |
    | 風格 | 極簡、復古、科幻、可愛 |
    | 視角 | 正面、45度俯視、多視角 |
    | 背景 | 純白、漸層、自然光、棚拍 |

    ### 多視角設計圖 Prompt
    ```
    一個[產品名稱]的3D產品設計圖，
    展示正面、側面、背面和45度視角，
    [風格描述]，[材質描述]，
    純白背景，商品攝影風格，高解析度
    ```
    """)

# ════════ 下午實作B ════════
elif selected == "afternoon_b":
    st.markdown('<div class="section-title">🖼️ 下午實作 B: 圖片優化</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 為什麼 AI 生成圖像需要優化？
    - AI 生成的圖像不一定符合列印需求
    - 解析度、色彩模式、背景都需要調整
    
    ### 常用優化工具
    | 工具 | 功能 | 費用 |
    |:----|:----|:----|
    | **ClipDrop** | 去背、打光、超解析度 | 免費版 |
    | **Leonardo.ai** | 圖片放大、風格轉換 | 免費 150點/天 |
    | **Adobe Firefly** | 生成填滿、延伸背景 | 免費版 |
    
    ### 全彩 3D 列印對圖像的要求
    | 項目 | 最低要求 |
    |:----|:---------|
    | 解析度 | ≥ 300 DPI |
    | 色彩模式 | RGB（螢幕）/ CMYK（印刷）|
    | 背景 | 純色或透明 |
    | 檔案格式 | PNG（支援透明背景）|
    
    ### 實作步驟
    1. 用 AI 生成設計圖
    2. 去背處理
    3. 調整解析度（至少 1024×1024）
    4. 色彩校正
    5. 輸出 PNG 格式
    """)

# ════════ 下午實作C ════════
elif selected == "afternoon_c":
    st.markdown('<div class="section-title">🧊 下午實作 C: 2D 轉 3D</div>', unsafe_allow_html=True)
    st.markdown("""
    ### AI 如何將 2D 圖片「腦補」成 3D 模型？
    - AI 從單張或多張圖片推測物體的立體結構
    - 從訓練資料中學習「這個物體長什麼樣子」
    - 生成網格（Mesh）＋紋理貼圖（Texture）
    
    ### 實作流程
    ```
    2D 設計圖（DALL-E 3）
         │
         ▼
    Meshy.ai / Tripo AI（2D→3D）
         │
         ▼
    模型優化（修復破面、調整比例）
         │
         ▼
    匯出 3MF（保留全彩資訊）
         │
         ▼
    Bambu Studio 切片
         │
         ▼
    全彩 3D 列印 🖨️
    ```
    
    ### 如何評估 3D 模型品質？
    - ✅ 幾何完整（無破面）
    - ✅ 紋理清晰（全彩貼圖無拉伸）
    - ✅ 比例協調（頭身比、尺寸）
    - ✅ 可列印（最小壁厚 ≥ 1.5mm）
    
    ### 實作常見問題
    | 問題 | 解決方法 |
    |:----|:---------|
    | 模型有破面 | Meshy 內建修復 / Bambu Studio 自動修復 |
    | 紋理模糊 | 提高輸入圖解析度 ≥ 1024px |
    | 比例怪異 | Meshy 中調整縮放 |
    | 無法列印 | 確認最小壁厚 ≥ 1.5mm |
    """)

# ── Footer ──
st.markdown("---")
st.markdown("<div style='text-align:center; color:#64748b; font-size:0.8rem;'>🤖 AI發展與應用 ｜ 教學網站版 ｜ 講師：嚴稑榛 ｜ 115.04.20</div>", unsafe_allow_html=True)
