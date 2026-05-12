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
    .flow-step { display: inline-block; background: #334155; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.8rem; margin: 0.2rem; }
    .flow-step .num { background: #c084fc; color: #0f172a; width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.7rem; margin-right: 0.3rem; }
    .tool-card { background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 1rem; margin-bottom: 0.5rem; }
    .tool-card .name { font-weight: 700; color: #c084fc; }
    .tool-card .desc { font-size: 0.8rem; color: #94a3b8; }
    hr { border-color: #334155; margin: 1.5rem 0; }
    .stDataFrame { font-size: 0.85rem; }
    .stMetric label { color: #94a3b8 !important; }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("<div style='font-size:1.2rem; font-weight:700; color:#c084fc; margin-bottom:1rem;'>✍️ 目錄</div>", unsafe_allow_html=True)

nav = {
    "intro": "📖 課程概述",
    "why": "💡 為什麼AI文案",
    "tools": "🔧 工具全景圖",
    "aida": "🎯 AIDA框架",
    "prompt": "💬 Prompt技巧",
    "types": "📝 文案類型",
    "optimize": "✨ 優化技巧",
    "canva": "🎨 Canva AI 實作",
    "gamma": "⚡ Gamma 簡報",
    "design": "🎭 設計原則",
    "ethics": "⚖️ 倫理與實戰",
    "action": "🗓️ 30天挑戰",
}

selected = None
for key, label in nav.items():
    if st.sidebar.button(label, key=f"nav_{key}", use_container_width=True, type="secondary"):
        selected = key
if not selected:
    selected = "intro"

st.sidebar.markdown("---")
st.sidebar.markdown("<div style='font-size:0.75rem; color:#64748b;'>講師：嚴稑榛<br>AI產品設計與全彩3D列印產品實作班<br>115.05.04</div>", unsafe_allow_html=True)

st.markdown("<div class='main-header'>✍️ AI 產品文案設計</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>從零基礎到商業簡報的 AI 文案全攻略</div>", unsafe_allow_html=True)
st.markdown("<div class='meta-text'>AI產品設計與全彩3D列印產品實作班 第⼀期 | 115.05.04 | 講師：嚴稑榛 | 工具：ChatGPT・Canva AI・Gamma・Claude・Notion AI</div>", unsafe_allow_html=True)
st.markdown("---")

# ════════ Intro ════════
if selected == "intro":
    st.markdown("<div class='section-title'>📖 課程概述</div>", unsafe_allow_html=True)

    st.subheader("上午課程：AI 文案設計")
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("🧠 Module 1")
    with col2:
        st.markdown("AI文案設計概論 — 為什麼需要AI文案、市場趨勢")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("💬 Module 2")
    with col2:
        st.markdown("Prompt Engineering 文案技巧")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("✨ Module 3")
    with col2:
        st.markdown("文案品質優化技巧")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("🛠️ Module 4")
    with col2:
        st.markdown("電商文案實戰模板")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("🔗 Module 5")
    with col2:
        st.markdown("Notion AI・Perplexity 等工具")

    st.subheader("下午課程：AI 簡報實務應用")
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("🎨 第一單元")
    with col2:
        st.markdown("Canva AI 魔法教室 — 15頁實作")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("⚡ 第二單元")
    with col2:
        st.markdown("Gamma 閃電簡報術 — 15頁實作")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("🎭 第三單元")
    with col2:
        st.markdown("文案與視覺完美結合")

    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("🏆 第四單元")
    with col2:
        st.markdown("成果發表與交流")

    cols = st.columns(4)
    with cols[0]:
        st.metric("⏱️ 節省時間", "85%", "每週省4小時")
    with cols[1]:
        st.metric("🌍 Canva用戶", "2.6億", "月活躍")
    with cols[2]:
        st.metric("⚡ Gamma用戶", "5,000萬+", "2025")
    with cols[3]:
        st.metric("📄 總頁數", "110頁", "含學科+術科")

# ════════ Why ════════
elif selected == "why":
    st.markdown("<div class='section-title'>💡 為什麼需要 AI 文案？</div>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["傳統文案困境", "AI文案解決方案"])
    with tab1:
        st.error("❌ 撰寫一份完整文案需數小時")
        st.error("❌ 創意靈感枯竭，不知道怎麼開始")
        st.error("❌ 多語言翻譯成本高")
        st.error("❌ 設計排版技能門檻高")
        st.error("❌ 修改來回溝通效率低")
    with tab2:
        st.success("✅ 60秒生成專業文案初稿")
        st.success("✅ 精準Prompt引導出優質內容")
        st.success("✅ 一鍵翻譯100+語言版本")
        st.success("✅ AI自動配圖排版與設計")
        st.success("✅ 即時優化，無限次修改")

    st.subheader("📊 市場趨勢")
    cols = st.columns(3)
    with cols[0]:
        st.metric("📈 行銷人員效率", "85%", "每週省4小時+")
    with cols[1]:
        st.metric("🎨 Canva AI功能", "10億+", "已被使用次數")
    with cols[2]:
        st.metric("👥 Gamma用戶", "5,000萬", "2025年")

# ════════ Tools ════════
elif selected == "tools":
    st.markdown("<div class='section-title'>🔧 AI 文案工具全景圖</div>", unsafe_allow_html=True)

    import pandas as pd
    tools_df = pd.DataFrame({
        "工具": ["ChatGPT ⭐", "Claude", "Canva AI ⭐", "Gamma ⭐", "Notion AI", "Perplexity"],
        "類型": ["文字生成", "文字生成", "設計+文案", "簡報生成", "文件工作流", "研究助手"],
        "特色": ["文案初稿利器", "長文邏輯最強", "Magic Write+設計", "一鍵互動式簡報", "AI寫作+知識管理", "AI搜尋+即時資訊"],
        "費用": ["✅ 免費", "✅ 免費", "✅ 免費版", "✅ 免費400點", "💲 付費", "✅ 免費"],
    })
    st.dataframe(tools_df, use_container_width=True, hide_index=True)

    st.subheader("工具整合矩陣")
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
    st.markdown("<div class='section-title'>🎯 優質文案黃金公式：AIDA 框架</div>", unsafe_allow_html=True)

    aida_data = {
        "步驟": ["Attention", "Interest", "Desire", "Action"],
        "中文": ["注意力", "興趣", "慾望", "行動"],
        "目標": ["抓住眼球", "說明價值", "想要擁有", "立即購買"],
        "範例": ["「3分鐘教你用AI寫出百萬文案！」", "功能特色、使用場景、解決痛點", "社會認同、限時優惠、成功案例", "「立即購買」「免費試用」"],
    }
    st.dataframe(aida_data, use_container_width=True, hide_index=True)

    st.subheader("電商商品頁文案完整框架")
    with st.container():
        st.markdown("""
**【商品標題】** [關鍵詞] + [獨特賣點] + [適用族群]（20字內）
範例：全彩3D列印客製化手機殼｜姓名圖案任意印｜送禮自用最佳選擇

**【第一段鉤子】** 用一個問題或場景喚起共鳴（30字內）
範例：你的手機殼跟別人長一樣嗎？用3D列印讓手機殼說你的故事！

**【產品核心介紹】** 是什麼 + 怎麼做 + 為什麼好（80字）

**【三大賣點條列】** ✓ 賣點1 ✓ 賣點2 ✓ 賣點3

**【行動呼籲】** 限時優惠 + 明確行動 + 稀缺感
""")

# ════════ Prompt ════════
elif selected == "prompt":
    st.markdown("<div class='section-title'>💬 Prompt Engineering 文案技巧</div>", unsafe_allow_html=True)

    st.subheader("AI 輔助文案五步驟")
    steps = ["確定目標受眾", "釐清文案目的", "設計Prompt", "AI生成初稿", "優化與設計"]
    cols = st.columns(5)
    for i, (col, step) in enumerate(zip(cols, steps)):
        with col:
            st.markdown(f"<div class='flow-step'><span class='num'>{i+1}</span>{step}</div>", unsafe_allow_html=True)

    st.subheader("萬用文案 Prompt")
    st.markdown("<div class='prompt-box'>你是專業3D列印電商文案師，幫我用AIDA架構為以下商品寫蝦皮頁面描述：\n商品：[產品名稱]\n材質：全彩3D列印PLA材質  尺寸：約[X]公分\n特色：[2-3個特色]\n請包含：吸睛標題、三點特色、使用情境、購買呼籲，總計200字內。</div>", unsafe_allow_html=True)

    st.subheader("Prompt 黃金公式")
    st.info("**角色 + 任務 + 細節 + 格式**")
    st.error("❌ 差：「幫我寫產品文案」")
    st.success("✅ 好：「你是3D列印電商文案師，幫我寫一款貓咪公仔的蝦皮商品頁，150字活潑台灣口語」")

# ════════ Types ════════
elif selected == "types":
    st.markdown("<div class='section-title'>📝 文案的類型與應用場景</div>", unsafe_allow_html=True)

    types_data = {
        "類型": ["產品說明文案", "行銷廣告文案", "社群媒體文案", "電商銷售文案", "品牌故事文案", "簡報簡介文案"],
        "應用場景": ["規格說明、功能介紹", "FB廣告、Google Ads", "IG貼文、Threads", "蝦皮商品描述", "關於我們、品牌使命", "商業提案、產品發布"],
        "建議工具": ["ChatGPT/Claude", "ChatGPT", "Canva AI", "ChatGPT", "Claude", "Gamma"],
    }
    st.dataframe(types_data, use_container_width=True, hide_index=True)

# ════════ Optimize ════════
elif selected == "optimize":
    st.markdown("<div class='section-title'>✨ 文案品質優化技巧</div>", unsafe_allow_html=True)

    st.subheader("四步驟優化工作流程")
    steps = ["生成初稿", "AI自我審稿", "風格調整", "A/B版本測試"]
    cols = st.columns(4)
    for i, (col, step) in enumerate(zip(cols, steps)):
        with col:
            st.markdown(f"<div class='flow-step'><span class='num'>{i+1}</span>{step}</div>", unsafe_allow_html=True)

    st.subheader("AI 審稿 Prompt")
    st.markdown("<div class='prompt-box'>請扮演專業文案審稿人，找出以下文案的3個可以改進的地方，並給出具體修改建議：\n[貼上你的文案]</div>", unsafe_allow_html=True)

    st.subheader("風格調整 Prompt")
    st.markdown("<div class='prompt-box'>請把以下文案改成[活潑搞笑/專業商務/溫情感人]風格，目標客群是[描述對象]，150字以內：\n[貼上你的文案]</div>", unsafe_allow_html=True)

# ════════ Canva ════════
elif selected == "canva":
    st.markdown("<div class='section-title'>🎨 Canva AI 魔法教室</div>", unsafe_allow_html=True)

    st.subheader("Canva AI 三大魔法功能")
    canva_data = {
        "功能": ["Magic Write", "Magic Design", "Magic Media"],
        "說明": ["AI 撰寫文案，直接插入設計", "上傳圖片→一鍵生成整套設計", "文字描述生成圖片"],
    }
    st.dataframe(canva_data, use_container_width=True, hide_index=True)

    st.subheader("Canva AI 操作流程")
    st.markdown("""
1. 前往 **canva.com**
2. 點選「設計」→ 選擇尺寸（IG貼文/Banner）
3. 使用 Magic Write 輸入需求
4. AI 自動生成文案與排版
5. 調整細節後下載
""")

# ════════ Gamma ════════
elif selected == "gamma":
    st.markdown("<div class='section-title'>⚡ Gamma 閃電簡報術</div>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["傳統做簡報", "AI 輔助做簡報"])
    with tab1:
        st.error("❌ 需要學 PowerPoint 技巧")
        st.error("❌ 自己找圖片素材")
        st.error("❌ 手動調整排版配色")
        st.error("❌ 花費數小時製作")
        st.error("❌ 不懂設計就很難看")
    with tab2:
        st.success("✅ 輸入幾個字就自動生成")
        st.success("✅ AI 自動配圖配色")
        st.success("✅ 一鍵美化排版")
        st.success("✅ 5分鐘完成一份簡報")
        st.success("✅ 人人都能做出專業感")

    st.subheader("Gamma 貼文案→秒變簡報")
    st.markdown("""
1. 在 Gamma 首頁點「建立新簡報」→「匯入」
2. 複製你寫好的文案貼入
3. 選擇簡報風格（現代/簡約/大膽）
4. 按「生成」，等 **10 秒**
5. 完整的簡報就出現了！
""")

    st.subheader("一鍵匯出格式")
    export_data = {
        "格式": ["PDF", "PowerPoint", "PNG/JPG", "公開連結"],
        "用途": ["客戶、列印、Email", "進階編輯", "社群媒體", "客戶即時瀏覽"],
    }
    st.dataframe(export_data, use_container_width=True, hide_index=True)

# ════════ Design ════════
elif selected == "design":
    st.markdown("<div class='section-title'>🎭 文案與視覺完美結合</div>", unsafe_allow_html=True)

    st.subheader("字體的力量 — 字型決定質感")
    font_data = {
        "字體": ["圓黑體", "細黑體", "明體", "手寫體", "粗黑體"],
        "感覺": ["可愛、親切", "簡約、現代", "典雅、高端", "溫暖、文青", "力量、衝擊"],
        "適用": ["年輕產品", "科技產品", "精品品牌", "個人品牌", "醒目標題"],
    }
    st.dataframe(font_data, use_container_width=True, hide_index=True)

    st.subheader("使用原則")
    st.markdown("- 一份簡報最多用 **2 種字體**")
    st.markdown("- 標題用粗字，內文用細字")
    st.markdown("- 重要字詞可放大或加粗")
    st.markdown("- 確保黑色文字在淺背景可讀")

    st.subheader("排版技巧")
    st.markdown("- **留白**：不要把每個角落塞滿")
    st.markdown("- **對齊**：元素整齊排列")
    st.markdown("- **對比**：大小/顏色/粗細對比")
    st.markdown("- **一致性**：全簡報風格統一")

# ════════ Ethics ════════
elif selected == "ethics":
    st.markdown("<div class='section-title'>⚖️ AI 文案使用倫理</div>", unsafe_allow_html=True)

    ethics_data = {
        "原則": ["事實查核", "著作權意識", "資料隱私", "人工潤稿", "AI揭露透明", "人機協作"],
        "說明": ["AI可能生成錯誤數字，人工查核", "確認AI圖片可商用（Canva Pro有授權）", "勿輸入客戶個資、商業機密", "AI是起點，加入品牌個性才動人", "部分場景需標示AI輔助", "AI放大能力，人腦提升品質"],
    }
    st.dataframe(ethics_data, use_container_width=True, hide_index=True)

    st.subheader("課堂三大實戰任務（30分鐘）")
    task_data = {
        "任務": ["1️⃣ ChatGPT文案挑戰", "2️⃣ Canva AI設計挑戰", "3️⃣ Gamma AI簡報挑戰"],
        "時間": ["10分鐘", "10分鐘", "10分鐘"],
        "內容": ["蝦皮標題+商品描述+三大賣點", "IG推廣文案+商品Banner+品牌配色", "6頁簡報：問題→解決方案→產品特色→市場→聯絡"],
    }
    st.dataframe(task_data, use_container_width=True, hide_index=True)

# ════════ 30天挑戰 ════════
elif selected == "action":
    st.markdown("<div class='section-title'>🗓️ 課後30天實踐挑戰</div>", unsafe_allow_html=True)

    st.markdown("### 第1週（第1-7天）— 基礎建立")
    st.checkbox("完成三大工具帳號設定（Canva/Gamma/ChatGPT）")
    st.checkbox("練習 Prompt 框架，生成 5 份不同產品文案")
    st.checkbox("用 Canva AI 完成一張商品 Banner")

    st.markdown("### 第2週（第8-14天）— 深化應用")
    st.checkbox("用 Gamma AI 生成第一份完整商業簡報")
    st.checkbox("建立 Notion AI 文案資料庫")
    st.checkbox("完成一篇品牌故事全稿")

    st.markdown("### 第3-4週（第15-30天）— 實戰整合")
    st.checkbox("完成一個完整產品的 AI 文案+設計+簡報套組")
    st.checkbox("在社群媒體發布 3 篇 AI 輔助文案並觀察成效")
    st.checkbox("建立個人 AI 文案作品集，準備求職或創業使用")

    st.info("💡 「AI 不會取代人，但會使用 AI 的人，會取代不會使用 AI 的人。」")

st.markdown("---")
st.markdown("<div style='text-align:center; color:#64748b; font-size:0.8rem;'>✍️ AI產品文案設計 ｜ 教學網站版 ｜ 講師：嚴稑榛 ｜ 115.05.04</div>", unsafe_allow_html=True)
