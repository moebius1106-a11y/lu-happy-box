import streamlit as st
import random
import time

# 1. 頁面基本配置
st.set_page_config(
    page_title="🌸 LU 寶貝的解壓開心盲盒 (AI加強版)",
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
    margin-bottom: 16px !important;
    text-align: center;
}
.card-tag {
    display: inline-block;
    padding: 5px 16px;
    border-radius: 20px;
    font-size: 0.88rem;
    font-weight: 700;
    margin-bottom: 12px;
}
.tag-dog { background-color: #FFF3BF; color: #D9480F; }
.tag-cat { background-color: #EBFBEE; color: #2B8A3E; }
.tag-meme { background-color: #E7F5FF; color: #1971C2; }
.tag-ai { background-color: #F3E8FF; color: #7950F2; border: 1.5px solid #D0BFFF; }
.tag-ssr { background-color: #FFE3E8; color: #D6336C; border: 1.5px dashed #FF6584; }

.card-title {
    font-size: 1.3rem;
    font-weight: 800;
    color: #D6336C;
    margin-bottom: 12px;
}
.card-content {
    font-size: 1.05rem;
    color: #4A3B40;
    line-height: 1.65;
    margin: 12px 0;
    white-space: pre-wrap;
    text-align: left;
    background: #FFF9FA;
    padding: 14px 16px;
    border-radius: 16px;
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

# 3. 巨量精選卡池資料庫（海量基底）
CARDS = [
    # ─── 🌭 臘腸狗與短腿專屬特區 ───
    {
        "type": "dog",
        "tag": "🌭 臘腸狗日常",
        "title": "世界上最遙遠的距離",
        "content": "臘腸狗的日常哲學：\n『我的上半身已經在客廳沙發了，但我的後腿還在廚房門口。』\n底盤太低，每次想跳上沙發都像在發射火箭，後腿蹬了半天還在原地，最後只能發出委屈的嗚嗚聲等抱抱！",
        "img": "https://images.unsplash.com/photo-1612536057832-2ff7ead58194?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "dog",
        "tag": "🌭 臘腸狗行為學",
        "title": "被窩裡的探頭熱狗",
        "content": "天冷時的臘腸狗：\n整條鑽進被窩只露出一顆黑鼻頭呼吸。\n你想拉開被子？牠會用整條長身軀死死夾住床墊，喉嚨發出呼嚕呼嚕的護被警告：『誰都別想叫本熱狗起床！』",
        "img": "https://images.unsplash.com/photo-1597633425046-08f5110420b5?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "dog",
        "tag": "🌭 臘腸狗視角",
        "title": "下雨天最大的敵人",
        "content": "別的狗狗下雨天是腳濕掉。\n臘腸狗下雨天出門散步五分鐘：肚皮洗地、胸毛泡水，直接從陸生動物變成水陸兩棲戰車！回家洗澡一臉生無可戀🐾",
        "img": ""
    },
    {
        "type": "dog",
        "tag": "🌭 臘腸狗日常",
        "title": "長條型生物的霸道佔位",
        "content": "一張雙人床明明很大。\n但只要一條臘腸狗往中間橫著一躺，整張床瞬間只剩下邊緣 10 公分給人類睡。\n而且千萬別試圖推牠，牠會像焊死在床上一樣重！",
        "img": ""
    },
    {
        "type": "dog",
        "tag": "🌭 臘腸狗警報器",
        "title": "身體雖小，肺活量超大",
        "content": "門外只要有一片樹葉掉下來：\n『汪！汪！汪汪汪！汪！』\n叫得像家裡有三隻藏獒入侵一樣，結果主人一開門看見外送員，牠一秒縮到主人小腿後面探頭：『...那個，有帶我的肉肉嗎？』",
        "img": ""
    },
    {
        "type": "dog",
        "tag": "🌭 臘腸短腿之謎",
        "title": "小短腿的尊嚴",
        "content": "千萬不要當著臘腸狗的面嘲笑牠的腿短。\n雖然牠跨過一根小水管需要深呼吸三秒＋助跑，但只要廚房傳來開起司片包裝的聲音，牠能以時速 80 公里底盤磨地飄移進來！",
        "img": ""
    },

    # ─── 🐶 汪星人爆笑日常 ───
    {
        "type": "dog",
        "tag": "🐶 柴犬頑固現場",
        "title": "散步終點站：躺平",
        "content": "走到了公園十字路口，柴柴突然決定：『我今天就走到這裡了。』\n脖子直接縮成雙下巴麻糬，四隻腳像塗了強力膠焊死在柏油路上，人類只能尷尬地在路人圍觀下把一整坨肉抱回家。",
        "img": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "dog",
        "tag": "🐶 黃金獵犬日常",
        "title": "世界上沒有壞心眼的小狗",
        "content": "把拖鞋咬爛了，被主人抓包時：\n耳朵向後貼成海豹、眼睛瞇成一條線，一邊假笑一邊用毛茸茸的大爪子搭在你手上按一按：『別生氣嘛～拖鞋是自己裂開的，我只是幫妳檢查材質！』",
        "img": ""
    },
    {
        "type": "dog",
        "tag": "🐶 柯基短腿大隊",
        "title": "樓梯是柯基永遠的痛",
        "content": "遇到三階以上的樓梯：\n大腦：『衝啊！』\n小短腿：『撲騰撲騰撲騰（懸空抓空氣）』。\n最後屁屁像顆吐司麵包一扭一扭地等著人類連狗帶屁股提上去～",
        "img": ""
    },
    {
        "type": "dog",
        "tag": "🐶 狗勾迷惑發言",
        "title": "你偷偷在廚房吃什麼？",
        "content": "你在房間撕開洋芋片包裝的聲音大概只有 5 分貝。\n但在隔壁房間睡得像豬一樣的狗勾，能在 0.01 秒內驚醒並滑行進廚房，坐在你面前眼神發光：『見者有份，這是這家裡的規矩。』",
        "img": ""
    },
    {
        "type": "dog",
        "tag": "🐶 薩摩耶微笑天使",
        "title": "泥巴水坑的誘惑",
        "content": "剛花兩千元去寵物美容洗得白泡泡幼咪咪的薩摩耶。\n一走到公園看到黑泥巴坑：眼神發亮、飛撲進去、打滾三圈！瞬間從純白天使變成髒髒包，還吐著舌頭對你燦笑：『主人看我漂不漂亮！』",
        "img": ""
    },

    # ─── 🐱 傲嬌主子迷惑行為 ───
    {
        "type": "cat",
        "tag": "🐱 貓咪物理學",
        "title": "昂貴貓窩 vs 破紙箱",
        "content": "人類花了 1800 買了北歐羊毛保暖豪華貓窩 ❌\n快遞送來的沾滿灰塵破紙箱 ⭕\n貓咪：『愚蠢的人類，別用你俗氣的審美來衡量我尊貴的紙箱城堡。』",
        "img": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "cat",
        "tag": "🐱 貓界霸王條款",
        "title": "可以摸，但只能摸三下",
        "content": "第一下：呼嚕呼嚕好舒服～\n第二下：本宮准你摸。\n第三下：一口咬住人類的手！\n『大膽！誰准你摸第四下的！』（咬完兩秒後又用頭蹭你的手心討肉泥）",
        "img": "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "cat",
        "tag": "🐱 半夜迷惑跑酷",
        "title": "凌晨三點的奧林匹克運動會",
        "content": "白天：睡得像一灘融化在地上的死水，怎麼戳都沒反應。\n凌晨 3:15：突然在大腦連線到外星信號，從客廳直線衝刺飛上衣櫃，再踩著人類的肚子起跳！『起床看我奔馳，人類！』",
        "img": ""
    },
    {
        "type": "cat",
        "tag": "🐱 監視狂貓",
        "title": "衛生間的專屬警衛",
        "content": "只要你進廁所關上門，門縫底下立刻會出現一隻毛茸茸的小白爪在那裡掏啊掏：\n『你是不是在裡面背著我偷偷吃好料？快開門！不要逼我一直叫！』",
        "img": ""
    },
    {
        "type": "cat",
        "tag": "🐱 貓貓的惡趣味",
        "title": "桌緣推土機",
        "content": "看著桌上的水杯。\n看著你。\n再伸出小爪爪把水杯往桌邊挪動 1 公分。\n看著你崩潰喊『不要！』，牠眼睛眨都不眨，一巴掌把水杯推下去：『我就喜歡看重力加速度的樣子。』",
        "img": ""
    },

    # ─── 😂 脆（Threads）爆笑迷因與共鳴廢文 ───
    {
        "type": "meme",
        "tag": "😂 脆上爆紅共鳴",
        "title": "下班後的系統重啟",
        "content": "『我下班後不是在偷懶，我是在進行碳基生物的系統格式化。』\n一進家門鞋子一脫，整個人像沒有骨頭的布丁一樣融化在床上一動不動，連伸手拿充電線都覺得那是奧運等級的極限運動。",
        "img": "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=600&auto=format&fit=crop&q=80"
    },
    {
        "type": "meme",
        "tag": "😂 脆上神比喻",
        "title": "薪水在戶頭的停留時間",
        "content": "5號發薪水：戶頭進帳感覺自己是全信義區最有錢的大老闆。\n6號繳房租、卡費、水電費、買日常用品：\n戶頭：『感謝您使用體驗版資金，試用期已結束，下次請早。』",
        "img": ""
    },
    {
        "type": "meme",
        "tag": "😂 脆友感情哲學",
        "title": "女生說的『隨便吃什麼都行』",
        "content": "男友：『吃火鍋？』\n女生：『昨天才吃過。』\n男友：『吃義大利麵？』\n女生：『今天不想吃澱粉。』\n男友：『那妳想吃什麼？』\n女生：『就說都可以啊，你都不動腦！』\n（正解：直接把最好吃的那家甜點或排隊名店端到她面前就對了！）",
        "img": ""
    },
    {
        "type": "meme",
        "tag": "😂 脆上真實迷因",
        "title": "天蠍女的極端切換",
        "content": "在外工作時：氣場兩米八，公事公辦，眼神冷得像西伯利亞的暴風雪。\n回到男友身邊時：『肚子餓...要抱抱...幫我開瓶蓋...今天誰誰誰好煩喔你要幫我罵他！』\n外表是女王，骨子裡只想當個被哄成胚胎的專屬小公主🥰",
        "img": ""
    },
    {
        "type": "meme",
        "tag": "😂 生活爆笑迷因",
        "title": "關於晚上滑手機的時間黑洞",
        "content": "11:00 PM：『再滑最後五分鐘脆就去睡覺。』\n11:05 PM：看到一個爆笑臘腸狗短影音。\n11:45 PM：開始研究北極熊的毛其實是透明的冷知識。\n01:30 AM：『我是誰？我在哪？明天早上八點要起床天啊！』",
        "img": ""
    },
    {
        "type": "meme",
        "tag": "😂 脆上爆笑對話",
        "title": "理智與食慾的拉扯",
        "content": "理智：『晚上十點後吃宵夜會胖，而且對腸胃不好。』\n肚子：『可是鹽酥雞是熱的，熱的食物能溫暖心靈，心靈健康人就健康。』\n結論：『老闆，鹹酥雞一份魷魚一份，九層塔蒜頭多一點！』",
        "img": ""
    },
    {
        "type": "meme",
        "tag": "😂 職場人間清醒",
        "title": "工作的動力來源",
        "content": "『我熱愛工作嗎？我不熱愛。但我熱愛花錢、熱愛吃好料、熱愛網購包裹到貨時拆箱的那一聲清脆膠帶聲。所以，今天也是為了包裹努力搬磚的一天！』",
        "img": ""
    },
    {
        "type": "meme",
        "tag": "😂 脆友神吐槽",
        "title": "出門前的儀式感",
        "content": "女生說『我快好了，再五分鐘出門！』的意思是：\n衣服試了三套還沒選好、隱形眼鏡剛戴進一隻、電棒捲剛插上電加熱、手機電量 12% 剛接上線。\n男友請自覺坐回沙發，至少還有半小時安心發呆時間！",
        "img": ""
    },
    {
        "type": "meme",
        "tag": "😂 現代社交禮儀",
        "title": "訊息已讀不回的心理學",
        "content": "『我看到訊息了，我也在大腦裡回覆了妳，但我的手指沒有接收到大腦的指令。所以技術上來說，我已經回覆過妳了。』——脆友的極致懶癌藉口。",
        "img": ""
    },

    # ─── ✨ 男友專屬隱藏彩蛋（SSR 系列） ───
    {
        "type": "ssr",
        "tag": "✨ 隱藏彩蛋・SSR 稀有卡",
        "title": "🎟️ 男友無條件溫柔按摩券",
        "content": "恭喜寶貝抽到極品 SSR！\n【兌換權利】：\n憑此卡找男友，可無條件兌換『肩頸或腿部舒壓按摩 30 分鐘』！\n附帶溫柔哄睡服務，永久有效、不可轉讓，隨時召喚即刻生效 🥰",
        "img": ""
    },
    {
        "type": "ssr",
        "tag": "✨ 隱藏彩蛋・SSR 稀有卡",
        "title": "🧋 男友專屬手搖飲外送券",
        "content": "恭喜寶貝抽到限量 SSR！\n【兌換權利】：\n今天想喝什麼手搖飲、或是想喝熱熱甜甜的黑糖飲品，出示此截圖給男友，男友立刻奉上，寶貝只要張嘴負責喝就好！❤️",
        "img": ""
    },
    {
        "type": "ssr",
        "tag": "✨ 隱藏彩蛋・SSR 稀有卡",
        "title": "🛡️ 免死金牌與無限哄人券",
        "content": "恭喜寶貝抽到頂級 SSR！\n【兌換權利】：\n今日不論心情多差、有多任性、想罵誰討厭鬼，男友全部站妳這邊，無條件陪妳同仇敵愾，把妳哄到心花怒放為止！🌸",
        "img": ""
    },
    {
        "type": "ssr",
        "tag": "✨ 隱藏彩蛋・SSR 稀有卡",
        "title": "🍗 深夜罪惡宵夜陪吃券",
        "content": "恭喜寶貝抽到深夜 SSR！\n【兌換權利】：\n只要妳想吃，不管是鹽酥雞、滷味還是熱豆花，男友無條件陪吃，所有發胖熱量男友通通替妳吸收！🥰",
        "img": ""
    }
]

# 4. 頂部標題區
st.markdown("""
<div style="text-align: center; margin-bottom: 12px;">
    <div style="font-size: 2.2rem;">🎁</div>
    <div style="color: #D6336C; font-size: 1.5rem; font-weight: 800;">LU 寶貝的解壓開心盲盒</div>
    <div style="color: #8C6D77; font-size: 0.9rem; margin-top: 4px;">不開心就來抽一張！滿滿臘腸狗、吸貓與爆笑脆文 🌸</div>
</div>
""", unsafe_allow_html=True)

# 5. Session State 抽卡記錄與防重複機制
if "drawn_indices" not in st.session_state:
    st.session_state.drawn_indices = []

if "current_card" not in st.session_state:
    st.session_state.current_card = random.choice(CARDS)

# 類別篩選器
theme_filter = st.radio(
    "想要抽什麼類型的盲盒呢？",
    ["🎲 全都要（隨機抽）", "🌭 臘腸狗與汪汪", "🐱 貓貓迷惑特區", "😂 爆笑脆文與迷因", "🤖 AI 即時脆文生成"],
    horizontal=True
)

# AI 生成動態卡片邏輯
def generate_ai_card():
    # 隨機靈感題目
    topics = [
        ("🌭 AI 創作：臘腸狗秘密心事", "如果臘腸狗會發脆文", "『今天主人出門五分鐘，我把他的襪子藏進沙發深處了。不是我壞，是襪子上面有主人的味道，我很想他。但這不妨礙我晚上繼續踩他的肚皮討肉泥吃。』\n\n#底盤低但愛很高 #臘腸哲學"),
        ("😂 AI 創作：脆友暴言日常", "當天蠍座女生說『沒事』", "『外人以為的沒事：真的沒事。\n男友必須知道的沒事：立刻放下手邊一切，準備三種好吃的甜點、一杯溫熱無糖茶，並在五秒內把她抱進懷裡說「誰欺負我的心頭肉了？我幫妳出氣！」』\n\n#生存指南 #專屬偏愛"),
        ("🐱 AI 創作：貓咪統治日記", "為什麼我半夜要盯著妳睡覺", "『愚蠢的人類閉上眼睛後，呼吸變得很慢。我必須跳到妳胸口上重重踩兩下，確定妳的心臟還在跳，順便確認明天早上六點準時開罐罐的奴隸依然健在。』\n\n#貓的傲嬌 #沉重但真實的愛"),
        ("😂 AI 創作：社畜的極致清醒", "我的靈魂在下班那一刻離開肉體", "『上班時：我是專業成熟的職場菁英。\n下班坐上捷運那一刻：我是一灘融化的爛泥巴。\n到家看到男友：『抱我～我走不動了～今天全世界都在為難我～』』\n\n#切換自如 #專屬撒嬌特權")
    ]
    chosen = random.choice(topics)
    return {
        "type": "ai",
        "tag": chosen[0],
        "title": chosen[1],
        "content": chosen[2],
        "img": ""
    }

def pick_next_card():
    if "AI" in theme_filter:
        return generate_ai_card()

    if "汪汪" in theme_filter:
        candidates = [i for i, c in enumerate(CARDS) if c["type"] in ["dog", "ssr"]]
    elif "貓貓" in theme_filter:
        candidates = [i for i, c in enumerate(CARDS) if c["type"] in ["cat", "ssr"]]
    elif "迷因" in theme_filter:
        candidates = [i for i, c in enumerate(CARDS) if c["type"] in ["meme", "ssr"]]
    else:
        candidates = list(range(len(CARDS)))
    
    available = [i for i in candidates if i not in st.session_state.drawn_indices]
    if not available:
        st.session_state.drawn_indices = []
        available = candidates
    
    selected_idx = random.choice(available)
    st.session_state.drawn_indices.append(selected_idx)
    if len(st.session_state.drawn_indices) > 15:
        st.session_state.drawn_indices.pop(0)
        
    return CARDS[selected_idx]

# 抽卡按鈕
if st.button("✨ 點我開盲盒！抽取今日快樂 ✨"):
    with st.spinner("正在為 LU 寶貝召喚爆笑能量...🐾"):
        time.sleep(0.2)
        st.session_state.current_card = pick_next_card()
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

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

# 7. 脆（Threads）熱搜直達專區
with st.expander("🌀 還是想去脆上晃晃？點這裡直達熱門療癒話題", expanded=False):
    st.caption("為寶貝過濾掉無聊吵架，精選 Threads 上最受歡迎的搞笑與寵物傳送門：")
    st.markdown('<a href="https://www.threads.net/search?q=%E8%87%98%E8%85%B8%E7%8B%97&serp_type=default" target="_blank" class="threads-btn">🌭 前往 Threads 查看最新【臘腸狗】短影音</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.threads.net/search?q=%E5%8F%AF%E6%84%9B%E5%B0%8F%E7%8B%97&serp_type=default" target="_blank" class="threads-btn">🐶 前往 Threads 查看最新【汪星人日常】</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.threads.net/search?q=%E7%88%86%E7%AC%91%E8%BF%B7%E5%9B%A0&serp_type=default" target="_blank" class="threads-btn">😂 前往 Threads 查看最新【爆笑迷因廢文】</a>', unsafe_allow_html=True)

# 男友專屬求救通道
st.markdown("""
<div style="text-align: center; margin-top: 18px;">
    <a href="https://line.me/ti/p/3u_xwcKRUB" target="_blank" style="color: #D6336C; text-decoration: none; font-size: 0.92rem; font-weight: bold;">
        💌 抽完了還是無聊？點此呼叫專屬男友陪妳聊聊 🥰
    </a>
</div>
""", unsafe_allow_html=True)
