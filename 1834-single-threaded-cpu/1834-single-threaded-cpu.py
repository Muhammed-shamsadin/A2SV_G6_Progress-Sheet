class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
         sorting is a good technique man, sort it out and then do ur thing, with the heap
         and track the time altogether.
        
        '''
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()
        # to ensure the minimum time gets popped out first
        heap = []
        answer = []
        # cpu starts with the 1st task, unless it finishes it won't add another task.
        # time = tasks[0][0]
        # heappush(heap, (tasks[0][1], tasks[0][2]))

        i = 0
        while i < len(tasks):
            if not heap:
                time = tasks[i][0]
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            process_time, index = heappop(heap)
            answer.append(index)

            time += process_time
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
        
        while heap:
            process_time, index = heappop(heap)
            answer.append(index)
        return answer 






        # if there exists same starting time for tasks, choose the one with smaller processtime


