#!/usr/bin/env python3
"""
AI x 3D列印產品一條龍設計 - 教學網站
Flask Web App
"""

from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# ── HTML Template ──────────────────────────────────────────────
INDEX_HTML = r"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI × 3D列印 產品一條龍設計</title>
    <style>
        /* ── Reset & Base ── */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            line-height: 1.7;
        }
        a { color: #60a5fa; text-decoration: none; }
        a:hover { color: #93c5fd; }

        /* ── Navbar ── */
        .navbar {
            position: sticky; top: 0; z-index: 100;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid #1e293b;
            padding: 0 2rem;
            display: flex; align-items: center;
            height: 60px; gap: 1.5rem;
            overflow-x: auto;
        }
        .navbar .logo {
            font-weight: 800; font-size: 1.1rem;
            color: #fbbf24; white-space: nowrap;
            flex-shrink: 0;
        }
        .navbar a {
            color: #94a3b8; font-size: 0.85rem;
            white-space: nowrap; padding: 0.3rem 0;
            border-bottom: 2px solid transparent;
            transition: 0.2s;
        }
        .navbar a:hover, .navbar a.active {
            color: #e2e8f0;
            border-bottom-color: #fbbf24;
        }

        /* ── Hero ── */
        .hero {
            text-align: center; padding: 4rem 2rem 3rem;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            border-bottom: 1px solid #1e293b;
        }
        .hero h1 {
            font-size: 2.5rem; font-weight: 800;
            background: linear-gradient(135deg, #fbbf24, #f59e0b);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .hero .subtitle { color: #94a3b8; font-size: 1.1rem; }
        .hero .meta {
            margin-top: 1rem; font-size: 0.85rem; color: #64748b;
        }

        /* ── Section Cards ── */
        .container { max-width: 1100px; margin: 0 auto; padding: 2rem; }

        .section-card {
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 16px;
            padding: 2rem; margin-bottom: 2rem;
            transition: 0.2s;
        }
        .section-card:hover {
            border-color: #475569;
            box-shadow: 0 4px 24px rgba(0,0,0,0.3);
        }
        .section-card h2 {
            font-size: 1.5rem; font-weight: 700;
            margin-bottom: 1.5rem; padding-bottom: 0.75rem;
            border-bottom: 2px solid #334155;
            display: flex; align-items: center; gap: 0.5rem;
        }
        .section-card h2 .emoji { font-size: 1.6rem; }
        .section-card h3 {
            font-size: 1.1rem; font-weight: 600;
            color: #fbbf24; margin: 1.2rem 0 0.5rem;
        }
        .section-card h4 {
            font-size: 0.95rem; font-weight: 600;
            color: #93c5fd; margin: 1rem 0 0.3rem;
        }
        .section-card p { margin-bottom: 0.75rem; color: #cbd5e1; }
        .section-card ul, .section-card ol {
            margin: 0.5rem 0 1rem 1.5rem;
            color: #cbd5e1;
        }
        .section-card li { margin-bottom: 0.3rem; }

        /* ── Table ── */
        .table-wrap { overflow-x: auto; margin: 1rem 0; }
        table {
            width: 100%; border-collapse: collapse;
            font-size: 0.85rem;
        }
        th {
            background: #334155; color: #fbbf24;
            padding: 0.6rem 0.8rem; text-align: left;
            font-weight: 600;
        }
        td {
            padding: 0.5rem 0.8rem;
            border-bottom: 1px solid #334155;
        }
        tr:hover td { background: #273548; }

        /* ── Code / Prompt Box ── */
        .code-block {
            background: #0f172a;
            border: 1px solid #334155; border-radius: 10px;
            padding: 1rem 1.2rem;
            font-family: 'Cascadia Code', 'Fira Code', monospace;
            font-size: 0.82rem;
            overflow-x: auto; margin: 0.8rem 0;
            color: #a5b4fc; white-space: pre-wrap;
        }
        .code-block .kw { color: #f472b6; }
        .code-block .str { color: #34d399; }
        .code-block .cmt { color: #64748b; font-style: italic; }

        .prompt-box {
            background: linear-gradient(135deg, #1e1b4b, #312e81);
            border: 1px solid #4338ca; border-radius: 10px;
            padding: 1rem 1.2rem;
            font-family: 'Cascadia Code', 'Fira Code', monospace;
            font-size: 0.82rem;
            margin: 0.8rem 0; white-space: pre-wrap;
            color: #c4b5fd;
        }

        /* ── Flow Steps ── */
        .flow-steps {
            display: flex; flex-wrap: wrap; gap: 0.5rem;
            margin: 1rem 0;
        }
        .flow-step {
            background: #334155; padding: 0.5rem 1rem;
            border-radius: 20px; font-size: 0.82rem;
            display: flex; align-items: center; gap: 0.4rem;
        }
        .flow-step .num {
            background: #fbbf24; color: #0f172a;
            width: 22px; height: 22px; border-radius: 50%;
            display: inline-flex; align-items: center; justify-content: center;
            font-weight: 700; font-size: 0.75rem;
        }

        /* ── Tool Grid ── */
        .tool-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 1rem; margin: 1rem 0;
        }
        .tool-card {
            background: #0f172a; border: 1px solid #334155;
            border-radius: 12px; padding: 1.2rem;
        }
        .tool-card .name { font-weight: 700; color: #fbbf24; }
        .tool-card .desc { font-size: 0.82rem; color: #94a3b8; margin-top: 0.3rem; }
        .tool-card .price {
            font-size: 0.75rem; color: #34d399;
            margin-top: 0.3rem;
        }

        /* ── Highlight Box ── */
        .highlight {
            background: #1e293b; border-left: 4px solid #fbbf24;
            padding: 1rem 1.2rem; border-radius: 0 10px 10px 0;
            margin: 1rem 0;
        }
        .highlight.info { border-left-color: #60a5fa; }
        .highlight.warn { border-left-color: #f97316; }
        .highlight.success { border-left-color: #34d399; }

        /* ── Footer ── */
        .footer {
            text-align: center; padding: 2rem;
            color: #64748b; font-size: 0.8rem;
            border-top: 1px solid #1e293b;
            margin-top: 2rem;
        }

        /* ── Responsive ── */
        @media (max-width: 768px) {
            .hero h1 { font-size: 1.8rem; }
            .navbar { padding: 0 1rem; gap: 1rem; }
            .section-card { padding: 1.2rem; }
        }
    </style>
</head>
<body>

<!-- ==================== Navbar ==================== -->
<nav class="navbar">
    <span class="logo">🧊 3D列印</span>
    <a href="#overview">課程概述</a>
    <a href="#tools">工具一覽</a>
    <a href="#flow">一條龍流程</a>
    <a href="#prompt">Prompt 技巧</a>
    <a href="#meshy">Meshy 操作</a>
    <a href="#copywriting">AI 文案</a>
    <a href="#slide">簡報製作</a>
    <a href="#shop">電商網站</a>
    <a href="#pricing">定價策略</a>
    <a href="#checklist">檢查清單</a>
</nav>

<!-- ==================== Hero ==================== -->
<div class="hero">
    <h1>AI × 全彩 3D 列印</h1>
    <div class="subtitle">產品一條龍設計｜從零到電商上架</div>
    <div class="meta">
        講師：嚴稑榛 ｜ 勞動部勞動力發展署桃竹苗分署 ｜ 2026.05.11
    </div>
</div>

<div class="container">

<!-- ============================================== -->
<!-- ============ 1. 課程概述 ====================== -->
<!-- ============================================== -->
<div class="section-card" id="overview">
    <h2><span class="emoji">🎯</span> 課程概述</h2>
    <p><strong>目標：</strong>用 AI 工具，<strong>1 小時內</strong>完成產品 Idea → 文案 → 3D 模型 → 電商上架！</p>

    <h3>市場背景</h3>
    <ul>
        <li>🇹🇼 台灣 3D 列印年市場規模 <strong>NT$150 億+</strong></li>
        <li>⚡ AI 工具輔助設計效率提升 <strong>300%</strong></li>
        <li>🏆 三大爆發領域：客製化公仔 / 工業原型 / 個人化禮品</li>
    </ul>

    <h3>學員成功案例</h3>
    <ul>
        <li><strong>陳先生（52歲）</strong>－前工廠作業員，蝦皮賣公仔月入 NT$18,000</li>
        <li><strong>林女士（45歲）</strong>－家庭主婦，Etsy 國際平台月收 USD 400-600</li>
        <li><strong>王先生（48歲）</strong>－前服務業，廟宇神明公仔系列接到企業訂單</li>
    </ul>
</div>

<!-- ============================================== -->
<!-- ============ 2. 工具一覽 ====================== -->
<!-- ============================================== -->
<div class="section-card" id="tools">
    <h2><span class="emoji">🔧</span> AI 工具一覽</h2>

    <h3>語言 AI</h3>
    <div class="tool-grid">
        <div class="tool-card">
            <div class="name">ChatGPT</div>
            <div class="desc">文案、問答、Prompt 測試</div>
            <div class="price">✅ 免費（GPT-4o）</div>
        </div>
        <div class="tool-card">
            <div class="name">Claude</div>
            <div class="desc">長文章、邏輯分析</div>
            <div class="price">✅ 免費（Sonnet）</div>
        </div>
        <div class="tool-card">
            <div class="name">Gemini</div>
            <div class="desc">Google 整合、即時搜尋</div>
            <div class="price">✅ 免費</div>
        </div>
    </div>

    <h3>3D 生成 AI</h3>
    <div class="table-wrap">
    <table>
        <tr><th>工具</th><th>免費額度</th><th>速度</th><th>列印品質</th><th>難度</th><th>推薦場景</th></tr>
        <tr><td><strong>Meshy.ai</strong> ⭐</td><td>200 點/月</td><td>30-60 秒</td><td>97%</td><td>中等</td><td>公仔/人偶列印首選</td></tr>
        <tr><td>Tripo3D</td><td>充足</td><td>2-10 秒</td><td>90%</td><td>最易</td><td>快速原型／初學者</td></tr>
        <tr><td>Rodin AI</td><td>預覽免費</td><td>2-5 分</td><td>最高</td><td>中等</td><td>高品質／商業用途</td></tr>
        <tr><td>Hunyuan3D</td><td>完全免費</td><td>60-100 秒</td><td>高</td><td>需 GPU</td><td>開源自架／研究用</td></tr>
    </table>
    </div>

    <h3>簡報 & 設計 AI</h3>
    <div class="tool-grid">
        <div class="tool-card">
            <div class="name">Gamma.app ⭐</div>
            <div class="desc">文案一鍵生成精美簡報</div>
            <div class="price">✅ 免費 400 點</div>
        </div>
        <div class="tool-card">
            <div class="name">Canva AI</div>
            <div class="desc">設計、簡報、圖片生成</div>
            <div class="price">✅ 免費版</div>
        </div>
        <div class="tool-card">
            <div class="name">Bing Image Creator</div>
            <div class="desc">中文描述即可生成圖片</div>
            <div class="price">✅ 完全免費</div>
        </div>
    </div>

    <h3>電商平台</h3>
    <ul>
        <li><strong>蝦皮</strong> － 台灣最大，流量入門首選</li>
        <li><strong>Etsy</strong> － 全球英語市場，高單價</li>
        <li><strong>Wix ADI</strong> － AI 建站，適合自有品牌</li>
        <li><strong>SHOPLINE</strong> － 台灣本土，支援 LINE Pay</li>
    </ul>
</div>

<!-- ============================================== -->
<!-- ============ 3. 一條龍流程 ==================== -->
<!-- ============================================== -->
<div class="section-card" id="flow">
    <h2><span class="emoji">🔄</span> 產品一條龍流程</h2>

    <div class="flow-steps">
        <span class="flow-step"><span class="num">1</span> 構思產品</span>
        <span class="flow-step"><span class="num">2</span> 設計 Prompt</span>
        <span class="flow-step"><span class="num">3</span> 生成 3D 模型</span>
        <span class="flow-step"><span class="num">4</span> 模型優化</span>
        <span class="flow-step"><span class="num">5</span> 全彩列印</span>
        <span class="flow-step"><span class="num">6</span> 清洗後處理</span>
        <span class="flow-step"><span class="num">7</span> 文案撰寫</span>
        <span class="flow-step"><span class="num">8</span> 電商上架</span>
    </div>

    <div class="highlight">
        <strong>💡 一句話總結：</strong>
        想法 → ChatGPT → Meshy.ai → Bambu Studio → 蝦皮上架！
    </div>
</div>

<!-- ============================================== -->
<!-- ============ 4. Prompt 技巧 =================== -->
<!-- ============================================== -->
<div class="section-card" id="prompt">
    <h2><span class="emoji">💬</span> Prompt 工程入門</h2>

    <h3>黃金公式</h3>
    <div class="code-block">
<span class="kw">角色</span> (你是…) + <span class="kw">任務</span> (幫我寫…) + <span class="kw">細節</span> (產品特色…) + <span class="kw">格式</span> (用條列式…)
    </div>

    <h3>差 vs 好的 Prompt</h3>
    <div class="highlight warn">
        ❌ 差：「幫我寫3D列印產品的文案。」
    </div>
    <div class="highlight success">
        ✅ 好：「你是專業3D列印電商文案師，幫我寫一款『可愛貓咪擺飾公仔』的蝦皮商品頁面文案，包含吸睛標題、3點特色、適合送禮說明，用活潑的台灣口語，150字內。」
    </div>

    <h3>3D 模型 Prompt 模板</h3>
    <div class="prompt-box">
"A cute sitting cat figurine, chubby proportions, wearing a tiny graduation cap, full color pastel tones, chibi style, 3D printable figurine, smooth surface, watertight mesh"
    </div>

    <div class="highlight">
        <strong>📌 3D 模型關鍵字：</strong> 一定加 <code>chibi style</code>（可愛比例）、<code>3D printable</code>、<code>watertight mesh</code>（確保列印）
    </div>
</div>

<!-- ============================================== -->
<!-- ============ 5. Meshy 操作 ==================== -->
<!-- ============================================== -->
<div class="section-card" id="meshy">
    <h2><span class="emoji">🧊</span> Meshy.ai 操作步驟</h2>
    <p>全球最受 3D 列印社群歡迎的 AI 模型生成工具。公仔列印相容率 <strong>97%</strong>！</p>

    <h3>6 步驟快速上手</h3>
    <ol>
        <li><strong>前往 meshy.ai</strong> － 用 Google 帳號一鍵登入，新用戶 200 免費點數</li>
        <li><strong>點選「Text to 3D」</strong> （或 Image to 3D 使用參考圖）</li>
        <li><strong>撰寫英文 Prompt</strong> － 效果比中文好</li>
        <li><strong>設定參數</strong> － 選 Sculpture / Cartoon 風格，按 Generate（消耗 10-20 點）</li>
        <li><strong>選最佳結果</strong> － 從 4 個預覽中選最喜歡的，按 Refine 精細化</li>
        <li><strong>匯出 3MF</strong> － 保留顏色資訊，準備切片列印！</li>
    </ol>

    <h3>台灣特色 Prompt 範本</h3>
    <div class="prompt-box">
<span class="cmt"># 台灣夜市小吃公仔</span>
"A cute chibi taiwanese street vendor, selling stinky tofu, wearing apron and bamboo hat, smiling, full color, 3D printable, watertight mesh"

<span class="cmt"># 貓咪擺飾（最熱銷！）</span>
"A cute sitting cat figurine, chubby proportions, wearing a tiny graduation cap, full color pastel tones, chibi style, 3D printable figurine, smooth surface"
    </div>
</div>

<!-- ============================================== -->
<!-- ============ 6. AI 文案 ======================= -->
<!-- ============================================== -->
<div class="section-card" id="copywriting">
    <h2><span class="emoji">✍️</span> AI 產品文案設計</h2>

    <h3>AIDA 黃金框架</h3>
    <div class="table-wrap">
    <table>
        <tr><th>步驟</th><th>中文</th><th>範例</th></tr>
        <tr><td><strong>A</strong>ttention</td><td>注意力</td><td>「全台唯一！3D列印客製化西裝男孩公仔」</td></tr>
        <tr><td><strong>I</strong>nterest</td><td>產生興趣</td><td>「百萬色彩全彩技術，細節栩栩如生」</td></tr>
        <tr><td><strong>D</strong>esire</td><td>激發渴望</td><td>「完美的桌上擺飾，還可以客製你的臉！」</td></tr>
        <tr><td><strong>A</strong>ction</td><td>行動呼籲</td><td>「限量20件，現在下單享9折！立即選購」</td></tr>
    </table>
    </div>

    <h3>萬用文案 Prompt</h3>
    <div class="prompt-box">
你是專業3D列印電商文案師，幫我用AIDA架構為以下商品寫蝦皮頁面描述：
商品：[產品名稱]
材質：全彩3D列印PLA材質  尺寸：約[X]公分
特色：[2-3個特色]
請包含：吸睛標題（含「客製化」「3D列印」關鍵字）、三點特色、使用情境、購買呼籲，總計200字內。
    </div>

    <h3>多版本策略</h3>
    <p>同一個產品，請 AI 寫不同風格 → 選最適合你的！</p>
    <ul>
        <li><strong>活潑搞笑版</strong> － 目標 25-35 歲上班族</li>
        <li><strong>正式禮品版</strong> － 目標 35-55 歲商務人士</li>
        <li><strong>節日限定版</strong> － 目標 20-40 歲送禮需求</li>
    </ul>
</div>

<!-- ============================================== -->
<!-- ============ 7. 簡報製作 ====================== -->
<!-- ============================================== -->
<div class="section-card" id="slide">
    <h2><span class="emoji">📊</span> 商業簡報製作</h2>

    <h3>Gamma.app 操作</h3>
    <ol>
        <li>前往 <strong>gamma.app</strong> 免費註冊</li>
        <li>點「New with AI」</li>
        <li>輸入產品文案或主題大綱</li>
        <li>選擇視覺風格和配色</li>
        <li>一鍵生成並編輯細節</li>
    </ol>

    <h3>5 頁完美簡報結構</h3>
    <div class="table-wrap">
    <table>
        <tr><th>頁數</th><th>內容</th></tr>
        <tr><td>第 1 頁</td><td>封面頁 — 產品名稱 + 一句話標語 + 精美圖片</td></tr>
        <tr><td>第 2 頁</td><td>問題頁 — 買家面臨的問題是什麼？引起共鳴</td></tr>
        <tr><td>第 3 頁</td><td>解決方案 — 你的產品如何完美解決這個問題</td></tr>
        <tr><td>第 4 頁</td><td>產品展示 — 照片 + 規格 + 特色 3 項</td></tr>
        <tr><td>第 5 頁</td><td>購買頁 — 價格 + 優惠 + 聯絡方式</td></tr>
    </table>
    </div>

    <h3>美感原則</h3>
    <ul>
        <li><strong>60-30-10 配色法</strong> — 主色60% + 輔色30% + 點綴色10%</li>
        <li><strong>最多 2 種字體</strong> — 粗體無襯線 + 細體無襯線</li>
        <li><strong>留白</strong> — 每頁 1-2 個重點 + 一張圖片就夠了</li>
    </ul>
</div>

<!-- ============================================== -->
<!-- ============ 8. 電商網站 ====================== -->
<!-- ============================================== -->
<div class="section-card" id="shop">
    <h2><span class="emoji">🛒</span> 電商網站建置</h2>

    <h3>AI 建站工具比較</h3>
    <div class="table-wrap">
    <table>
        <tr><th>工具</th><th>最適合</th><th>免費方案</th><th>付費</th></tr>
        <tr><td><strong>Wix ADI</strong></td><td>完整電商功能</td><td>有廣告</td><td>NT$200-600/月</td></tr>
        <tr><td><strong>Durable</strong></td><td>30 秒超快速建站</td><td>有限次數</td><td>$12/月</td></tr>
        <tr><td><strong>Hostinger AI</strong></td><td>長期划算</td><td>30 天試用</td><td>NT$80/月起</td></tr>
    </table>
    </div>

    <h3>台灣金流方案</h3>
    <ul>
        <li><strong>綠界科技 ECPay</strong> － 信用卡 / ATM / 超商代碼，手續費 2-3%</li>
        <li><strong>藍新金流</strong> － 信用卡 / 行動支付 / WebATM，手續費 2-3%</li>
        <li><strong>LINE Pay</strong> － 台灣超流行，手續費 2.2%</li>
    </ul>

    <div class="highlight info">
        💡 新手建議先用 <strong>綠界科技</strong>，Wix 和 Hostinger 都支援！
    </div>
</div>

<!-- ============================================== -->
<!-- ============ 9. 定價策略 ====================== -->
<!-- ============================================== -->
<div class="section-card" id="pricing">
    <h2><span class="emoji">💰</span> 定價策略（10cm 全彩公仔）</h2>

    <h3>成本結構</h3>
    <ul>
        <li>材料費（PLA+）：NT$35-80</li>
        <li>電費（列印 3 小時）：NT$5-10</li>
        <li>AI 工具費用分攤：NT$5-15</li>
        <li>後處理工時：NT$30-50</li>
        <li>包裝材料：NT$15-25</li>
        <li><strong>總成本約 NT$90-180 / 件</strong></li>
    </ul>

    <h3>建議售價</h3>
    <div class="table-wrap">
    <table>
        <tr><th>類型</th><th>售價</th><th>毛利率</th></tr>
        <tr><td>標準款（固定設計）</td><td>NT$380-580</td><td>60-70%</td></tr>
        <tr><td>客製款（半客製臉型）</td><td>NT$680-980</td><td>70-75%</td></tr>
        <tr><td>全客製款（完全訂製）</td><td>NT$1,200-2,000</td><td>75-85%</td></tr>
    </table>
    </div>
</div>

<!-- ============================================== -->
<!-- ============ 10. 檢查清單 ===================== -->
<!-- ============================================== -->
<div class="section-card" id="checklist">
    <h2><span class="emoji">✅</span> 列印前檢查清單</h2>

    <h3>Prompt 設計</h3>
    <ul>
        <li>☐ 角色描述清楚（種族 / 服裝 / 姿態）</li>
        <li>☐ 加入風格關鍵字（chibi / sculpture）</li>
        <li>☐ 加入 <code>3D printable</code>、<code>watertight mesh</code></li>
    </ul>

    <h3>模型生成</h3>
    <ul>
        <li>☐ 已用 Refine 功能精細化</li>
        <li>☐ 檢查無明顯破面 / 穿模</li>
        <li>☐ 比例符合預期</li>
    </ul>

    <h3>模型優化</h3>
    <ul>
        <li>☐ 最小壁厚 ≥ 1.5mm</li>
        <li>☐ 細部特徵 ≥ 2mm</li>
        <li>☐ 已修復網格問題</li>
    </ul>

    <h3>匯出設定</h3>
    <ul>
        <li>☐ <strong>選擇 3MF 格式</strong>（全彩保存，STL 只有單色！）</li>
        <li>☐ 確認模型方向正確</li>
        <li>☐ 尺寸正確（建議 8-15cm）</li>
    </ul>

    <div class="highlight warn">
        ⚠️ <strong>格式選錯＝全彩變黑白！</strong> 全彩 3D 列印必用 3MF 格式！
    </div>
</div>

<!-- ============================================== -->
<!-- ============ 課後行動計劃 ===================== -->
<!-- ============================================== -->
<div class="section-card">
    <h2><span class="emoji">📋</span> 課後 7 天行動計劃</h2>
    <ol>
        <li><strong>Day 1</strong> — 把今天的文案和簡報整理好，存到雲端</li>
        <li><strong>Day 2</strong> — 在蝦皮開一個試賣帳號，上架 1 個商品測試</li>
        <li><strong>Day 3</strong> — 用 AI 修圖後放到商品頁</li>
        <li><strong>Day 4</strong> — 把產品分享到 3 個 FB 社團或 IG 限動</li>
        <li><strong>Day 5</strong> — 用 AI 寫一篇 3D 列印相關部落格文章</li>
        <li><strong>Day 6-7</strong> — 統計瀏覽量，用 AI 分析並調整文案</li>
    </ol>
</div>

</div><!-- /container -->

<div class="footer">
    🧊 AI × 3D列印產品一條龍設計 ｜ 教學網站版 ｜ 資料來源：嚴稑榛老師課程
</div>

</body>
</html>
"""

# ── Routes ────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template_string(INDEX_HTML)

# ── Main ─────────────────────────────────────────────────────
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8899))
    print(f"🚀 教學網站啟動中 → http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
