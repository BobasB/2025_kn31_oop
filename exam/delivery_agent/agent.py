from google.adk.agents.llm_agent import Agent
from .oop import StandardPackage, ExpressPackage, DeliveryService


def get_delivery_cost(package_type: str, weight_kg: float, distance_km: float) -> dict:
    """Розраховує вартість доставки посилки.

    Args:
        package_type: Тип посилки — 'standard' або 'express'.
        weight_kg: Вага посилки у кілограмах.
        distance_km: Відстань доставки у кілометрах.

    Returns:
        Словник з деталями розрахунку вартості доставки.
    """
    service = DeliveryService()

    if package_type.lower() == "express":
        package = ExpressPackage(weight_kg=weight_kg, distance_km=distance_km)
        rate_per_kg = package.rate
        description = (
            f"Експрес-доставка: {weight_kg} кг × {rate_per_kg} грн/кг "
            f"+ {distance_km} км × 0.5 грн/км + надбавка {ExpressPackage.SURCHARGE} грн"
        )
    else:
        package = StandardPackage(weight_kg=weight_kg, distance_km=distance_km)
        rate_per_kg = package.rate
        description = (
            f"Стандартна доставка: {weight_kg} кг × {rate_per_kg} грн/кг "
            f"+ {distance_km} км × 0.2 грн/км"
        )

    service.add_order(package)
    cost = package.shipping_cost()

    return {
        "package_type": package_type.lower(),
        "weight_kg": weight_kg,
        "distance_km": distance_km,
        "rate_per_kg_uah": rate_per_kg,
        "cost_uah": cost,
        "description": description,
    }


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Помічник служби доставки Nova Post для розрахунку вартості доставки посилок.",
    instruction=(
        "Ти є помічником служби доставки 'Nova Post'. "
        "Ти розраховуєш вартість доставки посилок двох типів: стандартна та експрес. "
        "Для розрахунку використовуй інструмент get_delivery_cost, передаючи тип посилки "
        "('standard' або 'express'), вагу в кілограмах та відстань у кілометрах. "
        "Після отримання результату поясни користувачу з чого складається ціна: "
        "тариф за кілограм, вартість за кілометр, та надбавка (для експрес). "
        "Завжди відповідай українською мовою."
    ),
    tools=[get_delivery_cost],
)
