
import json
from pathlib import Path

import streamlit as st
from groq import Groq

# ============================================================
# 1. APP CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Content Generator Pro",
    page_icon="🤖",
    layout="wide"
)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

DATA_FILE = Path("products.json")


# ============================================================
# 2. SESSION STATE
# ============================================================

if "content_history" not in st.session_state:
    st.session_state.content_history = []

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "generated_content" not in st.session_state:
    st.session_state.generated_content = ""


# ============================================================
# 3. PRODUCT DATA FUNCTIONS
# ============================================================

def load_products():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        st.error("products.json must contain a list of products.")
        return []

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        st.error("products.json contains invalid JSON.")
        return []


products = load_products()


def save_products():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)


def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def product_name_exists(name, exclude_id=None):
    for product in products:
        if product["name"].strip().lower() == name.strip().lower():
            if product["id"] != exclude_id:
                return True
    return False


def generate_product_id():
    return max(
        (product["id"] for product in products),
        default=0
    ) + 1


def calculate_decision(profit_margin):
    if profit_margin >= 40:
        return "Scale"
    elif profit_margin >= 30:
        return "Keep"
    return "Review"


def analyze_product(product):
    quantity = product["quantity"]
    purchase_price = product["purchase_price"]
    selling_price = product["selling_price"]
    shipping = product["shipping"]

    product_cost = purchase_price * quantity
    revenue = selling_price * quantity
    total_cost = product_cost + shipping
    profit = revenue - total_cost

    profit_margin = (profit / revenue * 100) if revenue > 0 else 0

    if profit_margin >= 30:
        status = "Good"
    elif profit_margin >= 15:
        status = "Medium"
    else:
        status = "Low"

    return {
        "id": product["id"],
        "name": product["name"],
        "quantity": quantity,
        "cost": product_cost,
        "shipping": shipping,
        "total_cost": total_cost,
        "revenue": revenue,
        "profit": profit,
        "profit_margin": profit_margin,
        "status": status,
        "decision": calculate_decision(profit_margin)
    }


# ============================================================
# 4. CONTENT GENERATOR
# ============================================================

st.title("🤖 AI Content Generator Pro")
st.write("Create business content with AI and manage your product profitability.")

dashboard_tab, content_tab, product_tab = st.tabs(
    ["📊 Dashboard", "✍️ AI Content Generator", "📦 China Store Product Manager"]
)

with dashboard_tab:

    st.title("📊 Business Dashboard")

    st.write("Welcome to your business overview!")

    results = [analyze_product(product) for product in products]

    total_products = len(products)
    total_revenue = sum(item["revenue"] for item in results)
    total_cost = sum(item["total_cost"] for item in results)
    total_profit = sum(item["profit"] for item in results)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Products", total_products)
    col2.metric("Total Revenue", f"${total_revenue:,.2f}")
    col3.metric("Total Costs", f"${total_cost:,.2f}")
    col4.metric("Total Profit", f"${total_profit:,.2f}")

    # Best Product Analysis
    if results:

        best_product = max(
            results,
            key=lambda item: item["profit"]
        )

        st.success(
            f"🏆 Best Product: {best_product['name']} "
            f"| Profit: ${best_product['profit']:,.2f}"
        )

    # Products That Need Attention
    st.subheader("⚠️ Products Need Attention")

    low_margin_products = [
        item for item in results
        if item["status"] == "Low"
    ]

    if low_margin_products:

        for item in low_margin_products:

            st.warning(
                f"⚠️ {item['name']} "
                f"| Profit Margin: {item['profit_margin']:.2f}%"
            )

    else:
        st.success("All products have acceptable profit margins!")

    # Smart Business Recommendations
    st.subheader("💡 Smart Business Recommendations")

    if low_margin_products:

        for item in low_margin_products:

            st.info(
                f"💡 Recommendation for {item['name']}: "
                "Review purchase price, shipping costs, "
                "and selling price to improve profitability."
            )

    elif results:

        st.success(
            "Your products have acceptable profit margins. "
            "Keep monitoring costs and sales performance."
        )

    else:

        st.info(
            "Add your first product to receive smart business recommendations."
        )

    # Profit Chart
    st.subheader("📈 Profit by Product")

    if results:

        chart_data = {
            item["name"]: item["profit"]
            for item in results
        }

        st.bar_chart(chart_data)

    else:
        st.info("No products available. Add your first product!")

with content_tab:

    st.subheader("Create Marketing Content")

    topic = st.text_input(
        "What topic do you want to write about?"
    )

    content_type = st.sidebar.selectbox(
        "Choose content type:",
        [
            "Business Tips",
            "Instagram Caption",
            "Marketing Post",
            "Product Description"
        ]
    )

    content_length = st.sidebar.selectbox(
        "Choose Content Length:",
        ["Short", "Medium", "Long"]
    )

    brand_name = st.text_input(
        "Brand Name:",
        placeholder="Enter your company name..."
    )

    brand_description = st.text_area(
        "Describe your brand:",
        placeholder="Tell us about your company, products, services, and customers..."
    )

    custom_instructions = st.text_area(
        "Custom Instructions:",
        placeholder="Tell AI how you want your content to be written..."
    )

    content_prompts = {
        "Business Tips": "Write exactly 3 practical business tips for beginners.",
        "Instagram Caption": "Write a short, engaging Instagram caption with a strong hook and relevant emojis.",
        "Marketing Post": "Write a persuasive marketing post with a strong hook and a clear call to action.",
        "Product Description": "Write a professional product description focusing on features and customer benefits."
    }

    language = st.sidebar.selectbox(
        "Choose content language:",
        ["English", "Arabic", "Kurdish (Sorani)"]
    )

    tone = st.sidebar.selectbox(
        "Choose writing tone:",
        ["Professional", "Friendly", "Persuasive", "Motivational"]
    )

    creativity = st.sidebar.slider(
        "Creativity Level:",
        min_value=0.2,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    audience = st.sidebar.selectbox(
        "Choose target audience:",
        ["Entrepreneurs", "Students", "Business Owners", "Beginners"]
    )

    brand_voice = st.sidebar.selectbox(
        "Choose Brand Voice:",
        ["Friendly", "Professional", "Casual", "Luxury"]
    )

    if st.button("Generate Content", key="generate_content_button"):

        if topic.strip():

            with st.spinner("AI is generating content..."):

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "user",
                            "content": f"""
You are a professional business content creator.

Instructions: {content_prompts[content_type]}
Writing Tone: {tone}
Content Length: {content_length}
Target Audience: {audience}
Brand Voice: {brand_voice}
Brand Name: {brand_name}
Brand Description: {brand_description}
Custom Instructions: {custom_instructions}
Topic: {topic}

Write useful, engaging, and practical content.

Do not invent facts, prices, discounts, warranties,
return policies, product features, or customer testimonials.

Use the Brand Description as the only source of factual
information about the brand and its products.

Use the Topic only to understand the content idea,
not as a source of factual claims.

Do not include any claims from the Topic unless
they are confirmed in the Brand Description.

If a fact is missing from the Brand Description,
do not mention it.

Write the entire content in {language}.
Do not use any other language.
"""
                        }
                    ],
                    temperature=creativity
                )

            generated_content = response.choices[0].message.content

            st.session_state.generated_content = generated_content
            st.session_state.content_history.append(generated_content)

        else:
            st.warning("Please enter a topic.")

    if st.session_state.generated_content:

        st.subheader("Generated Content")

        st.code(
            st.session_state.generated_content,
            language=None
        )

        if st.button("⭐ Save to Favorites", key="save_favorite_button"):

            if st.session_state.generated_content not in st.session_state.favorites:

                st.session_state.favorites.append(
                    st.session_state.generated_content
                )

                st.success("Content saved to favorites!")

            else:
                st.info("This content is already in your favorites.")

        st.download_button(
            label="Download Content",
            data=st.session_state.generated_content,
            file_name="ai_content.txt",
            mime="text/plain"
        )

    # --------------------------------------------------------
    # CONTENT HISTORY
    # --------------------------------------------------------

    st.divider()
    st.subheader("🕘 Content History")

    if st.button("Clear History", key="clear_history_button"):
        st.session_state.content_history = []
        st.rerun()

    if st.session_state.content_history:
        for index, content in enumerate(st.session_state.content_history):
            with st.expander(f"History item {index + 1}"):
                st.write(content)
    else:
        st.info("No content history yet.")

    # --------------------------------------------------------
    # FAVORITE CONTENT
    # --------------------------------------------------------

    st.divider()
    st.subheader("⭐ Favorite Content")

    if st.session_state.favorites:

        for index, content in enumerate(st.session_state.favorites):

            with st.expander(f"Favorite {index + 1}"):

                edited_content = st.text_area(
                    "Edit your favorite content:",
                    value=content,
                    key=f"favorite_editor_{index}",
                    height=180
                )

                col_save, col_remove = st.columns(2)

                with col_save:
                    if st.button(
                        "💾 Save Edit",
                        key=f"save_favorite_edit_{index}"
                    ):
                        if edited_content.strip():
                            st.session_state.favorites[index] = edited_content
                            st.success("Favorite content updated!")
                            st.rerun()
                        else:
                            st.warning("Favorite content cannot be empty.")

                with col_remove:
                    if st.button(
                        "🗑️ Remove",
                        key=f"remove_favorite_{index}"
                    ):
                        st.session_state.favorites.pop(index)
                        st.rerun()

    else:
        st.info("No favorite content saved yet.")


# ============================================================
# 5. CHINA STORE PRODUCT MANAGER
# ============================================================

with product_tab:

    st.header("📦 China Store Product Manager")
    st.caption("Add, search, update, delete, and analyze your products.")

    # --------------------------------------------------------
    # BUSINESS REPORT
    # --------------------------------------------------------

    st.subheader("📊 Business Report")

    if products:

        results = [analyze_product(product) for product in products]

        total_revenue = sum(result["revenue"] for result in results)
        total_cost = sum(result["total_cost"] for result in results)
        total_profit = sum(result["profit"] for result in results)

        best_product = max(results, key=lambda result: result["profit"])
        worst_product = min(results, key=lambda result: result["profit"])

        metric1, metric2, metric3 = st.columns(3)

        metric1.metric("Total Revenue", f"${total_revenue:,.2f}")
        metric2.metric("Total Cost", f"${total_cost:,.2f}")
        metric3.metric("Total Profit", f"${total_profit:,.2f}")

        best_col, worst_col = st.columns(2)

        best_col.success(
            f"Best Product: {best_product['name']}\n\n"
            f"Profit: ${best_product['profit']:,.2f}"
        )

        worst_col.warning(
            f"Worst Product: {worst_product['name']}\n\n"
            f"Profit: ${worst_product['profit']:,.2f}"
        )

        st.subheader("Product Profit Analysis")

        st.dataframe(
            [
                {
                    "Product": result["name"],
                    "Quantity": result["quantity"],
                    "Revenue ($)": result["revenue"],
                    "Total Cost ($)": result["total_cost"],
                    "Profit ($)": result["profit"],
                    "Profit Margin (%)": round(result["profit_margin"], 2),
                    "Status": result["status"],
                    "Decision": result["decision"]
                }
                for result in results
            ],
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("Add your first product to see the business report.")

    st.divider()

    # --------------------------------------------------------
    # ADD PRODUCT
    # --------------------------------------------------------

    st.subheader("➕ Add Product")

    with st.form("add_product_form"):

        new_name = st.text_input("Product name")

        add_col1, add_col2 = st.columns(2)

        with add_col1:
            purchase_price = st.number_input(
                "Purchase price ($)",
                min_value=1,
                step=1,
                value=1,
                key="add_purchase_price"
            )

            quantity = st.number_input(
                "Quantity",
                min_value=1,
                step=1,
                value=1,
                key="add_quantity"
            )

        with add_col2:
            shipping = st.number_input(
                "Shipping cost ($)",
                min_value=0,
                step=1,
                value=0,
                key="add_shipping"
            )

            selling_price = st.number_input(
                "Selling price ($)",
                min_value=1,
                step=1,
                value=1,
                key="add_selling_price"
            )

        add_submitted = st.form_submit_button("Add Product")

    if add_submitted:

        clean_name = new_name.strip()

        if not clean_name:
            st.error("Product name cannot be empty.")

        elif product_name_exists(clean_name):
            st.error("A product with this name already exists.")

        else:
            new_product = {
                "id": generate_product_id(),
                "name": clean_name,
                "purchase_price": int(purchase_price),
                "quantity": int(quantity),
                "shipping": int(shipping),
                "selling_price": int(selling_price)
            }

            products.append(new_product)
            save_products()

            st.success("Product added successfully!")
            st.rerun()

    st.divider()

    # --------------------------------------------------------
    # SEARCH AND DISPLAY PRODUCTS
    # --------------------------------------------------------

    st.subheader("🔎 Search Products")

    search_name = st.text_input(
        "Search by product name",
        key="search_product_name"
    )

    matching_products = [
        product for product in products
        if search_name.strip().lower() in product["name"].lower()
    ]

    if matching_products:

        for product in matching_products:

            with st.expander(
                f"ID {product['id']} — {product['name']}"
            ):

                st.write(f"Purchase price: ${product['purchase_price']}")
                st.write(f"Selling price: ${product['selling_price']}")
                st.write(f"Quantity: {product['quantity']}")
                st.write(f"Shipping cost: ${product['shipping']}")

                analysis = analyze_product(product)

                st.write(f"Estimated revenue: ${analysis['revenue']:,.2f}")
                st.write(f"Estimated profit: ${analysis['profit']:,.2f}")
                st.write(
                    f"Profit margin: {analysis['profit_margin']:.2f}%"
                )
                st.write(f"Decision: {analysis['decision']}")

    elif products:
        st.info("No matching products found.")

    st.divider()

    # --------------------------------------------------------
    # UPDATE PRODUCT
    # --------------------------------------------------------

    st.subheader("✏️ Update Product")

    if products:

        product_options = {
            f"{product['id']} — {product['name']}": product["id"]
            for product in products
        }

        selected_update_label = st.selectbox(
            "Choose a product to update",
            list(product_options.keys()),
            key="update_product_select"
        )

        selected_update_id = product_options[selected_update_label]
        selected_product = find_product(selected_update_id)

        with st.form("update_product_form"):

            updated_name = st.text_input(
                "Product name",
                value=selected_product["name"]
            )

            update_col1, update_col2 = st.columns(2)

            with update_col1:
                updated_purchase_price = st.number_input(
                    "Purchase price ($)",
                    min_value=1,
                    step=1,
                    value=int(selected_product["purchase_price"]),
                    key="update_purchase_price"
                )

                updated_quantity = st.number_input(
                    "Quantity",
                    min_value=1,
                    step=1,
                    value=int(selected_product["quantity"]),
                    key="update_quantity"
                )

            with update_col2:
                updated_shipping = st.number_input(
                    "Shipping cost ($)",
                    min_value=0,
                    step=1,
                    value=int(selected_product["shipping"]),
                    key="update_shipping"
                )

                updated_selling_price = st.number_input(
                    "Selling price ($)",
                    min_value=1,
                    step=1,
                    value=int(selected_product["selling_price"]),
                    key="update_selling_price"
                )

            update_submitted = st.form_submit_button("Save Product Changes")

        if update_submitted:

            clean_updated_name = updated_name.strip()

            if not clean_updated_name:
                st.error("Product name cannot be empty.")

            elif product_name_exists(
                clean_updated_name,
                exclude_id=selected_product["id"]
            ):
                st.error("Another product already uses this name.")

            else:
                selected_product["name"] = clean_updated_name
                selected_product["purchase_price"] = int(updated_purchase_price)
                selected_product["quantity"] = int(updated_quantity)
                selected_product["shipping"] = int(updated_shipping)
                selected_product["selling_price"] = int(updated_selling_price)

                save_products()

                st.success("Product updated successfully!")
                st.rerun()

    else:
        st.info("There are no products to update.")

    st.divider()

    # --------------------------------------------------------
    # DELETE PRODUCT
    # --------------------------------------------------------

    st.subheader("🗑️ Delete Product")

    if products:

        delete_options = {
            f"{product['id']} — {product['name']}": product["id"]
            for product in products
        }

        selected_delete_label = st.selectbox(
            "Choose a product to delete",
            list(delete_options.keys()),
            key="delete_product_select"
        )

        selected_delete_id = delete_options[selected_delete_label]
        selected_delete_product = find_product(selected_delete_id)

        confirm_delete = st.checkbox(
            f"I confirm deleting {selected_delete_product['name']}",
            key="confirm_delete_product"
        )

        if st.button(
            "Delete Selected Product",
            key="delete_product_button",
            disabled=not confirm_delete
        ):

            products.remove(selected_delete_product)
            save_products()

            st.success("Product deleted successfully!")
            st.rerun()

    else:
        st.info("There are no products to delete.")
