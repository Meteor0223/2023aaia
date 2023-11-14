class Solution:
    def average(self, salary: List[int]) -> float:
        #print(sum(salary))
        #有陷阱，程式不對，先寫2行，等一下會修正
        return ( sum(salary)-max(salary)-min(salary) )/( len(salary)-2 )