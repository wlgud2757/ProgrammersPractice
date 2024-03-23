def solution(todo_list, finished):
    return [task for task, is_finished in zip(todo_list, finished) if not is_finished]

