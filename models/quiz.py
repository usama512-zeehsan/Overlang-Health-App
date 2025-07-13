from pydantic import BaseModel, EmailStr
from typing import List, Union, Literal

class QuizQuestion(BaseModel):
    id: str
    type: Literal["singleChoice", "multiChoice", "textInput", "numberInput"]
    question: str
    options: Union[List[str], None] = None

class QuizResponse(BaseModel):
    question_id: str
    answer: Union[str, int, List[str]]

class EmailCapture(BaseModel):
    email: EmailStr
    user_id: str
