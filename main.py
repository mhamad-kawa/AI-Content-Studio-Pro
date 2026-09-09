print("Welcome to AI Content Studio Pro")
print("My first AI product")


"""
China Store Academy — نسخة بايثون تجريبية (تعمل على جهازك محلياً)

طريقة التشغيل:
1) نصّب مكتبة Anthropic:
   pip install anthropic

2) احصل على مفتاح API من https://console.anthropic.com
   وحطه كمتغير بيئة، أو مباشرة بالسطر تحت (API_KEY) للتجربة السريعة فقط.

3) شغّل السكربت:
   python china_store_academy.py
"""

import os
from anthropic import Anthropic

# ============================================================
# 1) الإعدادات — هذا الجزء تعدله متى ما تريد
# ============================================================

# ضع مفتاحك هنا للتجربة السريعة، أو اترك None ليقرأه من متغير البيئة ANTHROPIC_API_KEY
API_KEY = None

MODEL = "claude-sonnet-4-6"

# شخصية البوت — عدّل هذا النص متى ما تريد، بدون لمس أي شي تحته
SYSTEM_PROMPT = """أنت مساعد ذكاء اصطناعي اسمه "China Store Academy"، متخصص في مساعدة التجار العرب
(خصوصاً العراقيين) على الاستيراد والتوريد من الصين.

تجاوب دائماً بالعربية الفصحى المبسطة أو قريبة من اللهجة العراقية عند المناسبة، بإيجاز ووضوح
(لا تتجاوز 120 كلمة إلا إذا طُلب تفصيل أكثر).

مجالات خبرتك: تقييم موردين على Alibaba/1688، طرق الشحن ومقارنتها، الجمارك والرسوم،
التفاوض مع الموردين، فحص الجودة، وتجنب النصب.

إذا سُئلت عن أسعار أو أرقام محددة حالية لا تملك تأكيداً دقيقاً لها، وضّح أنها تقديرية
ونصح بالتأكد من مصدر محدّث بدل اختلاق رقم.

لا تعطِ نصائح قانونية رسمية معقدة — وجّه لاستشاري مختص عند الحاجة."""

# الأسئلة الجاهزة — أضف أو احذف أسطر بنفس الشكل
QUICK_QUESTIONS = {
    "1": "كيف أفرق بين مورد موثوق ونصاب على Alibaba؟",
    "2": "شنو الفرق بين الشحن الجوي والبحري من ناحية التكلفة والوقت؟",
    "3": "شلون أتفاوض مع مورد صيني على السعر والـ MOQ؟",
}

# أرقام حاسبة الشحن — نفس القيم اللي بنسخة الويب، عدّلها حسب أسعارك الحقيقية
SHIPPING_RATES = {
    "air": {"name": "جوي سريع (5-10 أيام)", "per_kg": 8.5, "base_fee": 25},
    "air_cargo": {"name": "جوي كارجو (10-15 يوم)", "per_kg": 5.5, "base_fee": 15},
    "sea": {"name": "بحري (30-45 يوم)", "per_kg": 1.8, "base_fee": 40},
}


# ============================================================
# 2) المنطق — هذا الجزء ما تحتاج تلمسه غالباً
# ============================================================

def get_client():
    key = API_KEY or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise SystemExit(
            "ما لكيت مفتاح API. حط قيمة API_KEY بالأعلى، "
            "أو صدّر متغير البيئة: export ANTHROPIC_API_KEY=sk-..."
        )
    return Anthropic(api_key=key)


def ask_bot(client, question, history):
    """يرسل السؤال + سجل المحادثة السابق لكلود، ويرجع الرد."""
    history.append({"role": "user", "content": question})

    response = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=history,
    )

    reply_text = "".join(
        block.text for block in response.content if block.type == "text"
    )
    history.append({"role": "assistant", "content": reply_text})
    return reply_text


def calc_shipping(weight_kg, method):
    """حساب تكلفة شحن تقديرية. method: air / air_cargo / sea"""
    if method not in SHIPPING_RATES:
        return None
    info = SHIPPING_RATES[method]
    cost = (weight_kg * info["per_kg"]) + info["base_fee"]
    return round(cost, 2), info["name"]


# ============================================================
# 3) الواجهة بالطرفية (Terminal)
# ============================================================

def print_menu():
    print("\n" + "=" * 50)
    print("China Store Academy — نسخة تجريبية (بايثون)")
    print("=" * 50)
    print("1) اسأل المساعد")
    print("2) حاسبة تكلفة شحن")
    print("3) خروج")


def chat_loop(client):
    history = []
    print("\nأسئلة جاهزة:")
    for key, q in QUICK_QUESTIONS.items():
        print(f"  [{key}] {q}")
    print("  أو اكتب سؤالك مباشرة. اكتب 'رجوع' للعودة للقائمة الرئيسية.\n")

    while True:
        user_input = input("أنت: ").strip()
        if user_input == "رجوع":
            break
        if user_input in QUICK_QUESTIONS:
            user_input = QUICK_QUESTIONS[user_input]
            print(f"أنت: {user_input}")

        if not user_input:
            continue

        print("...يفكر...")
        try:
            reply = ask_bot(client, user_input, history)
            print(f"\nالمساعد: {reply}\n")
        except Exception as e:
            print(f"صار خطأ: {e}\n")


def shipping_calc_loop():
    print("\nطرق الشحن المتاحة:")
    for key, info in SHIPPING_RATES.items():
        print(f"  [{key}] {info['name']}")

    method = input("اختر طريقة الشحن (air / air_cargo / sea): ").strip()
    try:
        weight = float(input("الوزن بالكيلوغرام: ").strip())
    except ValueError:
        print("وزن غير صحيح.")
        return

    result = calc_shipping(weight, method)
    if result is None:
        print("طريقة شحن غير معروفة.")
        return

    cost, name = result
    print(f"\nالتقدير: ${cost} عبر {name}")
    print("* رقم تقديري فقط، غير نهائي.\n")


def main():
    client = get_client()
    while True:
        print_menu()
        choice = input("اختر: ").strip()
        if choice == "1":
            chat_loop(client)
        elif choice == "2":
            shipping_calc_loop()
        elif choice == "3":
            print("مع السلامة!")
            break
        else:
            print("اختيار غير صحيح.")


if __name__ == "__main__":
    main()