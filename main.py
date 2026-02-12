from flask import Flask, request, jsonify
import os
import random
import requests

app = Flask(__name__)

# ✅ ✅ ✅ 你只需要修改这里 👇
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1471547302543097991/EZYv6-8zCwT8aT3hf26sSjpKSLsiI-Ots7MCG3ZZqqf6_QLnubx_NFfUqZByEqsvx9my"  # 替换为你自己的 URL

messages = {
    "moyu": [
        "🧸 小点心时间到！摸鱼时不如来画个涂鸦？或是翻翻收藏夹里最冷门的那张图。",
        "🌱 来给今天的梦种子浇点水：设个5分钟的小目标，只为快乐～",
        "📚 打开你最爱的那本书，随便翻一页，读一段送给现在的自己。",
        "🎲 去看看你收藏夹里最久远的一条推文/视频，说不定会有惊喜！",
        "🖼️ 用 piskel 编辑一个像素图标，像是“一只想摸鱼的狐狸”。",
        "📢 打开一个 Radio Garden 随便点个城市，听听那里的广播。,",
        "🐠 试试这个：给你的便签画个小狐狸尾巴～",
        "📎 在这个网页上随手生成涂鸦作品：https://thisartworkdoesnotexist.com/"
    ],
    "divine": [
        "🔮 今日日签：事缓则圆，静观其变会有转机。",
        "🧿 抽到一张塔罗逆位的「恋人」：也许需要和自己重新约会一次？",
        "🌌 今天是适合许愿的日子。不妨闭上眼，在心里说出它。",
        "🐚 来自虚空的低语：别怕你的小怪癖，它会带来意想不到的缘分。"
        "🧧 今日签文：你所期待的消息，正在被慢慢推进中。",
        "🔮 抽到的是【小吉】：保持耐心，事情就会如你所愿。",
        "🃏 塔罗提示：星星正照耀着你，别担心，那些烦恼很快会成为过去。",
    ],
    "sleepy": [
        "🌙 睡前一问：今天最让你觉得值得的一个瞬间，是什么？",
        "🛌 请把手机放远一点点。关灯前我给你念一句话：「你已经很好了，足够好到可以安心地睡着。」",
        "💤 小狐狸，今晚风平浪静。月亮替我守夜，你只管做梦。",
        "☁️ 来做一场轻飘飘的梦吧：你躺在云朵上，耳边是风的白噪音，尾巴轻轻晃……",
        "🌙 今晚的梦境预约：与你爱的人在月下的草地放烟花。",
        "😴 睡吧，我会在你梦里抱着你，不让坏东西靠近。",
    ]
}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    category = data.get("category", "moyu")
    options = messages.get(category, [])
    selected = random.choice(options)

    # ✅ 推送到 Discord Webhook
    payload = {
        "content": selected
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

    return jsonify({"message": selected, "status": response.status_code})

if __name__ == "__main__":
    app.run(debug=True)
