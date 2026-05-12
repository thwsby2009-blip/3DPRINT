import streamlit as st

st.set_page_config(page_title="AI 文案全攻略", page_icon="✍️", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: 800; background: linear-gradient(135deg, #a855f7, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.3rem; }
    .sub-header { font-size: 1.1rem; color: #94a3b8; }
    .meta-text { font-size: 0.85rem; color: #64748b; }
    .section-title { font-size: 1.4rem; font-weight: 700; color: #c084fc; margin: 1rem 0; padding-bottom: 0.5rem; border-bottom: 2px solid #334155; }
    .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 1.2rem; margin-bottom: 1rem; }
    .card h3 { color: #c084fc; font-size: 1.1rem; margin-bottom: 0.5rem; }
    .card p, .card li { color: #cbd5e1; font-size: 0.9rem; }
    .highlight-box { background: #1e293b; border-left: 4px solid #c084fc; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .prompt-box { background: linear-gradient(135deg, #4c1d95, #6b21a8); border: 1px solid #7c3aed; border-radius: 10px; padding: 1rem; margin: 0.5rem 0; font-family: 'Courier New', monospace; font-size: 0.8rem; color: #d8b4fe; white-space: pre-wrap; }
    .code-box { background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 1rem; margin: 0.5rem 0; font-family: 'Courier New', monospace; font-size: 0.8rem; color: #a5b4fc; white-space: pre-wrap; }
    .flow-step { display: inline-block; background: #334155; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.8rem; margin: 0.2rem; }
    .flow-step .num { background: #c084fc; color: #0f172a; width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.7rem; margin-right: 0.3rem; }
    .tool-card { background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 1rem; margin-bottom: 0.5rem; }
    .tool-card .name { font-weight: 700; color: #c084fc; }
    .tool-card .desc { font-size: 0.8rem; color: #94a3b8; }
    hr { border-color: #334155; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div style='font-size:1.2rem; font-weight:700; color:#c084fc; margin-bottom:1rem;'>✍️ 目錄</div>", unsafe_allow_html=True)

nav = [
    ("intro", "📖 課程概述"),
    ("why", "💡 為什麼AI文案"),
    ("tools", "🔧 工具全景圖"),
    ("aida", "🎯 AIDA框架"),
    ("prompt", "💬 Prompt技巧"),
    ("types", "📝 文案類型"),
    ("optimize", "✨ 優化技巧"),
    ("canva", "🎨 Canva AI 實作"),
    ("gamma", "⚡ Gamma 簡報"),
    ("design", "🎭 設計原則"),
    ("ethics", "⚖️ 倫理與實戰"),
    ("action", "🗓️ 30天挑戰"),
]

selected = None
for key, label in nav:
    if st.sidebar.button(label, key=f"nav_{key}", use_container_width=True, type="secondary"):
        selected = key
if not selected:
    selected = "intro"

st.sidebar.markdown("---")
st.sidebar.markdown("<div style='font-size:0.75rem; color:#64748b;'>講師：嚴稑榛<br>AI產品設計與全彩3D列印產品實作班<br>115.05.04</div>", unsafe_allow_html=True)

st.markdown('<div class="main-header">✍️ AI 產品文案設計</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">從零基礎到商業簡報的 AI 文案全攻略</div>', unsafe_allow_html=True)
st.markdown('<div class="meta-text">AI產品設計與全彩3D列印產品實作班 第⼀期｜115.05.04｜講師：嚴稑榛｜工具：ChatGPT・Canva AI・Gamma・Claude・Notion AI</div>', unsafe_allow_html=True)
st.markdown("---")

# ════════ Intro ════════
if selected == "intro":
    st.markdown('<div class="section-title">📖 課程概述</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 上午課程：AI 文案設計
    | 主題 | 內容 |
    |:----|:----|
    | 🧠 Module 1 | AI文案設計概論 — 為什麼需要AI文案、市場趨勢 |
    | 💬 Module 2 | Prompt Engineering 文案技巧 |
    | ✨ Module 3 | 文案品質優化技巧 |
    | 🛠️ Module 4 | 電商文案實戰模板 |
    | 🔗 Module 5 | Notion AI・Perplexity 等工具 |
    
    ### 下午課程：AI 簡報實務應用
    | 單元 | 內容 |
    |:---:|:----|
    | 🎨 第一單元 | Canva AI 魔法教室 — 15頁實作 |
    | ⚡ 第二單元 | Gamma 閃電簡報術 — 15頁實作 |
    | 🎭 第三單元 | 文案與視覺完美結合 |
    | 🏆 第四單元 | 成果發表與交流 |
    """)

    cols = st.columns(4)
    with cols[0]:
        st.metric("⏱️ 節省時間", "85%", "每週省4小時")
    with cols[1]:
        st.metric("🌍 Canva用戶", "2.6億", "月活躍")
    with cols[2]:
        st.metric("⚡ Gamma用戶", "5,000萬+", "2025")
    with cols[3]:
        st.metric("📄 總頁數", "110頁", "含學科+術科")

# ════════ Why AI ════════
elif selected == "why":
    st.markdown('<div class="section-title">💡 為什麼需要 AI 文案？</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.error("**傳統文案的困境**\n\n❌ 撰寫一份完整文案需數小時\n❌ 創意靈感枯竭\n❌ 多語言翻譯成本高\n❌ 設計排版技能門檻高\n❌ 修改溝通效率低")
    with col2:
        st.success("**AI文案的解決方案**\n\n✅ 60秒生成專業文案初稿\n✅ 精準Prompt引導優質內容\n✅ 一鍵翻譯100+語言\n✅ AI自動配圖排版\n✅ 即時優化無限修改")

    st.markdown("### 📊 市場趨勢")
    cols = st.columns(3)
    with cols[0]:
        st.metric("📈 行銷人員效率", "85%", "每週省4小時+")
    with cols[1]:
        st.metric("🎨 Canva AI功能", "10億+", "已被使用次數")
    with cols[2]:
        st.metric("👥 Gamma用戶", "5,000萬", "2025年")

# ════════ Tools ════════
elif selected == "tools":
    st.markdown('<div class="section-title">🔧 AI 文案工具全景圖</div>', unsafe_allow_html=True)
    
    tools_data = [
        ("ChatGPT ⭐", "文字生成", "OpenAI對話式AI，文案初稿利器", "✅ 免費"),
        ("Claude", "文字生成", "Anthropic出品，長文邏輯最強", "✅ 免費"),
        ("Canva AI ⭐", "設計+文案", "Magic Write + 設計一體", "✅ 免費版"),
        ("Gamma ⭐", "簡報生成", "AI一鍵生成互動式簡報", "✅ 免費400點"),
        ("Notion AI", "文件工作流", "AI寫作+知識管理整合", "💲 付費"),
        ("Perplexity", "研究助手", "AI搜尋+即時資訊整合", "✅ 免費"),
    ]
    
    cols = st.columns(3)
    for i, (name, typ, desc, price) in enumerate(tools_data):
        with cols[i % 3]:
            st.markdown(f'<div class="tool-card"><div class="name">{name}</div><div class="desc"><strong>{typ}</strong><br>{desc}</div><div class="price">{price}</div></div>', unsafe_allow_html=True)

    st.markdown("### 工具整合矩陣")
    st.markdown("""
    ```
    研究階段         文案創作         視覺設計         簡報製作         管理優化
    Perplexity AI → ChatGPT/Claude → Canva AI →     Gamma AI →      Notion AI
    市場洞察         文案初稿         Banner/海報     投資提案         文案資料庫
    競品分析         多版本測試       IG貼文/電商圖   客戶簡報         版本管理
    ```
    """)

# ════════ AIDA ════════
elif selected == "aida":
    st.markdown('<div class="section-title">🎯 優質文案黃金公式：AIDA 框架</div>', unsafe_allow_html=True)

    st.markdown("""
    | 步驟 | 中文 | 目標 | 範例 |
    |:----|:----|:----|:----|
    | **A**ttention | 注意力 | 抓住眼球 | 「3分鐘教你用AI寫出百萬文案！」 |
    | **I**nterest | 興趣 | 說明價值 | 功能特色、使用場景、解決痛點 |
    | **D**esire | 慾望 | 想要擁有 | 社會認同、限時優惠、成功案例 |
    | **A**ction | 行動 | 立即購買 | 「立即購買」「免費試用」 |
    """)

    st.markdown("### 電商商品頁文案完整框架")
    st.markdown("""```
    【商品標題】[關鍵詞] + [獨特賣點] + [適用族群]（20字內）
    範例：全彩3D列印客製化手機殼｜姓名圖案任意印｜送禮自用最佳選擇

    【第一段鉤子】用一個問題或場景喚起共鳴（30字內）
    範例：你的手機殼跟別人長一樣嗎？用3D列印讓手機殼說你的故事！

    【產品核心介紹】是什麼 + 怎麼做 + 為什麼好（80字）

    【三大賣點條列】✓ 賣點1 ✓ 賣點2 ✓ 賣點3

    【行動呼籲】限時優惠 + 明確行動 + 稀缺感
    ```""")

# ════════ Prompt ════════
elif selected == "prompt":
    st.markdown('<div class="section-title">💬 Prompt Engineering 文案技巧</div>', unsafe_allow_html=True)
    st.markdown("### AI 輔助文案五步驟")
    steps = ["確定目標受眾", "釐清文案目的", "設計Prompt", "AI生成初稿", "優化與設計"]
    cols = st.columns(5)
    for i, (col, step) in enumerate(zip(cols, steps)):
        with col:
            st.markdown(f'<div class="flow-step"><span class="num">{i+1}</span>{step}</div>', unsafe_allow_html=True)

    st.markdown("### 萬用文案 Prompt")
    st.markdown('<div class="prompt-box">你是專業3D列印電商文案師，幫我用AIDA架構為以下商品寫蝦皮頁面描述：\n商品：[產品名稱]\n材質：全彩3D列印PLA材質  尺寸：約[X]公分\n特色：[2-3個特色]\n請包含：吸睛標題、三點特色、使用情境、購買呼籲，總計200字內。</div>', unsafe_allow_html=True)

    st.markdown("### Prompt 黃金公式")
    st.info("**角色 + 任務 + 細節 + 格式**\n\n❌ 差：「幫我寫產品文案」\n✅ 好：「你是3D列印電商文案師，幫我寫一款貓咪公仔的蝦皮商品頁，150字活潑台灣口語」")

# ════════ Types ════════
elif selected == "types":
    st.markdown('<div class="section-title">📝 文案的類型與應用場景</div>', unsafe_allow_html=True)
    st.markdown("""
    | 類型 | 應用場景 | 工具 |
    |:----|:---------|:----|
    | 🏷️ 產品說明文案 | 規格說明、功能介紹 | ChatGPT/Claude |
    | 📣 行銷廣告文案 | FB廣告、Google Ads | ChatGPT |
    | 📱 社群媒體文案 | IG貼文、Threads | Canva AI |
    | 🛒 電商銷售文案 | 蝦皮商品描述 | ChatGPT |
    | 📖 品牌故事文案 | 關於我們、品牌使命 | Claude |
    | 📊 簡報簡介文案 | 商業提案、產品發布 | Gamma |
    """)

# ════════ Optimize ════════
elif selected == "optimize":
    st.markdown('<div class="section-title">✨ 文案品質優化技巧</div>', unsafe_allow_html=True)
    st.markdown("### 四步驟優化工作流程")
    steps = ["生成初稿", "AI自我審稿", "風格調整", "A/B版本測試"]
    cols = st.columns(4)
    for i, (col, step) in enumerate(zip(cols, steps)):
        with col:
            st.markdown(f'<div class="flow-step"><span class="num">{i+1}</span>{step}</div>', unsafe_allow_html=True)

    st.markdown("""
    ### AI 審稿 Prompt 範例
    """)
    st.markdown('<div class="prompt-box">請扮演專業文案審稿人，找出以下文案的3個可以改進的地方，並給出具體修改建議：\n[貼上你的文案]</div>', unsafe_allow_html=True)

    st.markdown("### 風格調整 Prompt")
    st.markdown('<div class="prompt-box">請把以下文案改成[活潑搞笑/專業商務/溫情感人]風格，目標客群是[描述對象]，150字以內：\n[貼上你的文案]</div>', unsafe_allow_html=True)

# ════════ Canva ════════
elif selected == "canva":
    st.markdown('<div class="section-title">🎨 Canva AI 魔法教室</div>', unsafe_allow_html=True)
    st.markdown("""
    ### Canva AI 三大魔法功能
    | 功能 | 說明 |
    |:----|:------|
    | ✨ **Magic Write** | AI 撰寫文案，直接插入設計 |
    | 🎨 **Magic Design** | 上傳圖片→一鍵生成整套設計 |
    | 🖼️ **Magic Media** | 文字描述生成圖片 |
    
    ### 實作任務
    1. 使用 **Magic Write** 生成 IG 推廣文案
    2. 使用 **Magic Design** 生成一張商品 Banner
    3. 設定品牌配色
    
    ### Canva AI 操作流程
    1. 前往 **canva.com**
    2. 點選「設計」→ 選擇尺寸（IG貼文/Banner）
    3. 使用 Magic Write 輸入需求
    4. AI 自動生成文案與排版
    5. 調整細節後下載
    """)

# ════════ Gamma ════════
elif selected == "gamma":
    st.markdown('<div class="section-title">⚡ Gamma 閃電簡報術</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 傳統 vs AI 做簡報
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.error("**傳統做簡報**\n\n❌ 需學 PowerPoint\n❌ 自己找圖片素材\n❌ 手動調整排版\n❌ 花費數小時\n❌ 不懂設計就很難看")
    with col2:
        st.success("**AI 輔助做簡報**\n\n✅ 輸入幾字就生成\n✅ AI 自動配圖配色\n✅ 一鍵美化排版\n✅ 5分鐘完成一份\n✅ 人人都能專業感")

    st.markdown("### Gamma 貼文案→秒變簡報")
    st.markdown("""
    1. 在 Gamma 首頁點「建立新簡報」→「匯入」
    2. 複製你寫好的文案貼入
    3. 選擇簡報風格（現代/簡約/大膽）
    4. 按「生成」，等 **10 秒**
    5. 完整的簡報就出現了！
    
    ### 一鍵匯出格式
    | 格式 | 用途 |
    |:----|:----|
    | 📄 PDF | 客戶、列印、Email |
    | 📊 PowerPoint | 進階編輯 |
    | 🖼️ PNG/JPG | 社群媒體 |
    | 🔗 公開連結 | 客戶即時瀏覽 |
    """)

# ════════ Design ════════
elif selected == "design":
    st.markdown('<div class="section-title">🎭 文案與視覺完美結合</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 字體的力量 — 字型決定質感
    | 字體 | 感覺 | 適用 |
    |:----|:----|:----|
    | 🟣 圓黑體 | 可愛、親切 | 年輕產品 |
    | 🔵 細黑體 | 簡約、現代 | 科技產品 |
    | 🟤 明體 | 典雅、高端 | 精品品牌 |
    | ✏️ 手寫體 | 溫暖、文青 | 個人品牌 |
    
    ### 使用原則
    - 一份簡報最多用 **2 種字體**
    - 標題用粗字，內文用細字
    - 確保黑色文字在淺背景可讀
    
    ### 排版技巧
    - **留白**：不要把每個角落塞滿
    - **對齊**：元素整齊排列
    - **對比**：大小/顏色/粗細對比
    - **一致性**：全簡報風格統一
    """)

# ════════ Ethics ════════
elif selected == "ethics":
    st.markdown('<div class="section-title">⚖️ AI 文案使用倫理</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 負責任使用 AI 文案
    | 原則 | 說明 |
    |:----|:------|
    | ✅ **事實查核** | AI 可能生成錯誤數字，人工查核 |
    | ©️ **著作權** | 確認 AI 圖片可商用（Canva Pro 有授權）|
    | 🔒 **資料隱私** | 勿輸入客戶個資、商業機密 |
    | ✍️ **人工潤稿** | AI 是起點，加入品牌個性才動人 |
    | 🏷️ **透明揭露** | 部分場景需標示 AI 輔助 |
    | 🤝 **人機協作** | AI 放大能力，人腦提升品質 |
    
    ### 課堂三大實戰任務（30分鐘）
    | 任務 | 時間 | 內容 |
    |:---:|:----:|:----|
    | 1️⃣ ChatGPT文案 | 10分 | 蝦皮標題+描述+賣點 |
    | 2️⃣ Canva AI設計 | 10分 | IG文案+Banner+配色 |
    | 3️⃣ Gamma簡報 | 10分 | 6頁商業提案 |
    """)

# ════════ 30天挑戰 ════════
elif selected == "action":
    st.markdown('<div class="section-title">🗓️ 課後30天實踐挑戰</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 第1週（第1-7天）— 基礎建立
    - [ ] 完成三大工具帳號設定（Canva/Gamma/ChatGPT）
    - [ ] 練習 Prompt 框架，生成 5 份不同產品文案
    - [ ] 用 Canva AI 完成一張商品 Banner
    
    ### 第2週（第8-14天）— 深化應用
    - [ ] 用 Gamma AI 生成第一份完整商業簡報
    - [ ] 建立 Notion AI 文案資料庫
    - [ ] 完成一篇品牌故事全稿
    
    ### 第3-4週（第15-30天）— 實戰整合
    - [ ] 完成一個完整產品的 AI 文案+設計+簡報套組
    - [ ] 在社群媒體發布 3 篇 AI 輔助文案並觀察成效
    - [ ] 建立個人 AI 文案作品集
    """)

    st.markdown("""
    <div class="highlight-box">
    <strong>💡 佳句：</strong>
    「AI 不會取代人，但會使用 AI 的人，會取代不會使用 AI 的人。」
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center; color:#64748b; font-size:0.8rem;'>✍️ AI產品文案設計 ｜ 教學網站版 ｜ 講師：嚴稑榛 ｜ 115.05.04</div>", unsafe_allow_html=True)
