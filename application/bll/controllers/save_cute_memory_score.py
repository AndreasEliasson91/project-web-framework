from application.dll.repository import save_cute_memory_score_repo


def save_cute_memory_score(get_score):
    return save_cute_memory_score_repo.save_cute_memory_score(get_score)