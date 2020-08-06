from dataclasses import *

@dataclass
class Result:
    name: str
    math: int
    science: int
    english: int

def score():
    results = [
        Result("Alice", 100, 65, 57),
        Result("Bob", 45, 98, 100),
        Result("Charley", 50, 50, 50)]
    return results

def max_point(student):
    m_score = 0
    s_score = 0
    e_score = 0
    m_name = ""
    s_name = ""
    e_name = ""
    for x in student:
        if x.math >= m_score:
            m_score = x.math
            m_name = x.name
        if x.science >= s_score:
            s_score = x.science
            s_name = x.name
        if x.english >= e_score:
            e_score = x.english
            e_name = x.name
    return f"数学:{m_name}、物理:{s_name}、英語:{e_name}"

def total_max_point(student):
    total = 0
    name = ""
    for x in student:
        if (x.math + x.science + x.english) >= total:
            total = x.math + x.science + x.english
            name = x.name
    return f"総合:{name}"

print(max_point(score()))
print(total_max_point(score()))
#