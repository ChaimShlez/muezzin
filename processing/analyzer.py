import re


class Analyzer:
    def __init__(self):
        self.hostile=None
        self.no_hostile=None
        self.text=None



    def set_text(self,text):
        self.text=text

    def set_hostile(self,hostile):
        self.hostile=hostile

    def set_no_hostile(self,no_hostile):
        self.no_hostile=no_hostile

    def add_score(self):

        count=0
        score = 0
        matches = re.findall(r"(?=("+'|'.join(self.no_hostile)+r"))", self.text)
        score += len(matches)
        count+=1

        matches = re.findall(r"(?=(" + '|'.join(self.hostile) + r"))", self.text)
        score += (len(matches) * 2)
        count += 1

        return score+count


    def add_ratio(self,score):
         ratio=score/len(self.text)

         return ratio

    def risk_level(self,ratio):
        if ratio>=0.5:
            return "high"

        elif ratio >=0.3:
            return "medium"

        elif ratio >=0.1:
            return "little"
        else:
            return "none"


    def is_bds(self,risk):
        if risk in ("medium","high"):
            return True
        else:
            return False



    def manager_analyzer(self):

        score=self.add_score()

        ratio=self.add_ratio(score)
        # print("b",ratio)
        ratio=ratio*100
        # print("a",ratio)

        risk=self.risk_level(ratio)
        is_bds=self.is_bds(risk)
        return ratio,risk,is_bds














