import streamlit as st
import os

# ── Page Config ──
st.set_page_config(
    page_title="AI × 3D列印 產品一條龍設計",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ──
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem; font-weight: 800;
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }
    .sub-header { font-size: 1.1rem; color: #94a3b8; margin-bottom: 0.3rem; }
    .meta-text { font-size: 0.85rem; color: #64748b; }
    .section-title {
        font-size: 1.4rem; font-weight: 700;
        color: #fbbf24; margin: 1rem 0 1rem;
        padding-bottom: 0.5rem; border-bottom: 2px solid #334155;
    }
    .card {
        background: #1e293b; border: 1px solid #334155;
        border-radius: 12px; padding: 1.2rem; margin-bottom: 1rem;
    }
    .card h3 { color: #fbbf24; font-size: 1.1rem; margin-bottom: 0.5rem; }
    .card p, .card li { color: #cbd5e1; font-size: 0.9rem; }
    .highlight-box {
        background: #1e293b; border-left: 4px solid #fbbf24;
        padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0;
    }
    .prompt-box {
        background: linear-gradient(135deg, #1e1b4b, #312e81);
        border: 1px solid #4338ca; border-radius: 10px;
        padding: 1rem; margin: 0.5rem 0;
        font-family: 'Courier New', monospace; font-size: 0.8rem;
        color: #c4b5fd; white-space: pre-wrap;
    }
    .flow-step {
        display: inline-block; background: #334155;
        padding: 0.4rem 0.8rem; border-radius: 20px;
        font-size: 0.8rem; margin: 0.2rem;
    }
    .flow-step .num {
        background: #fbbf24; color: #0f172a;
        width: 20px; height: 20px; border-radius: 50%;
        display: inline-flex; align-items: center; justify-content: center;
        font-weight: 700; font-size: 0.7rem; margin-right: 0.3rem;
    }
    .tool-card {
        background: #0f172a; border: 1px solid #334155;
        border-radius: 10px; padding: 1rem; margin-bottom: 0.5rem;
    }
    .tool-card .name { font-weight: 700; color: #fbbf24; }
    .tool-card .desc { font-size: 0.8rem; color: #94a3b8; }
    .tool-card .price { font-size: 0.75rem; color: #34d399; }
    .check-item { margin: 0.3rem 0; font-size: 0.9rem; }
    hr { border-color: #334155; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar Navigation ──
st.sidebar.markdown("<div style='font-size:1.2rem; font-weight:700; color:#fbbf24; margin-bottom:1rem;'>🧊 目錄</div>", unsafe_allow_html=True)

nav_items = [
    ("overview", "🎯 課程概述"),
    ("tools", "🔧 工具一覽"),
    ("flow", "🔄 一條龍流程"),
    ("prompt", "💬 Prompt 技巧"),
    ("meshy", "🧊 Meshy 操作"),
    ("copy", "✍️ AI 文案"),
    ("slide", "📊 簡報製作"),
    ("shop", "🛒 電商網站"),
    ("pricing", "💰 定價策略"),
    ("checklist", "✅ 檢查清單"),
]

selected = None
for key, label in nav_items:
    if st.sidebar.button(label, key=f"nav_{key}", use_container_width=True, type="secondary"):
        selected = key

if not selected:
    selected = "overview"

st.sidebar.markdown("---")
st.sidebar.markdown("<div style='font-size:0.75rem; color:#64748b;'>講師：嚴稑榛<br>勞動部桃竹苗分署<br>2026.05.11</div>", unsafe_allow_html=True)

# ── Hero ──
st.markdown('<div class="main-header">🧊 AI × 全彩 3D 列印</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">產品一條龍設計｜從零到電商上架</div>', unsafe_allow_html=True)
st.markdown('<div class="meta-text">講師：嚴稑榛 ｜ 勞動部勞動力發展署桃竹苗分署 ｜ 2026.05.11</div>', unsafe_allow_html=True)
st.markdown("---")

# ══════════════════════════════════════
# 各章節內容
# ══════════════════════════════════════

# ── 1. 課程概述 ──
if selected == "overview":
    st.markdown('<div class="section-title">🎯 課程概述</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🇹🇼 台灣3D列印市場", "NT$150億+", "年規模")
    with col2:
        st.metric("⚡ AI效率提升", "300%", "輔助設計")
    with col3:
        st.metric("⏱️ 商業化時間", "1小時", "Idea→上架")

    st.markdown("""
    <div class="card">
    <h3>📌 課程目標</h3>
    <p>用 AI 工具，<strong>1 小時內</strong>完成產品 Idea → 文案 → 3D 模型 → 電商上架！</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👤 學員成功案例")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**陳先生（52歲）**\n\n前工廠作業員\n蝦皮賣公仔月入 NT$18,000")
    with col2:
        st.info("**林女士（45歲）**\n\n家庭主婦\nEtsy 月收 USD 400-600")
    with col3:
        st.info("**王先生（48歲）\n\n前服務業\n廟宇神明公仔接企業訂單")

# ── 2. 工具一覽 ──
elif selected == "tools":
    st.markdown('<div class="section-title">🔧 AI 工具一覽</div>', unsafe_allow_html=True)

    st.markdown("### 🤖 語言 AI")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="tool-card"><div class="name">ChatGPT</div><div class="desc">文案、問答、Prompt 測試</div><div class="price">✅ 免費（GPT-4o）</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="tool-card"><div class="name">Claude</div><div class="desc">長文章、邏輯分析</div><div class="price">✅ 免費（Sonnet）</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="tool-card"><div class="name">Gemini</div><div class="desc">Google 整合</div><div class="price">✅ 免費</div></div>', unsafe_allow_html=True)

    st.markdown("### 🧊 3D 生成 AI")
    data = {
        "工具": ["Meshy.ai ⭐", "Tripo3D", "Rodin AI", "Hunyuan3D"],
        "免費額度": ["200點/月", "充足", "預覽免費", "完全免費"],
        "速度": ["30-60秒", "2-10秒", "2-5分", "60-100秒"],
        "列印品質": ["97%", "90%", "最高", "高"],
        "推薦場景": ["公仔首選", "初學者", "商業用途", "開源研究"],
    }
    st.dataframe(data, use_container_width=True, hide_index=True)

    st.markdown("### 📊 簡報 & 設計 AI")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="tool-card"><div class="name">Gamma.app ⭐</div><div class="desc">文案一鍵生成精美簡報</div><div class="price">✅ 免費 400點</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="tool-card"><div class="name">Canva AI</div><div class="desc">設計、簡報、圖片生成</div><div class="price">✅ 免費版</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="tool-card"><div class="name">Bing Image Creator</div><div class="desc">中文描述即可生成圖片</div><div class="price">✅ 完全免費</div></div>', unsafe_allow_html=True)

# ── 3. 一條龍流程 ──
elif selected == "flow":
    st.markdown('<div class="section-title">🔄 產品一條龍流程</div>', unsafe_allow_html=True)

    steps = ["構思產品", "設計 Prompt", "生成3D模型", "模型優化", "全彩列印", "清洗後處理", "文案撰寫", "電商上架"]
    cols = st.columns(8)
    for i, (col, step) in enumerate(zip(cols, steps)):
        with col:
            st.markdown(f'<div class="flow-step"><span class="num">{i+1}</span>{step}</div>', unsafe_allow_html=True)

    st.markdown("")
    st.markdown("""
    <div class="highlight-box">
    <strong>💡 一句話總結：</strong>
    想法 → ChatGPT → Meshy.ai → Bambu Studio → 蝦皮上架！
    </div>
    """, unsafe_allow_html=True)

# ── 4. Prompt 技巧 ──
elif selected == "prompt":
    st.markdown('<div class="section-title">💬 Prompt 工程入門</div>', unsafe_allow_html=True)

    st.markdown("### 黃金公式")
    st.code("角色 + 任務 + 細節 + 格式", language="text")

    st.markdown("### 差 vs 好的 Prompt")
    st.error("❌ 差：「幫我寫3D列印產品的文案。」")
    st.success('✅ 好：「你是專業3D列印電商文案師，幫我寫一款可愛貓咪擺飾公仔的蝦皮商品頁面文案，包含吸睛標題、3點特色、適合送禮說明，用活潑的台灣口語，150字內。」')

    st.markdown("### 3D 模型 Prompt 模板")
    st.code('"A cute sitting cat figurine, chubby proportions, wearing a tiny graduation cap, full color pastel tones, chibi style, 3D printable figurine, smooth surface, watertight mesh"', language="text")

    st.info("📌 3D 模型關鍵字：一定加 chibi style（可愛比例）、3D printable、watertight mesh（確保列印）")

# ── 5. Meshy 操作 ──
elif selected == "meshy":
    st.markdown('<div class="section-title">🧊 Meshy.ai 操作步驟</div>', unsafe_allow_html=True)
    st.markdown("全球最受 3D 列印社群歡迎的 AI 模型生成工具。公仔列印相容率 **97%**！")

    st.markdown("### 6 步驟快速上手")
    for i, step in enumerate([
        "前往 **meshy.ai** — 用 Google 帳號一鍵登入，新用戶 200 免費點數",
        "點選 **Text to 3D**（或 Image to 3D 使用參考圖）",
        "撰寫**英文 Prompt** — 效果比中文好",
        "設定參數 — 選 Sculpture / Cartoon 風格，按 Generate（消耗 10-20 點）",
        "選最佳結果 — 從 4 個預覽中選最喜歡的，按 Refine 精細化",
        "匯出 **3MF** — 保留顏色資訊，準備切片列印！",
    ], 1):
        st.markdown(f"**{i}.** {step}")

    st.markdown("### 台灣特色 Prompt 範本")
    st.code('# 台灣夜市小吃公仔\n"A cute chibi taiwanese street vendor, selling stinky tofu, wearing apron and bamboo hat, smiling, full color, 3D printable, watertight mesh"\n\n# 貓咪擺飾（最熱銷！）\n"A cute sitting cat figurine, chubby proportions, wearing a tiny graduation cap, full color pastel tones, chibi style, 3D printable figurine, smooth surface"')

# ── 6. AI 文案 ──
elif selected == "copy":
    st.markdown('<div class="section-title">✍️ AI 產品文案設計</div>', unsafe_allow_html=True)

    st.markdown("### AIDA 黃金框架")
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        st.markdown("**A**ttention")
    with col2:
        st.markdown("注意力")
    with col3:
        st.markdown("「全台唯一！3D列印客製化西裝男孩公仔」")

    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        st.markdown("**I**nterest")
    with col2:
        st.markdown("產生興趣")
    with col3:
        st.markdown("「百萬色彩全彩技術，細節栩栩如生」")

    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        st.markdown("**D**esire")
    with col2:
        st.markdown("激發渴望")
    with col3:
        st.markdown("「完美的桌上擺飾，還可以客製你的臉！」")

    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        st.markdown("**A**ction")
    with col2:
        st.markdown("行動呼籲")
    with col3:
        st.markdown("「限量20件，現在下單享9折！立即選購」")

    st.markdown("### 萬用文案 Prompt")
    st.code("""你是專業3D列印電商文案師，幫我用AIDA架構為以下商品寫蝦皮頁面描述：
商品：[產品名稱]
材質：全彩3D列印PLA材質  尺寸：約[X]公分
特色：[2-3個特色]
請包含：吸睛標題（含「客製化」「3D列印」關鍵字）、三點特色、使用情境、購買呼籲，總計200字內。""")

# ── 7. 簡報製作 ──
elif selected == "slide":
    st.markdown('<div class="section-title">📊 商業簡報製作</div>', unsafe_allow_html=True)
    st.markdown("### Gamma.app 操作")
    for i, step in enumerate([
        "前往 **gamma.app** 免費註冊",
        "點 **New with AI**",
        "輸入產品文案或主題大綱",
        "選擇視覺風格和配色",
        "一鍵生成並編輯細節",
    ], 1):
        st.markdown(f"**{i}.** {step}")

    st.markdown("### 5 頁完美簡報結構")
    data = {
        "頁數": ["第1頁", "第2頁", "第3頁", "第4頁", "第5頁"],
        "內容": ["封面 — 產品名稱 + 標語 + 圖片", "問題頁 — 引起共鳴", "解決方案", "產品展示 — 照片 + 規格", "購買頁 — 價格 + 優惠"],
    }
    st.dataframe(data, use_container_width=True, hide_index=True)

    st.markdown("### 美感原則")
    st.markdown("- **60-30-10 配色法**：主色60% + 輔色30% + 點綴色10%")
    st.markdown("- **最多 2 種字體**：粗體無襯線 + 細體無襯線")
    st.markdown("- **留白**：每頁 1-2 個重點 + 一張圖片就夠了")

# ── 8. 電商網站 ──
elif selected == "shop":
    st.markdown('<div class="section-title">🛒 電商網站建置</div>', unsafe_allow_html=True)
    st.markdown("### AI 建站工具比較")
    data = {
        "工具": ["Wix ADI", "Durable", "Hostinger AI"],
        "適合": ["完整電商", "超快速建站", "長期划算"],
        "免費方案": ["有廣告", "有限次數", "30天試用"],
        "付費": ["NT$200-600/月", "$12/月", "NT$80/月起"],
    }
    st.dataframe(data, use_container_width=True, hide_index=True)

    st.markdown("### 台灣金流方案")
    st.markdown("- **綠界科技 ECPay**：信用卡 / ATM / 超商代碼，手續費 2-3%")
    st.markdown("- **藍新金流**：信用卡 / 行動支付 / WebATM，手續費 2-3%")
    st.markdown("- **LINE Pay**：台灣超流行，手續費 2.2%")
    st.info("💡 新手建議先用綠界科技，Wix 和 Hostinger 都支援！")

# ── 9. 定價策略 ──
elif selected == "pricing":
    st.markdown('<div class="section-title">💰 定價策略（10cm 全彩公仔）</div>', unsafe_allow_html=True)

    st.markdown("### 成本結構")
    st.markdown("- 材料費（PLA+）：NT$35-80")
    st.markdown("- 電費（列印 3 小時）：NT$5-10")
    st.markdown("- AI 工具費用分攤：NT$5-15")
    st.markdown("- 後處理工時：NT$30-50")
    st.markdown("- 包裝材料：NT$15-25")
    st.markdown("**總成本約 NT$90-180 / 件**")

    st.markdown("### 建議售價")
    data = {
        "類型": ["標準款", "客製款", "全客製款"],
        "售價": ["NT$380-580", "NT$680-980", "NT$1,200-2,000"],
        "毛利率": ["60-70%", "70-75%", "75-85%"],
    }
    st.dataframe(data, use_container_width=True, hide_index=True)

# ── 10. 檢查清單 ──
elif selected == "checklist":
    st.markdown('<div class="section-title">✅ 列印前檢查清單</div>', unsafe_allow_html=True)

    st.markdown("### Prompt 設計")
    st.checkbox("角色描述清楚（種族/服裝/姿態）", key="c1")
    st.checkbox("加入風格關鍵字（chibi / sculpture）", key="c2")
    st.checkbox("加入 3D printable、watertight mesh", key="c3")

    st.markdown("### 模型生成")
    st.checkbox("已用 Refine 功能精細化", key="c4")
    st.checkbox("檢查無明顯破面/穿模", key="c5")
    st.checkbox("比例符合預期", key="c6")

    st.markdown("### 模型優化")
    st.checkbox("最小壁厚 ≥ 1.5mm", key="c7")
    st.checkbox("細部特徵 ≥ 2mm", key="c8")
    st.checkbox("已修復網格問題", key="c9")

    st.markdown("### 匯出設定")
    st.checkbox("選擇 3MF 格式（全彩保存！）", key="c10")
    st.checkbox("確認模型方向正確", key="c11")
    st.checkbox("尺寸正確（建議 8-15cm）", key="c12")

    st.warning("⚠️ 格式選錯＝全彩變黑白！全彩 3D 列印必用 3MF 格式！")

# ── Footer ──
st.markdown("---")
st.markdown("<div style='text-align:center; color:#64748b; font-size:0.8rem;'>🧊 AI × 3D列印產品一條龍設計 ｜ 教學網站版 ｜ 資料來源：嚴稑榛老師課程</div>", unsafe_allow_html=True)
