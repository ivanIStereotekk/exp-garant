from pydantic import BaseModel
from typing import List



# Схемы получения типизированных данных

class PostSchema(BaseModel):
    """Pydantic схема для получения данных"""
    category: str
    content: str

class PostReadSchema(PostSchema):
    """Схема получения Post ORM модели"""
    id: int
    class Config:
        orm_mode = True
        #from_attributes = True

class PostStatisticSchema(BaseModel): 
    """Pydantic схема для получения статистики по постам"""
    post_id: int
    word_count: int
    counted: dict
