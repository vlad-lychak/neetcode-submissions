class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        stud = Counter(students)

        for s in sandwiches:
            if stud[s] > 0:
                res -= 1
                stud[s] -= 1
            else:
                break
        
        return res