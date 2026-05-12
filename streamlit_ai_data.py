import streamlit as st

st.set_page_config(page_title="AI 數位內容與數據分析", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: 800; background: linear-gradient(135deg, #3b82f6, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.3rem; }
    .sub-header { font-size: 1.1rem; color: #94a3b8; }
    .meta-text { font-size: 0.85rem; color: #64748b; }
    .section-title { font-size: 1.4rem; font-weight: 700; color: #60a5fa; margin: 1rem 0; padding-bottom: 0.5rem; border-bottom: 2px solid #334155; }
    .card { background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 1.2rem; margin-bottom: 1rem; }
    .card h3 { color: #60a5fa; font-size: 1.1rem; margin-bottom: 0.5rem; }
    .card p, .card li { color: #cbd5e1; font-size: 0.9rem; }
    .highlight-box { background: #1e293b; border-left: 4px solid #60a5fa; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .code-box { background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 1rem; margin: 0.5rem 0; font-family: 'Courier New', monospace; font-size: 0.8rem; color: #a5b4fc; white-space: pre-wrap; }
    .flow-step { display: inline-block; background: #334155; padding: 0.4rem 0.8rem; border-radius: 20px; font-size: 0.8rem; margin: 0.2rem; }
    .flow-step .num { background: #60a5fa; color: #0f172a; width: 20px; height: 20px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.7rem; margin-right: 0.3rem; }
    .tool-card { background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 1rem; margin-bottom: 0.5rem; }
    .tool-card .name { font-weight: 700; color: #60a5fa; }
    .tool-card .desc { font-size: 0.8rem; color: #94a3b8; }
    hr { border-color: #334155; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──
st.sidebar.markdown("<div style='font-size:1.2rem; font-weight:700; color:#60a5fa; margin-bottom:1rem;'>📊 目錄</div>", unsafe_allow_html=True)

nav = [
    ("intro", "📖 課程概述"),
    ("m1", "🧠 Module 1: AI與數據"),
    ("m2", "📊 Module 2: 數據分析流程"),
    ("m3", "📂 Module 3: 資料類型"),
    ("m4", "🤖 Module 4: AIGC"),
    ("m5", "⚙️ Module 5: 機器學習"),
    ("m6", "💼 Module 6: 職場AI"),
    ("afternoon", "🛠️ 下午術科"),
    ("gsc", "🔍 Google Search Console"),
    ("ga4", "📈 Google Analytics 4"),
    ("trends", "📉 Google Trends"),
    ("sheets", "📋 Google Sheets"),
    ("colab", "🐍 Python/Colab"),
    ("ml_lab", "🧪 ML 實作"),
    ("api", "🔌 AI API 串接"),
]

selected = None
for key, label in nav:
    if st.sidebar.button(label, key=f"nav_{key}", use_container_width=True, type="secondary"):
        selected = key
if not selected:
    selected = "intro"

st.sidebar.markdown("---")
st.sidebar.markdown("<div style='font-size:0.75rem; color:#64748b;'>講師：嚴稑榛<br>勞動部桃竹苗分署<br>115.04.27</div>", unsafe_allow_html=True)

# ── Hero ──
st.markdown('<div class="main-header">📊 AI 數位內容與數據分析</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">學科課程｜第二天上午 115.04.27</div>', unsafe_allow_html=True)
st.markdown('<div class="meta-text">AI產品設計與全彩3D列印產品實作班 第⼀期｜班級代碼：162052｜授課講師：嚴稑榛</div>', unsafe_allow_html=True)
st.markdown("---")

# ════════ Intro ════════
if selected == "intro":
    st.markdown('<div class="section-title">📖 課程概述</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 今日課程大綱
    | 時間 | 主題 |
    |:----|:----|
    | 9:00–9:50 | AI 與數據世界 — 什麼是AI、ML、Deep Learning；數據的價值與案例 |
    | 10:00–10:50 | 數據分析流程 — Data Pipeline、CRISP-DM、資料蒐集與清洗 |
    | 11:00–11:50 | 資料類型與結構 — 結構化/非結構化、CSV/JSON、Big Data概念 |
    | 13:00–13:50 | AI 內容生成（AIGC）— GPT運作、Prompt Engineering、生成圖片/影片 |
    | 14:00–14:50 | 機器學習概念 — 監督/非監督式學習、模型訓練、Explainable AI |
    | 15:00–15:50 | 職場AI 應用 — 電商/金融/製造/3D列印、職涯路徑規劃 |
    """)

    cols = st.columns(3)
    with cols[0]:
        st.metric("🌍 全球AI市場", "$5,000億", "2026預估")
    with cols[1]:
        st.metric("🇹🇼 台灣AI商機", "NT$16兆", "年規模")
    with cols[2]:
        st.metric("⚡ 效率提升", "300%+", "AI輔助")

# ════════ M1 ════════
elif selected == "m1":
    st.markdown('<div class="section-title">🧠 Module 1: AI 與數據世界</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 什麼是 AI？
    - **AI** = 讓電腦模擬人類智慧行為的技術
    - 1956年達特茅斯會議首次提出
    - 核心目標：讓機器能夠學習、推理、理解語言、辨識圖像
    
    ### AI → ML → DL 三層關係
    ```
    ┌────────────────────────────────┐
    │  人工智慧 (AI)                  │
    │  ┌──────────────────────────┐  │
    │  │  機器學習 (ML)            │  │
    │  │  ┌────────────────────┐  │  │
    │  │  │  深度學習 (DL)      │  │  │
    │  │  │  神經網路           │  │  │
    │  │  └────────────────────┘  │  │
    │  └──────────────────────────┘  │
    └────────────────────────────────┘
    ```
    
    ### 三大核心應用領域
    | 領域 | 案例 |
    |:----|:----|
    | 🏥 醫療健康 | AI聽診器、醫學影像辨識、藥物研發加速 |
    | 💰 金融科技 | 詐騙偵測、量化交易、智能客服 |
    | 🏭 智慧製造 | 產品瑕疵檢測、設備維護預測、3D列印品質監控 |
    
    ### ChatGPT 技術原理
    - **Transformer 架構**（2017年Google提出）
    - 訓練資料：數千億個網路文字
    - **RLHF**（人類反饋強化學習）
    - GPT-4 參數量約 **1 兆**
    """)

# ════════ M2 ════════
elif selected == "m2":
    st.markdown('<div class="section-title">📊 Module 2: 數據分析流程</div>', unsafe_allow_html=True)
    st.markdown("""
    ### CRISP-DM 標準流程（業界最常使用）
    """)
    steps = ["業務理解", "資料理解", "資料準備", "建模", "評估", "部署"]
    cols = st.columns(6)
    for i, (col, step) in enumerate(zip(cols, steps)):
        with col:
            st.markdown(f'<div class="flow-step"><span class="num">{i+1}</span>{step}</div>', unsafe_allow_html=True)

    st.markdown("""
    ### Data Pipeline（數據管線）
    ```
    資料來源 → 擷取(Extract) → 轉換(Transform) → 載入(Load) → 分析 → 可視化
      │           │                │               │         │        │
      ├ ERP/CRM   ├ API            ├ 清洗          ├ DB      ├ SQL    ├ 儀表板
      ├ 網站日志  ├ Web Crawler    ├ 正規化        ├ Data    ├ Python ├ 報表
      ├ IoT傳感器 ├ Excel匯入      ├ 特徵工程      ├ Lake    ├ ML     ├ BI工具
      └ 社群媒體  └ CSV/JSON       └ 合併          └ DW      └ AI     └ 圖表
    ```
    
    ### 數據驅動決策
    - 相比直覺決策，數據驅動決策成功率高出 **5 倍**
    - 獲利率提升 **23%**
    
    ### 台灣產業數據應用
    - **台積電**：AI晶片良率優化
    - **鴻海**：智慧工廠
    - **台灣大**：健康AI
    """)

# ════════ M3 ════════
elif selected == "m3":
    st.markdown('<div class="section-title">📂 Module 3: 資料類型與結構</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 資料分類
    | 類型 | 說明 | 範例 |
    |:----|:----|:----|
    | **結構化** | 表格形式，行列分明 | Excel、SQL資料表、CSV |
    | **半結構化** | 有結構但可變 | JSON、XML、HTML |
    | **非結構化** | 無固定格式 | 圖片、影片、PDF、語音 |
    
    ### CSV vs JSON
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**CSV（表格形式）**")
        st.code("姓名,年齡,城市\n張小明,28,台北\n李小花,35,台中", language="text")
    with col2:
        st.markdown("**JSON（樹狀結構）**")
        st.code('{"users":[\n  {"name":"張小明","age":28,"city":"台北"},\n  {"name":"李小花","age":35,"city":"台中"}\n]}', language="json")

    st.markdown("### Big Data 的 5V 特性")
    st.markdown("- **Volume**（大量）：從 TB 到 ZB")
    st.markdown("- **Velocity**（快速）：即時串流數據")
    st.markdown("- **Variety**（多樣）：結構化＋非結構化")
    st.markdown("- **Veracity**（真實性）：數據品質")
    st.markdown("- **Value**（價值）：從數據中提煉商業價值")

# ════════ M4 ════════
elif selected == "m4":
    st.markdown('<div class="section-title">🤖 Module 4: AI 內容生成（AIGC）</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 生成式 AI 的三大能力
    | 類型 | 工具 | 應用 |
    |:----|:----|:----|
    | 📝 文字生成 | ChatGPT, Claude | 文案、程式碼、翻譯 |
    | 🖼️ 圖片生成 | Midjourney, DALL-E | 產品圖、設計稿 |
    | 🎬 影片生成 | Sora, Runway | 行銷短片 |
    
    ### GPT 運作原理
    - **Transformer** + **Attention機制** + **RLHF**
    - 預測下一個詞：根據前文機率分佈選擇最可能的詞
    - 開源替代：LLaMA（Meta）、TAIDE（台灣版）
    
    ### Prompt Engineering 黃金公式
    **角色 + 任務 + 細節 + 格式**
    """)
    st.info("❌ 差：「幫我寫一篇產品介紹。」")
    st.success('✅ 好：「你是3D列印產品行銷專家，幫我寫一篇貓咪公仔的蝦皮商品頁面，150字，活潑台灣口語，含3個emoji，結尾要有促購句。」')

    st.markdown("### AI 倫理與風險")
    st.warning("⚠️ 幻覺（Hallucination）— AI可能編造事實，重要資訊需人工驗證")

# ════════ M5 ════════
elif selected == "m5":
    st.markdown('<div class="section-title">⚙️ Module 5: 機器學習概念</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 三種學習方式
    | 類型 | 說明 | 案例 |
    |:----|:----|:----|
    | 🔵 **監督式學習** | 有標籤資料訓練 | 圖片分類、房價預測 |
    | 🟢 **非監督式學習** | 無標籤，自己找規律 | 客戶分群、異常檢測 |
    | 🟡 **強化學習** | 獎勵機制學習 | AlphaGo、自駕車 |
    
    ### ML 模型訓練流程
    1. 收集資料
    2. 資料清洗
    3. 特徵工程
    4. 選擇演算法
    5. 訓練模型
    6. 評估（準確率/精確率）
    7. 部署
    8. 監控與迭代
    
    ### Explainable AI（可解釋AI）
    - AI 黑盒問題
    - XAI 幫助理解「為什麼模型做出這個決定」
    - 台灣法規要求：AI 決策需可解釋（如信用評分）
    """)

# ════════ M6 ════════
elif selected == "m6":
    st.markdown('<div class="section-title">💼 Module 6: 職場AI 應用</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 各產業 AI 應用
    | 產業 | 應用 |
    |:----|:----|
    | 🛒 電商 | 推薦系統、智能客服、庫存預測（蝦皮、momo） |
    | 🏦 金融 | 詐騙偵測、信用評分、量化交易 |
    | 🏭 製造 | 瑕疵檢測、預測維護、3D列印監控 |
    | 🏛️ 政府 | 智慧城市、交通預測、防災系統 |
    | 📚 教育 | 適性學習、AI助教、自動評分 |
    
    ### AI 職涯路徑
    - **初階**：AI工具使用者（Prompt Engineer）
    - **中階**：AI應用開發者（整合API、分析資料）
    - **高階**：AI模型開發者（訓練微調模型）
    
    ### 台灣 AI 人才市場
    - 職缺年增率：**35%+**
    - 平均薪資：比同級非AI職缺高 **30-50%**
    """)

# ════════ 下午術科 ════════
elif selected == "afternoon":
    st.markdown('<div class="section-title">🛠️ 下午術科實作課程</div>', unsafe_allow_html=True)
    st.markdown("""
    **時間：13:00 – 18:00（5小時）**
    
    ### 下午實作大綱
    | 實作 | 主題 | 內容 |
    |:---:|:----|:----|
    | 實作 1 | 🐍 Python + Google Colab | 免安裝雲端環境、第一支Python程式、EDA |
    | 實作 2 | 📋 Google Sheets 數據分析 | 表單設計、資料清理、自動化 |
    | 實作 3 | 🔌 AI API 串接 | DeepSeek API、情感分析 |
    | 實作 4 | 🤖 ML 實作 | scikit-learn、分類/迴歸模型 |
    | 實作 5 | 📊 Google 工具串流 | GSC + GA4 + Trends + Sheets 整合 |
    
    ### Google 串流數據分析流程
    ```
    Google Search Console → GA4 → Google Trends → Google Sheets → Colab分析
         (搜尋流量)      (網站行為)    (趨勢)       (數據彙整)     (Python處理)
    ```
    """)

# ════════ GSC ════════
elif selected == "gsc":
    st.markdown('<div class="section-title">🔍 Google Search Console</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 什麼是 GSC？
    Google 提供的免費工具，讓你了解網站在 Google 搜尋中的表現。
    
    ### 主要功能
    - 查看帶來流量的關鍵字
    - 了解網站的點擊率（CTR）
    - 發現網站的索引問題
    - 提交 Sitemap 加速收錄
    
    ### 實作練習：找出熱門搜尋問題
    1. 進入 **Google Search Console**
    2. 點選 **成效 → 查詢**
    3. 觀察哪些關鍵字帶來最多流量
    4. 用這些資料決定下一篇文章/產品的主題
    
    ### 常用指標
    | 指標 | 說明 |
    |:----|:----|
    | 曝光次數 | 你的內容出現在搜尋結果的次數 |
    | 點擊次數 | 使用者實際點擊的次數 |
    | CTR（點擊率） | 點擊 ÷ 曝光 |
    | 平均排名 | 你的內容平均出現在第幾位 |
    """)

# ════════ GA4 ════════
elif selected == "ga4":
    st.markdown('<div class="section-title">📈 Google Analytics 4</div>', unsafe_allow_html=True)
    st.markdown("""
    ### GA4 的事件思維
    不同於舊版 UA（以頁面瀏覽為主），GA4 以**事件**為核心：
    
    ```
    使用者登入 → 事件: login
    使用者搜尋 → 事件: search
    加入購物車 → 事件: add_to_cart
    完成購買 → 事件: purchase
    ```
    
    ### 常用指標對照
    | GA4 指標 | 說明 |
    |:---------|:----|
    | Sessions | 工作階段數 |
    | Users | 不重複使用者 |
    | Engagement Rate | 參與率 |
    | Conversions | 轉換次數 |
    
    ### 實作練習
    1. 使用 **GA4 Demo Account**（google Analytics 提供的示範帳號）
    2. 觀察流量來源、使用者行為
    3. 整理成每週觀察報表
    """)

# ════════ Trends ════════
elif selected == "trends":
    st.markdown('<div class="section-title">📉 Google Trends</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 什麼是 Google Trends？
    查看搜尋趨勢的免費工具，幫助你了解什麼主題正在熱門。
    
    ### 三大用途
    1. **選題分析**：知道現在大家搜尋什麼
    2. **季節性預測**：了解哪些主題在特定時間會爆紅
    3. **競爭分析**：比較不同關鍵字的搜尋量
    
    ### 實作練習：找可教可做的主題
    1. 到 **trends.google.com**
    2. 輸入你有興趣的主題關鍵字
    3. 觀察趨勢曲線
    4. 找出上升中的相關主題
    
    ### 實例
    ```
    搜尋: "3D列印公仔"
    → 趨勢曲線過去12個月持續上升
    → 相關主題: "全彩列印" "+350%" (快速上升)
    → 地區: 台灣北部為主
    ```
    """)

# ════════ Sheets ════════
elif selected == "sheets":
    st.markdown('<div class="section-title">📋 Google Sheets 數據分析</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 為什麼用 Sheets 做數據分析？
    - ✅ 免費、雲端、協作
    - ✅ 串接 Google Forms 自動收集資料
    - ✅ Google Apps Script 自動化
    - ✅ 可連接 GSC / GA4 資料
    
    ### 週報模板結構
    ```
    ┌──────────────────────────────────────────────┐
    │  📊 第X週 數據週報                           │
    ├──────┬───────┬──────┬──────┬──────┬────────┤
    │ 日期 │ 曝光   │ 點擊 │ CTR  │ 排名 │ 備註   │
    ├──────┼───────┼──────┼──────┼──────┼────────┤
    │ 4/21 │ 1,200 │ 85   │ 7.1% │ 4.2  │        │
    │ 4/22 │ 980   │ 72   │ 7.3% │ 4.5  │        │
    └──────┴───────┴──────┴──────┴──────┴────────┘
    ```
    
    ### 實作練習
    1. 用 Google Forms 設計數據收集表單
    2. 自動彙整到 Sheets
    3. 用 Sheets 函式做基本分析
    4. 製作每週自動報表
    """)

# ════════ Colab/Python ════════
elif selected == "colab":
    st.markdown('<div class="section-title">🐍 Python / Google Colab 實作</div>', unsafe_allow_html=True)
    st.markdown("""
    ### Google Colab — 免安裝雲端 Python 環境
    - 瀏覽器直接寫 Python
    - 免費 GPU 可用
    - 可讀取 Google Drive
    
    ### 第一支 Python 程式
    ```python
    print("Hello, AI 數據分析!")
    ```
    
    ### pandas — 資料分析的瑞士刀
    """)
    st.code("""import pandas as pd

# 建立 DataFrame（類似 Excel 工作表）
data = {
    "姓名": ["張小明", "李小花", "王大偉", "陳美玲"],
    "年齡": [28, 35, 42, 29],
    "城市": ["台北", "台中", "高雄", "台北"],
    "月薪": [45000, 62000, 55000, 48000]
}
df = pd.DataFrame(data)

# 基本分析
print(df.describe())        # 統計摘要
print(df.groupby('城市').mean())  # 分組平均""", language="python")

    st.markdown("### EDA（探索性資料分析）步驟")
    st.markdown("1. 載入資料 → `pd.read_csv()`")
    st.markdown("2. 查看前5筆 → `df.head()`")
    st.markdown("3. 基本統計 → `df.describe()`")
    st.markdown("4. 檢查缺失值 → `df.isnull().sum()`")
    st.markdown("5. 視覺化 → `df.plot()`")

# ════════ ML實作 ════════
elif selected == "ml_lab":
    st.markdown('<div class="section-title">🧪 機器學習實作</div>', unsafe_allow_html=True)
    st.markdown("""
    ### scikit-learn — 5 分鐘訓練第一個 AI 模型
    
    #### 分類模型：鳶尾花品種辨識
    """)
    st.code("""from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. 載入資料
iris = load_iris()
X, y = iris.data, iris.target

# 2. 分割訓練/測試
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. 訓練模型
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 4. 預測與評估
y_pred = model.predict(X_test)
print(f"準確率: {accuracy_score(y_test, y_pred):.2%}")""", language="python")

    st.markdown("#### 迴歸模型：預測連續數值")
    st.code("""from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# 簡單線性迴歸
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([150, 200, 250, 300, 350])

model = LinearRegression()
model.fit(X, y)

print(f"斜率: {model.coef_[0]:.2f}")
print(f"截距: {model.intercept_:.2f}")
print(f"預測 X=6: {model.predict([[6]])[0]:.2f}")""", language="python")

# ════════ API ════════
elif selected == "api":
    st.markdown('<div class="section-title">🔌 AI API 串接實作</div>', unsafe_allow_html=True)
    st.markdown("""
    ### 什麼是 API？
    API = Application Programming Interface（應用程式介面）
    讓你的程式可以跟 AI 模型溝通。
    
    ### 統一三步驟（所有模型相同）
    1. **設定 API Key**（授權）
    2. **建立 Prompt**（下指令）
    3. **取得回應**（獲得結果）
    
    ### DeepSeek API 串接
    """)
    st.code("""import requests

# 設定
API_KEY = "你的DeepSeek API Key"
url = "https://api.deepseek.com/v1/chat/completions"

# Prompt
payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "你是專業數據分析師"},
        {"role": "user", "content": "請分析這組銷售數據的趨勢"}
    ]
}

# 呼叫 API
headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.post(url, json=payload, headers=headers)
print(response.json()["choices"][0]["message"]["content"])""", language="python")

    st.markdown("### 實作：AI 情感分析（批量處理客戶評論）")
    st.code("""system_prompt = \"\"\"你是「彩印工坊」的AI客服助手。
請分析以下客戶評論的情緒：
- 正面 😊 / 中性 😐 / 負面 😠
- 一句話說明原因
- 如果是負面，建議處理方式
\"\"\" """, language="python")

# ── Footer ──
st.markdown("---")
st.markdown("<div style='text-align:center; color:#64748b; font-size:0.8rem;'>📊 AI數位內容與數據分析 ｜ 教學網站版 ｜ 講師：嚴稑榛 ｜ 115.04.27</div>", unsafe_allow_html=True)
