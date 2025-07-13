from models.quiz import QuizResponse
from models.response import Recommendation
from services.ai_handler import call_ai_for_recommendation

def extract_age_group(age: int) -> str:
    if age < 13:
        return "child"
    elif 13 <= age <= 19:
        return "teen"
    elif 20 <= age <= 60:
        return "adult"
    else:
        return "senior"

def generate_recommendations(responses: list[QuizResponse]) -> Recommendation:
    response_map = {r.question_id: r.answer for r in responses}
    age = response_map.get("age")
    if not age:
        raise ValueError("Age is required for age-targeted localization")

    age_group = extract_age_group(int(age))

    user_context = "\n".join([f"{k}: {v}" for k, v in response_map.items()])

    ai_input = f"""
User's quiz responses:
{user_context}

The user's age group is: {age_group.upper()}.

You MUST tailor your tips, products, and tone specifically for this age group:
- CHILD: Fun, playful, safe (NO caffeine, supplements, yoga, or complex routines)
- TEEN: Simple, health-building advice (NO strong supplements or diagnosis)
- ADULT: Stress balance, energy support, and active lifestyle
- SENIOR: Mobility, simplicity, low-risk routines

Return only a JSON object like:
{{
  "goal": "string",
  "tips": ["tip1", "tip2"],
  "products": ["product1", "product2"],
  "cta": "string"
}}
"""

    raw = call_ai_for_recommendation(ai_input)

    return Recommendation(
        goal=raw.get("goal", "General Wellness"),
        tips=raw.get("tips", ["Stay hydrated", "Exercise regularly"]),
        products=raw.get("products", ["Multivitamin", "Yoga mat"]),
        call_to_action=raw.get("cta", "Visit your physician")
    )


# def generate_recommendations(responses: list[QuizResponse]) -> Recommendation:
    response_map = {r.question_id: r.answer for r in responses}
    age = response_map.get("age")
    if not age:
        raise ValueError("Age is required for age-targeted localization")

    age_group = extract_age_group(int(age))
    
    ai_input = "\n".join([f"{k}: {v}" for k, v in response_map.items()])
    ai_input += f"\nAge group: {age_group}"

    raw = call_ai_for_recommendation(ai_input)

    # Example: Parse AI output
    return Recommendation(
        goal=raw.get("goal", "General Wellness"),
        tips=raw.get("tips", ["Stay hydrated", "Exercise regularly"]),
        products=raw.get("products", ["Multivitamin", "Yoga mat"]),
        call_to_action=raw.get("cta", "Visit your physician")
    )
