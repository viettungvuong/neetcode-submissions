class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pq = []
        available = {}
        n=len(tasks)
        next_jump=[]
        for i in range(n):
            task=tasks[i]
            if available.get(task[0]) is None:
                available[task[0]]=[]
            available[task[0]].append(i)
            if task[0] not in next_jump:
                heapq.heappush(next_jump,task[0])
        res=[]
        next_end=-1

        while next_jump:
            i=heapq.heappop(next_jump)
            if available.get(i) is not None:
                for task_index in available[i]:
                    heapq.heappush(pq, (tasks[task_index][1], task_index))

            if i>=next_end and pq:
                processing_time, task_index = heapq.heappop(pq)
                print(f"Process task with {processing_time} processing time at {i} - task index {task_index}")
                res.append(task_index)
                next_end=i+processing_time
                if next_end not in next_jump:
                    print(f"Add end time {next_end}")
                    heapq.heappush(next_jump,next_end)   
        
        return res