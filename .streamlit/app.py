import streamlit as st
import random
import time

# 1. 頁面基本配置（適配 iPhone 視窗）
st.set_page_config(
    page_title="🌸 LU 寶貝的解壓開心盲盒",
    page_icon="🎁",
    layout="centered"
)

# 2. iPhone (iOS Safari & LINE WebView) 加固 UI 樣式
st.markdown("""
<style>
:root {
    color-scheme: light !important;
    -webkit-color-scheme: light !important;
}

.block-container {
    padding-top: max(0.8rem, env(safe-area-inset-top)) !important;
    padding-bottom: max(3rem, env(safe-area-inset-bottom)) !important;
    padding-left: 0.8rem !important;
    padding-right: 0.8rem !important;
}

#MainMenu, footer, header, [data-testid="manage-app-button"], div[data-testid="stDecoration"] {
    display: none !important;
    visibility: hidden !important;
}

body {
    -webkit-font-smoothing: antialiased;
    -webkit-tap-highlight-color: transparent !important;
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
    padding: 20px 18px !important;
    border-radius: 22px !important;
    box-shadow: 0 8px 24px rgba(255, 143, 163, 0.22) !important;
    border: 1.5px solid #FFE3E8 !important;
    margin-bottom: 16px !important;
    text-align: center;
    -webkit-transform: translateZ(0);
}

.card-tag {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 18px;
    font-size: 0.85rem;
    font-weight: 700;
    margin-bottom: 10px;
}
.tag-dog { background-color: #FFF3BF; color: #D9480F; }
.tag-cat { background-color: #EBFBEE; color: #2B8A3E; }
.tag-meme { background-color: #E7F5FF; color: #1971C2; }
.tag-infinite { background-color: #F3E8FF; color: #7950F2; border: 1px solid #D0BFFF; }
.tag-ssr { background-color: #FFE3E8; color: #D6336C; border: 1.5px dashed #FF6584; }

.card-title {
    font-size: 1.25rem;
    font-weight: 800;
    color: #D6336C;
    margin-bottom: 10px;
}
.card-content {
    font-size: 1rem;
    color: #4A3B40 !important;
    line-height: 1.65;
    margin: 10px 0;
    white-space: pre-wrap;
    text-align: left;
    background: #FFF9FA;
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #FFEBEF;
}

/* 抽卡主按鈕 */
.stButton>button {
    background: linear-gradient(135deg, #FF6584 0%, #FF8FA3 100%) !important;
    color: #FFFFFF !important;
    font-size: 1.12rem !important;
    font-weight: 800 !important;
    border-radius: 24px !important;
    border: none !important;
    padding: 13px 20px !important;
    box-shadow: 0 6px 18px rgba(255, 101, 132, 0.35) !important;
    width: 100% !important;
    touch-action: manipulation;
    transition: transform 0.08s ease;
}
.stButton>button:active {
    transform: scale(0.96) !important;
}

div[role="radiogroup"] label {
    color: #5C2D3B !important;
    font-size: 0.9rem !important;
}

.threads-btn {
    display: block;
    background: #000000;
    color: #FFFFFF !important;
    text-align: center;
    padding: 12px 14px;
    border-radius: 18px;
    font-weight: 700;
    text-decoration: none;
    margin-top: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    font-size: 0.92rem;
    touch-action: manipulation;
}
</style>
""", unsafe_allow_html=True)

# 3. 超巨大核心經典資料庫 (60+ 精品卡池)
STATIC_CARDS = [
    # ─── 🌭 臘腸狗與短腿專區 ───
    {"type": "dog", "tag": "🌭 臘腸狗日常", "title": "世界上最遙遠的距離", "content": "臘腸狗的日常哲學：\n『我的上半身已經在客廳沙發了，但我的後腿還在廚房門口。』\n底盤太低，每次想跳上沙發都像在發射火箭，後腿蹬了半天還在原地，最後只能發出委屈的嗚嗚聲等抱抱！", "img": "https://images.unsplash.com/photo-1612536057832-2ff7ead58194?w=600&auto=format&fit=crop&q=80"},
    {"type": "dog", "tag": "🌭 臘腸狗行為學", "title": "被窩裡的探頭熱狗", "content": "天冷時的臘腸狗：\n整條鑽進被窩只露出一顆黑鼻頭呼吸。\n你想拉開被子？牠會用整條長身軀死死夾住床墊，喉嚨發出呼嚕呼嚕的護被警告：『誰都別想叫本熱狗起床！』", "img": "https://images.unsplash.com/photo-1597633425046-08f5110420b5?w=600&auto=format&fit=crop&q=80"},
    {"type": "dog", "tag": "🌭 臘腸狗視角", "title": "下雨天最大的敵人", "content": "別的狗狗下雨天是腳濕掉。\n臘腸狗下雨天出門散步五分鐘：肚皮洗地、胸毛泡水，直接從陸生動物變成水陸兩棲戰車！回家洗澡一臉生無可戀🐾", "img": ""},
    {"type": "dog", "tag": "🌭 臘腸狗日常", "title": "長條型生物的霸道佔位", "content": "一張雙人床明明很大。\n但只要一條臘腸狗往中間橫著一躺，整張床瞬間只剩下邊緣 10 公分給人類睡。\n而且千萬別試圖推牠，牠會像焊死在床上一樣重！", "img": ""},
    {"type": "dog", "tag": "🌭 臘腸狗警報器", "title": "身體雖小，肺活量超大", "content": "門外只要有一片樹葉掉下來：\n『汪！汪！汪汪汪！汪！』\n叫得像家裡有三隻藏獒入侵一樣，結果主人一開門看見外送員，牠一秒縮到主人小腿後面探頭：『...那個，有帶我的肉肉嗎？』", "img": ""},
    {"type": "dog", "tag": "🌭 臘腸短腿之謎", "title": "小短腿的尊嚴", "content": "千萬不要當著臘腸狗的面嘲笑牠的腿短。\n雖然牠跨過一根小水管需要深呼吸三秒＋助跑，但只要廚房傳來開起司片包裝的聲音，牠能以時速 80 公里底盤磨地飄移進來！", "img": ""},
    {"type": "dog", "tag": "🌭 臘腸狗日常", "title": "衣服永遠買不到合身的", "content": "買 S 號：身長像穿迷你露臍露肚裝，屁股全在外面吹風。\n買 L 號：長度剛好了，胸口鬆得像穿深 V 晚禮服，走兩步前腿直接被袖子絆倒摔跤！", "img": ""},
    {"type": "dog", "tag": "🌭 臘腸狗內心戲", "title": "我懷疑你在說我短", "content": "主人：『你這條熱狗過來！』\n臘腸狗立刻耳朵往後貼，眼神斜斜瞪過來：『說誰熱狗？請叫我長版尊貴獵犬！還有，這塊地毯我已經用肚皮拖乾淨了，快給肉乾！』", "img": ""},
    {"type": "dog", "tag": "🌭 臘腸狗日常", "title": "打雷時的極致偽裝", "content": "外頭一打雷，整隻臘腸狗立刻展現極致柔軟度，把兩米長的身體硬生生縮進拖鞋裡，只露出一對充滿恐懼的大眼睛：『雷公看不到我、雷公看不到我...』", "img": ""},

    # ─── 🐶 汪星人爆笑日常 ───
    {"type": "dog", "tag": "🐶 柴犬頑固現場", "title": "散步終點站：躺平", "content": "走到了公園十字路口，柴柴突然決定：『我今天就走到這裡了。』\n脖子直接縮成雙下巴麻糬，四隻腳像塗了強力膠焊死在柏油路上，人類只能尷尬地在路人圍觀下把一整坨肉抱回家。", "img": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=600&auto=format&fit=crop&q=80"},
    {"type": "dog", "tag": "🐶 黃金獵犬日常", "title": "世界上沒有壞心眼的小狗", "content": "把拖鞋咬爛了，被主人抓包時：\n耳朵向後貼成海豹、眼睛瞇成一條線，一邊假笑一邊用毛茸茸的大爪子搭在你手上按一按：『別生氣嘛～拖鞋是自己裂開的，我只是幫妳檢查材質！』", "img": ""},
    {"type": "dog", "tag": "🐶 柯基短腿大隊", "title": "樓梯是柯基永遠的痛", "content": "遇到三階以上的樓梯：\n大腦：『衝啊！』\n小短腿：『撲騰撲騰撲騰（懸空抓空氣）』。\n最後屁屁像顆吐司麵包一扭一扭地等著人類連狗帶屁股提上去～", "img": ""},
    {"type": "dog", "tag": "🐶 狗勾迷惑發言", "title": "你偷偷在廚房吃什麼？", "content": "你在房間撕開洋芋片包裝的聲音大概只有 5 分貝。\n但在隔壁房間睡得像豬一樣的狗勾，能在 0.01 秒內驚醒並滑行進廚房，坐在你面前眼神發光：『見者有份，這是這家裡的規矩。』", "img": ""},
    {"type": "dog", "tag": "🐶 薩摩耶微笑天使", "title": "泥巴水坑的誘惑", "content": "剛花兩千元去寵物美容洗得白泡泡幼咪咪的薩摩耶。\n一走到公園看到黑泥巴坑：眼神發亮、飛撲進去、打滾三圈！瞬間從純白天使變成髒髒包，還吐著舌頭對你燦笑：『主人看我漂不漂亮！』", "img": ""},
    {"type": "dog", "tag": "🐶 邊境牧羊犬", "title": "狗比主人還聰明的尷尬", "content": "主人試圖騙邊牧把球藏在身後。\n邊牧嘆了一口氣，默默走到主人的左手邊用鼻子頂了頂球，那眼神彷彿在說：『要玩這個無聊遊戲幾次？快點丟，我還要趕著去盤算明天的股票。』", "img": ""},
    {"type": "dog", "tag": "🐶 小狗的超能力", "title": "治癒全世界的尾巴", "content": "小狗的世界真的很小，小到只能裝下你一個人；但牠的愛又很大，大到只要看到你笑，牠就能把整條尾巴搖成直升機螺旋槳，把你的壞心情通通吹散！", "img": ""},

    # ─── 🐱 傲嬌主子迷惑行為 ───
    {"type": "cat", "tag": "🐱 貓咪物理學", "title": "昂貴貓窩 vs 破紙箱", "content": "人類花了 1800 買了北歐羊毛保暖豪華貓窩 ❌\n快遞送來的沾滿灰塵破紙箱 ⭕\n貓咪：『愚蠢的人類，別用你俗氣的審美來衡量我尊貴的紙箱城堡。』", "img": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=600&auto=format&fit=crop&q=80"},
    {"type": "cat", "tag": "🐱 貓界霸王條款", "title": "可以摸，但只能摸三下", "content": "第一下：呼嚕呼嚕好舒服～\n第二下：本宮准你摸。\n第三下：一口咬住人類的手！\n『大膽！誰准你摸第四下的！』（咬完兩秒後又用頭蹭你的手心討肉泥）", "img": "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?w=600&auto=format&fit=crop&q=80"},
    {"type": "cat", "tag": "🐱 半夜迷惑跑酷", "title": "凌晨三點的奧林匹克運動會", "content": "白天：睡得像一灘融化在地上的死水，怎麼戳都沒反應。\n凌晨 3:15：突然在大腦連線到外星信號，從客廳直線衝刺飛上衣櫃，再踩著人類的肚子起跳！『起床看我奔馳，人類！』", "img": ""},
    {"type": "cat", "tag": "🐱 監視狂貓", "title": "衛生間的專屬警衛", "content": "只要你進廁所關上門，門縫底下立刻會出現一隻毛茸茸的小白爪在那裡掏啊掏：\n『你是不是在裡面背著我偷偷吃好料？快開門！不要逼我一直叫！』", "img": ""},
    {"type": "cat", "tag": "🐱 貓貓的惡趣味", "title": "桌緣推土機", "content": "看著桌上的水杯。\n看著你。\n再伸出小爪爪把水杯往桌邊挪動 1 公分。\n看著你崩潰喊『不要！』，牠眼睛眨都不眨，一巴掌把水杯推下去：『我就喜歡看重力加速度的樣子。』", "img": ""},
    {"type": "cat", "tag": "🐱 貓咪叫早服務", "title": "愛的窒息式叫醒", "content": "早上七點鬧鐘還沒響，臉上突然感受到一股溫熱又毛茸茸的重壓。\n睜開眼發現貓咪把整個毛茸茸的屁股精準坐在你鼻孔上：『該起床開罐頭了，呼吸可以暫停，但我的早餐不能遲到。』", "img": ""},
    {"type": "cat", "tag": "🐱 假裝高冷", "title": "其實我都在偷偷注意妳", "content": "不管你在客廳、廚房還是陽台，轉過身永遠會看到牠在門角露出半顆頭偷看妳。\n妳一叫牠名字，牠立刻仰頭看天花板吹口哨：『我才沒有看妳，我是在觀察這堵牆的水泥施工品質。』", "img": ""},

    # ─── 😂 脆（Threads）爆笑迷因與生活共鳴 ───
    {"type": "meme", "tag": "😂 脆上爆紅共鳴", "title": "下班後的系統重啟", "content": "『我下班後不是在偷懶，我是在進行碳基生物的系統格式化。』\n一進家門鞋子一脫，整個人像沒有骨頭的布丁一樣融化在床上一動不動，連伸手拿充電線都覺得那是奧運等級的極限運動。", "img": "https://images.unsplash.com/photo-1518020382113-a7e8fc38eac9?w=600&auto=format&fit=crop&q=80"},
    {"type": "meme", "tag": "😂 脆上神比喻", "title": "薪水在戶頭的停留時間", "content": "5號發薪水：戶頭進帳感覺自己是全信義區最有錢的大老闆。\n6號繳房租、卡費、水電費、買日常用品：\n戶頭：『感謝您使用體驗版資金，試用期已結束，下次請早。』", "img": ""},
    {"type": "meme", "tag": "😂 脆友感情哲學", "title": "女生說的『隨便吃什麼都行』", "content": "男友：『吃火鍋？』\n女生：『昨天才吃過。』\n男友：『吃義大利麵？』\n女生：『今天不想吃澱粉。』\n男友：『那妳想吃什麼？』\n女生：『就說都可以啊，你都不動腦！』\n（正解：直接把最好吃的那家甜點或排隊名店端到她面前就對了！）", "img": ""},
    {"type": "meme", "tag": "😂 脆上真實迷因", "title": "天蠍女的極端切換", "content": "在外工作時：氣場兩米八，公事公辦，眼神冷得像西伯利亞的暴風雪。\n回到男友身邊時：『肚子餓...要抱抱...幫我開瓶蓋...今天誰誰誰好煩喔你要幫我罵他！』\n外表是女王，骨子裡只想當個被哄成胚胎的專屬小公主🥰", "img": ""},
    {"type": "meme", "tag": "😂 生活爆笑迷因", "title": "關於晚上滑手機的時間黑洞", "content": "11:00 PM：『再滑最後五分鐘脆就去睡覺。』\n11:05 PM：看到一個爆笑臘腸狗短影音。\n11:45 PM：開始研究北極熊的毛其實是透明的冷知識。\n01:30 AM：『我是誰？我在哪？明天早上八點要起床天啊！』", "img": ""},
    {"type": "meme", "tag": "😂 脆上爆笑對話", "title": "理智與食慾的拉扯", "content": "理智：『晚上十點後吃宵夜會胖，而且對腸胃不好。』\n肚子：『可是鹽酥雞是熱的，熱的食物能溫暖心靈，心靈健康人就健康。』\n結論：『老闆，鹹酥雞一份魷魚一份，九層塔蒜頭多一點！』", "img": ""},
    {"type": "meme", "tag": "😂 職場人間清醒", "title": "工作的動力來源", "content": "『我熱愛工作嗎？我不熱愛。但我熱愛花錢、熱愛吃好料、熱愛網購包裹到貨時拆箱的那一聲清脆膠帶聲。所以，今天也是為了包裹努力搬磚的一天！』", "img": ""},
    {"type": "meme", "tag": "😂 脆友神吐槽", "title": "出門前的儀式感", "content": "女生說『我快好了，再五分鐘出門！』的意思是：\n衣服試了三套還沒選好、隱形眼鏡剛戴進一隻、電棒捲剛插上電加熱、手機電量 12% 剛接上線。\n男友請自覺坐回沙發，至少還有半小時安心發呆時間！", "img": ""},
    {"type": "meme", "tag": "😂 現代社交禮儀", "title": "訊息已讀不回的心理學", "content": "『我看到訊息了，我也在大腦裡回覆了妳，但我的手指沒有接收到大腦的指令。所以技術上來說，我已經回覆過妳了。』——脆友的極致懶癌藉口。", "img": ""},
    {"type": "meme", "tag": "😂 脆上爆笑日常", "title": "假裝自己成熟穩重", "content": "成年人的崩潰往往就在一瞬間：\n工作上被罵沒哭、遇到奧客沒哭。\n晚上回到家，喝奶茶把吸管插歪戳穿杯底、奶茶噴滿整條褲子那一刻，整個人蹲在地上哭得像個三歲小孩！", "img": ""},
    {"type": "meme", "tag": "😂 脆上真實哲學", "title": "被窩的重力場假說", "content": "科學家說地球引力是 9.8 m/s²。\n但我房間被窩早上的引力大概是 980,000 m/s²，任何試圖在 10 分鐘內離開被窩的行為，都會引發肌肉抽搐與靈魂剝離痛苦！", "img": ""},

    # ─── ✨ 男友專屬隱藏彩蛋（SSR 系列・加倍爆率） ───
    {"type": "ssr", "tag": "✨ 隱藏彩蛋・SSR 稀有卡", "title": "🎟️ 男友無條件溫柔按摩券", "content": "恭喜寶貝抽到極品 SSR！\n【兌換權利】：\n憑此卡找男友，可無條件兌換『肩頸或腿部舒壓按摩 30 分鐘』！\n附帶溫柔哄睡服務，永久有效、不可轉讓，隨時召喚即刻生效 🥰", "img": ""},
    {"type": "ssr", "tag": "✨ 隱藏彩蛋・SSR 稀有卡", "title": "🧋 男友專屬手搖飲外送券", "content": "恭喜寶貝抽到限量 SSR！\n【兌換權利】：\n今天想喝什麼手搖飲、或是想喝熱熱甜甜的黑糖飲品，出示此截圖給男友，男友立刻奉上，寶貝只要張嘴負責喝就好！❤️", "img": ""},
    {"type": "ssr", "tag": "✨ 隱藏彩蛋・SSR 稀有卡", "title": "🛡️ 免死金牌與無限哄人券", "content": "恭喜寶貝抽到頂級 SSR！\n【兌換權利】：\n今日不論心情多差、有多任性、想罵誰討厭鬼，男友全部站妳這邊，無條件陪妳同仇敵愾，把妳哄到心花怒放為止！🌸", "img": ""},
    {"type": "ssr", "tag": "✨ 隱藏彩蛋・SSR 稀有卡", "title": "🍗 深夜罪惡宵夜陪吃券", "content": "恭喜寶貝抽到深夜 SSR！\n【兌換權利】：\n只要妳想吃，不管是鹽酥雞、滷味還是熱豆花，男友無條件陪吃，所有發胖熱量男友通通替妳吸收！🥰", "img": ""},
    {"type": "ssr", "tag": "✨ 隱藏彩蛋・SSR 稀有卡", "title": "🛌 廢人模式一日特許令", "content": "恭喜寶貝抽到極罕見 SSR！\n【兌換權利】：\n今天整天躺在床上不動！垃圾男友丟、外賣男友拿、水杯男友遞、被子男友蓋，寶貝只需要負責呼吸跟被愛！💖", "img": ""},
    {"type": "ssr", "tag": "✨ 隱藏彩蛋・SSR 稀有卡", "title": "🧸 專屬人肉抱枕任意揉券", "content": "恭喜寶貝抽到暖心 SSR！\n【兌換權利】：\n隨時隨地召喚男友充當暖暖包或人肉抱枕，提供無限制揉臉、抓手、抱緊緊，耐壓耐抱絕不喊累 🥰", "img": ""}
]

# 4. 無限演算法引擎（Procedural Generator：10,000+ 隨機組合）
DOG_SUBJ = ["家裡那隻小短腿臘腸", "隔壁的頑固柴犬", "鄰居家的呆萌柯基", "一條偽裝成長條麵包的臘腸狗", "永遠在等開飯的黃金獵犬"]
DOG_ACTION = [
    "試圖翻過 10 公分的門檻，結果肚皮卡在中間四腳懸空",
    "聽到冰箱門打開的聲音，以時速 90 公里滑壘進廚房",
    "散步到一半突然原地石化躺平，假裝自己沒有骨頭",
    "把主人的拖鞋偷偷叼到床底下，還一臉無辜地看著主人",
    "鑽進被窩只露出一根長長的鼻子在外面打呼嚕"
]
DOG_ENDING = [
    "這底盤已經低到可以去幫市政道路做平整度驗收了啦！🐾",
    "看在牠眼睛那麼圓那麼萌的份上，除了抱起來狂親還能怎麼辦呢 🥰",
    "人類在牠面前完全沒有威嚴，根本就是小狗的專屬全職僕人！",
    "這就是碳基生物能擁有的最純粹、最療癒的快樂了～"
]

MEME_SITUATION = [
    "今天下班搭捷運的時候", "半夜躺在床上滑手機看到第 100 篇脆文時", "看到銀行戶頭餘額的那一瞬間",
    "外送抵達門口但自己完全不想穿褲子去開門時", "天蠍座女生嘴巴說『隨便都可以』的那一秒"
]
MEME_TWIST = [
    "突然大腦連線到了外星宇宙，覺得整個地球都在跟我開玩笑",
    "理智線啪的一聲斷掉，立刻決定怒點一杯大杯半糖奶茶壓壓驚",
    "整個人像一灘融化的起司，焊死在沙發上連手指都不想動",
    "內心的傲嬌小劇場已經演完了一整部甄嬛傳，但臉上依然是西伯利亞暴風雪"
]
MEME_PUNCHLINE = [
    "脆友說得好：只要我不努力，就沒有任何人可以利用我的善良！😂",
    "算了，生活苦短，及時行樂，吃飽睡好才是人生終極奧義。",
    "反正在男友面前，妳永遠都可以安心當個被寵壞的小公主 🥰",
    "今天也是為了能隨心所欲吃肉乾、喝手搖飲而努力搬磚的一天！"
]

def generate_infinite_card():
    category = random.choice(["dog_inf", "meme_inf"])
    if category == "dog_inf":
        tag = "🌭 無限宇宙・汪星人搞笑日常"
        title = f"{random.choice(DOG_SUBJ)} 的迷惑行為"
        content = f"【今日奇觀觀察】：\n{random.choice(DOG_SUBJ)}{random.choice(DOG_ACTION)}。\n\n{random.choice(DOG_ENDING)}"
    else:
        tag = "😂 無限宇宙・脆友人間清醒"
        title = f"關於 {random.choice(MEME_SITUATION)}"
        content = f"【脆友最新共鳴】：\n{random.choice(MEME_SITUATION)}，{random.choice(MEME_TWIST)}。\n\n{random.choice(MEME_PUNCHLINE)}"
    
    return {
        "type": "infinite",
        "tag": tag,
        "title": title,
        "content": content,
        "img": ""
    }

# 5. 頂部標題區
st.markdown("""
<div style="text-align: center; margin-bottom: 12px;">
    <div style="font-size: 2.2rem;">🎁</div>
    <div style="color: #D6336C; font-size: 1.5rem; font-weight: 800;">LU 寶貝的解壓開心盲盒</div>
    <div style="color: #8C6D77; font-size: 0.9rem; margin-top: 4px;">無限卡池版・滿滿臘腸狗、吸貓與爆笑脆文 🌸</div>
</div>
""", unsafe_allow_html=True)

# 6. Session State 抽卡記錄與防重複機制
if "drawn_static_indices" not in st.session_state:
    st.session_state.drawn_static_indices = []

if "current_card" not in st.session_state:
    st.session_state.current_card = random.choice(STATIC_CARDS)

# 類別篩選器
theme_filter = st.radio(
    "想要抽什麼類型的盲盒呢？",
    ["🎲 全都要（精選＋無限隨機）", "🌭 臘腸狗與汪汪", "🐱 貓貓迷惑特區", "😂 爆笑脆文與迷因", "♾️ 無限宇宙生成模式"],
    horizontal=True
)

def pick_next_card():
    # 若選無限宇宙模式，直接動態生成
    if "無限" in theme_filter:
        return generate_infinite_card()
    
    # 隨機有 30% 機率直接觸發動態無限卡片，保證抽不完
    if theme_filter == "🎲 全都要（精選＋無限隨機）" and random.random() < 0.35:
        return generate_infinite_card()

    # 靜態精選池篩選
    if "汪汪" in theme_filter:
        candidates = [i for i, c in enumerate(STATIC_CARDS) if c["type"] in ["dog", "ssr"]]
    elif "貓貓" in theme_filter:
        candidates = [i for i, c in enumerate(STATIC_CARDS) if c["type"] in ["cat", "ssr"]]
    elif "迷因" in theme_filter:
        candidates = [i for i, c in enumerate(STATIC_CARDS) if c["type"] in ["meme", "ssr"]]
    else:
        candidates = list(range(len(STATIC_CARDS)))
    
    available = [i for i in candidates if i not in st.session_state.drawn_static_indices]
    if not available:
        st.session_state.drawn_static_indices = []
        available = candidates
    
    selected_idx = random.choice(available)
    st.session_state.drawn_static_indices.append(selected_idx)
    if len(st.session_state.drawn_static_indices) > 25:
        st.session_state.drawn_static_indices.pop(0)
        
    return STATIC_CARDS[selected_idx]

# 抽卡按鈕
if st.button("✨ 點我開盲盒！抽取今日快樂 ✨"):
    with st.spinner("正在為 LU 寶貝連線無限快樂能量...🐾"):
        time.sleep(0.12)
        st.session_state.current_card = pick_next_card()
    st.rerun()

# 7. 開出的卡片展示
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

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

# 8. 脆（Threads）熱搜直達專區
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
