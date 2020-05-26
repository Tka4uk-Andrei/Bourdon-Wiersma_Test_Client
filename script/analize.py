
def calculate_attention_switch(completed_count, err_count):
    if (completed_count == 0):
        return 0
    return float(err_count) / float(completed_count)