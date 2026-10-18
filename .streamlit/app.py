import streamlit as st
import random
import time

# 1. 頁面基本配置
st.set_page_config(
    page_title="🌸 LU 寶貝的解壓開心盲盒",
    page_icon="🎁",
    layout="centered"
)

# 2. 專屬粉嫩歡樂 UI 樣式
st.markdown("""
<style>
:root {
    color-scheme: light !important;
}
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2.5rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}
#MainMenu, footer, header {
    visibility: hidden !important;
    display: none !important;
}
div[data-testid="stDecoration"],
[data-testid="manage-app-button"] {
    display: none !important;
    visibility: hidden !important;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "PingFang TC", "Helvetica Neue", sans-serif;
    color: #4A3B40 !important;
    background-color: #FFF5F7 !important;
}
.stApp {
    background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 100%) !important;
}

/* 盲盒卡片效果 */
.card-box {
    background: #FFFFFF !important;
    padding: 22px !important;
    border-radius: 24px !important;
    box-shadow: 0 8px 25px rgba(255, 143, 163, 0.25) !important;
    border: 2px solid #FFE3E8 !important;
    margin-bottom: 20px !important;
    text-align: center;
}
.card-tag {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 12px;
}
.tag-dog { background-color: #FFF3BF; color: #D9480F; }
.tag-cat { background-color: #EBFBEE; color: #2B8A3E; }
.tag-meme { background-color: #E7F5FF; color: #1971C2; }
.tag-ssr { background-color: #FFE3E8; color: #D6336C; border: 1.5px dashed #FF6584; }

.card-title {
    font-size: 1.25rem;
    font-weight: 800;
    color: #D6336C;
    margin-bottom: 10px;
}
.card-content {
    font-size: 1.05rem;
    color: #4A3B40;
    line-height: 1.6;
    margin: 14px 0;
    white-space: pre-wrap;
}

/* 抽卡主按鈕 */
.stButton>button {
    background: linear-gradient(135deg, #FF6584 0%, #FF8FA3 100%) !important;
    color: #FFFFFF !important;
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    border-radius: 25px !important;
    border: none !important;
    padding: 14px 28px !important;
    box-shadow: 0 6px 18px rgba(255, 101, 132, 0.35) !important;
    width: 100% !important;
    transition: transform 0.1s ease-in-out !important;
}
.stButton>button:active {
    transform: scale(0.98) !important;
}

/* 外部跳轉按鈕 */
.threads-btn {
    display: block;
    background: #000000;
    color: #FFFFFF !important;
    text-align: center;
    padding: 12px 16px;
    border-radius: 20px;
    font-weight: 700;
    text-decoration: none;
    margin-top: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

# 3. 歡樂解壓卡池資料庫（包含臘腸狗、吸貓、爆笑脆文、SSR男友兌換券）
CARDS = [
    # 臘腸狗與汪星人專區
    {
        "type": "dog",
        "tag": "🌭 臘腸狗呆萌日常",
        "title": "世界上最遙遠的距離",
        "content": "臘腸狗的日常哲學：\n『我的身體已經在客廳沙發了，但我的後腿還在廚房門口。』\n底盤太低，每次想跳上沙發都像在發射火箭，最後只能發出委屈的嗚嗚聲等抱抱！",
        "img": "https://images.unsplash.com/photo-1612536057832-2ff7ead58194?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "dog",
        "tag": "🌭 臘腸狗迷惑行為",
        "title": "誰准你看我的小短腿？",
        "content": "散步十分鐘，肚皮擦地五分鐘。\n遇到小水坑直接變成水陸兩棲戰車。\n回家第一件事：理所當然躺平，用小短腿朝天討摸摸～🐾",
        "img": "https://images.unsplash.com/photo-1597633425046-08f5110420b5?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "dog",
        "tag": "🐶 汪汪暖心充電",
        "title": "小狗有什麼心事呢？",
        "content": "小狗的世界真的很簡單：\n你出門五分鐘，牠覺得你離開了一萬年；\n你回到家那一秒，牠尾巴搖到像螺旋槳快要起飛！今天也要被小狗純粹的愛治癒喔～",
        "img": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=600&auto=format&fit=crop&q=80"
    },
    # 貓貓迷惑行為專區
    {
        "type": "cat",
        "tag": "🐱 主子迷惑行為",
        "title": "貓咪的液體物理學",
        "content": "買了 1500 元的豪華貓窩 ❌\n裝貓窩的免錢爛紙箱 ⭕\n『人類，別用你狹隘的審美來定義我的尊貴城堡。』",
        "img": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "cat",
        "tag": "🐱 傲嬌主子日常",
        "title": "可以摸，但只能摸三下",
        "content": "第一下：好舒服呼嚕嚕～\n第二下：主子恩賜你摸。\n第三下：一口咬下去！\n『摸夠了沒？誰准你摸第四下的！』（然後一秒後又蹭過來討罐罐）",
        "img": "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=600&auto=format&fit=crop&q=80"
    },
    # 爆笑脆文與生活廢話迷因
    {
        "type": "meme",
        "tag": "😂 脆上爆笑日常",
        "title": "脆友神發言：下班後的狀態",
        "content": "『我下班後不是在休息，我是在進行碳基生物的系統重啟。』\n躺在床上一動不動，連滑手機都嫌手痠，只想被當成植物好好澆水。",
        "img": "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "meme",
        "tag": "😂 脆上共鳴廢文",
        "title": "天蠍座的獨特省電模式",
        "content": "外人眼中的天蠍：高冷、神祕、看透一切。\n私底下的天蠍：『好懶喔...想吃好吃的...想被摸頭...不想出門...』\n傲嬌只是保護色，內心其實是想要被無條件哄上天的小胚胎！",
        "img": "https://images.unsplash.com/photo-1543610892-0b1f7e6d8ac1?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "meme",
        "tag": "😂 人間真實迷因",
        "title": "關於減肥與美食",
        "content": "肚子餓時：『明天一定要開始少吃！』\n看到好吃的端上桌：『不能浪費食物，這是對廚師的尊重。』\n人生苦短，及時行樂，吃飽了才有力氣可愛！",
        "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600&auto=format&fit=crop&q=80"
    },
    # 隱藏 SSR 男友專屬兌換券彩蛋
    {
        "type": "ssr",
        "tag": "✨ 隱藏彩蛋・SSR 稀有卡",
        "title": "🎟️ 男友無條件寵愛兌換券",
        "content": "恭喜寶貝抽到極品 SSR！\n【兌換權利】：\n1. 憑此卡可隨時兌換男友專屬按摩 30 分鐘。\n2. 獲得無條件好喝飲品外送一杯。\n3. 免死金牌一張，享有無限被哄被抱抱權益！🥰",
        "img": ""
    }
]

# 4. 頂部標題區
st.markdown("""
<div style="text-align: center; margin-bottom: 12px;">
    <div style="font-size: 2.2rem;">🎁</div>
    <div style="color: #D6336C; font-size: 1.5rem; font-weight: 800;">LU 寶貝的解壓開心盲盒</div>
    <div style="color: #8C6D77; font-size: 0.9rem; margin-top: 4px;">不開心就來抽一張！滿滿狗狗、貓貓與爆笑迷因 🌸</div>
</div>
""", unsafe_allow_html=True)

# 5. Session State 抽卡記錄
if "current_card" not in st.session_state:
    st.session_state.current_card = random.choice(CARDS)

# 類別篩選器
theme_filter = st.radio(
    "想要抽什麼類型的盲盒呢？",
    ["🎲 全都要（隨機抽）", "🌭 臘腸狗與汪汪", "🐱 貓貓迷惑特區", "😂 爆笑脆文與迷因"],
    horizontal=True
)

def pick_card():
    if "汪汪" in theme_filter:
        pool = [c for c in CARDS if c["type"] in ["dog", "ssr"]]
    elif "貓貓" in theme_filter:
        pool = [c for c in CARDS if c["type"] in ["cat", "ssr"]]
    elif "迷因" in theme_filter:
        pool = [c for c in CARDS if c["type"] in ["meme", "ssr"]]
    else:
        pool = CARDS
    return random.choice(pool)

# 抽卡按鈕
if st.button("✨ 點我開盲盒！抽取今日快樂 ✨"):
    with st.spinner("正在為 LU 寶貝召喚快樂能量...🐾"):
        time.sleep(0.3)
        st.session_state.current_card = pick_card()
    st.rerun()

# 6. 開出的卡片展示
card = st.session_state.current_card

tag_class = f"tag-{card['type']}"
st.markdown(f"""
<div class="card-box">
    <span class="card-tag {tag_class}">{card['tag']}</span>
    <div class="card-title">{card['title']}</div>
    <div class="card-content">{card['content']}</div>
</div>
""", unsafe_allow_html=True)

if card.get("img"):
    st.image(card["img"], use_container_width=True)

st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

# 7. 脆（Threads）熱搜直達專區
with st.expander("🌀 還是想滑脆？點這裡直達熱門爆笑話題", expanded=False):
    st.caption("為寶貝過濾掉無聊吵架，精選 Threads 上最受歡迎的療癒話題直達車：")
    st.markdown('<a href="https://www.threads.net/search?q=%E8%87%98%E8%85%B8%E7%8B%97&serp_type=default" target="_blank" class="threads-btn">🌭 前往 Threads 查看最新【臘腸狗】短影音</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.threads.net/search?q=%E5%8F%AF%E6%84%9B%E5%B0%8F%E7%8B%97&serp_type=default" target="_blank" class="threads-btn">🐶 前往 Threads 查看最新【汪星人日常】</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.threads.net/search?q=%E7%88%86%E7%AC%91%E8%BF%B7%E5%9B%A0&serp_type=default" target="_blank" class="threads-btn">😂 前往 Threads 查看最新【爆笑迷因廢文】</a>', unsafe_allow_html=True)

# 男友專屬求救通道
st.markdown("""
<div style="text-align: center; margin-top: 20px;">
    <a href="https://line.me/ti/p/3u_xwcKRUB" target="_blank" style="color: #D6336C; text-decoration: none; font-size: 0.9rem; font-weight: bold;">
        💌 抽完了還是無聊？點此呼叫專屬男友陪妳聊聊 🥰
    </a>
</div>
""", unsafe_allow_html=True)
