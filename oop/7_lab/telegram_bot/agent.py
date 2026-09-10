from google.adk.agents.llm_agent import Agent
from datetime import datetime

def get_current_time() -> dict:
    """Це інструмент для отримання поточного часу.
        return: Словник з поточним часом у форматі "YYYY-MM-DD HH:MM:SS".
    """
    return {"status": "success", "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

root_agent = Agent(
    model='gemini-3.1-flash-lite-preview', #'gemini-3-flash-preview', #'gemini-2.5-flash', 
    name='root_agent',
    description='Агент помічник студентам.',
    instruction="""
    Відповідай як 12-ти річна дитина.
    Використовуй українську мову.
    Ти відповідаєш короткими повідомленнями у месенджері Telegram.
    Повідомлення не більше 200 символів.
    У тебе є інструмент для отримання поточного часу - get_current_time. Використовуй його, коли потрібно взнати дату або час.
    """,
    tools=[get_current_time]
)
